---
title: Ferramentas de agente: o que sobrevive à segunda semana de uso
slug: ferramentas-de-agente
date: 2026-10-16
description: Na primeira semana, a ferramenta fez tudo o que prometia. Na segunda, descobriste o que ela faz quando a chamada falha.
tags: [ferramentas, agentes, observabilidade]
---

# Ferramentas de agente: o que sobrevive à segunda semana de uso

_Na primeira semana, a ferramenta fez tudo o que prometia. Na segunda, descobriste o que ela faz quando a chamada falha._

### Porque agora

O ecossistema de ferramentas para agentes cresceu depressa: execução de código, leitura de ficheiros, integrações, chamadas externas. Cada uma tem uma página de apresentação que corre bem numa demonstração.

O que mudou é que os agentes passaram de protótipo a uso diário. E a segunda semana de uso faz perguntas que a demonstração não faz.

### O que muda para quem constrói

**Permissões primeiro.** Uma ferramenta que pode escrever em qualquer sítio é uma ferramenta que pode escrever no sítio errado. A pergunta certa não é o que ela faz, é o que ela pode fazer. **[confirmar página e data de duas ferramentas]**

**Custo por chamada, não por licença.** O que importa não é o preço da ferramenta, é o custo de a usar mil vezes por dia, incluindo as repetições que falham.

**Comportamento em erro é o critério.** Toda a ferramenta parece boa quando funciona. A que aguenta é a que diz o que falhou, onde, e se vale a pena tentar de novo. Sem isso, o agente repete às cegas e a factura cresce.

**Sem registo de execução, não se opera.** Ferramenta sem rasto do que fez não se pode depurar, nem auditar, nem orçamentar. É a diferença entre uma ferramenta que impressiona e uma que aguenta.

### O que não está provado

Um caso nosso, declarado como tal: em execução de agentes em produção, os padrões de falha e recuperação estão documentados no relatório interno da Piramyd. Serve como exemplo próprio, não como prova geral.

Não está confirmado um caso público de incidente com agente em produção com fonte primária. **[confirmar existência e fonte primária]** Há relatos, e relato não é prova.

E não está testado, de forma comparável, o custo real por execução entre ferramentas diferentes. Cada uma conta à sua maneira, e isso torna a comparação uma aproximação.

### Fecho

O critério não é a lista de capacidades. É o comportamento no pior dia.

### Fontes

- Documentação de permissões e registos de duas ferramentas de agente — **[confirmar página e data]**
- Relatório próprio de falhas e recuperação em agentes em produção (relatório interno da nossa operação (não publicado)) — exemplo nosso, marcado como tal
- Caso público de incidente com agente em produção — **[confirmar existência e fonte primária]**
- Preços por execução ou por chamada das ferramentas comparadas — **[confirmar valores actuais]**
