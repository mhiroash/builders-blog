**16 de Outubro de 2026**

# Agentes que correm sozinhos: onde falham na realidade

O agente acerta em nove passos de dez. A tarefa tem vinte. Faz as contas antes de confiar nele.
## Porque agora

Tarefas de longa duração passaram de demonstração a promessa de produto. Agentes que correm dezenas de passos, chamam ferramentas, leem ficheiros e voltam a decidir estão a ser postos em produção.
O discurso público mede-os por passo. É uma métrica conveniente, porque cada passo isolado parece fiável. O que mudou este ano é que já há tarefas longas suficientes para a aritmética se notar. [confirmar benchmark público de tarefas longas e data]
## O que muda para quem constrói

A fiabilidade composta é cruel. Se cada passo tem 90% de sucesso e a tarefa tem vinte passos independentes, a probabilidade de chegar ao fim é cerca de 12%. Não é uma questão de o modelo ser bom. É multiplicação.
Por isso, a engenharia útil não está no prompt. Está nos pontos de verificação: onde o agente confirma que o passo anterior produziu o resultado esperado, o que faz quando não produziu, e quanto custa repetir. Um agente sem travões está a construir uma demonstração.
O erro tem preço. Cada tentativa falhada gasta tokens e tempo. Um agente que repete às cegas pode custar mais do que a tarefa que substitui. Recuperação de erro não é um detalhe de qualidade — é a diferença entre um custo previsível e um custo aberto.
## O que não está provado

Os benchmarks de tarefas longas medem conjuntos controlados. Nenhum inclui as tuas ferramentas, os teus dados ou o teu pior dia. [confirmar benchmark e data]
Um caso próprio, declarado como tal: no nosso sistema em produção, o padrão stream_retries_exhausted e all_provider_keys_failed aparece quando as tentativas se esgotam sem sucesso. É o comportamento esperado de um sistema com limites — e mostra que o limite existe, não que o desenho esteja errado.
O que ninguém testou em produção: quantos passos um agente pode correr antes de o custo de recuperação ultrapassar o valor da tarefa. Cada domínio tem a sua resposta.
## Fecho

A fiabilidade de um agente não é a média dos passos, é o produto deles.
## Fontes


- Benchmark público de tarefas longas com agentes, com taxa de sucesso completa vs. por passo — [confirmar benchmark e data]
- Relatório próprio: relatório interno da nossa operação (não publicado) documenta stream_retries_exhausted e all_provider_keys_failed — exemplo nosso, marcado como tal
- Documentação do fornecedor sobre limites de passos e execução — [confirmar por fornecedor]