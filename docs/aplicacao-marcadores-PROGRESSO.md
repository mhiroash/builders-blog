# Progresso — TASK-2026-10-20-030
Aplicar as correcções dos 42 marcadores aos posts do blog IA.
Fonte: `docs/verificacao-marcadores.md` (versão actual, commit cf5559b).

## Estado final — COMPLETO ✅ (20/10)

**Descoberta-chave:** 6 dos 7 posts já estavam corrigidos em disco (trabalho do turno anterior
aplicado antes de morrer). Só o `uma-chave-*` tinha os 7 marcadores. Verificado marcador a marcador
contra a verificação antes de confiar.

| Post | Marcadores | Estado |
|---|---|---|
| agentes-que-correm-sozinhos | 4 | já corrigido (verificado: frases do METR verbatim, fontes completas) |
| benchmark-nao-mede-o-teu-caso | 6 | já corrigido (verificado: L33 reescrita com v4.3.2; L35/L44/L45 removidos) |
| custo-do-contexto-longo | 7 | já corrigido (verificado: L33/L45 removidos; fontes com preços) |
| ferramentas-de-agente | 5 | já corrigido (verificado: incidente removido; fontes reescritas) |
| modelos-abertos-vs-fronteira | 6 | já corrigido (verificado: «12 pontos, 46 contra 58» na L15) |
| soberania-de-dados | 7 | já corrigido (verificado: artigos 28.º(2) e 44.º na L17 e nas fontes) |
| uma-chave-**muitos**-fornecedores | 7 | **corrigido neste turno** (era o único com marcadores) |

## O que foi feito neste turno no `uma-chave-muitos-fornecedores`
- L23: termos do OpenRouter citados (versão 31/08/2026, secções 4.6 e 5.5).
- L31: frase «não existe caso público» substituída pelo estudo arXiv:2609.31288
  (5 139 migrações; 82% depois do encerramento; 94% hard-coded; 8% trocam de fornecedor).
- L33: taxas do OpenRouter (Standard 5,5% / Business 8%) + comportamento na mudança de preço.
- L43-46: lista de fontes reescrita — Piramyd com a contradição declarada (54 vs 56, fornecedores
  não publicados), OpenRouter pricing/terms, arXiv, preços directos DeepSeek/OpenAI/Anthropic.
- **Título e slug revistos:** «dezanove fornecedores» → «muitos fornecedores»
  (o número não tem suporte publicado; o site contradiz-se). Slug: `uma-chave-muitos-fornecedores`.
- Slug actualizado nos 4 sítios que o build usa: `scripts/build.py` (SLUGS), `scripts/extract_posts.py`,
  `templates/post-meta.json` (título+excerpt também), `templates/index-listing.html` (título+excerpt).
- Ficheiro renomeado: `posts/uma-chave-dezanove-fornecedores.md` → `posts/uma-chave-muitos-fornecedores.md`.

## Verificação
- `grep '\[confirmar'` em posts/: **0** em 7 ficheiros.
- `grep 'dezanove'` em posts/, scripts e templates: **0**.
- `python3 scripts/build.py`: build completo, 7 posts + index + rss.
- `grep '\[confirmar'` em dist/: **0**.
- `build.py --check`: diferenças esperadas — o live ainda serve a versão antiga (slugs antigos,
  marcadores presentes) e o novo slug dá 404 no live. **Publicar é passo separado e exige aprovação.**

## Pendências (fora do âmbito desta tarefa)
- Deploy do `dist/` para o live (exige aprovação do dono; `scripts/deploy.sh`).
- O `backup.sh` ainda usa `git push` sem credenciais (ver PROGRESSO.md da TASK-2026-10-18-012).
