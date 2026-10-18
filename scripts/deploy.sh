#!/usr/bin/env bash
#
# deploy.sh — Publicar o Blog de Notícias IA
#
# Stack: Markdown → build.py → dist → tivra-publish
#
# Uso: ./scripts/deploy.sh
#
# Requer: tivra-publish (CLI da plataforma), python3
# Site: https://noticias-ia-cndd-sites.tivrai.dev
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

SITE_NAME="noticias-ia-cndd-sites"
DIST_DIR="dist"

echo "=== Blog de Notícias IA — deploy ==="
echo "Raiz: $REPO_ROOT"

# 1. Verificar pré-condições
if [ ! -d "posts" ]; then
    echo "ERRO: pasta posts/ não encontrada" >&2
    exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERRO: python3 não encontrado" >&2
    exit 1
fi

# 2. Build
echo ""
echo "→ A construir (build.py)..."
python3 scripts/build.py

if [ ! -d "$DIST_DIR" ]; then
    echo "ERRO: build não produziu $DIST_DIR/" >&2
    exit 1
fi

# 3. Verificações mínimas antes de publicar
echo ""
echo "→ Verificações pré-publicação..."

# 3a. Sem segredos no dist
if grep -rIE '(api[_-]?key|secret|password|token|BEGIN [A-Z ]*PRIVATE KEY)' "$DIST_DIR" >/dev/null 2>&1; then
    echo "ERRO: possível segredo detectado em $DIST_DIR/ — abortar" >&2
    exit 1
fi

# 3b. Sem marcadores [confirmar] visíveis
if grep -rI '\[confirmar' "$DIST_DIR" >/dev/null 2>&1; then
    echo "ERRO: marcadores [confirmar] presentes em $DIST_DIR/ — abortar" >&2
    exit 1
fi

# 3c. Contagem de posts esperada
POST_COUNT=$(find "$DIST_DIR" -name index.html -mindepth 2 | wc -l)
echo "   posts no dist: $POST_COUNT"

# 4. Publicar
echo ""
echo "→ A publicar via tivra-publish ($SITE_NAME)..."
if command -v tivra-publish >/dev/null 2>&1; then
    tivra-publish "$SITE_NAME" "$DIST_DIR"
    echo ""
    echo "✓ Publicado: https://${SITE_NAME}.tivrai.dev"
else
    echo "AVISO: tivra-publish não encontrado no PATH." >&2
    echo "O dist/ está pronto em $REPO_ROOT/$DIST_DIR — publicar manualmente." >&2
    exit 2
fi