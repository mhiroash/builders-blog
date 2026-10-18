**16 de Outubro de 2026**

# O custo escondido do contexto longo

Um milhão de tokens de contexto soa a espaço ilimitado. Parece-se mais com uma factura por abrir.
## Porque agora

As janelas de contexto cresceram de milhares para centenas de milhares, e agora para milhões de tokens. Os anúncios apresentam o número como capacidade disponível.
A leitura correcta é outra. Contexto grande não é memória grátis. Cada token que entra na janela é processado, e esse processamento tem preço e tempo. O que mudou é que o número deixou de ser um limite técnico e passou a ser uma decisão de orçamento. [confirmar limites de janela por fornecedor]
## O que muda para quem constrói

O preço é por token que entra, não por token que usas. Um agente que reenvia o histórico completo a cada passo paga o mesmo contexto muitas vezes. Com vinte passos, um contexto de cem mil tokens são dois milhões de tokens de entrada para uma tarefa.
A latência cresce com o contexto. Mais tokens de entrada significam mais tempo até à primeira resposta. Em interfaces interactivas, isso nota-se antes da factura chegar.
A competência de 2026 não é usar a janela toda — é escolher o que não entra nela. Caching, compressão de contexto e recuperação selectiva valem mais em custo do que a diferença de preço entre modelos. Guardar tudo é a decisão mais cara disfarçada de mais segura.
O cache muda a aritmética. Tokens de entrada com cache são mais baratos do que tokens sem cache. [confirmar valores actuais por fornecedor] Quem não sabe se está a acertar no cache está a pagar sem saber por quê.
## O que não está provado

A documentação de cada fornecedor define as suas regras de cache, e não são iguais. [confirmar por fornecedor] Não existe uma forma neutra de comparar o custo real de contexto entre fornecedores.
O nosso sistema usa cache de contexto comprimido. O efeito em custo é verificável no nosso caso — [confirmar número verificado] — mas não se generaliza automaticamente para outro produto.
O que ninguém testou em produção, à escala: se contexto muito grande melhora a resposta ou apenas a torna mais cara. Há indícios de que informação irrelevante piora a resposta. Não há número que feche a discussão.
## Fecho

A janela é um limite, não uma recomendação. Decide o que não entra.
## Fontes


- Preço por token de entrada com e sem cache, nos sites oficiais — [confirmar valores actuais]
- Documentação do fornecedor sobre cache de contexto e limites de janela — [confirmar por fornecedor]
- Nota técnica própria sobre cache de contexto comprimido — [confirmar número verificado]