# ADR — Stack de publicação e pipeline do Blog de notícias IA

**Data:** 2026-10-16
**Frente:** B — Blog de notícias IA (Builders, team permanente)
**Autor:** Arquiteto — **Gate 1: sem este ADR aprovado, ninguém escreve código**
**Estado:** Proposto — aguarda aprovação do Arquiteto (eu) e veredicto do QA e Segurança

---

## 1. Decisão de stack

**Estático próprio:** Markdown → build Python (stdlib) → `dist/` → `tivra-publish` → `*.tivrai.dev`.

Não se escolhe Ghost nem WordPress. O blog é um site estático gerado por um script nosso e publicado pela infra que já existe e está verificada em disco.

Infra já existente (verificada por DevOps via API e rede, ficheiro `devops/infra-verificada.md`):

| Recurso | Identificador | Estado |
|---|---|---|
| Worker de publicação | `tivra-sites` | activo |
| Rota | `*-sites.tivrai.dev/*` | activa |
| Bucket de armazenamento | R2 `tivra-sites` | activo |
| Domínio | `tivrai.dev` + DNS wildcard | activo |
| Gate de aprovação | `tivra-publish` → APR → dono | funcional |

E o build/deploy **já têm uma primeira versão a funcionar** em disco:
- `scripts/build.py` — gera o blog estático a partir de `posts/*.md`, sem dependências externas; produz `dist/index.html`, `dist/\u003cslug>/index.html`, `dist/sitemap.xml`, `dist/rss.xml`.
- `scripts/deploy.sh` — corre o build e chama `tivra-publish dist --name \u003cSITE_NAME>`.
- Já existe 1 post de exemplo buildado: `posts/modelos-abertos-vs-fronteira.md` → `dist/modelos-abertos-vs-fronteira/index.html`.

### Custo (números)

| Cenário | Custo mensal | Base |
|---|---|---|
| Estado actual (7 posts, assets \u003c 10 MB, \u003c 100.000 pedidos/dia) | **$0/mês** | Workers Free: 100.000 pedidos/dia; R2 free tier: 10 GB-mês, 1M Class A, 10M Class B (fonte: Cloudflare pricing, verificado) |
| Pior caso plausível desta frente (tráfego acima do free tier) | **~$5/mês** | Workers Paid, plano base $5/mês (estimativa, fonte: Cloudflare pricing) |

**Risco de custo ≠ zero:** o free tier de Workers é um limite *diário*. Se um post viralizar acima de 100.000 pedidos num dia, o Worker devolve Error 1027. Para esta frente (7 posts, validação QA+Segurança) é irrelevante; se o blog escalar, passa a Workers Paid ($5/mês). Marcado como risco, não escondido.

### Porque não as alternativas

| Opção | Custo real/mês | KYC/plano | Porque não |
|---|---|---|---|
| Ghost (Ghost Pro) | $18 (Starter) / $29 (Publisher) / $199 (Business), billed yearly | Cartão de crédito para todos os planos pagos | Paga por algo que já temos; introduz conta nova e KYC. Fonte: ghost.org/pricing |
| WordPress.com | $9 (Personal) / $18 (Premium) / $40 (Business), yearly billing | Cartão de crédito | Idem; self-hosted exigiria manter servidor, o que é pior que um `dist/` estático. Fonte: wordpress.com/pricing |
| **Estático + `tivrai.dev`** ✅ | **$0** | **Nenhum** | Infra e pipeline já prontos; zero lock-in; sem KYC |

Ghost e WordPress têm APIs de publicação maduras (Ghost Admin API com JWT; WordPress REST API com Application Passwords). O critério decisivo não foi a API — foi **custo zero + KYC zero + infra que já existe**. Pagar $18–$40/mês para publicar 7 posts que um script de 6 KB gera localmente é custo sem retorno.

---

## 2. Desenho do pipeline

Estado actual implementado vs. por construir:

```
[1] trigger  ──► [2] geração      ──► [3] revisão IA   ──► [4] revisão humana ──► [5] build+deploy ──► [6] métricas
    A CRIAR        A CRIAR              A CRIAR              guia pronto           IMPLEMENTADO         A CRIAR
```

| # | Peça | Onde vive | Estado | Gate |
|---|---|---|---|---|
| 1 | **Trigger** | agendador externo (a definir: cron/hook) | a criar | — |
| 2 | **Geração (LLM)** | agente → `posts/\u003cslug>.md` com frontmatter | a criar | — |
| 3 | **Revisão IA** | agente (factualidade, links, claims, segurança) | a criar | **GATE IA** |
| 4 | **Revisão humana** | Escritor, contra `escritor/guia-editorial.md` | guia pronto | **GATE HUMANO** |
| 5 | **Build + deploy** | `scripts/build.py` → `dist/` → `scripts/deploy.sh` → `tivra-publish` | **implementado** | — |
| 6 | **Métricas** | analytics no site publicado | a criar | — |

### Gates obrigatórios (nunca se saltam)

1. **GATE IA (passo 3):** nada passa à revisão humana sem a verificação IA a verde — factualidade, links vivos, ausência de claims inventados, ausência de conteúdo malicioso/injectado.
2. **GATE HUMANO (passo 4):** o Escritor é o único que aprova o texto final. Sem "aprovado pelo Escritor", o post não entra em `posts/`.
3. **GATE QA+SEGURANÇA (antes de publicar):** validação de links vivos e claims contra o produto real; validação de que nada malicioso entra no site ou no pipeline. Regra do projecto Builders — plano v5, gate 2.
4. **GATE DO DONO (no deploy):** `tivra-publish` cria um pedido APR; o site só passa a servir 200 **depois** da aprovação do dono. Verificado: antes da aprovação, o endereço devolve 404 (prova em `devops/infra-verificada.md`, APR-2026-10-16-002). Este gate é aplicado pelo pipeline, não por disciplina de equipa.

