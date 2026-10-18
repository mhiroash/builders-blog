# PROGRESSO — TASK-2026-10-18-012

Publicar os 7 posts corrigidos do blog IA + build stdlib + backup diário.

## Passo 0 — Reconhecimento (18/10)

- `/workspace/builders-blog` existe e tem: `posts/` (7 md), `scripts/` (build.py, deploy.sh, backup.sh, extract_posts.py), `templates/`, `assets/`, `dist/`, `dist-live/`, `docs/`, `reconstituicao/`, `seguranca/`.
- `dist-live/` é a cópia do site publicado que sobreviveu ao apagão; `dist/` é o build local actual.
- **Site live responde HTTP 200** e o post `agentes-que-correm-sozinhos/` é **byte-idêntico** a `dist-live/agentes-que-correm-sozinhos/index.html`.
- **Os 7 posts live AINDA têm marcadores `[confirmar]`** (4 no post de exemplo). Os `posts/*.md` em disco também têm 4 cada.
- `scripts/build.py` actual importa `markdown` (dependência fora da stdlib) — é isso que o ADR proíbe.

## Passo 1 — build.py só com stdlib — FEITO

- [x] `markdown_body()` substituído por renderer stdlib (parágrafos, `###`, listas `- `, `**bold**`, `` `code` ``, `_em_`).
- [x] `pip uninstall markdown` → `import markdown` dá ModuleNotFoundError; `python3 scripts/build.py` corre na mesma.
- [x] `python3 scripts/build.py` produz `dist/` **byte-idêntico** ao build anterior com a lib `markdown` (diff -rq: sem diferenças).
- [x] `python3 scripts/build.py --check` → 8/8 páginas IGUAL (exit 0).
- [x] **Diferença documentada:** o live serve o HTML com um beacon de analytics da Cloudflare injectado antes de `</body>` (367 B). O `--check` remove-o antes de comparar; sem isso todas as páginas apareciam "DIFERENTE" por causa desses 367 B.
- Backup do build antigo: `scripts/build.py.bak-markdown`.

## Passo 2 — publicar os 7 posts corrigidos

- [ ] localizar os textos corrigidos (513-597 palavras, 0 `[confirmar]`)
- [ ] se não existirem em lado nenhum, sinalizar (não inventar)

## Passo 3 — backup diário

- [ ] montar e testar
