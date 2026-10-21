---
title: Uma chave, muitos fornecedores: o que a agregação de modelos resolve e o que esconde
slug: uma-chave-muitos-fornecedores
date: 2026-10-16
description: Uma chave para muitos fornecedores é uma linha de código. É também um único ponto onde tudo pode mudar de preço.
tags: [gateways, fornecedores, dependência]
---

# Uma chave, muitos fornecedores: o que a agregação de modelos resolve e o que esconde

_Uma chave para muitos fornecedores é uma linha de código. É também um único ponto onde tudo pode mudar de preço de uma semana para a outra._

### Porque agora

Os gateways e agregadores de modelos deixaram de ser um atalho de prototipagem e passaram a ser infraestrutura de produção. Uma API, muitos fornecedores, uma factura.

A proposta é clara: não gerir um contrato, um SDK e uma forma de autenticar por fornecedor. Para uma equipa pequena, isso é semanas de trabalho poupadas. O que mudou é a escala — já há produtos inteiros a correr por cima de um intermediário.

### O que muda para quem constrói

**O que se ganha é operacional, e é real.** Uma chave, um ponto de facturação, uma forma de trocar de modelo sem reescrever a integração. Trocar de fornecedor passa a ser mudar um nome de modelo, não um projecto.

**O que se perde é controlo sobre três coisas: preço, limite de ritmo e disponibilidade.** O preço é do intermediário, não do fornecedor. O limite de ritmo é o do intermediário. E quando um modelo desaparece, desaparece para ti no dia em que o intermediário decidir. Nos termos de um gateway — OpenRouter, versão de 31 de Agosto de 2026 — a secção 4.6 diz que o preço pode mudar com aviso prévio, e que se não aceitares eles podem descontinuar o serviço. A secção 5.5 vai mais longe: o acesso a um modelo pode ser cortado a pedido do fornecedor, e o gateway "não pode garantir" aviso prévio em todas as circunstâncias.

**O desenho que resiste é o que mantém uma saída.** Quem agrega deve manter uma rota directa de recurso para os dois ou três modelos que sustentam o produto. Não é desconfiança — é o mesmo princípio de não ter um único fornecedor de base de dados sem plano de saída.

**O ponto de facturação único é também um ponto de falha único.** Se o intermediário tem um mau dia, todos os teus modelos têm um mau dia ao mesmo tempo. A redundância que ganhas em fornecedores perdes em intermediário.

### O que não está provado

O caso não é anedótico: num estudo sobre 5 139 migrações reais, 82% só aconteceram depois de o modelo ser encerrado — depois de a aplicação começar a falhar. Em 94% dos casos o identificador do modelo estava escrito no código, e só 8% trocaram de fornecedor. É essa a factura de confiar num único caminho.

Os preços dos intermediários mudam. Os valores que compares hoje podem não ser os de amanhã. A camada do intermediário tem preço próprio: a Standard do OpenRouter cobra 5,5% sobre as chamadas, a Business 8%. E, se o preço mudar, continuam a servir o pedido — cobram à taxa nova. É literalmente o que os termos dizem.

E não está testado, em produção, quanto custa sair de um gateway a meio de um produto a correr. A resposta depende de quantas decisões foram tomadas a assumir a API do intermediário.

### Fecho

A agregação ganha quase sempre — até ao dia em que o intermediário muda as regras. Mantém a saída aberta.

### Fontes

- Página de preços da Piramyd (produto nosso): três planos — Solo $30, Growth $50, Scale $90 por mês, tokens ilimitados, uma chave de API; o número de modelos difere entre páginas (54 na de preços, 56 na de modelos) e o de fornecedores não é publicado. https://piramyd.cloud/pricing · https://piramyd.cloud/models (consultados 20/10/2026)
- OpenRouter — página de preços: Standard 5,5% e Business 8% sobre as chamadas; a FAQ diz que, mudando o preço, o pedido continua a ser servido à taxa nova. https://openrouter.ai/pricing (consultado 20/10/2026)
- OpenRouter — Termos de Serviço (31/08/2026), secção 4.6 «Changes to Fees» e secção 5.5 «Suspension and Termination»: aviso prévio de alterações de preço; corte de acesso a um modelo a pedido do fornecedor, sem garantia de aviso. https://openrouter.ai/terms (consultado 20/10/2026)
- When the Model Retires, arXiv:2609.31288 — estudo empírico de 5 139 migrações: 82% só depois do encerramento do modelo; 94% com o identificador escrito no código; 8% trocam de fornecedor. https://arxiv.org/abs/2609.31288 (consultado 20/10/2026)
- Preços directos por 1M de tokens: DeepSeek (`deepseek-flash`) input $0.15 off-peak / $0.30 peak, cache-hit $0.003/$0.006, output $0.60/$1.20; OpenAI (`gpt-6-astra`) input $10.00, cached $1.00, output $50.00; Anthropic (Fable 5.1) input $10, output $50. https://api-docs.deepseek.com/quick_start/pricing · https://developers.openai.com/api/docs/pricing · https://www.anthropic.com/pricing (consultados 20/10/2026)
