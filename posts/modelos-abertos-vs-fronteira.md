---
title: Modelos abertos vs. modelos de fronteira: onde está a linha em Outubro de 2026
slug: modelos-abertos-vs-fronteira
date: 2026-10-16
description: Os benchmarks dizem que a distância desapareceu. A factura diz outra coisa.
tags: [modelos, custo, produção]
---

# Modelos abertos vs. modelos de fronteira: onde está a linha em Outubro de 2026

_Os gráficos dizem que a diferença desapareceu. Depois chegas à factura do mês._

### Porque agora

O discurso mudou este ano. Os modelos abertos deixaram de ser a alternativa barata e passaram a ser a escolha por omissão em muitas equipas. Os números que circulam apoiam isso: no índice da Artificial Analysis (v4.3.2, Outubro de 2026), o melhor modelo aberto está a 12 pontos do melhor fechado — 46 contra 58. A distância encurtou nos últimos dois anos, mas doze pontos num índice que junta dez avaliações ainda decide em que tarefas confias no aberto.

O que mudou não foi só a qualidade. Foi o custo. Um modelo aberto servido por um fornecedor de inferência pode custar uma fracção do preço por milhão de tokens de um modelo de fronteira. O `deepseek-flash` cobra $0.15 por milhão de tokens de input fora de ponta e $0.60 de output. O `gpt-6-astra` cobra $10 e $50. É uma diferença de cerca de sessenta vezes no input — e é essa a razão pela qual o aberto deixou de ser a alternativa e passou a ser a omissão. A pergunta deixou de ser "qual é melhor" e passou a ser "para quê".

### O que muda para quem constrói

Três consequências concretas, por ordem de impacto.

**Primeira: a escolha passa a ser por tarefa, não por produto.** Extrair campos, classificar, resumir e gerar código com testes são tarefas onde um modelo aberto actual chega. Raciocínio longo com muitas ferramentas ainda favorece a fronteira. Uma equipa que usa um só modelo para tudo está a pagar fronteira em trabalho de aberto.

**Segunda: o custo por tarefa deixa de ser o custo por token.** É o produto dos tokens gastos pela tarefa pelo preço do token. Um modelo mais barato que precisa de duas tentativas pode sair mais caro do que um que acerta à primeira. Medir só o preço da tabela é medir metade do problema.

**Terceira: a operação muda de sítio.** Com um modelo aberto servido por terceiros, a latência e a disponibilidade dependem desse fornecedor. Com um modelo de fronteira, dependem do fornecedor do modelo. Em qualquer dos casos, quem constrói fica com uma dependência que não controla.

### O que não está provado

Os benchmarks não medem o teu caso. Medem o conjunto que o autor escolheu, com a métrica que o autor definiu. Nenhum deles inclui os teus dados, os teus erros aceitáveis ou o teu orçamento.

Também não está provado que a distância se mantenha. A vantagem dos modelos abertos pode ser temporária, e a fronteira pode voltar a abrir. O custo de uma migração já foi medido: num estudo sobre 5 139 migrações reais, 82% aconteceram depois do encerramento do modelo — depois de a aplicação começar a falhar — e em 94% dos casos o nome do modelo estava escrito no código. O esforço mediano de uma migração vai de 6 linhas a quase 700. A vantagem de um modelo aberto dura até ao dia em que o fornecedor o retira.

E há uma incerteza que ninguém testou em produção: quanto custa, na prática, migrar de um modelo para outro a meio de um produto a correr. A resposta depende de quantas decisões de desenho foram tomadas a assumir um modelo específico.

### Fecho

Escolhe pelo perfil da tarefa, não pelo ranking. Mede o teu caso, não o benchmark de outro.

### Fontes

- Artificial Analysis, Intelligence Index v4.3.2 — o vigente em Outubro de 2026; dez avaliações, entre elas Terminal-Bench 4.0, SciCode e AutomationBench-AA. https://artificialanalysis.ai/models (consultado 20/10/2026)
- METR, Time Horizon 1.1 — horizonte de tarefa, actualizado a 8 de Setembro de 2026. https://metr.org/time-horizons/ (consultado 20/10/2026)
- Preços por 1M de tokens: DeepSeek (aberto) https://api-docs.deepseek.com/quick_start/pricing · OpenAI (fronteira) https://developers.openai.com/api/docs/pricing · Anthropic (fronteira) https://www.anthropic.com/pricing (todos consultados 20/10/2026)
- Página de preços da Piramyd (produto nosso): Solo $30 / Growth $50 / Scale $90 por mês, todos os modelos incluídos, sem cobrança por token — mais de 50 modelos na última leitura. https://piramyd.cloud/pricing (consultado 20/10/2026)
