#!/usr/bin/env python3
"""Build script para o Blog de Notícias IA.

Stack: Markdown → build.py → dist → tivra-publish
"""

import html as html_lib
import re
import shutil
from pathlib import Path

# Configuração
POSTS_DIR = Path("posts")
DIST_DIR = Path("dist")

def slugify(title: str) -> str:
    """Converter título em slug. Remove tudo o que não seja alfanumérico/hífen."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s-]+", "-", slug)
    slug = slug.strip("-")
    # Defesa: nunca permitir separadores de caminho no slug
    if not slug or "/" in slug or "\\" in slug or slug.startswith("."):
        raise ValueError(f"Slug inválido: {title!r}")
    return slug

def render_html(text: str) -> str:
    """
    Converter texto em HTML com escape de segurança.
    Usa html.escape() para prevenir XSS/HTML injection.
    """
    # Escape de HTML antes de qualquer processamento
    text = html_lib.escape(text)

    # Headers
    text = re.sub(r"^# (.*$)", r"<h1>\1</h1>", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.*$)", r"<h2>\1</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^### (.*$)", r"<h3>\1</h3>", text, flags=re.MULTILINE)

    # Bold (apenas texto, não tags HTML)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    # Code (insere tags <code> sem escape adicional — já escapado)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)

    # Lists
    lines = text.split("\n")
    in_list = False
    result = []
    for line in lines:
        if line.strip().startswith("- "):
            if not in_list:
                result.append("<ul>")
                in_list = True
            # Escape o conteúdo do <li> antes de inserir
            content = html_lib.escape(line.strip()[2:])
            result.append(f"  <li>{content}</li>")
        elif line.strip() == "":
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append("")
        else:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(line)
    if in_list:
        result.append("</ul>")
    text = "\n".join(result)

    # Links: escapar href e bloquear javascript: e data:
    def safe_link(match):
        text = match.group(1)  # texto do link
        href = match.group(2)  # href

        # Bloquear javascript: e (injecção de código)
        if href.lower().startswith(('javascript:', 'data:')):
            # Retornar apenas o texto do link, sem href
            return f"{text}"

        # Escape href
        href = html_lib.escape(href)

        return f"<a href='{href}'>{html_lib.escape(text)}</a>"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", safe_link, text)

    return text

def render_markdown(md_path: Path) -> str:
    """Renderizar Markdown para HTML (wrapper)."""
    md = md_path.read_text(encoding='utf-8')
    return render_html(md)

def build():
    """Construir o blog estático."""
    DIST_DIR.mkdir(exist_ok=True)

    # Limpar dist/
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()

    # Copiar assets
    assets = [
        ("dist-live/favicon.svg", "favicon.svg"),
        ("dist-live/rss.xml", "rss.xml"),
    ]
    for src, dst in assets:
        src_path = Path(src)
        if src_path.exists():
            shutil.copy(src_path, DIST_DIR / dst)
            print(f"✓ {dst}")

    # CSS do site live (extraído do index.html)
    css = """/* Blog Design Tokens */
body {
    font-family: Inter, system-ui, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 1rem;
    line-height: 1.6;
    background: #fff;
    color: #0A0A0A;
}

a {
    text-decoration: none;
}

.blog-header-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.blog-logo {
    font-weight: 700;
    font-size: 1.5rem;
}

.blog-nav-links {
    display: flex;
    gap: 1rem;
}

.blog-nav-link {
    color: #0A0A0A;
    text-decoration: underline;
}

.blog-post-title {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    line-height: 1.2;
}

.blog-post-meta {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.blog-post-author {
    font-size: 0.95rem;
    color: #333;
}

.blog-post-content p {
    margin-bottom: 1rem;
}

.blog-post-content h3 {
    font-size: 1.4rem;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
}

.blog-post-content ul {
    margin-bottom: 1rem;
    padding-left: 2rem;
}

.blog-post-content li {
    margin-bottom: 0.5rem;
}

.blog-post-content strong {
    font-weight: 600;
}

.blog-post-content code {
    background: #f4f4f4;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: monospace;
}

.blog-read-link {
    color: #0A0A0A;
    text-decoration: underline;
}

.blog-badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 600;
}

