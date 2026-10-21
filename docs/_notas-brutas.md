# Notas brutas — TASK-2026-10-20-002 (Pesquisador)

## CONSULTA 2026-10-20 (browser, fonte primária)

### DeepSeek — https://api-docs.deepseek.com/quick_start/pricing (consultado 20/10/2026)
Modelos: deepseek-flash (DeepSeek-V4.1-Flash-1017), deepseek-v4-pro (DeepSeek-V4-Pro-0813)
- CONTEXT LENGTH: 1M ambos. MAX OUTPUT: 384K.
- deepseek-flash: input cache HIT off-peak $0.003 / peak $0.006 por 1M; cache MISS off-peak $0.15 / peak $0.30; output off-peak $0.60 / peak $1.20
- deepseek-v4-pro: cache hit off-peak $0.022 / peak $0.044; cache miss off-peak $0.66 / peak $1.32; output off-peak $1.98 / peak $3.96
- Off-peak = metade do peak. Peak 01:00-04:00 e 06:00-10:00 UTC, seg-sex.
- Citação de cache: "cache hit" é ~1/50 do preço sem cache no flash ($0.003 vs $0.15).

### Anthropic — https://www.anthropic.com/pricing (HTML guardado em disco 18/10/2026, 1.24 MB)
Fable 5.1: Prompt caching Read $0.25/MTok, Write $12.50/MTok, Input $10/MTok, Output $50/MTok (desconto cache 10x na leitura)
Opus 5.5: Read $0.20, Write $5, Input $4, Output $20
Sonnet 5.5: Read $0.10, Write $2.50, Input $2, Output $10
Haiku 5.5: <=100K Read $0.01/Write $0.125, Input $0.10, Output $0.50; >100K Read $0.05/Write $0.625, Input $0.50, Output $2.50
- Nota oficial: caching 5 min TTL. US-only inference a 1.1x. Batch 50%.
- Context window: "Up to 1M varies by model".

### Google Gemini — https://ai.google.dev/gemini-api/docs/pricing (HTML guardado em disco 18/10/2026)
- "Last updated 2026-10-16 UTC"
- Gemini 4 Argon: input $2.00/1M até 30/11/2026, $4.00 a partir de 01/12/2026; output $10.00 até 30/11/2026.

### OpenAI — https://developers.openai.com/api/docs/pricing (consultado 20/10/2026, browser)
gpt-6-astra: Input $10.00, Cached input $1.00, Cache writes $12.50, Output $50.00
gpt-6.1-sol: Input $2.00, Cached $0.10, Cache writes $2.50, Output $10.00
gpt-6-luna: Input $0.10, Cached $0.01, Cache writes $0.125, Output $0.50
- "Regional processing (data residency) endpoints are charged a 10% uplift for models released on or after March 5, 2026."
- "Priority processing was renamed Fast mode on July 30, 2026."
- Web search $10/1k calls.

### Piramyd — https://piramyd.cloud/pricing + /models (consultado 20/10/2026, browser)
- Solo $30/mês, Growth $50/mês, Scale $90/mês. Confirmado inline: "Monthly price $30 / $50 / $90", "Models All 54", "Unlimited tokens, no per-token charges".
- Fórmula de preço NOVA (não é preço por token): RPM + agentes simultâneos. Solo 10 RPM, Growth 25 RPM, Scale 50 RPM.
- Página /models: "54 models. One key." "All companies (54)" — 19 empresas listadas, 54 modelos somados.
- NÃO existe na página a frase "19 fornecedores". A afirmação "54 modelos de 19 providers, uma chave" NÃO é verificável na página como está escrita.
- 13 modelos "online right now" (dinâmico).

### RGPD — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 20/10/2026, browser)
Texto integral carregado (356 774 chars). Art. 28.º(2): subcontratante não pode contratar outro subcontratante sem autorização escrita prévia do responsável. Art. 28.º(3)(g): elimina ou devolve todos os dados pessoais após o fim da prestação (aplica-se a subprocessadores).
Art. 32.º refere-se a segurança do tratamento (pseudonimização/encriptação).
- Conclusão: o artigo que "decide contratos" sobre onde o pedido é processado é o Art. 28.º(2) e (3)(g), não o 32.º.
- CORRECÇÃO: a primeira leitura do sidebar deu "All companies (54)" e a segunda "All companies (56)". Valores dinâmicos (a lista mudou entre leituras na mesma sessão). A soma dos botões dá 56 modelos em 20 empresas na 2.ª leitura, 54 na 1.ª. Página diz no topo "54 models. One key." de forma desactualizada face ao próprio sidebar.
  -> "54 modelos de 19 fornecedores" NÃO é exacto hoje. Ler o valor vivo, não citar número fixo. É o risco nº1 para o post "uma-chave-dezanove-fornecedores".

