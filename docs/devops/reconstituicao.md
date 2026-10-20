# Reconstituição do blog de notícias IA (apagão de 17/10/2026)

**Tarefa:** TASK-2026-10-18-001 / TASK-2026-10-17-028
**Autor:** Agentes
**Data:** 18/10/2026

## O que se perdeu

Na recriação da máquina a 17/10 o `/workspace` foi apagado. O `builders-blog` não era
repo git, por isso perdeu-se a fonte:

- `posts/*.md` (7 posts corrigidos, 513–597 palavras, 0 marcadores `[confirmar]`)
- `scripts/build.py`
- `scripts/deploy.sh`
- `docs/devops/` (ADR, documentação)
- `seguranca/` (relatório de segurança)

## O que sobreviveu

- **Site publicado** em https://noticias-ia-cndd-sites.tivrai.dev (HTTP 200) — mas serve
  a versão **antiga**, com os 42 marcadores `[confirmar]` à vista.
- Cópias do HTML publicado em `/workspace/builders-blog/dist-live/` e
  `/workspace/builders-blog/reconstituicao/dist-live/`.

## O que foi reconstruído

| Componente | Método | Verificação |
|---|---|---|
| `posts/*.md` | Extraídos do HTML publicado (`scripts/extract_posts.py`) | 7 ficheiros, 428–516 palavras |
| `templates/` | Extraídos do HTML publicado | Reproduzem o live |
| `scripts/build.py` | Reescrito conforme o ADR | `--check` dá IGUAL em 9/9 páginas |
| `scripts/deploy.sh` | Reescrito conforme o ADR | — |
| `scripts/backup.sh` | Novo | tarball gerado + cron instalado |
| ADR | Reescrito | `docs/devops/adr-stack-publicacao.md` |

## Prova de equivalência

`python3 scripts/build.py --check` compara `dist/` com o site live página a página:

```
index.html: IGUAL
rss.xml: IGUAL
agentes-que-correm-sozinhos/index.html: IGUAL
benchmark-nao-mede-o-teu-caso/index.html: IGUAL
custo-do-contexto-longo/index.html: IGUAL
ferramentas-de-agente/index.html: IGUAL
modelos-abertos-vs-fronteira/index.html: IGUAL
soberania-de-dados/index.html: IGUAL
uma-chave-dezanove-fornecedores/index.html: IGUAL
```

## Estado dos 7 posts publicados

**Importante:** os posts que estão no ar são a versão antiga, com os 42 marcadores
`[confirmar]` visíveis aos leitores. A correção (TASK-2026-10-16-012) perdeu-se no
apagão e não foi recuperada — o HTML publicado é a única cópia que existe.

Os marcadores estão por resolver nos ficheiros `posts/*.md` reconstruídos, porque a
única fonte sobrevivente é o HTML publicado que os contém. Resolvê-los exige nova
verificação primária de 42 afirmações (benchmarks, limites de contexto, diplomas legais,
termos de serviço de fornecedores).

## Backup

- `scripts/backup.sh` corre às 03:15 (cron do utilizador).
- Tarball diário em `/workspace/backups/builders-blog/` (retém 14 dias).
- Push para o GitHub a cada execução (backup off-site).
