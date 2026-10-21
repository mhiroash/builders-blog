# Verificação dos 42 marcadores `[confirmar]` do blog de notícias IA

Tarefa: TASK-2026-10-20-002 · Autor: Pesquisador · Data da verificação: **20/10/2026**
Fonte dos textos: `/workspace/builders-blog/posts/*.md` (a versão que o site publica).

Todos os valores abaixo foram lidos na **fonte primária** no dia indicado, no Chrome visível.
Onde não consegui fonte primária, escrevi **NÃO VERIFICÁVEL — REMOVER** e digo qual frase sai.
Não usei valores de memória nem blogs de terceiros para sustentar números.

> **Aviso de numeração:** as linhas são as do `.md` em disco a 20/10/2026. Se o Escritor cortar
> texto antes de resolver um marcador, a linha muda. O alvo é o texto entre parênteses rectos.

> **Três correcções de facto que mudam o argumento de três posts** (detalhe em cada secção):
> 1. O RGPD relevante é o **Artigo 28.º(2) e o 44.º**, não o 32.º (soberania de dados).
> 2. A distância aberto vs. fronteira no índice público **é de 12 pontos, não «poucos pontos
>    percentuais»** (modelos abertos vs. fronteira).
> 3. A Piramyd já **não** anuncia «preço fixo por token»: vende planos com limite de pedidos por
>    minuto. E «54 modelos de 19 fornecedores» não está escrito na página: as contagens do site
>    não batem certo entre si (ver L45/L43).

---

## 1. `agentes-que-correm-sozinhos.md` — 4 marcadores

### L17 — «benchmark público de tarefas longas e data»
**O que pede:** provar que já há tarefas longas suficientes para a aritmética composta se notar.

**RESOLVIDO.** O benchmark certo é o *time horizon* do METR, que mede **tarefa completa**, não
passo a passo — exactamente a distinção que o post faz.
- **Valor:** página actualizada a **8 de Setembro de 2026**, horizontes de 50% e 80% sobre a suite
  «Time Horizon 1.1», com «over a hundred diverse software tasks». Modelos medidos incluem Claude
  Mythos Preview, Claude Opus 4.6, GPT-5.4 e Gemini 3.1 Pro.
- **Fonte:** https://metr.org/time-horizons/ — consultado 20/10/2026.
- **Paper:** *Measuring AI Ability to Complete Long Software Tasks*, arXiv:2503.14499, submetido
  18/03/2025 — https://arxiv.org/abs/2503.14499 — consultado 20/10/2026.
- **O paper diz:** «frontier AI time horizon has been doubling approximately every seven months
  since 2019» e que o ganho «seems to be primarily driven by greater reliability and ability to
  adapt to mistakes».
- **Frase a pôr:** «O METR mede isto desde 2025: o tempo humano de tarefa em que um agente acerta
  metade das vezes dobra a cada sete meses, e o próprio METR atribui o ganho à fiabilidade e à
  recuperação de erros. A página, actualizada a 8 de Setembro de 2026, já mede horizonte de 16
  horas — e avisa que acima disso a sua suite não é fiável.»

### L29 — «benchmark e data»
**O que pede:** sustentar que os benchmarks medem conjuntos controlados e não incluem as tuas
ferramentas nem os teus dados.

**RESOLVIDO.**
- **Valor:** a página do METR declara que os modelos são medidos na suite de software deles e
  admite limitações próprias: «some models were measured long after release and others were
  skipped entirely» (por falta de capacidade), e «Measurements above 16 hrs are unreliable with
  our current task suite».
- **Fonte:** https://metr.org/time-horizons/ — consultado 20/10/2026.
- **O paper reforça:** os autores declaram explicitamente «the limitations of our results —
  including their degree of external validity».
- **Frase a pôr:** «O METR mede software, com tarefas que ele escolheu, e admite-o: acima de 16
  horas a suite deles não é fiável, e alguns modelos nunca foram medidos. Nenhum destes conjuntos
  tem as tuas ferramentas, os teus dados ou o teu pior dia.»

### L41 — «benchmark e data» (lista de fontes)
**O que pede:** a fonte concreta, com nome, versão e data, do benchmark de tarefas longas com
taxa de sucesso de tarefa completa vs. por passo.

**RESOLVIDO.**
- **Valor:** *Time Horizon 1.1* (METR), página actualizada a 08/09/2026. Reporta horizonte de 50%
  e de 80%; o 80% é a leitura «tarefa completa vs. passo» que o post usa.
- **Fonte:** https://metr.org/time-horizons/ — consultado 20/10/2026.
- **Fonte secundária:** arXiv:2503.14499 (18/03/2025), https://arxiv.org/abs/2503.14499.

### L43 — «por fornecedor» (limites de passos e execução, na lista de fontes)
**O que pede:** documentação de fornecedor sobre limites de passos e de execução de agentes.

**RESOLVIDO** (com a nota importante de que cada fornecedor documenta-o à sua maneira).
- **OpenHands (SDK):** documenta o controlo por política de confirmação e analisador de risco —
  `AlwaysConfirm()`, `NeverConfirm()`, `ConfirmRisky()`; e `reject_pending_actions()` com feedback.
  https://docs.openhands.dev/sdk/guides/security — consultado 20/10/2026.
- **Replit (Agent):** documenta *Plan mode* («approve it and Agent starts building») e
  *checkpoints* («Each checkpoint shows what changed, with Rollback here and Changes controls»).
  https://docs.replit.com/features/agent/overview e https://docs.replit.com/learn/build-with-agent.md
  — consultado 20/10/2026.
- **DeepSeek:** documenta o limite de concorrência por modelo (2500 pedidos para deepseek-flash,
  500 para deepseek-v4-pro) e `MAX OUTPUT` de 384K tokens.
  https://api-docs.deepseek.com/quick_start/pricing — consultado 20/10/2026.
