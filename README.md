# Blog de Notícias IA — código-fonte

Código-fonte do blog **Notícias IA**, publicado em
<https://noticias-ia-cndd-sites.tivrai.dev>.

> **Nota de reconstituição (2026-10-17).** O `/workspace` foi apagado na recriação da
> máquina (18/10) e este projecto não era repo git — o código-fonte perdeu-se. Este
> repositório foi reconstituído a partir do HTML publicado (única fonte sobrevivente),
> conforme TASK-2026-10-17-028. O site no ar **não foi alterado**.

## Stack

Estático: **Markdown → `scripts/build.py` → `dist/` → `tivra-publish`**.

Decisão registada em `devops/adr-stack-publicacao.md` (ADR, custo $0/mês).

## Estrutura

```
posts/              7 posts em Markdown (fonte editorial)
scripts/build.py    gerador estático (Markdown → HTML)
scripts/deploy.sh   build + verificações + publicação
docs/               guias de reconstituição e ferramentas
devops/             ADR da stack de publicação
seguranca/          relatório de segurança do build
dist/               saída do build (não versionada)
```

## Uso

```bash
# Gerar o site
python3 scripts/build.py

# Publicar (requer tivra-publish e aprovação)
./scripts/deploy.sh
```

## Estado do conteúdo

Os 7 posts em `posts/` foram extraídos do HTML publicado. O site live ainda contém os
**42 marcadores `[confirmar]`** e ~400–500 palavras por post — é a versão anterior às
correcções de QA. A versão corrigida (513–597 palavras, 0 marcadores), aprovada e
entregue em TASK-2026-10-16-012, **perdeu-se no apagão** e não está no site live.

Ver `docs/diferencas-build-local-live.md` para a comparação build local vs. live.
