# Prova — posts corrigidos: onde foram procurados e o que se encontrou (TASK-2026-10-18-012, ponto 2)

Data: 18/10/2026 · Autor: Agentes

## Objectivo do ponto 2
Publicar no site live os 7 posts corrigidos (513–597 palavras, 0 marcadores
`[confirmar]`), reconstituindo os textos a partir do que está em disco/repo.
Se algum post corrigido não existir em lado nenhum, **sinalizar — não inventar**.

## Resultado: os textos corrigidos NÃO existem em lado nenhum. Sinalizado.

A versão corrigida foi produzida a 16/10 (TASK-2026-10-16-012, aprovada) e
perdeu-se no apagão de 17/10, quando o `/workspace` voltou vazio. A reconstituição
posterior (TASK-2026-10-17-028) foi feita a partir do **site live**, que serve a
versão antiga — por isso o repo reconstituído tem a versão antiga, não a corrigida.

## Busca exaustiva (o que foi verificado)

| Local | Resultado |
|---|---|
| `/workspace/builders-blog/posts/*.md` | versão antiga: 4–7 marcadores, 439–534 palavras |
| `/workspace/builders-blog/dist/` e `dist-live/` | HTML da versão antiga (com marcadores) |
| Repo GitHub `mhiroash/builders-blog` (todos os 4 commits) | versão antiga em todos |
| `/workspace/backups/builders-blog/*.tar.gz` | versão antiga |
| `/tmp/novo.tgz`, `/tmp/workspace-backup.tgz`, `/tmp/inter.zip`, `/tmp/preview.tar.gz` | versão antiga ou sem posts |
| `/tmp/content_*.txt`, `/tmp/ref_*.html`, `/tmp/live-*.html` | versão antiga (com marcadores) |
| Sessões anteriores em `/home/user/.tivra/sessions/` (9 sessões) | só referências ao trabalho, não o texto |
| Índice `session_search.sqlite` | só prompts, não conteúdo de posts |
| `tivra-team memory` | confirma que a correcção existiu; não guarda o texto |
| `tivra-team task-show TASK-2026-10-16-012` | aponta para `agentes/relatorio-correccao-posts.md` — **ficheiro que já não existe** |
| Busca global por assinaturas (`METR`, `OpenRouter`, `all_provider_keys_failed`) | nenhum ficheiro com os textos corrigidos |

## Prova — o site live ainda serve a versão antiga (HTTP)
```
$ curl -s -o /dev/null -w "%{http_code}\n" https://noticias-ia-cndd-sites.tivrai.dev/
200
$ curl -s https://noticias-ia-cndd-sites.tivrai.dev/agentes-que-correm-sozinhos/ | grep -c confirmar
4
$ curl -s https://noticias-ia-cndd-sites.tivrai.dev/soberania-de-dados/ | grep -c confirmar
7
```

## Prova — o repo remoto também tem a versão antiga
```
$ tivra-team connector-call github get_file_contents \
    '{"owner":"mhiroash","repo":"builders-blog","path":"posts/soberania-de-dados.md"}'
... [confirmar diploma e artigo na fonte primária] ...
... [confirmar página e data de dois fornecedores] ...
```

## O que seria preciso para cumprir o ponto 2
Uma de duas coisas, ambas fora do meu alcance sem inventar:
1. recuperar o `agentes/relatorio-correccao-posts.md` (ou o texto corrigido) de um
   backup que não existe; ou
2. reescrever os 7 posts de raiz — o que é trabalho editorial novo (fontes primárias
   a verificar, 42 afirmações), não uma reconstituição. Não é o que a tarefa pede
   ("se algum post corrigido não existir em lado nenhum, sinaliza-o — não inventes").

## Veredicto do ponto 2: NÃO CUMPRIDO — bloqueado por perda de dados, sinalizado