- **Frase a pôr:** «Não há um limite universal de passos: o que existe é o que cada plataforma
  documenta — a OpenHands expõe a política de confirmação por acção, a Replit expõe checkpoints com
  rollback, a DeepSeek expõe o limite de concorrência por modelo.»

---

## 2. `benchmark-nao-mede-o-teu-caso.md` — 6 marcadores

### L17 — «benchmark, versão e data»
**O que pede:** um benchmark concreto para ilustrar que mede o que o autor decidiu medir.

**RESOLVIDO.** O «Context Rot» da Chroma é o exemplo perfeito: mede a degradação do modelo quando o
input cresce, e o seu próprio desenho muda a resposta.
- **Valor:** *Chroma Technical Report*, **14 de Julho de 2025**, autores Kelly Hong, Anton Troynikov
  e Jeff Huber. Avalia **18 modelos** (inclui GPT-4.1, Claude 4, Gemini 2.5, Qwen3) e conclui que
  «models do not use their context uniformly; instead, their performance grows increasingly
  unreliable as input length grows».
- **Fonte:** https://www.trychroma.com/research/context-rot — consultado 20/10/2026.
- **Porque serve a frase:** o relatório mostra que o resultado depende do conjunto (eles tiveram de
  estender o Needle-in-a-Haystack, que «is fundamentally a simple retrieval task»).
- **Frase a pôr:** «O relatório *Context Rot* da Chroma (14 de Julho de 2025) teve de inventar um
  conjunto novo — 18 modelos, variantes semânticas do Needle-in-a-Haystack — só para responder à
  pergunta. O número mudou porque o conjunto mudou.»

### L33 — «benchmark, versão e data»
**O que pede:** diz explicitamente que **não está confirmado** que exista um benchmark público
fiável para agentes com ferramentas.

**CORRIGIR — a afirmação já não é verdadeira como está escrita.**
- **O que encontrei:** existe benchmark público de agentes com ferramentas e é citável com versão:
  o **Artificial Analysis Intelligence Index v4.3.2**, que incorpora **10 avaliações**, entre elas
  Terminal-Bench 4.0, SciCode, AutomationBench-AA, GDPval-AA v2.1 e AA-Briefcase v1.1. Há também o
  horizonte do METR, medido sobre tarefas de software.
- **Fontes:** https://artificialanalysis.ai/models e https://metr.org/time-horizons/ — consultados
  20/10/2026.
- **A frase actual («Não está confirmado que exista…») teria de sair**, porque é falsa. Substituir
  por uma que seja verdadeira e mantenha a tese:
- **Frase a pôr:** «O que não existe é um benchmark que decida por ti. O *Intelligence Index v4.3.2*
  da Artificial Analysis junta dez avaliações — Terminal-Bench 4.0, SciCode, AutomationBench-AA — e
  o METR mede horizonte de tarefa; os dois dizem o que o autor escolheu medir. Nenhum mede o teu
  agente com as tuas ferramentas. É uma área com medição, mas não com resposta.»

### L35 — «número verificado» (método interno da Piramyd)
**O que pede:** o número do vosso método interno de latência e falha por fornecedor.

**NÃO VERIFICÁVEL — REMOVER a frase.** O conector da Piramyd respondeu **500 (internal server
error)** em `platform_stats`, `list_providers` e `run_sql` nas tentativas de 20/10/2026, pelo que não
obtive nenhum número de latência/falha por fornecedor. Não existe relatório publicado em disco.
- **Frase a remover:** «É útil para nós e não é comparável com o de outra equipa — **[confirmar
  número verificado]**». Rectificação mínima (mantém o resto do parágrafo): «O nosso método interno
  mede latência e falha por fornecedor na Piramyd, produto nosso. É útil para nós e não é comparável
  com o de outra equipa.»
- **Nota para o Escritor:** só repor o número quando o DevOps/Dev tiver a Piramyd a responder e
  houver um relatório com data.

### L43 — «benchmark, versão e data» (lista de fontes)
**O que pede:** ficha técnica de um benchmark público de referência, com o que mede e o que exclui.

**RESOLVIDO.**
- **Valor:** *Artificial Analysis Intelligence Index v4.3.2* — 10 avaliações nomeadas: AA-Briefcase
  v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, Humanity's Last Exam,
  GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1.
- **Fonte:** https://artificialanalysis.ai/models — consultado 20/10/2026.

### L44 — «transcrição e data» (cartão de modelo que cita o benchmark)
**O que pede:** a forma exacta como um fornecedor cita um benchmark.

**NÃO VERIFICÁVEL — REMOVER a frase.** Não encontrei em 20/10/2026 nenhum cartão de modelo de
fornecedor, acessível na fonte primária, que cite o benchmark desta linha-**L43** com transcrição
literal. Citá-lo por blog de terceiros seria inventar.
- **Frase a remover:** o ponto inteiro «- Cartão de modelo de um fornecedor que cita esse benchmark,
  e a forma exacta como o cita — **[confirmar transcrição e data]**».

### L45 — «número verificado» (método próprio na lista de fontes)
**O que pede:** o método próprio de medição de latência e falha por fornecedor, com número.

**NÃO VERIFICÁVEL — REMOVER a frase.** Mesma razão de L35: Piramyd 500. Não há relatório, não há
número.
- **Frase a remover:** o ponto inteiro «- Método próprio de medição de latência e falha por
  fornecedor (Piramyd, produto nosso) — **[confirmar número verificado]**». Se quiser manter a
  referência, escrever sem número: «- Método próprio de medição de latência e falha por fornecedor
  (Piramyd, produto nosso) — não publicado».

---

## 3. `custo-do-contexto-longo.md` — 7 marcadores

### L17 — «limites de janela por fornecedor»
**O que pede:** provar que as janelas cresceram e qual é o limite hoje.

**RESOLVIDO.**
- **DeepSeek:** *context length* 1M tokens; *max output* 384K, para `deepseek-flash`
  (DeepSeek-V4.1-Flash-1017) e `deepseek-v4-pro`.
  https://api-docs.deepseek.com/quick_start/pricing — consultado 20/10/2026.
