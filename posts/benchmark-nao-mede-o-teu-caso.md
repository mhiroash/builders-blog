---
title: O benchmark que os fornecedores citam não mede o que tu vais usar
slug: benchmark-nao-mede-o-teu-caso
date: 2026-10-16
description: O número que aparece na manchete foi medido num conjunto que provavelmente não se parece nada com o teu.
tags: [benchmarks, avaliação, medição]
---

# O benchmark que os fornecedores citam não mede o que tu vais usar

_O número que aparece na manchete foi medido num conjunto que provavelmente não se parece nada com o teu. Isto não é um escândalo. É aritmética._

### Porque agora

Os cartões de modelo passaram a ser material de marketing. Cada lançamento vem com uma tabela, e cada tabela tem um número em negrito. As equipas começaram a escolher por essa tabela.

O problema não é os números serem falsos. É serem respostas a perguntas que o fornecedor escolheu. Um benchmark mede o que o seu autor decidiu medir, no conjunto que decidiu usar. O relatório *Context Rot* da Chroma (14 de Julho de 2025) teve de inventar um conjunto novo — 18 modelos, variantes semânticas do Needle-in-a-Haystack — só para responder à pergunta. O número mudou porque o conjunto mudou.

### O que muda para quem constrói

**Antes de acreditar num número, faz três perguntas.** Que conjunto foi usado? Que métrica define sucesso? Que tarefas ficaram de fora? Se as respostas não descrevem o teu produto, o número não te diz nada.

**Dez testes próprios valem mais do que qualquer tabela pública.** Escreve dez casos com os teus dados, com o teu critério de erro aceitável. Mede o custo e a falha nesses dez. Demora meio dia e responde à pergunta que interessa.

**Mede o custo, não só a qualidade.** Um modelo que acerta mais mas gasta três vezes os tokens pode sair mais caro por tarefa. O benchmark raramente traz essa coluna.

**A medição própria tem de ser contínua.** Um modelo que servia em Outubro pode não servir em Janeiro. Se só mediste uma vez, estás a decidir com dados de outro trimestre.

### O que não está provado

Um benchmark público é uma prova sobre o trabalho do autor, não sobre o teu caso. Isso não o invalida — só limita o que podes concluir.

O que não existe é um benchmark que decida por ti. O *Intelligence Index v4.3.2* da Artificial Analysis junta dez avaliações — Terminal-Bench 4.0, SciCode, AutomationBench-AA — e o METR mede horizonte de tarefa; os dois dizem o que o autor escolheu medir. Nenhum mede o teu agente com as tuas ferramentas. É uma área com medição, mas não com resposta.

O nosso método interno mede latência e falha por fornecedor na Piramyd, produto nosso. É útil para nós e não é comparável com o de outra equipa.

### Fecho

Um benchmark é uma prova sobre o trabalho do autor. A tua prova é a que corres tu.

### Fontes

- Artificial Analysis, Intelligence Index v4.3.2 — dez avaliações nomeadas: Terminal-Bench 4.0, SciCode, AutomationBench-AA, GDPval-AA v2.1, AA-Briefcase v1.1, entre outras. https://artificialanalysis.ai/models (consultado 20/10/2026)
- Chroma, Context Rot — Technical Report, 14 de Julho de 2025; 18 modelos avaliados. https://www.trychroma.com/research/context-rot (consultado 20/10/2026)
- Método próprio de medição de latência e falha por fornecedor (Piramyd, produto nosso) — não publicado