### Anthropic — https://platform.claude.com/docs/en/manage-claude/data-residency (consultado 20/10/2026, browser)
- Dois controlos independentes: "Inference geo" (por pedido, parâmetro `inference_geo`) e "Workspace geo" (armazenamento em repouso + endpoint processing como code execution).
- inference_geo: "global" (default) ou "us" (só EUA). Resposta devolve `usage.inference_geo` quando engenharia aplica = verificável pelo cliente.
- PREÇO POR REGIÃO (resposta directa ao marcador da L33 de soberania): Claude 4.6+ com inference_geo="us" custa 1.1x o preço padrão em todas as categorias (input, output, cache writes, cache reads). "Global routing: standard pricing applies".
- **Europa NÃO aparece**: "an effective Workspace geo of 'us', which is currently the only available workspace geo" -> não há residência na UE neste produto hoje. Isto altera o argumento do post (que pressupõe escolher região europeia).

### Anthropic — https://www.anthropic.com/legal/privacy (consultado 20/10/2026, browser)
- "Effective September 10, 2026".
- Conversas individuais apagadas: removidas imediatamente do histórico e "automatically deleted from our back-end within 30 days".
- FAQ do /pricing (HTML 18/10): "US-only inference is available at 1.1x pricing for input and output tokens" — coerente com docs.

### Google Gemini — https://ai.google.dev/gemini-api/docs/available-regions (consultado 20/10/2026, browser)
- A página "Available regions" lista PAÍSES onde o serviço está disponível (inclui Portugal, Angola), NÃO onde o dado é processado. É uma confusão que o post tem de evitar de propósito.
- Para fixar a região de processamento tem de se usar a plataforma empresarial (Gemini Enterprise Agent Platform / Vertex), não a Gemini API pública — texto da própria página: "try the Gemini API in Gemini Enterprise Agent Platform".
- https://ai.google.dev/gemini-api/docs/data-residency -> 404 (não existe esta página).
- Preços (HTML 18/10): "Last updated 2026-10-16 UTC".

### OpenAI — https://developers.openai.com/api/docs/guides/your-data (consultado 20/10/2026, browser)
- "By default, abuse monitoring logs ... retained for up to 30 days, unless longer retention is required by law".
- "Data residency controls are a project configuration option ... Contact our sales team to see if you're eligible. Data residency endpoints are charged a 10% uplift for models released on or after March 5, 2026."
- Zero Data Retention / Modified Abuse Monitoring: só com aprovação prévia da OpenAI.
=> Os DOIS fornecedores (Anthropic 1.1x, OpenAI +10%) cobram exactamente o mesmo acréscimo pela residência, e ambos a tratam como configuração de projecto, não como cláusula de contrato. Isto valida o parágrafo "A resposta não está no contrato, está na configuração" E o marcador de preço por região.

### METR — https://metr.org/time-horizons/ (consultado 20/10/2026, browser)
- "LAST UPDATED September 8, 2026". Página: "This page is no longer actively updated."
- Métrica: 50% e 80% time horizon sobre a suite "Time Horizon 1.1", "over a hundred diverse software tasks".
- Escala do gráfico vai a "Measurements above 16 hrs are unreliable with our current task suite".
- Modelo mais recente medido: "Claude Mythos Preview (early)". Outros: GPT-5.4, Gemini 3.1 Pro, Claude Opus 4.6.
- Aviso metodológico útil ao post (prova de que o benchmark não mede o teu caso): "some models were measured long after release and others were skipped entirely" por falta de capacidade.
- Paper: arXiv 2503.14499 (v1) "Measuring AI Ability to Complete Long Tasks"; blog 19/03/2025 cita doubling time ~7 meses.
- IMPORTANTE: é medição de horizonte de TAREFA COMPLETA (não por passo) -> serve os marcadores L17/L41 de "agentes-que-correm-sozinhos" e L43 de "benchmark-nao-mede-o-teu-caso".