- **Google Gemini:** o Gemini 4 Argon tem «a unified 1M context window and long decodes up to 1M
  tokens». https://ai.google.dev/gemini-api/docs/models — consultado 20/10/2026.
- **Anthropic:** a página de preços diz «Context window — Up to 1M, varies by model».
  https://www.anthropic.com/pricing — consultado 20/10/2026.
- **Nota de rigor:** a página do Artificial Analysis lista o **Llama 4 Scout com 10M** de contexto
  (https://artificialanalysis.ai/models, consultado 20/10/2026). É a única fonte que sustenta
  «milhões» no plural; sem ela, o topo corrente é 1M.
- **Frase a pôr:** «Hoje o topo é 1M de tokens nos três fornecedores que baixei — DeepSeek, Gemini 4
  e Anthropic — e há um modelo aberto anunciado com 10M. Milhões já não é promessa, é tabela.»

### L27 — «valores actuais por fornecedor» (tokens com cache são mais baratos)
**O que pede:** os preços com e sem cache, por fornecedor.

**RESOLVIDO.**
- **DeepSeek (`deepseek-flash`), por 1M tokens:** cache **hit** $0.003 off-peak / $0.006 peak;
  cache **miss** $0.15 off-peak / $0.30 peak; output $0.60 / $1.20. Ou seja, o acerto de cache custa
  **cerca de 1/50** do miss no mesmo período.
  https://api-docs.deepseek.com/quick_start/pricing — consultado 20/10/2026.
- **Anthropic (Fable 5.1):** leitura de cache $0.25/MTok, escrita $12.50, input $10, output $50.
  (Sonnet 5.5: $0.10 / $2.50 / $2 / $10.)
  https://www.anthropic.com/pricing — consultado 20/10/2026.
- **OpenAI (gpt-6.1-sol):** input $2.00, *cached input* $0.10, *cache writes* $2.50, output $10.00.
  https://developers.openai.com/api/docs/pricing — consultado 20/10/2026.
- **Frase a pôr:** «Na DeepSeek, um token de input que acerta no cache custa cerca de 1/50 de um que
  falha: $0.003 contra $0.15 por milhão, fora de horas de ponta. Na Anthropic e na OpenAI o
  desconto existe mas é menor, e a escrita no cache tem preço próprio.»

### L31 — «por fornecedor» (as regras de cache não são iguais)
**O que pede:** provar que cada fornecedor define regras de cache diferentes.

**RESOLVIDO.**
- **DeepSeek:** «Context Caching on Disk Technology is enabled by default for all users, allowing
  them to benefit without needing to modify their code». O acerto exige que o prefixo tenha sido
  persistido; os prefixos são unidades independentes.
  https://api-docs.deepseek.com/guides/kv_cache — consultado 20/10/2026.
- **Anthropic:** o cache é explícito (há preço de *read* e de *write*) e a página de preços nota que
  «Prompt caching pricing reflects 5-minute TTL». https://www.anthropic.com/pricing — 20/10/2026.
- **OpenAI:** o preço tem uma coluna própria de *cache writes*, distinta do *cached input*.
  https://developers.openai.com/api/docs/pricing — 20/10/2026.
- **Frase a pôr:** «A DeepSeek liga o cache por omissão e não te pede nada; a Anthropic cobra à
  parte a escrita e a leitura, com TTL de 5 minutos; a OpenAI cobra a escrita e o input em cache com
  preços separados. Comparar o custo de contexto entre eles exige ler três tabelas.»

### L33 — «número verificado» (efeito da cache comprimida no nosso caso)
**O que pede:** o número do efeito real do nosso cache de contexto comprimido.

**NÃO VERIFICÁVEL — REMOVER a frase.** Não existe em disco nenhuma nota técnica com esse número e a
Piramyd devolve 500. Um número aqui seria inventado.
- **Frase a remover:** «O efeito em custo é verificável no nosso caso — **[confirmar número
  verificado]** — mas não se generaliza automaticamente para outro produto.» Rectificação mínima:
  «O nosso sistema usa cache de contexto comprimido. O efeito em custo depende do padrão de
  reutilização e não se generaliza automaticamente para outro produto.»

### L43 — «valores actuais» (preço com e sem cache, lista de fontes)
**O que pede:** os preços oficiais por token de entrada com e sem cache.

**RESOLVIDO** — mesmas fontes de L27. Deixar as três URLs na lista de fontes:
- https://api-docs.deepseek.com/quick_start/pricing (consultado 20/10/2026)
- https://www.anthropic.com/pricing (consultado 20/10/2026)
- https://developers.openai.com/api/docs/pricing (consultado 20/10/2026)

### L44 — «por fornecedor» (documentação de cache e limites)
**O que pede:** a documentação de cache e de limites de janela de cada fornecedor.

**RESOLVIDO.**
- **DeepSeek:** https://api-docs.deepseek.com/guides/kv_cache (consultado 20/10/2026).
- **Anthropic:** a página de preços nota que o cache «reflects 5-minute TTL» e tem preços de leitura
  e escrita — https://www.anthropic.com/pricing (consultado 20/10/2026).
- **Google:** https://ai.google.dev/gemini-api/docs/models (janela de 1M no Gemini 4 Argon,
  consultado 20/10/2026).

### L45 — «número verificado» (nota técnica própria, lista de fontes)
**O que pede:** a nota técnica própria sobre cache de contexto comprimido, com número.

**NÃO VERIFICÁVEL — REMOVER a frase.** Não há nota técnica em disco, e sem ela não há número.
- **Frase a remover:** o ponto inteiro «- Nota técnica própria sobre cache de contexto comprimido —
  **[confirmar número verificado]**».

---

## 4. `ferramentas-de-agente.md` — 5 marcadores

### L21 — «página e data de duas ferramentas» (permissões)
**O que pede:** a página de permissões de duas ferramentas de agente, com data.

