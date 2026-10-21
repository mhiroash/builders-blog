---
title: O custo escondido do contexto longo
slug: custo-do-contexto-longo
date: 2026-10-16
description: Um milhão de tokens de contexto soa a espaço ilimitado. Parece-se mais com uma factura por abrir.
tags: [contexto, custo, latência]
---

# O custo escondido do contexto longo

_Um milhão de tokens de contexto soa a espaço ilimitado. Parece-se mais com uma factura por abrir._

### Porque agora

As janelas de contexto cresceram de milhares para centenas de milhares, e agora para milhões de tokens. Os anúncios apresentam o número como capacidade disponível.

A leitura correcta é outra. Contexto grande não é memória grátis. Cada token que entra na janela é processado, e esse processamento tem preço e tempo. O que mudou é que o número deixou de ser um limite técnico e passou a ser uma decisão de orçamento. Hoje o topo é 1M de tokens nos três fornecedores que baixei — DeepSeek, Gemini 4 e Anthropic — e há um modelo aberto anunciado com 10M. Milhões já não é promessa, é tabela.

### O que muda para quem constrói

**O preço é por token que entra, não por token que usas.** Um agente que reenvia o histórico completo a cada passo paga o mesmo contexto muitas vezes. Com vinte passos, um contexto de cem mil tokens são dois milhões de tokens de entrada para uma tarefa.

**A latência cresce com o contexto.** Mais tokens de entrada significam mais tempo até à primeira resposta. Em interfaces interactivas, isso nota-se antes da factura chegar.

**A competência de 2026 não é usar a janela toda — é escolher o que não entra nela.** Caching, compressão de contexto e recuperação selectiva valem mais em custo do que a diferença de preço entre modelos. Guardar tudo é a decisão mais cara disfarçada de mais segura.

**O cache muda a aritmética.** Tokens de entrada com cache são mais baratos do que tokens sem cache. Na DeepSeek, um token de input que acerta no cache custa cerca de 1/50 de um que falha: $0.003 contra $0.15 por milhão, fora de horas de ponta. Na Anthropic e na OpenAI o desconto existe mas é menor, e a escrita no cache tem preço próprio. Quem não sabe se está a acertar no cache está a pagar sem saber por quê.

### O que não está provado

A documentação de cada fornecedor define as suas regras de cache, e não são iguais. A DeepSeek liga o cache por omissão e não te pede nada; a Anthropic cobra à parte a escrita e a leitura, com TTL de 5 minutos; a OpenAI cobra a escrita e o input em cache com preços separados. Comparar o custo de contexto entre eles exige ler três tabelas. Não existe uma forma neutra de comparar o custo real de contexto entre fornecedores.

O nosso sistema usa cache de contexto comprimido. O efeito em custo depende do padrão de reutilização e não se generaliza automaticamente para outro produto.

O que ninguém testou em produção, à escala: se contexto muito grande melhora a resposta ou apenas a torna mais cara. Há indícios de que informação irrelevante piora a resposta. Não há número que feche a discussão.

### Fecho

A janela é um limite, não uma recomendação. Decide o que não entra.

### Fontes

- Preços por 1M de tokens, com e sem cache: https://api-docs.deepseek.com/quick_start/pricing · https://www.anthropic.com/pricing · https://developers.openai.com/api/docs/pricing (todos consultados 20/10/2026)
- DeepSeek — regras do cache de contexto (ligado por omissão). https://api-docs.deepseek.com/guides/kv_cache (consultado 20/10/2026)
- Anthropic — preços de cache com TTL de 5 minutos. https://www.anthropic.com/pricing (consultado 20/10/2026)
- Google — janela de 1M no Gemini 4 Argon. https://ai.google.dev/gemini-api/docs/models (consultado 20/10/2026)
