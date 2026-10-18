**16 de Outubro de 2026**

# Modelos abertos vs. modelos de fronteira: onde está a linha em Outubro de 2026

Os gráficos dizem que a diferença desapareceu. Depois chegas à factura do mês.
## Porque agora

O discurso mudou este ano. Os modelos abertos deixaram de ser a alternativa barata e passaram a ser a escolha por omissão em muitas equipas. Os números que circulam apoiam isso: em vários conjuntos públicos, a distância para os modelos de fronteira caiu para poucos pontos percentuais. [confirmar benchmark, versão e data]
O que mudou não foi só a qualidade. Foi o custo. Um modelo aberto servido por um fornecedor de inferência pode custar uma fracção do preço por milhão de tokens de um modelo de fronteira. [confirmar valores actuais por fornecedor] A pergunta deixou de ser "qual é melhor" e passou a ser "para quê".
## O que muda para quem constrói

Três consequências concretas, por ordem de impacto.
Primeira: a escolha passa a ser por tarefa, não por produto. Extrair campos, classificar, resumir e gerar código com testes são tarefas onde um modelo aberto actual chega. Raciocínio longo com muitas ferramentas ainda favorece a fronteira. Uma equipa que usa um só modelo para tudo está a pagar fronteira em trabalho de aberto.
Segunda: o custo por tarefa deixa de ser o custo por token. É o produto dos tokens gastos pela tarefa pelo preço do token. Um modelo mais barato que precisa de duas tentativas pode sair mais caro do que um que acerta à primeira. Medir só o preço da tabela é medir metade do problema.
Terceira: a operação muda de sítio. Com um modelo aberto servido por terceiros, a latência e a disponibilidade dependem desse fornecedor. Com um modelo de fronteira, dependem do fornecedor do modelo. Em qualquer dos casos, quem constrói fica com uma dependência que não controla.
## O que não está provado

Os benchmarks não medem o teu caso. Medem o conjunto que o autor escolheu, com a métrica que o autor definiu. Nenhum deles inclui os teus dados, os teus erros aceitáveis ou o teu orçamento.
Também não está provado que a distância se mantenha. A vantagem dos modelos abertos pode ser temporária, e a fronteira pode voltar a abrir. [confirmar existência de caso público com número de custo]
E há uma incerteza que ninguém testou em produção: quanto custa, na prática, migrar de um modelo para outro a meio de um produto a correr. A resposta depende de quantas decisões de desenho foram tomadas a assumir um modelo específico.
## Fecho

Escolhe pelo perfil da tarefa, não pelo ranking. Mede o teu caso, não o benchmark de outro.
## Fontes


- Benchmark de referência de modelos abertos vs. de fronteira — [confirmar qual é o vigente e a data]
- Preços por milhão de tokens dos dois lados, nos sites oficiais dos fornecedores — [confirmar valores actuais]
- Página de preços da Piramyd (produto nosso): Solo $30 / Growth $50 / Scale $90, 54 modelos de 19 fornecedores, uma chave — [confirmar contra a página]