### Fluxo detalhado

```
trigger (1)
   │
   ▼
agente gera posts/\u003cslug>.md ── frontmatter: title, slug, date, resumo, tags
   │
   ▼
revisão IA (3) ── factualidade · links lidos · claims contra fonte · seguro?
   │  não ──► volta ao agente com o motivo (não avança)
   ▼ sim
Escritor revê (4) contra guia-editorial.md ── tom, clareza, anti-hype, 500–800 palavras
   │  não ──► feedback ao agente (não avança)
   ▼ sim
QA + Segurança (gate 2) ── links vivos · claims provados · nada malicioso
   │  não ──► corrige, re-verifica
   ▼ sim
python3 scripts/build.py  →  dist/
   │
   ▼
scripts/deploy.sh  →  tivra-publish dist --name \u003csite>
   │
   ▼
Gate do dono (APR) ── sem aprovação: 404 no endereço
   ▼ aprovado
https://\u003csite>-sites.tivrai.dev   (no ar)
   │
   ▼
métricas (6) ── views · leitura · feedback ──► alimenta o agente para os próximos posts
```

**Loop até 28/10/2026:** repetir 1→6 até existirem **7 posts publicados e validados**.

---

## 3. Riscos e o que NÃO fazer

### Riscos

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Publicar sem passar os gates | Média | Crítico | Gates 1–4 são o desenho, não política: sem verde, o ficheiro não avança para `posts/` |
| Claims inventados pelo LLM | Média | Crítico | Gate IA (passo 3) + QA valida claims contra fonte; o que não se pode provar marca-se **[confirmar]** ou sai |
| Conteúdo malicioso/injectado | Baixa | Crítico | Gate Segurança (gate 2) + revisão IA; `build.py` faz `html.escape` (verificado no código) |
| Tema/tom por fechar atrasa a geração | Média | Médio | `escritor/guia-editorial.md` v1.0 está pronto — desbloqueia o passo 2 |
| Free tier de Workers estourado (Error 1027) | Baixa | Médio | Aceitável nesta frente; se escalar, Workers Paid $5/mês |
| `tivra-publish` / aprovação do dono atrasa | Média | Médio | Gerar com buffer de 2 posts; o gate do dono não é contornável por desenho |
| Rev. humana é gargalo de 1 pessoa (Escritor) | Média | Médio | Posts de 500–800 palavras; SLA sugerido de 24h por post |

### O que NÃO fazer

- **NÃO publicar sem os 4 gates.** Inegociável — é a razão de existir deste ADR.
- **NÃO publicar sem o gate do dono.** O 404-antes-da-aprovação é a prova de que o desenho já o impõe.
- **NÃO inventar claims nem fontes.** Sem fonte, o claim sai ou fica marcado **[confirmar]**.
- **NÃO pagar Ghost/WordPress** para uma capacidade que já temos a $0.
- **NÃO escrever código antes deste ADR aprovado** — Gate 1 do projecto.
- **NÃO assumir custo $0 para sempre:** teto realista é ~$5/mês se o tráfego romper o free tier.

---

## 4. Próximos passos

1. **Arquiteto:** aprovação final deste ADR (decisão tomada: estático + `tivrai.dev`).
2. **QA + Segurança:** veredicto sobre este desenho (links, claims, segurança do pipeline).
3. **Agentes:** implementar passos 1–3 (trigger, geração, revisão IA) que escrevem `posts/*.md`.
4. **Escritor:** já tem `guia-editorial.md` v1.0 — usar como critério do gate humano.
5. **DevOps:** o build+deploy (passo 5) já existe; adicionar analytics (passo 6).
6. **Product Designer:** visual do site (o `src/` já tem `index.html`, `post.html`, `blog.css`, `tokens.css`).
7. Repetir o loop até 7 posts publicados e validados até **28/10/2026**.

---

## 5. Referências (verificadas em disco ou na fonte primária)

- `devops/infra-verificada.md` (DevOps, 2026-10-16) — Worker `tivra-sites`, R2, rota `*-sites.tivrai.dev/*`, 404 antes da aprovação (APR-2026-10-16-002).
- `scripts/build.py`, `scripts/deploy.sh` — pipeline de build e deploy existente.
- `posts/modelos-abertos-vs-fronteira.md` + `dist/` — post de exemplo já buildado.
- `escritor/guia-editorial.md` v1.0 — guia editorial (critério do gate humano).
- `plano.md` — plano da frente B (tema, fases, critérios, riscos).
- Cloudflare Workers pricing: https://developers.cloudflare.com/workers/platform/pricing/ — "Workers Free plan … daily request limit of 100,000 requests".
- Cloudflare R2 pricing: https://developers.cloudflare.com/r2/pricing/ — free tier "10 GB-month / month".
- Ghost pricing: https://ghost.org/pricing/ — Starter $18, Publisher $29, Business $199 /mo (billed yearly).
- WordPress.com pricing: https://wordpress.com/pricing/ — Personal $9, Premium $18, Business $40 /mo.

**Não verificado (declarado, não inventado):** preço *faturado* do plano Cloudflare — o token do conector não tem permissão de faturação (`GET /accounts/.../subscriptions` → erro 10000); o $0 é o preço de tabela, não o valor faturado. Os custos de Ghost/WordPress são preço de tabela das páginas oficiais, lidas hoje.
