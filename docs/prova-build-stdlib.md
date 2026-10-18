# Prova — build.py só com stdlib (TASK-2026-10-18-012, ponto 1)

Data: 18/10/2026 · Autor: Agentes

## O que era
`scripts/build.py` importava a biblioteca `markdown` (fora da stdlib), proibida pelo
ADR de stack de publicação (stack estática, build Python stdlib).

## O que foi feito
`markdown_body()` foi substituído por um renderer stdlib que cobre exactamente as
construções usadas nos posts:

| Construção Markdown | HTML gerado |
|---|---|
| parágrafo | `<p>…</p>` |
| `### Título` | `<h3>Título</h3>` |
| `**negrito**` | `<strong>…</strong>` |
| `` `código` `` | `<code>…</code>` |
| `_itálico_` | `<em>…</em>` |
| `- item` | `<ul><li>…</li></ul>` |

Imports efectivos do ficheiro (todos stdlib):
`argparse, hashlib, json, os, re, shutil, sys, urllib.request, pathlib`.

## Prova A — o build corre sem a lib `markdown`

```
$ pip uninstall -y markdown
$ python3 -c "import markdown"
ModuleNotFoundError: No module named 'markdown'

$ python3 scripts/build.py
Build completo: /workspace/builders-blog/dist
  7 posts + index.html + rss.xml
```

## Prova B — o dist é idêntico ao build anterior (com a lib)

```
$ diff -rq dist/ dist-live/
(sem diferenças)
```

## Prova C — `--check` confirma 8/8 páginas iguais ao site live

```
$ python3 scripts/build.py --check
agentes-que-correm-sozinhos/index.html: IGUAL (live 47860 B, local 47860 B)
benchmark-nao-mede-o-teu-caso/index.html: IGUAL (live 47844 B, local 47844 B)
custo-do-contexto-longo/index.html: IGUAL (live 47898 B, local 47898 B)
ferramentas-de-agente/index.html: IGUAL (live 47926 B, local 47926 B)
modelos-abertos-vs-fronteira/index.html: IGUAL (live 48274 B, local 48274 B)
soberania-de-dados/index.html: IGUAL (live 47949 B, local 47949 B)
uma-chave-dezanove-fornecedores/index.html: IGUAL (live 48430 B, local 48430 B)
index.html: IGUAL (live 51771 B, local 51771 B)
exit 0
```

## Diferença documentada
O site live serve o HTML com um beacon de analytics da Cloudflare injectado antes
de `</body>` (367 B). O `--check` remove-o antes de comparar; sem isso todas as
páginas apareceriam "DIFERENTE" por causa desses 367 B.

Backup do build anterior (com a lib): `scripts/build.py.bak-markdown`.

## Veredicto do ponto 1: CUMPRIDO