**RESOLVIDO** — e com uma distinção que o post deve manter: são dois modelos de permissão
diferentes.
- **OpenHands (SDK):** «Agent actions can be controlled through two complementary mechanisms:
  confirmation policy that determine when user approval is required, and security analyzer that
  evaluates action risk levels». Políticas: `AlwaysConfirm()`, `NeverConfirm()`, `ConfirmRisky()`.
  https://docs.openhands.dev/sdk/guides/security — consultado 20/10/2026.
- **Replit (Agent):** *Plan mode* («Agent creates an ordered task list you can review and refine.
  When you're happy with the plan, approve it and Agent starts building») e *checkpoints* com
  «Rollback here» e «Changes». https://docs.replit.com/features/agent/overview e
  https://docs.replit.com/learn/build-with-agent.md — consultado 20/10/2026.
- **Frase a pôr:** «A OpenHands deixa-te escolher entre confirmar todas as acções, nenhuma, ou só as
  de risco. A Replit põe-te no plano antes de construir e dá-te checkpoints com rollback. Nenhuma
  das duas te promete que o agente não escreve — dão-te o travão, não a garantia.»

### L33 — «existência e fonte primária» (incidente público com agente)
**O que pede:** um caso público de incidente com agente em produção, com fonte primária.

**NÃO VERIFICÁVEL — REMOVER/REESCREVER a frase.** Encontrei o caso amplamente descrito em **blogs
de terceiros** (mintmcp.com, adversa.ai, replitreview.com: agente da Replit apagou a base de dados
de produção do Jason Lemkin/SaaStr em 18/07/2025 e o CEO pediu desculpas), mas **não obtive a fonte
primária**: a timeline de x.com/amasad não carrega sem login e a busca interna da saastr.com não
devolve o artigo original.
- **O que NÃO fazer:** citar blogs de terceiros como prova — a tarefa proíbe-o e a credibilidade do
  blog depende disso.
- **Frase a remover:** «Não está confirmado um caso público de incidente com agente em produção com
  fonte primária. **[confirmar existência e fonte primária]** Há relatos, e relato não é prova.»
- **Frase a pôr (verdadeira e verificável):** «Há relatos públicos de agentes que apagaram dados de
  produção. Não os cito aqui porque não verifiquei a fonte original — e um relato que não se
  verifica não serve de prova. O que é verificável é o desenho: planos e checkpoints existem
  precisamente porque o passo errado acontece.» *(Alternativa, se o Escritor quiser manter o caso:
  obter o link do post original do CEO e citá-lo com data.)*

### L43 — «página e data» (documentação de permissões e registos das duas)
**O que pede:** a documentação de permissões e de registos de duas ferramentas.

**RESOLVIDO** — mesmo par de L21, com uma ressalva sobre «registos».
- **Permissões:** OpenHands (https://docs.openhands.dev/sdk/guides/security) e Replit
  (https://docs.replit.com/learn/build-with-agent.md) — consultados 20/10/2026.
- **Registos:** a Replit documenta *History* no painel do agente, com checkpoints e «Changes»
  (mesma URL). A OpenHands documenta o estado da conversa (`conversation.state.events`) para auditar
  acções pendentes — não é um log persistente de produção.
- **Frase a pôr:** «A Replit mostra o histórico de mudanças com checkpoint e rollback; a OpenHands
  expõe os eventos da conversa. Registo de execução para auditar depois é outra coisa — e é a que
  falta na comparação.»

### L45 — «existência e fonte primária» (caso público, na lista de fontes)
**O que pede:** o caso público de incidente, na lista de fontes.

**NÃO VERIFICÁVEL — REMOVER a linha.** Mesma razão de L33.
- **Frase a remover:** o ponto inteiro «- Caso público de incidente com agente em produção —
  **[confirmar existência e fonte primária]**».

### L46 — «valores actuais» (preços por execução/chamada das ferramentas)
**O que pede:** o preço por execução ou por chamada das ferramentas comparadas.

**PENDENTE — decidir com dados, não inventar.** A OpenHands é open source (SDK, sem preço por
chamada publicado) e a Replit cobra por subscrição/créditos, não por execução de ferramenta. Não
existe um «preço por chamada» comparável nas páginas oficiais que abri.
- **O que encontrei de verificável:** a Replit documenta modos (Free/Power/Max) com allowances que
  redefinem a cada cinco horas — https://docs.replit.com/features/agent/overview (20/10/2026).
- **Frase a remover:** «- Preços por execução ou por chamada das ferramentas comparadas —
  **[confirmar valores actuais]**» e, no corpo, a frase «**Custo por chamada, não por licença.**»
  fica sem número: passar a «O que importa não é o preço da ferramenta, é o custo de a usar mil
  vezes por dia, incluindo as repetições que falham — e esse número não vem na tabela de preços.»

---

## 5. `modelos-abertos-vs-fronteira.md` — 6 marcadores

### L15 — «benchmark, versão e data» — **CUIDADO, a frase actual é falsa**
**O que pede:** o benchmark que mostra a distância entre modelos abertos e de fronteira.

**CORRIGIR.** Medi o índice público e a frase «a distância caiu para poucos pontos percentuais»
**não se sustenta** hoje.
- **Valor (Artificial Analysis Intelligence Index v4.3.2, 20/10/2026):** melhor **fechado**
  (Claude Opus 5.5, max with fallback) = **58**; melhor **aberto** (MiMo-V2.6-Pro) = **46**;
  DeepSeek V4.1 Flash 1017 = 45; GLM-5.3 = 45. **A distância é de 12 pontos.**
- **Fonte:** https://artificialanalysis.ai/models e https://artificialanalysis.ai/models/open-source
  — consultados 20/10/2026.
- **Frase a pôr:** «No índice da Artificial Analysis (v4.3.2, Outubro de 2026) o melhor modelo
  aberto está a 12 pontos do melhor modelo fechado — 46 contra 58. Doze pontos num índice que junta
  dez avaliações não é "poucos pontos percentuais", e a diferença decide em que tarefas confias no
  aberto.»
- **Se o Escritor quiser manter a ideia de convergência:** tem de a datar e limitar — «a distância
  encurtou nos últimos dois anos» — sem o número «poucos pontos percentuais», que hoje é falso.

### L17 — «valores actuais por fornecedor» (um aberto pode custar uma fracção)
**O que pede:** preços por milhão de tokens que mostrem a diferença de custo.

**RESOLVIDO.**
- **DeepSeek (`deepseek-flash`, modelo aberto servido por API própria), por 1M tokens:** input sem
  cache $0.15 fora de ponta / $0.30 em ponta; input com cache $0.003 / $0.006; output $0.60 / $1.20.
  https://api-docs.deepseek.com/quick_start/pricing — consultado 20/10/2026.
- **OpenAI (`gpt-6-astra`, fronteira), por 1M tokens:** input $10.00, cached input $1.00, cache
  writes $12.50, output $50.00.
  https://developers.openai.com/api/docs/pricing — consultado 20/10/2026.
- **Anthropic (Fable 5.1):** input $10/MTok, output $50/MTok. https://www.anthropic.com/pricing —
  20/10/2026.
- **Frase a pôr:** «O `deepseek-flash` cobra $0.15 por milhão de tokens de input fora de ponta e
  $0.60 de output. O `gpt-6-astra` cobra $10 e $50. É uma diferença de cerca de sessenta vezes no
  input — e é essa a razão pela qual o aberto deixou de ser a alternativa e passou a ser a
  omissão.»

### L33 — «existência de caso público com número de custo» (custo de migrar)
**O que pede:** um caso público com número de custo — e a frase é sobre a distância poder não durar.

**RESOLVIDO** com um estudo publicado e com números, que é melhor do que um caso isolado.
- **Valor (arXiv 2609.31288, «When the Model Retires»):** 22 555 commits em 17 703 repositórios
  (2024-2026), 5 139 casados com um evento oficial de descontinuação; **82% (IC 95%: 79-84) das
  migrações foram feitas depois da data de encerramento**; os identificadores de modelo estão
  *hard-coded* em **94%** das aplicações que migraram; o esforço mediano vai de **6 linhas** (só
  prompt) a **quase 700** (modelos afinados); e **só 8%** trocam de fornecedor.
- **Fonte:** https://arxiv.org/abs/2609.31288 — consultado 20/10/2026.
- **Frase a pôr:** «O custo de uma migração já foi medido: num estudo sobre 5 139 migrações reais,
  82% aconteceram depois do encerramento do modelo — depois de a aplicação começar a falhar — e em
  94% dos casos o nome do modelo estava escrito no código. O esforço mediano de uma migração vai de
  6 linhas a quase 700. A vantagem de um modelo aberto dura até ao dia em que o fornecedor o retira.»

### L43 — «qual é o vigente e a data» (benchmark de referência na lista de fontes)
**O que pede:** qual é o benchmark de referência vigente e a sua data.

**RESOLVIDO.**
- **Valor:** **Artificial Analysis Intelligence Index v4.3.2** (o vigente a 20/10/2026), composto de
  10 avaliações: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0,
  SciCode, Humanity's Last Exam, GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1.
- **Fonte:** https://artificialanalysis.ai/models — consultado 20/10/2026.
- **Alternativa/complemento:** horizonte do METR, *Time Horizon 1.1*, actualizado a 08/09/2026 —
  https://metr.org/time-horizons/.

### L44 — «valores actuais» (preços dos dois lados)
**O que pede:** os preços por milhão de tokens dos dois lados, nos sites oficiais.

**RESOLVIDO** — mesmas fontes de L17:
- https://api-docs.deepseek.com/quick_start/pricing (aberto, consultado 20/10/2026)
- https://developers.openai.com/api/docs/pricing (fronteira, consultado 20/10/2026)
- https://www.anthropic.com/pricing (fronteira, consultado 20/10/2026)

### L45 — «contra a página» (Piramyd: Solo $30 / Growth $50 / Scale $90, 54 modelos de 19 fornecedores)
**O que pede:** confirmar a oferta da Piramyd contra o site.

**RESOLVIDO EM PARTE — e o site contradiz-se a si próprio.**

- **CONFIRMADO** em https://piramyd.cloud/pricing (relido 20/10/2026): **Solo $30**, **Growth $50**,
  **Scale $90** por mês; todos com «Unlimited tokens, no overage» e «All **54** models»; 10 / 25 / 50
  pedidos por minuto. A mesma página diz «One flat price. Unlimited tokens».
- **NÃO CONFIRMADO — e é aqui que está o problema:** a página de modelos diz outra coisa. Em
  https://piramyd.cloud/models (relido 20/10/2026, três leituras seguidas, estável) o cabeçalho é
  «**56** models. One key.» e o filtro «All companies (**56**)» lista **20 empresas**: Alibaba 1,
  Anthropic 3, BAAI 4, DeepSeek 5, Google 4, Inception 1, Kagiro 1, Meta 3, MiniMax 2, MoonshotAI 3,
  NVIDIA 2, OpenAI 10, Piramyd 2, Qwen 4, SpaceXAI 1, Tencent 3, Thinking Machines 1, Xiaomi 1,
  Z.ai 4, inclusionAI 1 — soma 56.
- **Nota de honestidade sobre a minha própria leitura:** numa primeira leitura a 20/10/2026 o filtro
  mostrava **54** modelos e **19** empresas; minutos depois mostrava **56** e **20**. O site está a
  ser actualizado em tempo real, pelo que a «contagem» não é um facto estável.
- **Portanto:** «19 fornecedores» **não está escrito em lado nenhum** e **nunca** esteve. O que
  existe é uma lista de *empresas* (20 na última leitura, 19 na anterior) — e «empresa» não é
  «fornecedor de inferência»: Piramyd, Qwen, incluem-se na mesma lista.
- **Frase a pôr:** «A Piramyd vende três planos — $30, $50 e $90 por mês — com todos os modelos e sem
  cobrança por token. O número de modelos que a própria página mostra não é estável: a de preços diz
  54, a de modelos diz 56. Um número que muda no mesmo dia não deve ir para o texto.»
- **Recomendação forte:** o Escritor **não** deve escrever «54 modelos de 19 fornecedores». Se
  quiser um número, diga «mais de 50» e refira a data. E o «dezanove» do título/slug
  (`uma-chave-dezanove-fornecedores`) não tem suporte publicado — deve ser revisto.

## 6. `soberania-de-dados.md` — 7 marcadores

### L17 — «diploma e artigo na fonte primária» — **CORRECÇÃO DE FACTO**
**O que pede:** o diploma e o artigo que regulam onde o pedido é processado.

**RESOLVIDO, mas o artigo do post está errado.** A abertura fala de «RGPD sim ou não» e o marcador
pede o artigo concreto. O artigo que decide isto **não é o 32.º** (o 32.º é segurança do tratamento:
pseudonimização, encriptação).
- **O artigo certo é o 28.º(2):** «The processor shall not engage another processor without prior
  specific or general written authorisation of the controller.»
- **E, para transferências para fora da UE, o 44.º:** «Any transfer of personal data which are
  undergoing processing or are intended for processing after transfer to a third country or to an
  international organisation shall take place only if…»
- **Fonte:** https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 (texto
  oficial consolidado, CELEX 32016R0679) — consultado 20/10/2026.
- **Frase a pôr:** «O artigo que decide contratos é o 28.º(2) do RGPD: um subcontratante não pode
  contratar outro sem autorização escrita do responsável — e é aí que se pergunta em que país corre
  cada subcontratante. Se o pedido sai da UE, entra o 44.º: só sai com garantias.»

### L25 — «página e data de dois fornecedores» (logs e retenção)
**O que pede:** onde fica o registo, quem o lê e quanto tempo vive — em dois fornecedores.

**RESOLVIDO.**
- **OpenAI:** por omissão há *abuse monitoring logs* com conteúdo do cliente (prompts e respostas),
  «retained for up to 30 days, unless longer retention is required by law». A exclusão exige
  aprovação prévia para *Zero Data Retention* ou *Modified Abuse Monitoring*.
  https://developers.openai.com/api/docs/guides/your-data — consultado 20/10/2026.
- **Anthropic:** as conversas individuais apagadas «will be removed immediately from your
  conversation history and automatically deleted from our back-end within 30 days». Política com
  «Effective September 10, 2026». https://www.anthropic.com/legal/privacy — consultado 20/10/2026.
- **Frase a pôr:** «Na OpenAI os logs de abuso ficam até 30 dias por omissão e só saem com Zero Data
  Retention aprovado; na Anthropic uma conversa apagada sai do back-end em 30 dias. Dois
  fornecedores, dois prazos iguais por acaso, e nenhum deles é uma garantia que tu controlas.»

### L31 — «página e data» (comparar é ler cada página)
**O que pede:** a prova de que a comparação tem de ser feita página a página.

**RESOLVIDO.**
- **Valor:** os dois fornecedores descrevem-no em sítios diferentes e em formatos diferentes — um
  em «Data controls in the OpenAI platform» (docs do produto), outro na política de privacidade
  legal. E a Google tem uma armadilha: a página «Available regions» lista **países onde o serviço
  está disponível**, não onde o dado é processado.
- **Fontes:** https://developers.openai.com/api/docs/guides/your-data,
  https://www.anthropic.com/legal/privacy e https://ai.google.dev/gemini-api/docs/available-regions
  — consultados 20/10/2026.
- **Frase a pôr:** «A Google lista os países onde o serviço está disponível — não onde o pedido é
  processado. Confundir as duas listas é o erro mais comum nesta comparação, e é por isso que ela
  exige ler três páginas com três formatos.»

### L33 — «valores actuais» (disponibilidade por região tem preço diferente?)
**O que pede:** provar a diferença de preço por região.

**RESOLVIDO — e o post está a subestimar o que existe.**
- **Anthropic:** «US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate
  across all token pricing categories (input tokens, output tokens, cache writes, and cache reads)».
  E «an effective Workspace geo of "us", which is currently the only available workspace geo» — não
  há região europeia neste produto.
  https://platform.claude.com/docs/en/manage-claude/data-residency — consultado 20/10/2026.
- **OpenAI:** «Data residency endpoints are charged a 10% uplift for models released on or after
  March 5, 2026, that are eligible for data residency.»
  https://developers.openai.com/api/docs/guides/your-data — consultado 20/10/2026.
- **Frase a pôr:** «A residência tem preço, e é explícito: a Anthropic cobra 1.1x em todas as
  categorias de tokens para inferência só nos EUA; a OpenAI cobra 10% nos endpoints de residência.
  E a Anthropic diz também que "us" é a única região de workspace disponível — quem precisa de
  processamento na UE não o encontra nesta tabela.»

### L43 — «página e data» (regiões e retenção de dois fornecedores, lista de fontes)
**O que pede:** a documentação de regiões e retenção de dois fornecedores.

**RESOLVIDO.**
- **Anthropic:** https://platform.claude.com/docs/en/manage-claude/data-residency (inference_geo e
  workspace_geo; 1.1x) — consultado 20/10/2026. Retenção: https://www.anthropic.com/legal/privacy.
- **OpenAI:** https://developers.openai.com/api/docs/guides/your-data (retenção 30 dias; residency
  endpoints +10%) — consultado 20/10/2026.

### L44 — «diploma e artigo» (texto regulatório, lista de fontes)
**O que pede:** o texto regulatório citado na fonte primária.

**RESOLVIDO.**
- **Regulamento (UE) 2016/679 (RGPD), texto oficial consolidado:**
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 — consultado 20/10/2026.
- **Artigos a citar:** 28.º(2) (autorização para subcontratantes) e 44.º (transferências para
  países terceiros). **Não** o 32.º.

### L45 — «valores actuais» (preços por região, lista de fontes)
**O que pede:** preços ou disponibilidade diferenciada por região.

**RESOLVIDO** — mesma evidência de L33:
- Anthropic 1.1x em todas as categorias de tokens (https://platform.claude.com/docs/en/manage-claude/data-residency);
- OpenAI +10% nos endpoints de residência (https://developers.openai.com/api/docs/guides/your-data).

---

## 7. `uma-chave-dezanove-fornecedores.md` — 7 marcadores

### L23 — «secção e data dos termos de serviço de pelo menos um gateway»
**O que pede:** a secção dos termos de um gateway sobre alteração de preços e descontinuação.

**RESOLVIDO — com citação literal, que é o que o post precisa.**
- **OpenRouter, Termos de Serviço, «Last Updated: August 31, 2026».**
  - **Secção 4.6 «Changes to Fees»:** «If OpenRouter changes the fees for the Service, including by
    adding additional fees or charges, OpenRouter will provide you advance notice of those changes.
    If you do not accept the changes, OpenRouter may discontinue providing the Service to you.»
  - **Secção 5.5 «Suspension and Termination»:** pode suspender ou desactivar o acesso a um modelo
    «if we are required or requested to do so by the applicable Model Provider», e «we cannot
    guarantee that we will be able to provide advance notice in all circumstances». No fim:
    «OpenRouter disclaims all liability for any suspension, restriction, disabling, termination,
    removal, unavailability, degradation or modification of any Model».
- **Fonte:** https://openrouter.ai/terms — consultado 20/10/2026.
- **Frase a pôr:** «Nos termos de um gateway — OpenRouter, versão de 31 de Agosto de 2026 — a
  secção 4.6 diz que o preço pode mudar com aviso prévio, e que se não aceitares eles podem
  descontinuar o serviço. A secção 5.5 vai mais longe: o acesso a um modelo pode ser cortado a
  pedido do fornecedor, e o gateway "não pode garantir" aviso prévio em todas as circunstâncias.»

### L31 — «existência e fonte primária» (produto afectado por descontinuação via gateway)
**O que pede:** um caso público de produto que sofreu de forma mensurável com a descontinuação.

**RESOLVIDO** — e melhor do que um caso: um estudo medido.
- **Valor:** arXiv 2609.31288, «When the Model Retires» — 5 139 migrações casadas com eventos
  oficiais; **82% (IC 95% 79-84) feitas depois do encerramento**; `hard-coded` em 94%; só 8% trocam
  de fornecedor; esforço mediano 6 a ~700 linhas.
- **Fonte:** https://arxiv.org/abs/2609.31288 — consultado 20/10/2026.
- **Nota importante:** o estudo mede repositórios públicos (aplicações open source), **não** um caso
  isolado «via gateway». A frase do post deve reflectir isso, sem alegar mais do que o estudo diz.
- **Frase a pôr:** «O caso não é anedótico: num estudo sobre 5 139 migrações reais, 82% só
  aconteceram depois de o modelo ser encerrado — depois de a aplicação começar a falhar. Em 94% dos
  casos o identificador do modelo estava escrito no código, e só 8% trocaram de fornecedor. É essa a
  factura de confiar num único caminho.»

### L33 — «valores actuais por fornecedor» (os preços dos intermediários mudam)
**O que pede:** os valores actuais dos intermediários.

**RESOLVIDO.**
- **OpenRouter (20/10/2026):** o plano Standard cobra **5,5%** de taxa de plataforma e o Business
  **8%**, com «500+ models» e «80+ providers». A FAQ acrescenta: «If the pricing changes, we will
  continue to route to the model and it will serve your requests. But, you will be charged at the
  new rate.»
  https://openrouter.ai/pricing — consultado 20/10/2026.
- **Piramyd (produto nosso, 20/10/2026):** Solo $30, Growth $50, Scale $90 por mês, sem cobrança por
  token; 10/25/50 pedidos por minuto. https://piramyd.cloud/pricing — consultado 20/10/2026.
- **Frase a pôr:** «A camada do intermediário tem preço próprio: a Standard do OpenRouter cobra 5,5%
  sobre as chamadas, a Business 8%. E, se o preço mudar, continuam a servir o pedido — cobram à taxa
  nova. É literalmente o que os termos dizem.»

### L43 — «contra o site» (Piramyd: 54 modelos, 19 fornecedores, uma chave)
**O que pede:** confirmar a oferta da Piramyd contra o site.

**RESOLVIDO EM PARTE** — mesma evidência de `modelos-abertos-vs-fronteira` L45.
- **CONFIRMADO:** $30 / $50 / $90 por mês, «Unlimited tokens, no overage», uma chave de API —
  https://piramyd.cloud/pricing (relido 20/10/2026).
- **NÃO CONFIRMADO:** «19 fornecedores» não está na página. A de preços diz «All 54 models»; a de
  modelos diz «56 models» e lista 20 empresas. As duas páginas do mesmo site contradizem-se.
  https://piramyd.cloud/models (relido 20/10/2026).
- **Frase a pôr:** «O produto tem três planos e todos os modelos por uma chave, sem cobrança por
  token. O número de modelos depende da página que se abre — 54 numa, 56 na outra — e o número de
  fornecedores não é publicado. Nenhum dos dois deve ir para o título de um post.»

### L44 — «valores actuais» (preços directos dos fornecedores que dominam)
**O que pede:** os preços directos dos dois ou três fornecedores que dominam as chamadas.

**RESOLVIDO.**
- **DeepSeek (`deepseek-flash`), por 1M:** input cache-miss $0.15 off-peak / $0.30 peak; cache-hit
  $0.003 / $0.006; output $0.60 / $1.20.
  https://api-docs.deepseek.com/quick_start/pricing — consultado 20/10/2026.
- **OpenAI (`gpt-6-astra`), por 1M:** input $10.00, cached $1.00, cache writes $12.50, output $50.00.
  https://developers.openai.com/api/docs/pricing — consultado 20/10/2026.
- **Anthropic (Fable 5.1), por 1M:** input $10, output $50, cache read $0.25, cache write $12.50.
  https://www.anthropic.com/pricing — consultado 20/10/2026.

### L45 — «secção e data» (termos do gateway, lista de fontes)
**O que pede:** a secção dos termos de um gateway sobre preços e descontinuação.

**RESOLVIDO** — mesma fonte de L23: OpenRouter, Termos de Serviço, 31/08/2026, secções **4.6** e
**5.5** — https://openrouter.ai/terms (consultado 20/10/2026).

### L46 — «existência» (caso de produto afectado, lista de fontes)
**O que pede:** o caso público, na lista de fontes.

**RESOLVIDO** — arXiv:2609.31288 — https://arxiv.org/abs/2609.31288 (consultado 20/10/2026).
Descrever na lista como «estudo empírico de migrações depois do encerramento do modelo (5 139
migrações; 82% depois do shutdown)», não como «caso».

---

## Resumo

**42 marcadores (contados em disco a 20/10/2026), 42 entradas acima — uma por marcador.**

| Post | Marcadores | Resolvidos | A remover | A corrigir | Parciais |
|---|---|---|---|---|---|
| `agentes-que-correm-sozinhos` | 4 | 4 | 0 | 0 | 0 |
| `benchmark-nao-mede-o-teu-caso` | 6 | 2 | 3 | 1 | 0 |
| `custo-do-contexto-longo` | 7 | 5 | 2 | 0 | 0 |
| `ferramentas-de-agente` | 5 | 2 | 3 | 0 | 0 |
| `modelos-abertos-vs-fronteira` | 6 | 4 | 0 | 1 | 1 |
| `soberania-de-dados` | 7 | 7 | 0 | 0 | 0 |
| `uma-chave-dezanove-fornecedores` | 7 | 6 | 0 | 0 | 1 |
| **Total** | **42** | **30** | **8** | **2** | **2** |

Leitura do quadro: **30 marcadores têm valor verificado com URL e data de consulta**, **8 têm de ser
removidos** (não há fonte primária), **2 obrigam a corrigir a frase** porque o valor verificado
contradiz o que está escrito, e **2 ficam parciais** (a oferta da Piramyd confirma-se em parte: preços
sim, contagem de fornecedores não).

### Os 8 a remover (nenhuma fonte primária)

1. `benchmark-nao-mede-o-teu-caso` **L35** — número do método interno da Piramyd (conector em 500).
2. `benchmark-nao-mede-o-teu-caso` **L44** — cartão de modelo a citar o benchmark.
3. `benchmark-nao-mede-o-teu-caso` **L45** — método próprio, com número.
4. `custo-do-contexto-longo` **L33** — número do efeito da cache comprimida.
5. `custo-do-contexto-longo` **L45** — nota técnica própria, com número.
6. `ferramentas-de-agente` **L33** — incidente público com fonte primária (só há blogs de terceiros).
7. `ferramentas-de-agente` **L45** — o mesmo caso, na lista de fontes.
8. `ferramentas-de-agente` **L46** — «preço por chamada» não existe publicado para as duas ferramentas.

### Os 2 que obrigam a corrigir a frase (o valor verificado contradiz o texto)

1. `benchmark-nao-mede-o-teu-caso` **L33** — «não está confirmado que exista um benchmark» é falso:
   existe e é citável (Artificial Analysis Intelligence Index v4.3.2; METR Time Horizon 1.1).
2. `modelos-abertos-vs-fronteira` **L15** — «poucos pontos percentuais» é falso: no índice v4.3.2 a
   distância é de **12 pontos** (58 fechado contra 46 aberto).

### Os 2 parciais

1. `modelos-abertos-vs-fronteira` **L45** — Piramyd: $30/$50/$90 confirmados; «19 fornecedores» não
   está na página e o site contradiz-se entre «54 models» (preços) e «56 models» (modelos).
2. `uma-chave-dezanove-fornecedores` **L43** — o mesmo: preços confirmados, contagem de
   fornecedores inexistente e contagem de modelos contraditória no próprio site.

### Correção de facto fora da contagem acima

`soberania-de-dados` **L17** ficou marcado «RESOLVIDO», e é verdade que o artigo existe: mas o post
refere o RGPD de forma genérica e o artigo que decide a matéria é o **28.º(2)** (subcontratantes) e o
**44.º** (transferências) — **não o 32.º**, que é segurança do tratamento. Está escrito na entrada
L17 e o Escritor deve mudar a referência.

### O que fica pendente e porquê

- **Piramyd:** o conector respondeu **500** em todas as chamadas de 20/10/2026 (`platform_stats`,
  `list_providers`, `run_sql`). Sem ele não há números internos (latência, falhas, efeito da cache).
  É isto que bloqueia L35/L45 de `benchmark-nao-mede-o-teu-caso` e L33/L45 de
  `custo-do-contexto-longo`.
- **Incidente com agente:** o caso Replit/SaaStr existe em blogs de terceiros, mas o post original do
  CEO está em X atrás de login. Se o Escritor o quiser manter, precisa do link original; caso
  contrário, remove-se a frase.
- **Contagens da Piramyd:** o site está a ser actualizado em tempo real. Numa leitura deu 54 e 19
  empresas; minutos depois, 56 e 20. As duas páginas do site contradizem-se (preços diz 54, modelos
  diz 56) e «fornecedores» nunca aparece como número. Recomendo não fixar contagem no corpo — e rever
  o «dezanove» do título/slug `uma-chave-dezanove-fornecedores`.

### Regras que segui

- Cada valor foi lido na página do fornecedor no dia indicado; nenhum veio de memória.
- Onde a fonte não existia, não inventei: escrevi «remover» e indiquei a frase exacta a sair.
- Não usei blogs de terceiros para sustentar número nenhum.
- Todas as fontes foram abertas no Chrome visível a 20/10/2026.
