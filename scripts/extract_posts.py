#!/usr/bin/env python3
"""Extrai os 7 posts publicados (dist-live/*/index.html) para Markdown.

Ferramenta de reconstituição (TASK-2026-10-18-001). Não faz parte do
pipeline de build; corre uma vez para recuperar a fonte a partir do HTML
publicado que sobreviveu ao apagão de 17/10.

O Markdown gerado é a fonte de verdade do repo. O build.py consome-o e
reproduz o HTML publicado (verificado com `build.py --check`).
"""
import re
import html
import os
import sys

SLUGS = [
    "agentes-que-correm-sozinhos",
    "benchmark-nao-mede-o-teu-caso",
    "custo-do-contexto-longo",
    "ferramentas-de-agente",
    "modelos-abertos-vs-fronteira",
    "soberania-de-dados",
    "uma-chave-muitos-fornecedores",
]

INLINE = [
    (re.compile(r"<code>(.*?)</code>", re.DOTALL), r"`\1`"),
    (re.compile(r"<strong>(.*?)</strong>", re.DOTALL), r"**\1**"),
    (re.compile(r"<em>(.*?)</em>", re.DOTALL), r"*\1*"),
    (re.compile(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', re.DOTALL), r"[\2](\1)"),
]


def inline(text):
    for rx, repl in INLINE:
        text = rx.sub(repl, text)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def split_blocks(content):
    """Divide HTML em blocos de nível superior (tags balanceadas)."""
    blocks = []
    depth = 0
    start = None
    tag_rx = re.compile(r"<(/?)([a-zA-Z0-9]+)[^>]*?(/?)>")
    for m in tag_rx.finditer(content):
        closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if name in ("br", "img", "hr", "input", "meta", "link"):
            continue
        if not closing:
            if depth == 0:
                start = m.start()
            if not selfclose:
                depth += 1
        else:
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append(content[start:m.end()])
                start = None
    return blocks


def block_to_md(block):
    block = block.strip()
    if not block:
        return ""
    m = re.match(r"<h2[^>]*>(.*?)</h2>", block, re.DOTALL)
    if m:
        return "## " + inline(m.group(1))
    m = re.match(r"<h3[^>]*>(.*?)</h3>", block, re.DOTALL)
    if m:
        return "### " + inline(m.group(1))
    m = re.match(r"<p[^>]*>(.*?)</p>", block, re.DOTALL)
    if m:
        return inline(m.group(1))
    m = re.match(r"<blockquote[^>]*>(.*?)</blockquote>", block, re.DOTALL)
    if m:
        return "> " + inline(m.group(1))
    m = re.match(r"<ul[^>]*>(.*?)</ul>", block, re.DOTALL)
    if m:
        items = re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.DOTALL)
        return "\n".join("- " + inline(i) for i in items)
    m = re.match(r"<ol[^>]*>(.*?)</ol>", block, re.DOTALL)
    if m:
        items = re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.DOTALL)
        return "\n".join("%d. %s" % (n + 1, inline(i)) for n, i in enumerate(items))
    return inline(block)


def extract(slug, src_dir):
    path = os.path.join(src_dir, slug, "index.html")
    with open(path, encoding="utf-8") as f:
        c = f.read()

    title_m = re.search(r'<h1 class="blog-post-title">(.*?)</h1>', c, re.DOTALL)
    title = html.unescape(title_m.group(1)) if title_m else slug

    desc_m = re.search(r'<meta name="description" content="([^"]*)"', c)
    desc = html.unescape(desc_m.group(1)) if desc_m else ""

    date_m = re.search(r'<time datetime="([^"]*)"', c)
    date = date_m.group(1) if date_m else ""

    tags_m = re.search(r'<div class="blog-post-tags">(.*?)</div>', c, re.DOTALL)
    tags = re.findall(r"<span[^>]*>([^<]+)</span>", tags_m.group(1)) if tags_m else []
    tags = [html.unescape(t).strip() for t in tags if t.strip()]

    cd_start = c.find('<div class="blog-post-content">')
    # O conteúdo termina no fecho do div, antes do container das tags
    tags_idx = c.find('<div class="blog-post-tags">', cd_start)
    cd_end = c.rfind("</div>", cd_start, tags_idx)
    content = c[cd_start:cd_end]

    # O lead é uma <p class="blog-lead"> — vira itálico no Markdown
    lead_m = re.search(r'<p class="blog-lead">(.*?)</p>', content, re.DOTALL)
    lead = inline(lead_m.group(1)) if lead_m else ""
    content = re.sub(r'<p class="blog-lead">.*?</p>', "", content, flags=re.DOTALL)
    content = content.replace('<div class="blog-post-content">', "")

    body_blocks = [block_to_md(b) for b in split_blocks(content)]
    body = "\n\n".join(b for b in body_blocks if b)

    front = ["---", "title: %s" % title, "slug: %s" % slug, "date: %s" % date]
    if desc:
        front.append("description: %s" % desc)
    if tags:
        front.append("tags: [%s]" % ", ".join(tags))
    front.append("---")

    parts = ["\n".join(front), "# %s" % title]
    if lead:
        parts.append("_" + lead + "_")
    parts.append(body)
    return "\n\n".join(parts) + "\n"


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "dist-live"
    out = sys.argv[2] if len(sys.argv) > 2 else "posts"
    os.makedirs(out, exist_ok=True)
    for slug in SLUGS:
        md = extract(slug, src)
        dest = os.path.join(out, slug + ".md")
        with open(dest, "w", encoding="utf-8") as f:
            f.write(md)
        body = md.split("---", 2)[-1]
        words = len(re.sub(r"[#*`\[\]()_]", "", body).split())
        print("%s -> %s (%d palavras)" % (slug, dest, words))


if __name__ == "__main__":
    main()
