---
title: Agentes que correm sozinhos: onde falham na realidade
slug: agentes-que-correm-sozinhos
date: 2026-10-16
description: Um agente que acerta em 90% dos passos falha a tarefa completa muito mais vezes do que 90%.
tags: [agentes, fiabilidade, produção]
---

# Agentes que correm sozinhos: onde falham na realidade

_O agente acerta em nove passos de dez. A tarefa tem vinte. Faz as contas antes de confiar nele._

### Porque agora

Tarefas de longa duração passaram de demonstração a promessa de produto. Agentes que correm dezenas de passos, chamam ferramentas, leem ficheiros e voltam a decidir estão a ser postos em produção.

O discurso público mede-os por passo. É uma métrica conveniente, porque cada passo isolado parece fiável. O que mudou este ano é que já há tarefas longas suficientes para a aritmética se notar. O METR mede isto desde 2025: o tempo humano de tarefa em que um agente acerta metade das vezes dobra a cada sete meses, e o próprio METR atribui o ganho à fiabilidade e à recuperação de erros. A página, actualizada a 8 de Setembro de 2026, já mede horizonte de 16 horas — e avisa que acima disso a sua suite não é fiável.

### O que muda para quem constrói

**A fiabilidade composta é cruel.** Se cada passo tem 90% de sucesso e a tarefa tem vinte passos independentes, a probabilidade de chegar ao fim é cerca de 12%. Não é uma questão de o modelo ser bom. É multiplicação.

**Por isso, a engenharia útil não está no prompt.** Está nos pontos de verificação: onde o agente confirma que o passo anterior produziu o resultado esperado, o que faz quando não produziu, e quanto custa repetir. Um agente sem travões está a construir uma demonstração.

**O erro tem preço.** Cada tentativa falhada gasta tokens e tempo. Um agente que repete às cegas pode custar mais do que a tarefa que substitui. Recuperação de erro não é um detalhe de qualidade — é a diferença entre um custo previsível e um custo aberto.

### O que não está provado

Os benchmarks de tarefas longas medem conjuntos controlados. Nenhum inclui as tuas ferramentas, os teus dados ou o teu pior dia. O METR mede software, com tarefas que ele escolheu, e admite-o: acima de 16 horas a suite deles não é fiável, e alguns modelos nunca foram medidos.

Um caso próprio, declarado como tal: no nosso sistema em produção, o padrão `stream_retries_exhausted` e `all_provider_keys_failed` aparece quando as tentativas se esgotam sem sucesso. É o comportamento esperado de um sistema com limites — e mostra que o limite existe, não que o desenho esteja errado.

O que ninguém testou em produção: quantos passos um agente pode correr antes de o custo de recuperação ultrapassar o valor da tarefa. Cada domínio tem a sua resposta.

### Fecho

A fiabilidade de um agente não é a média dos passos, é o produto deles.

### Fontes

- METR, Time Horizon 1.1 — horizontes de 50% e 80% em mais de cem tarefas de software; página actualizada a 8 de Setembro de 2026. https://metr.org/time-horizons/ (consultado 20/10/2026)
- Measuring AI Ability to Complete Long Software Tasks, arXiv:2503.14499 (18/03/2025). https://arxiv.org/abs/2503.14499 (consultado 20/10/2026)
- Relatório próprio: relatório interno da nossa operação (não publicado) documenta `stream_retries_exhausted` e `all_provider_keys_failed` — exemplo nosso, marcado como tal
- OpenHands SDK — política de confirmação por acção (AlwaysConfirm, NeverConfirm, ConfirmRisky) e rejeição de acções pendentes. https://docs.openhands.dev/sdk/guides/security (consultado 20/10/2026)
- Replit Agent — Plan mode e checkpoints com rollback. https://docs.replit.com/features/agent/overview (consultado 20/10/2026)
- DeepSeek — limite de concorrência por modelo (2500 pedidos em deepseek-flash; 500 em deepseek-v4-pro) e saída máxima de 384K tokens. https://api-docs.deepseek.com/quick_start/pricing (consultado 20/10/2026)