### RGPD — texto oficial EUR-Lex CELEX:32016R0679 (consultado 20/10/2026, browser)
URL: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
- Art. 28.º(1): responsável só pode usar subcontratantes que dêem garantias suficientes.
- Art. 28.º(2), CITAÇÃO LITERAL: "The processor shall not engage another processor without prior specific or general written authorisation of the controller." -> é ESTE o artigo que decide o que o fornecedor de inferência pode fazer com subcontratantes e onde.
- Art. 44.º (transferências): "Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organisation shall take place only if..." -> é ESTE o artigo das transferências para fora da UE.
- Art. 5.º: princípios (licitude, limitação de finalidades).
- O Art. 32.º é segurança do tratamento (pseudonimização/encriptação) e não responde a "em que país corre o pedido".
=> Artigo 32.º NÃO é o correcto. Artigos 28.º(2) e 44.º são.

### OpenRouter (gateway) — https://openrouter.ai/terms e /pricing (consultado 20/10/2026, browser)
TERMOS (Last Updated: August 31, 2026):
- Secção 4.6 "Changes to Fees": "If OpenRouter changes the fees for the Service, including by adding additional fees or charges, OpenRouter will provide you advance notice of those changes. If you do not accept the changes, OpenRouter may discontinue providing the Service to you."
- Secção 5.3 "Changes to Model Terms": os termos do modelo podem ser alterados pelo fornecedor; o uso continuado = aceitação.
- Secção 5.5 "Suspension and Termination": o gateway pode suspender/desactivar o acesso a um modelo se o fornecedor o pedir; "we cannot guarantee that we will be able to provide advance notice in all circumstances"; e "OpenRouter disclaims all liability for any suspension, restriction, disabling, termination, removal, unavailability, degradation or modification of any Model".
FAQ de preços (respostas factuais):
- Depreciação: "If a model is deprecated, you will receive a 404 when you request it, with an error message like 'no endpoints for this model found.'"
- Alteração de preço: "we will continue to route to the model and it will serve your requests. But, you will be charged at the new rate".
- Região: "Send requests to eu.openrouter.ai to keep inference with providers in the EU, or to us.openrouter.ai to keep it in the US" — incluído nos planos Business e Enterprise.
- Rate limit: "no plan-based rate limit on paid models"; o limite vem do fornecedor. Free models 20 RPM / 50 dia.
- Taxa de plataforma: Standard 5,5%, Business 8%. Modelos: Standard 500+, 80+ providers.
- Falhas: "An attempt that errors is not charged for its model tokens".
=> O post "uma-chave-dezanove-fornecedores" tem PROVA PRIMÁRIA para 4.6/5.3/5.5 e para o 404. O marcador pode ser resolvido com citação exacta.

### Replit Agent — docs (consultado 20/10/2026, browser)
- https://docs.replit.com/features/agent/overview : Agent "takes action ... from planning to deployment". Plan mode: "Agent creates an ordered task list you can review and refine. When you're happy with the plan, approve it and Agent starts building."
- https://docs.replit.com/learn/build-with-agent.md : "Checkpoints help you recover when a change goes in the wrong direction." "Open History in the Agent panel to see checkpoints. Each checkpoint shows what changed, with Rollback here and Changes controls."
  -> PROVA PRIMÁRIA de que rollback e revisão de mudanças existem como controlo documentado.
- https://docs.replit.com/learn/security-checklist.md : checklist oficial pede validação de input, CSRF, "Keep sensitive data out of the browser" com Replit Secrets.
- NÃO encontrei, na documentação pública da Replit, uma página que declare permissões por ferramenta (allow-list de escrita). Se o post disser "permissões primeiro", tem de citar o que existe (Plan mode + checkpoints + Secrets), não uma política de permissões que não está publicada.

### OpenHands — https://docs.openhands.dev/sdk/guides/security (consultado 20/10/2026, browser)
- "Agent actions can be controlled through two complementary mechanisms: confirmation policy that determine when user approval is required, and security analyzer that evaluates action risk levels."
- Políticas: `AlwaysConfirm()` (aprovar tudo), `NeverConfirm()` (executa sem aprovar), `ConfirmRisky()` (só acções de risco).
- Rejeição com feedback: `reject_pending_actions("...")`.
- Código no docs: `conversation.reject_pending_actions("User rejected because actions seem too risky.")`.
=> SEGUNDA ferramenta com documentação primária de permissões. Com Replit (Plan mode + checkpoints + Secrets) fecha o marcador "permissões de duas ferramentas".

