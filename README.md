# Blog de notícias IA

Blog de interpretação de notícias de IA para quem constrói produto. Stack estática
própria, custo zero mensal, sem lock-in.

**Site publicado:** https://noticias-ia-cndd-sites.tivrai.dev

## Estrutura

```
posts/              7 posts em Markdown (fonte de verdade)
templates/          templates HTML/CSS recuperados do site publicado
assets/             favicon.svg, theme.js
scripts/build.py    Markdown -> dist/ (HTML estático)
scripts/deploy.sh   build + verificação + envio para aprovação (tivra-publish)
scripts/backup.sh   backup diário (tarball local + push git)
scripts/extract_posts.py  ferramenta de reconstituição (não faz parte do build)
docs/devops/        ADR e documentação de infraestrutura
dist/               saída do build (não versionada)
```

## Build

```bash
pip install markdown
python3 scripts/build.py           # gera dist/
python3 scripts/build.py --check   # compara dist/ com o site live
```

O build reproduz o site publicado byte a byte (verificado em 18/10/2026).

## Deploy

```bash
./scripts/deploy.sh          # build + verificação + envio para aprovação
./scripts/deploy.sh --check  # só verifica
```

Nada é publicado sem aprovação do dono (gate 3 do Builders).

## Backup

`scripts/backup.sh` corre diariamente às 03:15 (cron) e faz:
1. tarball datado em `/workspace/backups/builders-blog/` (retém 14 dias);
2. commit + push para o GitHub (backup off-site).

O disco local não é backup fiável — o push para o GitHub é o que garante a recuperação.

## Segurança

- Sem execução de código no servidor (estático).
- CSP estrito (`default-src 'self'`).
- Sem segredos no repo.
- Checklist de segurança: `seguranca/relatorio-seguranca-blog-ia.md`.

## Contexto

- ADR: `docs/devops/adr-stack-publicacao.md`
- Reconstituição após o apagão de 17/10: `docs/devops/reconstituicao.md`
