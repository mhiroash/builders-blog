#!/usr/bin/env python3
"""Extrair posts em Markdown a partir do HTML publicado."""

from bs4 import BeautifulSoup
from pathlib import Path

def extract_markdown(html: str, slug: str) -> str:
    """Converter HTML do post em Markdown."""
    soup = BeautifulSoup(html, 'lxml')

    # Título
    title_tag = soup.find('h1', class_='blog-post-title')
    title = title_tag.get_text(strip=True) if title_tag else slug.replace('-', ' ').title()

    # Data
    time_tag = soup.find('time')
    date = time_tag.get_text(strip=True) if time_tag else ""

    # Conteúdo
    content_div = soup.find('div', class_='blog-post-content')
    if not content_div:
        return ""

    lines = []
    if date:
        lines.append(f"**{date}**")
        lines.append("")
    lines.append(f"# {title}")
    lines.append("")

    # Processar filhos
    for child in content_div.children:
        if child.name is None:
            continue
        elif child.name in ('h3', 'h2'):
            text = child.get_text(strip=True)
            lines.append(f"## {text}")
            lines.append("")
        elif child.name == 'p':
            text = child.get_text(' ', strip=True)
            lines.append(text)
        elif child.name == 'strong':
            text = child.get_text(strip=True)
            if not text.startswith('[confirmar'):
                lines.append(f"**{text}**")
        elif child.name == 'ul':
            lines.append("")
            for li in child.find_all('li', recursive=False):
                text = li.get_text(' ', strip=True)
                lines.append(f"- {text}")
        elif child.name == 'li':
            text = child.get_text(' ', strip=True)
            lines.append(f"- {text}")

    return '\n'.join(lines)

def main():
    dist_live = Path("dist-live")
    posts_dir = Path("posts")

    posts_dir.mkdir(exist_ok=True)

    slugs = [
        "agentes-que-correm-sozinhos",
        "benchmark-nao-mede-o-teu-caso",
        "custo-do-contexto-longo",
        "ferramentas-de-agente",
        "modelos-abertos-vs-fronteira",
        "soberania-de-dados",
        "uma-chave-dezanove-fornecedores",
    ]

    for slug in slugs:
        html_file = dist_live / slug / "index.html"
        if html_file.exists():
            html = html_file.read_text(encoding='utf-8', errors='ignore')
            md_content = extract_markdown(html, slug)
            md_file = posts_dir / f"{slug}.md"
            md_file.write_text(md_content, encoding='utf-8')
            print(f"✓ {slug}.md ({len(md_content)} chars)")
        else:
            print(f"✗ {slug}.html não encontrado")

    print(f"\nTotal: {len(list(posts_dir.glob('*.md')))} posts")

if __name__ == "__main__":
    main()