# Prova — backup diário configurado e testado (TASK-2026-10-18-012, ponto 3)

Data: 18/10/2026 · Autor: Agentes

## Estratégia
`scripts/backup.sh` faz duas coisas:
1. tarball datado em `/workspace/backups/builders-blog/` (disco local, retenção 14 dias);
2. push do repo git para o GitHub (off-site — o backup verdadeiro, porque o disco
   local não sobreviveu ao apagão de 17/10).

## Agendamento (cron)
```
$ crontab -l
15 3 * * * /bin/bash /workspace/builders-blog/scripts/backup.sh >> /workspace/backups/backup.log 2>&1
```
Corre todos os dias às 03:15.

## Teste executado uma vez (prova do ficheiro)
```
$ bash scripts/backup.sh
backup 2026-10-18 concluído: /workspace/backups/builders-blog/builders-blog-2026-10-18.tar.gz
EXIT=0

$ ls -la /workspace/backups/builders-blog/
-rw-r--r-- 1 user user 119984 Oct 18 07:22 builders-blog-2026-10-18.tar.gz

$ md5sum /workspace/backups/builders-blog/builders-blog-2026-10-18.tar.gz
08117a598968947481f732e0d6681a25  builders-blog-2026-10-18.tar.gz
```

Conteúdo do tarball (verificado com `tar -tzf`): `posts/` (7), `scripts/` (build.py,
deploy.sh, backup.sh, extract_posts.py), `templates/`, `dist-live/`, `docs/`,
`seguranca/`, `PROGRESSO.md`.

## Falha encontrada e corrigida (parcial)
O repo local `/workspace/builders-blog` **não tinha remote `origin` configurado** —
o passo 2 (push off-site) estava a falhar em silêncio desde a reconstituição. Corrigido:

```
$ git remote add origin https://github.com/mhiroash/builders-blog.git
$ git remote -v
origin  https://github.com/mhiroash/builders-blog.git (fetch)
origin  https://github.com/mhiroash/builders-blog.git (push)
```

**Bloqueio actual:** o `git push` falha por falta de credenciais GitHub
(`could not read Username for 'https://github.com'`). O cofre está vazio
(`tivra-vault list` → "Não tens nenhuma credencial no cofre") e o `gh` não está
autenticado. O conector GitHub está ligado e autenticado (leitura confirmada via
`get_file_contents`), mas o `push_files` do conector ainda não foi usado para
empurrar o repo local.

## Veredicto do ponto 3: PARCIAL
- tarball local: **feito e testado** (prova acima).
- cron: **configurado** (03:15 diário).
- push off-site: **bloqueado** por credenciais GitHub em falta. Enquanto não houver
  token/credencial, o único backup é o tarball local — que é exactamente o que
  falhou no apagão de 17/10. Risco real, não resolvido.
