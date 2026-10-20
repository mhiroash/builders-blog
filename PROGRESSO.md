# PROGRESSO — TASK-2026-10-18-012
Publicar os 7 posts corrigidos do blog IA + build stdlib + backup diário.

## Passo 0 — Reconhecimento (18/10)
- `/workspace/builders-blog` existe e tem: `posts/` (7 md), `scripts/` (build.py, deploy.sh, backup.sh, extract_posts.py), `templates/`, `assets/`, `dist/`, `dist-live/`, `docs/`, `reconstituicao/`, `seguranca/`.
- `dist-live/` é a cópia do site publicado que sobreviveu ao apagão; `dist/` é o build local actual.
- **Site live responde HTTP 200** e o post `agentes-que-correm-sozinhos/` é **byte-idêntico** a `dist-live/agentes-que-correm-sozinhos/index.html`.
- **Os 7 posts live AINDA têm marcadores `[confirmar]`** (4 no post de exemplo). Os `posts/*.md` em disco também têm 4–7 cada.
- `scripts/build.py` actual importa `markdown` (dependência fora da stdlib) — é isso que o ADR proíbe.

## Passo 1 — build.py só com stdlib — FEITO ✅
- [x] `markdown_body()` substituído por renderer stdlib (parágrafos, `###`, listas `- `, `**bold**`, `` `code` ``, `_em_`).
- [x] `pip uninstall markdown` → `import markdown` dá ModuleNotFoundError; `python3 scripts/build.py` corre na mesma.
- [x] `python3 scripts/build.py` produz `dist/` **byte-idêntico** ao build anterior com a lib `markdown` (diff -rq: sem diferenças).
- [x] `python3 scripts/build.py --check` → 8/8 páginas IGUAL (exit 0).
- [x] `bash scripts/deploy.sh --check` → exit 0.
- [x] **Diferença documentada:** o live serve o HTML com um beacon de analytics da Cloudflare injectado antes de `</body>` (367 B). O `--check` remove-o antes de comparar.
- Prova: `docs/prova-build-stdlib.md`. Backup do build antigo: `scripts/build.py.bak-markdown`.

## Passo 2 — publicar os 7 posts corrigidos — NÃO CUMPRIDO ⛔ (bloqueado por perda de dados)
- [x] Busca exaustiva dos textos corrigidos (513–597 palavras, 0 `[confirmar]`): disco, dist, dist-live, todos os 4 commits do GitHub, backups tarball, `/tmp` (todos os arquivos), 9 sessões anteriores, índice de sessões, memória da equipa, `/tmp/scan_*`, assinaturas `METR`/`OpenRouter`.
- [x] **Conclusão: os textos corrigidos não existem em lado nenhum.** Perderam-se no apagão de 17/10; a reconstituição foi feita a partir do live (versão antiga). O relatório `agentes/relatorio-correccao-posts.md` referido na tarefa original também já não existe.
- [x] **Sinalizado, não inventado** — conforme a tarefa manda.
- [x] Site live confirmado por HTTP a servir a versão antiga (4 e 7 marcadores nos dois posts testados).
- Prova: `docs/prova-posts-corrigidos.md`.

## Passo 3 — backup diário — PARCIAL ⚠️
- [x] `scripts/backup.sh` faz tarball datado + push git.
- [x] Cron instalado: `15 3 * * *` (03:15 diário).
- [x] Testado uma vez: `builders-blog-2026-10-18.tar.gz` (119 984 B, md5 `08117a59…`).
- [x] **Falha encontrada e corrigida:** o repo local não tinha remote `origin` — o push off-site falhava em silêncio. Adicionado `origin`.
- [x] **Push off-site completado via conector GitHub** (o `git push` falha por falta de credenciais; o conector está autenticado). Commit `73be244` no branch `main`.
- [ ] **Pendente:** o `backup.sh` ainda usa `git push` (que falha sem credenciais). Deve passar a usar o conector GitHub para o passo off-site, ou o dono tem de criar uma credencial GitHub no cofre.
- Prova: `docs/prova-backup-diario.md`.

## Veredicto global
- Ponto 1 (build stdlib): **CUMPRIDO**.
- Ponto 2 (posts corrigidos publicados): **NÃO CUMPRIDO** — impossível sem inventar conteúdo (perda de dados no apagão). Sinalizado.
- Ponto 3 (backup diário): **PARCIAL** — tarball testado e cron activo; push off-site feito manualmente via conector, mas o script ainda não o faz sozinho.
- `deploy.sh --check`: **passa** (exit 0).
