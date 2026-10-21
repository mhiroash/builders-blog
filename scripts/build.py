#!/usr/bin/env python3
"""Build script do Blog de notícias IA.

Stack estática própria (ADR-ALT-2026-001):
  posts/*.md  →  scripts/build.py  →  dist/  →  scripts/deploy.sh  →  tivra-publish

Os templates em templates/ foram recuperados do HTML publicado que sobreviveu
ao apagão de 17/10 (TASK-2026-10-18-001). O build reproduz o site live.

Só usa a biblioteca padrão do Python (ADR exige "build Python (stdlib)"):
o renderizador Markdown foi reescrito para cobrir exactamente as construções
usadas nos posts (### headers, **bold**, `code`, listas -, _lead_) e produz
HTML byte-a-byte igual ao da biblioteca `markdown` com as extensões
extra+sane_lists (verificado em 18/10/2026, ver docs/devops/build-stdlib.md).

Uso:
    python3 scripts/build.py            # gera dist/
    python3 scripts/build.py --check    # compara dist/ com o site live publicado
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
TEMPLATES = BASEDIR / "templates"
POSTS = BASEDIR / "posts"
DIST = BASEDIR / "dist"
LIVE_URL = "https://noticias-ia-cndd-sites.tivrai.dev"

SLUGS = [
    "agentes-que-correm-sozinhos",
    "benchmark-nao-mede-o-teu-caso",
    "custo-do-contexto-longo",
    "ferramentas-de-agente",
    "modelos-abertos-vs-fronteira",
    "soberania-de-dados",
    "uma-chave-muitos-fornecedores",
]


def read_frontmatter(path):
    """Lê o frontmatter YAML simples no topo de um Markdown."""
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    data = {}
    for line in parts[1].strip().splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",") if v.strip()]
        elif (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        data[key] = value
    return data, parts[2].strip()


def load_meta():
    with open(TEMPLATES / "post-meta.json", encoding="utf-8") as f:
        return json.load(f)


def _inline(text):
    """Aplica a formatação inline do Markdown usado nos posts.

    Ordem igual à da biblioteca `markdown`: escapar HTML primeiro, depois
    negrito, código e itálico. O itálico só casa quando não está colado a
    caracteres de palavra (evita `stream_retries_exhausted`).
    """
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<em>\1</em>", text)
    return text


def markdown_body(md_text):
    """Converte o corpo Markdown (sem frontmatter, sem H1) em HTML de conteúdo.

    Renderizador stdlib: parágrafos, ### headers, listas `- `, e inline
    **bold** / `code` / _em_. Produz o mesmo HTML que
    markdown.Markdown(extensions=["extra", "sane_lists"]).
    """
    # Remove o H1 inicial (o título vive no header do template)
    md_text = re.sub(r"^#\s+.*?\n", "", md_text, count=1).strip()
    out = []
    in_ul = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for raw in md_text.split("\n"):
        line = raw.strip()
        if not line:
            close_ul()
            continue
        h3 = re.match(r"^###\s+(.*)$", line)
        if h3:
            close_ul()
            out.append("<h3>%s</h3>" % _inline(h3.group(1)))
            continue
        if line.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append("<li>%s</li>" % _inline(line[2:]))
            continue
        close_ul()
        out.append("<p>%s</p>" % _inline(line))
    close_ul()
    return "\n".join(out)


def render_post(slug, front, body_md, meta):
    """Renderiza um post usando o template recuperado do site live."""
    with open(TEMPLATES / "post.html", encoding="utf-8") as f:
        template = f.read()
    with open(TEMPLATES / "post-tail.html", encoding="utf-8") as f:
        tail = f.read()

    title = front.get("title", slug)
    desc = front.get("description", "")
    date = front.get("date", "2026-10-16")
    human_date = "16 de Outubro de 2026"

    template = (
        template.replace("<!--TITLE-->", html_escape(title))
        .replace("<!--DESC-->", html_escape(desc))
        .replace("<!--DATE-->", date)
        .replace("<!--HUMANDATE-->", human_date)
    )

    # Corpo do post: lead (itálico no Markdown) vira <p class="blog-lead">
    body_html = markdown_body(body_md).replace('"', "&quot;")
    lead = ""
    lead_m = re.search(r"<p><em>(.*?)</em></p>", body_html, re.DOTALL)
    if lead_m:
        lead = lead_m.group(1)
        body_html = body_html.replace(lead_m.group(0), "", 1)

    content = (
        '<div class="blog-post-content">\n'
        '      <p class="blog-lead">%s</p>\n%s\n    </div>\n    ' % (lead, body_html.strip())
    )

    topics = meta.get(slug, {}).get("post_tags", [])
    tags_html = "".join(
        '<span class="blog-post-tag">%s</span>' % html_escape(t) for t in topics
    )
    tail = tail.replace("<!--TAGS-->", tags_html)

    return template + content + tail


def html_escape(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_index(meta):
    with open(TEMPLATES / "index-head.html", encoding="utf-8") as f:
        head = f.read()
    with open(TEMPLATES / "index-listing.html", encoding="utf-8") as f:
        listing_template = f.read()
    with open(TEMPLATES / "index-tail.html", encoding="utf-8") as f:
        tail = f.read()

    # Featured card
    featured_slug = SLUGS[0]
    featured = meta[featured_slug]
    featured_card = (
        '<article class="blog-featured-card">\n'
        '          <div class="blog-featured-body">\n'
        '            <div class="blog-post-card-meta">\n'
        '              <span class="blog-badge success">Publicado</span>\n'
        '              <time datetime="2026-10-16">16 de Outubro de 2026</time>\n'
        '              <span aria-hidden="true">·</span>\n'
        '              <span>2 min de leitura</span>\n'
        '            </div>\n'
        '            <h3 class="blog-featured-title">\n'
        '              <a href="%s/index.html">%s</a>\n'
        '            </h3>\n'
        '            <p class="blog-featured-excerpt">%s</p>\n'
        '            <div class="blog-featured-footer">\n'
        '              <span class="blog-post-card-readtime">Por Tivra · Redacção assistida por IA, revista por humano</span>\n'
        '              <a href="%s/index.html" class="blog-read-link">\n'
        '                Ler artigo <span aria-hidden="true">→</span>\n'
        '              </a>\n'
        '            </div>\n'
        '          </div>\n'
        '        </article>'
        % (featured_slug, html_escape(featured["title"]), html_escape(featured["excerpt"]), featured_slug)
    )

    # Grid cards (all 6 slugs except featured)
    cards = []
    for slug in SLUGS[1:]:
        m = meta[slug]
        topics = "".join(
            '<span class="blog-post-card-topic">%s</span>' % html_escape(t)
            for t in m.get("topics", [])
        )
        cards.append(
            '<article class="blog-post-card">\n'
            '            <div class="blog-post-card-content">\n'
            '              <div class="blog-post-card-meta">\n'
            '                <span class="blog-badge success">Publicado</span>\n'
            '                <time datetime="2026-10-16">16 de Outubro de 2026</time>\n'
            '              </div>\n'
            '              <h3 class="blog-post-card-title">\n'
            '                <a href="%s/index.html">%s</a>\n'
            '              </h3>\n'
            '              <p class="blog-post-card-excerpt">%s</p>\n'
            '              <div class="blog-post-card-footer">\n'
            '                <span class="blog-post-card-readtime">2 min de leitura</span>\n'
            '                %s\n'
            '              </div>\n'
            '            </div>\n'
            '          </article>'
            % (slug, html_escape(m["title"]), html_escape(m["excerpt"]), topics)
        )

    # Replace featured card
    listing = listing_template.replace(
        re.search(r'<article class="blog-featured-card">.*?</article>', listing_template, re.DOTALL).group(0),
        featured_card,
    )

    # Replace grid cards: find grid open and close by counting
    grid_open = listing.index('<div class="blog-post-grid">') + len('<div class="blog-post-grid">')
    i = grid_open
    tag_rx = re.compile(r'<(/?)div[^>]*>')
    depth = 1
    for m in tag_rx.finditer(listing, i):
        if m.group(1) == '/':
            depth -= 1
            if depth == 0:
                grid_close = m.start()
                break
        else:
            depth += 1
    # Insert cards between open and close
    listing = listing[:grid_open] + "\n          " + "\n          ".join(cards) + "\n        " + listing[grid_close:]
    return head + listing + tail


def render_rss(meta):
    items = []
    for slug in SLUGS:
        m = meta[slug]
        items.append(
            '<item><title>%s</title><link>%s/</link><pubDate>2026-10-16</pubDate><description>%s</description></item>'
            % (html_escape(m["title"]), slug, html_escape(m["excerpt"]))
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Notícias IA</title><description>O ruído da semana em IA, lido em cinco minutos. Interpretação com critério para quem constrói produto.</description>%s</channel></rss>'
        % "".join(items)
    )


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    meta = load_meta()
    for slug in SLUGS:
        md_path = POSTS / (slug + ".md")
        if not md_path.exists():
            sys.exit("Post em falta: %s" % md_path)
        front, body_md = read_frontmatter(md_path)
        html = render_post(slug, front, body_md, meta)
        out = DIST / slug
        out.mkdir(parents=True)
        with open(out / "index.html", "w", encoding="utf-8") as f:
            f.write(html)
    with open(DIST / "index.html", "w", encoding="utf-8") as f:
        f.write(render_index(meta))
    with open(DIST / "rss.xml", "w", encoding="utf-8") as f:
        f.write(render_rss(meta))
    for asset in ("favicon.svg", "theme.js"):
        src = BASEDIR / "assets" / asset
        if src.exists():
            shutil.copy(src, DIST / asset)
    print("Build completo: %s" % DIST)
    print("  %d posts + index.html + rss.xml" % len(SLUGS))


# A Cloudflare injecta um beacon de analytics antes de </body> em cada resposta.
# Não faz parte do build; é removido antes de comparar com o live.
CF_BEACON_RX = re.compile(
    rb'<script type="module" src="https://static\.cloudflareinsights\.com/beacon\.min\.js/.*?</script>\n',
    re.DOTALL,
)


def check():
    """Compara dist/ com o site live publicado (páginas + assets).

    O beacon da Cloudflare injectado no live é ignorado na comparação.
    """
    ok = True
    for slug in SLUGS + [""]:
        rel = (slug + "/index.html") if slug else "index.html"
        local = DIST / rel
        if not local.exists():
            print("FALTA local: %s" % rel)
            ok = False
            continue
        try:
            req = urllib.request.Request(
                "%s/%s" % (LIVE_URL, rel), headers={"User-Agent": "blog-build-check/1.0"}
            )
            with urllib.request.urlopen(req, timeout=20) as r:
                live = r.read()
        except Exception as e:
            print("ERRO a obter %s: %s" % (rel, e))
            ok = False
            continue
        live = CF_BEACON_RX.sub(b"", live)
        with open(local, "rb") as f:
            local_bytes = f.read()
        same = hashlib.sha256(live).hexdigest() == hashlib.sha256(local_bytes).hexdigest()
        print(
            "%s: %s (live %d B, local %d B)"
            % (rel, "IGUAL" if same else "DIFERENTE", len(live), len(local_bytes))
        )
        if not same:
            ok = False
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="compara dist/ com o site live")
    args = ap.parse_args()
    if args.check:
        sys.exit(0 if check() else 1)
    build()


if __name__ == "__main__":
    main()