.blog-badge.success {
    background: #e0f2fe;
    color: #0369a1;
}

.blog-skip-link {
    position: absolute;
    top: 0;
    left: 0;
    padding: 1rem;
    z-index: 100;
}

.blog-theme-toggle {
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
}
"""

    (DIST_DIR / "blog.css").write_text(css, encoding='utf-8')
    print(f"✓ blog.css")

    # Gerar HTML para cada post
    for md_file in POSTS_DIR.glob("*.md"):
        match = re.match(r"^(?P<title>[^/]+)\.md$", md_file.name)
        if not match:
            continue

        title = match.group("title")
        slug = slugify(title)
        print(f"→ {md_file.name} → {slug}")

        html_content = render_markdown(md_file)

        # Template de post
        template = f"""<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Notícias IA</title>
  <meta name="description" content="Notícias IA — interpretação com critério">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="alternate" type="application/rss+xml" href="/rss.xml">
  <link rel="stylesheet" href="/blog.css">
</head>
<body>
  <a href="#conteudo" class="blog-skip-link">Saltar para o conteúdo</a>
  <header class="blog-header-nav">
    <a href="/" class="blog-logo">Notícias<span>IA</span></a>
    <nav class="blog-nav-links" aria-label="Navegação principal">
      <a href="/" class="blog-nav-link" aria-current="page">Artigos</a>
      <a href="#" class="blog-nav-link">Arquivo</a>
      <a href="#" class="blog-nav-link">Sobre</a>
    </nav>
    <button type="button" class="blog-theme-toggle" aria-label="Alternar tema claro e escuro">
      <span aria-hidden="true">◐</span>
    </button>
  </header>
  <main id="conteudo">
    <article class="blog-post-header">
      <div class="blog-container">
        <header>
          <div class="blog-post-meta">
            <time datetime="2026-10-16">16 de Outubro de 2026</time>
            <span aria-hidden="true">·</span>
            <span>2 min de leitura</span>
            <span aria-hidden="true">·</span>
            <span class="blog-badge success">Publicado</span>
          </div>
          <h1 class="blog-post-title">{title}</h1>
        </header>
        <footer>
          <p class="blog-post-author">
            Por <a href="#">Tivra</a> · Redacção assistida por IA, revista por humano
          </p>
        </footer>
      </div>
    </article>
    <div class="blog-post-content">
{html_content}
    </div>
  </main>
  <footer>
    <p><a href="/" class="blog-read-link">← todos os artigos</a></p>
  </footer>
</body>
</html>"""

        post_dir = DIST_DIR / slug
        post_dir.mkdir(exist_ok=True)
        (post_dir / "index.html").write_text(template, encoding='utf-8')
        print(f"  ✓ {slug}/index.html")

    # Sitemap
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://noticias-ia-cndd-sites.tivrai.dev/</loc><changefreq>weekly</changefreq></url>
"""
    for md_file in POSTS_DIR.glob("*.md"):
        match = re.match(r"^(?P<title>[^/]+)\.md$", md_file.name)
        if not match:
            continue
        slug = slugify(match.group("title"))
        sitemap += f'  <url><loc>https://noticias-ia-cndd-sites.tivrai.dev/{slug}/</loc><changefreq>weekly</changefreq></url>\n'
    sitemap += "</urlset>"
    (DIST_DIR / "sitemap.xml").write_text(sitemap, encoding='utf-8')
    print(f"  ✓ sitemap.xml")

    print(f"\n✓ Build completo: {len(list(POSTS_DIR.glob('*.md')))} posts → {DIST_DIR}")

if __name__ == "__main__":
    build()