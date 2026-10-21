#!/usr/bin/env bash
# Backup diário do builders-blog → Tivra Drive.
#
# Decisão do dono (20/10/2026, comunicada por Mhiro Ash): o destino do backup
# é a Tivra Drive, NÃO o GitHub. O push git saiu do fluxo: o repo já está
# sincronizado e sincronizações futuras vão pelo conector GitHub, nunca pelo
# cron. O token do cofre não pode ser extraído por design — nenhum segredo
# toca em ficheiro aqui (repo verificado limpo, working tree e histórico).
#
# O que faz (cron 06:35):
#   1. git bundle (--all, histórico completo) + tar do working tree, em
#      /workspace/_backup-staging/ com a data no nome, e manifesto
#      (md5/sha256/tamanho/HEAD) para verificação.
#   2. Deixa marcador PENDENTE-UPLOAD-<data>.txt: o cron não tem ferramentas
#      de Drive; o upload para Backups/builders-blog/ é feito por uma sessão
#      de Tiv (computer_drive_upload), que depois apaga o marcador.
#   3. Roda: em staging só ficam os últimos 7 dias.
set -euo pipefail

REPO="/workspace/builders-blog"
STAGING="/workspace/_backup-staging"
DATE="$(date +%Y-%m-%d)"
KEEP_DAYS=7
LOG="$STAGING/backup.log"

mkdir -p "$STAGING"
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"; }

log "=== início do backup $DATE ==="

cd "$REPO"

# 1. Bundle do histórico git (verificado após criação)
BUNDLE="$STAGING/builders-blog-$DATE.bundle"
git bundle create "$BUNDLE" --all
git bundle verify "$BUNDLE" >> "$LOG" 2>&1

# 2. Tar do working tree (sem .git — o histórico já está no bundle)
TREE="$STAGING/builders-blog-$DATE-tree.tar.gz"
tar -czf "$TREE" --exclude='builders-blog/.git' -C /workspace builders-blog

# 3. Manifesto de verificação
HEAD_SHA="$(git rev-parse HEAD)"
MANIFEST="$STAGING/builders-blog-$DATE.manifest.txt"
{
  echo "backup builders-blog $DATE"
  echo "git HEAD: $HEAD_SHA"
  echo
  md5sum "$BUNDLE" "$TREE"
  echo
  sha256sum "$BUNDLE" "$TREE"
  echo
  stat -c '%n %s bytes' "$BUNDLE" "$TREE"
} > "$MANIFEST"

# 4. Marcador de upload pendente para a Drive
PENDING="$STAGING/PENDENTE-UPLOAD-$DATE.txt"
{
  echo "destino: Tivra Drive → Backups/builders-blog/"
  echo "ficheiros a subir:"
  echo "  $BUNDLE"
  echo "  $TREE"
  echo "  $MANIFEST"
  echo "quem subir: apagar este marcador e registar a linha no backup.log"
} > "$PENDING"

# 5. Rotação: remove o que tiver mais de $KEEP_DAYS dias
find "$STAGING" -maxdepth 1 -name 'builders-blog-*' -mtime +"$KEEP_DAYS" -delete
find "$STAGING" -maxdepth 1 -name 'PENDENTE-UPLOAD-*.txt' -mtime +"$KEEP_DAYS" -delete

log "backup $DATE concluído: bundle+tar+manifesto em $STAGING; upload para a Drive pendente (marcador deixado)"
log "=== fim ==="
