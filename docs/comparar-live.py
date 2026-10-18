#!/usr/bin/env python3
"""Comparar o build local com o site live (texto extraído)."""

import re
import subprocess
import difflib
from pathlib import Path
from bs4 import BeautifulSoup

SLUGS = [
    "agentes-que-correm-sozinhos",
    "benchmark-nao-mede-o-teu-caso",
    "custo-do-contexto-longo",
    "ferramentas-de-agente",
    "modelos-abertos-vs-fronteira",
    "soberania-de-dados",
    "uma-chave-dezanove-fornecedores",
]

BASE = "https://noticias-ia-cndd-sites.tivrai.dev"

def text_of(html: str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='blog-post-content')
    if not content:
        return ""
    return re.sub(r'\s+', ' ', content.get_text(' ', strip=True)).strip()

def words(text: str) -> int:
    return len(text.split())

report = []
report.append("COMPARAÇÃO BUILD LOCAL vs SITE LIVE")
report.append("=" * 60)
report.append("")

total_local = 0
total_live = 0

for slug in SLUGS:
    # Local
    local_file = Path("dist") / slug / "index.html"
    local_html = local_file.read_text(encoding='utf-8') if local_file.exists() else ""
    local_text = text_of(local_html)

    # Live
    r = subprocess.run(["curl", "-sS", f"{BASE}/{slug}/index.html"], capture_output=True, text=True)
    live_html = r.stdout
    live_text = text_of(live_html)

    lw = words(local_text)
    vw = words(live_text)
    total_local += lw
    total_live += vw

    # Confirmar marcadores
    local_conf = local_text.count('[confirmar')
    live_conf = live_text.count('[confirmar')

    # Similaridade
    if live_text:
        ratio = difflib.SequenceMatcher(None, local_text, live_text).ratio()
    else:
        ratio = 0.0

    report.append(f"{slug}")
    report.append(f"  palavras: local={lw}  live={vw}")
    report.append(f"  [confirmar]: local={local_conf}  live={live_conf}")
    report.append(f"  similaridade texto: {ratio:.1%}")
    report.append("")

report.append("=" * 60)
report.append(f"TOTAL palavras: local={total_local}  live={total_live}")
report.append("")

Path("/tmp/comparacao.txt").write_text("\n".join(report), encoding='utf-8')
print("\n".join(report))
