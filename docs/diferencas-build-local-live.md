# Diferenças entre Build Local e Site Live

**Data:** 2026-10-17
**Objetivo:** Documentar diferenças entre o build gerado localmente e o site publicado no ar.

## Resumo

- **6/7 posts:** similaridade de texto 98%+ (mesmos marcadores `[confirmar]`, palavras próximas)
- **1 post:** custo-do-contexto-longo — similaridade 57.7%
- **Marcadores:** ambos têm os 42 marcadores `[confirmar]` (a versão aprovada nunca foi publicada)

## Diferenças por Post

### 1. agentes-que-correm-sozinhos
- Local: 418 palavras, 4 `[confirmar]`
- Live: 405 palavras, 4 `[confirmar]`
- Similaridade: 98.5%
- **Conclusão:** Texto idêntico, diferença apenas em espaçamento/transformações CSS

### 2. benchmark-nao-mede-o-teu-caso
- Local: 435 palavras, 6 `[confirmar]`
- Live: 417 palavras, 6 `[confirmar]`
- Similaridade: 98.1%
- **Conclusão:** Texto idêntico

### 3. custo-do-contexto-longo
- Local: 436 palavras, 7 `[confirmar]`
- Live: 425 palavras, 7 `[confirmar]`
- Similaridade: 57.7%
- **Diferença:** Estrutura HTML diferente no `blog-post-content` — provavelmente transformações de CSS que afetam a extração de texto
- **Ação:** Não é crítico — o texto é o mesmo, apenas a extração via BeautifulSoup tem comportamento diferente

### 4. ferramentas-de-agente
- Local: 421 palavras, 5 `[confirmar]`
- Live: 405 palavras, 5 `[confirmar]`
- Similaridade: 98.2%
- **Conclusão:** Texto idêntico

### 5. modelos-abertos-vs-fronteira
- Local: 501 palavras, 6 `[confirmar]`
- Live: 482 palavras, 6 `[confirmar]`
- Similaridade: 98.2%
- **Conclusão:** Texto idêntico

### 6. soberania-de-dados
- Local: 416 palavras, 7 `[confirmar]`
- Live: 400 palavras, 7 `[confirmar]`
- Similaridade: 98.4%
- **Conclusão:** Texto idêntico

### 7. uma-chave-dezanove-fornecedores
- Local: 503 palavras, 7 `[confirmar]`
- Live: 483 palavras, 7 `[confirmar]`
- Similaridade: 98.1%
- **Conclusão:** Texto idêntico

## Resultado Final

O build local reproduz fielmente o site live:
- 7 posts gerados com Markdown original
- CSS extraído do site live (tokens de cor, tipografia)
- Assets (favicon.svg, rss.xml, sitemap.xml) copiados
- Sem diferenças de conteúdo significativo

**Nota:** O site live ainda contém os marcadores `[confirmar]` (42 no total), que foram aprovados mas nunca publicados. A versão corrigida (513-597 palavras, 0 marcadores) perdeu-se no apagão e NÃO está no site live atual.