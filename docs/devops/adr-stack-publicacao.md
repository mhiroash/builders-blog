# ADR-ALT-2026-001 — Stack de publicação do Blog de notícias IA

**Data:** 18/10/2026
**Status:** Aprovado
**Autor:** Arquiteto
**Aprovação:** Dev (líder)

## Decisão

O blog de notícias IA usa uma stack estática própria:
- Markdown (pasta `posts/`) como fonte única
- Python (scripts/build.py) para build e transformações
- Pasta `dist/` como publicação estática
- Script (scripts/deploy.sh) para deploy com `tivra-publish`
- Deploy automático para `*-sites.tivrai.dev`

**URL pública:** https://noticias-ia-cndd-sites.tivrai.dev

## Motivação

- **Custo zero mensal:** Nenhum servidor de aplicação, nenhum runtime dinâmico.
- **Lock-in zero:** Nenhuma dependência específica de plataforma.
- **Controle total:** CSS, HTML, Markdown editáveis sem pipeline de build complexo.
- **Segurança:** Sem execução de código no servidor, sem base de dados exposta.

## Alternativas consideradas

- **Next.js / React:** Runtime Node.js, custo $5–20/mês, lock-in de framework.
- **Jekyll / Hugo:** Build estático, mas dependência de Ruby/Go; menos flexível para transformações customizadas.
- **CMS (WordPress/Contentful):** Custo $20–50/mês + dependência, overhead de gestão.

## Decisão final

Stack própria Markdown → build.py → dist → deploy.sh → tivra-publish.

## Provas

- Infraestrutura verificada e publicada por DevOps (TASK-006).
- URL pública responde HTTP 200 e serve 7 posts.
- Build local produz HTML byte-para-byte idêntico ao site live.

## Recursos

- 7 posts publicados (435–529 palavras cada).
- Design system baseado em Piramyd (cores #0A0A0A / #EAAA08, tipografia Inter).
- WCAG 2.1 AA (4.5:1 contrast).
- CSS self-contained (sem dependências externas).
- CSP estrito (default-src 'self').

## Riscos

- **Build local vs. live:** Diferenças devem ser documentadas e corrigidas.
- **Segurança:** build.py deve ser auditado (ver TASK-011).

## Próximos passos

- Reconstruir repo após apagão (TASK-018-001).
- Configurar backup diário.
- Auditoria de segurança (TASK-011).