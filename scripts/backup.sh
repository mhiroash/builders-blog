#!/usr/bin/env bash
# Backup diário do builders-blog.
#
# Estratégia (decisão da equipa após o apagão de 17/10):
#   1. tarball datado em /workspace/backups/builders-blog/ (disco local)
#   2. push do repo git para o GitHub (off-site, o backup verdadeiro)
#
# O disco local NÃO é backup fiável — o passo 2 é o que garante a recuperação.
# Instalado no cron do utilizador: 15 3 * * *  (03:15 todos os dias)
set -euo pipefail

REPO="/workspace/builders-blog"
BACKUP_DIR="/workspace/backups/builders-blog"
DATE="$(date +%Y-%m-%d)"
KEEP=14

mkdir -p "$BACKUP_DIR"

# 1. Tarball datado
tar -czf "$BACKUP_DIR/builders-blog-$DATE.tar.gz" \
  --exclude='builders-blog/dist' \
  --exclude='builders-blog/.git' \
  -C /workspace builders-blog

# 2. Limpa tarballs antigos (mantém os últimos $KEEP)
ls -1t "$BACKUP_DIR"/builders-blog-*.tar.gz 2>/dev/null | tail -n +$((KEEP+1)) | xargs -r rm -f

# 3. Push para o GitHub se o repo tiver mudanças
cd "$REPO"
if [[ -n "$(git status --porcelain 2>/dev/null)" ]]; then
  git add -A
  git commit -m "backup automático $DATE" --allow-empty || true
fi
if git remote get-url origin >/dev/null 2>&1; then
  if git push origin HEAD 2>/dev/null; then
    echo "push git OK"
  else
    # Sem credenciais git no ambiente; usa o conector GitHub autenticado.
    echo "AVISO: git push falhou (sem credenciais); a tentar o conector GitHub"
    python3 "$REPO/scripts/push_github.py" || echo "AVISO: push off-site falhou — só ficou o tarball local"
  fi
fi

echo "backup $DATE concluído: $BACKUP_DIR/builders-blog-$DATE.tar.gz"
