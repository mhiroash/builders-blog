---
title: Soberania de dados: onde é que o teu prompt é processado
slug: soberania-de-dados
date: 2026-10-16
description: A discussão pública fica no "RGPD sim ou não". A pergunta que decide contratos é mais concreta.
tags: [regulação, dados, infraestrutura]
---

# Soberania de dados: onde é que o teu prompt é processado

_O teu pedido sai de Lisboa e é processado em três regiões diferentes antes de voltar. Se vendes a empresas, alguém te vai pedir esta frase por escrito._

### Porque agora

A regulação de dados em inferência deixou de ser tema jurídico e passou a tema de produto. Quem vende a empresas na Europa começou a receber a pergunta na fase de compra, não na fase de auditoria.

A discussão pública fica no "RGPD sim ou não". A pergunta que decide contratos é mais concreta: em que região física é processado cada pedido, e durante quanto tempo é retido. O artigo que decide contratos é o 28.º(2) do RGPD: um subcontratante não pode contratar outro sem autorização escrita do responsável — e é aí que se pergunta em que país corre cada subcontratante. Se o pedido sai da UE, entra o 44.º: só sai com garantias.

### O que muda para quem constrói

**A residência do processamento é requisito de venda.** Passou a escolher-se o fornecedor de modelos com o mesmo critério com que se escolhe o fornecedor de base de dados: região, retenção, subcontratantes.

**A resposta não está no contrato, está na configuração.** Um fornecedor pode oferecer processamento numa região, mas o pedido só corre lá se o produto o pedir. Isto é trabalho de engenharia, não de departamento jurídico.

**Os logs são a parte esquecida.** Onde fica o registo do pedido, quem o pode ler e quanto tempo vive são perguntas separadas da região de processamento. Muitas equipas respondem à primeira e não sabem responder à segunda. Na OpenAI os logs de abuso ficam até 30 dias por omissão e só saem com Zero Data Retention aprovado; na Anthropic uma conversa apagada sai do back-end em 30 dias. Dois fornecedores, dois prazos iguais por acaso, e nenhum deles é uma garantia que tu controlas.

**O que se perde em escolha ganha-se em venda.** Menos fornecedores elegíveis significa menos opções de preço. Para quem vende a empresas europeias, é um custo que se aceita.

### O que não está provado

Não há uma forma neutra de comparar fornecedores neste ponto. Cada um descreve as suas regiões e retenção de forma diferente, e a comparação exige ler cada página. A Google lista os países onde o serviço está disponível — não onde o pedido é processado. Confundir as duas listas é o erro mais comum nesta comparação, e é por isso que ela exige ler três páginas com três formatos.

Não está confirmado que a disponibilidade diferenciada por região tenha preço diferente. A residência tem preço, e é explícito: a Anthropic cobra 1.1x em todas as categorias de tokens para inferência só nos EUA; a OpenAI cobra 10% nos endpoints de residência. E a Anthropic diz também que "us" é a única região de workspace disponível — quem precisa de processamento na UE não o encontra nesta tabela. Quando existe, raramente é publicada de forma simples.

E não está testado, à escala, se a latência de processar numa região específica compensa para produtos com utilizadores em vários continentes. Cada caso é um caso.

### Fecho

Se vendes a empresas, a região onde o prompt corre é uma funcionalidade. Trata-a como tal.

### Fontes

- Anthropic — residência de dados (inference_geo, 1.1x) e política de privacidade com retenção de 30 dias. https://platform.claude.com/docs/en/manage-claude/data-residency · https://www.anthropic.com/legal/privacy (consultados 20/10/2026)
- OpenAI — retenção dos logs de abuso (30 dias por omissão) e endpoints de residência de dados (+10%). https://developers.openai.com/api/docs/guides/your-data (consultado 20/10/2026)
- Regulamento (UE) 2016/679 (RGPD), artigos 28.º(2) (subcontratantes) e 44.º (transferências para países terceiros), texto oficial consolidado. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 (consultado 20/10/2026)
- Residência de dados com preço: Anthropic cobra 1.1x em todas as categorias de tokens; OpenAI cobra +10% nos endpoints de residência (fontes das linhas acima, consultadas 20/10/2026)