### Artificial Analysis — /models e /models/open-source (consultado 20/10/2026, browser)
ÍNDICE: "Artificial Analysis Intelligence Index v4.3.2" — 10 avaliações (AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, Humanity's Last Exam, GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1).
Ranking global: Claude Opus 5.5 (max with fallback) 58; Claude Fable 5.1 53; GPT-6 Astra 53; Gemini 4 Argon (high) 53; Muse Wonder 52; GPT-6.1 Sol 52; Grok 4.7 46; MiMo-V2.6-Pro 46; DeepSeek V4.1 Flash 1017 (max) 45; GLM-5.3 (max) 45.
Melhor ABERTO: MiMo-V2.6-Pro 46 (2 800 B param) e DeepSeek V4.1 Flash 45. Melhor FECHADO: 58.
=> DISTÂNCIA REAL HOJE: 58 - 46 = 12 pontos. NÃO são "poucos pontos percentuais".
   A frase "a distância para os modelos de fronteira caiu para poucos pontos percentuais" NÃO é sustentada por esta fonte. Tem de ser corrigida para ~12 pontos no índice v4.3.2, ou removida.
Maior janela de contexto listada: Llama 4 Scout 10M; GPT-6 Sol 1M; Kimi K3 1M. DeepSeek 1M (docs DeepSeek).

### Janelas de contexto — fontes primárias (consultado 20/10/2026)
- Gemini 4 Argon: "unified 1M context window and long decodes up to 1M tokens" (https://ai.google.dev/gemini-api/docs/models)
- DeepSeek deepseek-flash e deepseek-v4-pro: CONTEXT LENGTH 1M, MAX OUTPUT 384K (https://api-docs.deepseek.com/quick_start/pricing)
- Anthropic: "Context window Up to 1M varies by model" (/pricing, HTML 18/10); Haiku 5.5 tem preço diferente acima de 100K tokens.
- Artificial Analysis lista Llama 4 Scout com 10M; GPT-6 Sol 1M; Kimi K3 1M.
=> "janelas cresceram de milhares para centenas de milhares, e agora para milhões" -> hoje o topo é 1M na maioria e 10M num modelo aberto. "milhões" (plural) só se sustentado pelo Llama 4 Scout.

### Incidente público com agente em produção — busca (20/10/2026)
- Fontes SECUNDÁRIAS (blogs de terceiros) referem o incidente Replit/SaaStr de Julho 2025: mintmcp.com/blog/replit-agent-production-database-deletion; adversa.ai/blog/ai-coding-agent-incidents/; replitreview.com/replit-deletes-production-database/. Todos afirmam que o agente da Replit apagou a base de dados de produção do Jason Lemkin (SaaStr) a 18/07/2025 e que o CEO Amjad Masad pediu desculpas publicamente a 19/07/2025.
- TENTATIVA DE FONTE PRIMÁRIA: x.com/amasad não carrega a timeline sem login (só o perfil). saastr.com busca interna por "replit" e "database deleted" não devolve o artigo original nos primeiros resultados. NÃO confirmei nenhum post original do CEO nem da SaaStr.
- CONCLUSÃO para os marcadores: o incidente existe e é amplamente documentado, MAS a fonte primária acessível sem login não foi obtida. Recomendação: ou citar com ressalva as fontes secundárias (não é o padrão do blog), ou reformular a frase para "há relatos públicos bem documentados, e o CEO da Replit reconheceu o incidente" — mas mesmo isso precisa do post original.
- DECISÃO PROPOSTA: marcar como NÃO VERIFICÁVEL — REMOVER a afirmação "não está confirmado um caso público..." é falsa hoje; a frase tem de ser reescrita. Se o Escritor quiser citar o caso, precisa do link do post original (que está atrás de login do X).

### Chroma — "Context Rot" (https://www.trychroma.com/research/context-rot, consultado 20/10/2026)
- "CHROMA TECHNICAL REPORT, July 14, 2025". Autores: Kelly Hong, Anton Troynikov, Jeff Huber.
- "we evaluate 18 LLMs, including OpenAI GPT-4.1, Claude 4, Gemini 2.5, and Qwen3". "their performance grows increasingly unreliable as input length grows".
- Distingue-se do "Needle in a Haystack", que "is fundamentally a simple retrieval task".
=> Serve a afirmação "Há indícios de que informação irrelevante piora a resposta" (custo do contexto longo, L35). Não é "provado à escala", é exactamente um indício documentado.
- Se o post citar números exactos, TENHO de os ler na fonte; a página tem secções (Impact of Distractors, LongMemEval, Repeated Words). NÃO citar números de terceiros.

### arXiv 2609.31288 — "When the Model Retires: An Empirical Study of LLM Migration in Open-Source Applications" (consultado 20/10/2026)
URL: https://arxiv.org/abs/2609.31288
Abstract (citações literais):
- "providers retire on their own schedule, with notice periods ranging from one year to two weeks."
- 22 555 commits, 17 703 repos não-fork (2024-2026); 5 139 casados com evento oficial; amostra de 300 validada por dois codificadores (kappa 0,89-0,95).
- "an estimated 82% (95% CI 79-84) of migrations away from retired models were committed after the shutdown date - after the application had started failing".
- "The share tracks the provider's notice policy: 89% for Anthropic's 60-114-day notices versus 13% for OpenAI's one-year Assistants API notice".
- "Model identifiers are hard-coded in 94% of migrating applications".
- "migration effort scales from a median of 6 added lines for prompt-only applications to nearly 700 for fine-tuned ones, and only 8% of migrations switch provider."
=> RESOLVE e REFORÇA os marcadores de "uma-chave-dezanove-fornecedores" L31 (caso público mensurável de descontinuação) e de "modelos-abertos-vs-fronteira" L33 (custo de migrar). Este é o número que faltava ao blog e é de fonte publicada.

### arXiv 2503.14499 — METR (consultado 20/10/2026)
- Submetido 18/03/2025. Título "Measuring AI Ability to Complete Long Software Tasks".
- Métrica: "50%-task-completion time horizon".
- "frontier AI time horizon has been doubling approximately every seven months since 2019".
- "the increase ... seems to be primarily driven by greater reliability and ability to adapt to mistakes".
- Limitação declarada pelos autores: "the limitations of our results -- including their degree of external validity".
=> Excelente para "agentes-que-correm-sozinhos": o ganho vem da fiabilidade e da recuperação de erros, não do prompt. Confirma a tese do post com fonte primária e admite a limitação.

### DeepSeek — Context Caching (https://api-docs.deepseek.com/guides/kv_cache, consultado 20/10/2026)
- "Context Caching on Disk Technology is enabled by default for all users, allowing them to benefit without needing to modify their code."
- Reglas: cache hit exige que o prefixo tenha sido persistido; prefixos independentes; persistência nos limites de request e a intervalos fixos.
- Preços com cache hit ~1/50 do sem cache (flash: $0.003 vs $0.15).
=> Prova primária de que as regras de cache DIFEREM por fornecedor: DeepSeek é automático em disco; Anthropic exige marcar explicitamente os blocos (write/read, TTL 5 min); OpenAI é automático (cached input) mas com preço diferente. O parágrafo do post "não são iguais" fica sustentado com estes três.

### PIRAMYD — RELECTURA 20/10/2026 02:55 (importante)
- /models: "56 models. One key. No per-token bill." e "All companies (56)" -> 20 empresas (soma 56).
- /pricing: as três vezes "All 54 models". PREÇOS $30/$50/$90 inalterados.
- => O PRÓPRIO SITE contradiz-se: preços dizem 54, modelos dizem 56.
- 1.ª leitura (02:10) deu 54 e 19 empresas; 2.ª e 3.ª (02:55) deram 56 e 20. Lista dinâmica.
- "19 fornecedores" NUNCA aparece como número. O que existe é lista de EMPRESAS, que inclui a própria Piramyd e a Qwen — não é a mesma coisa que fornecedor de inferência.
- /v1/models sem chave devolve 200 mas só 23 modelos e 11 owners (subconjunto grátis) -> NÃO serve para contar.
- Correccao aplicada no relatorio: L45 de modelos-abertos e L43 de uma-chave passam a dizer que o site se contradiz; recomendacao de nao fixar numero e rever o "dezanove" do slug.
