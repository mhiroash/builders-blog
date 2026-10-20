#!/usr/bin/env bash
# Deploy do Blog de notícias IA.
#
# Stack (ADR-ALT-2026-001):
#   posts/*.md -> scripts/build.py -> dist/ -> scripts/deploy.sh -> tivra-publish
#
# Uso:
#   ./scripts/deploy.sh            # build + publica dist/ para aprovação
#   ./scripts/deploy.sh --check    # verifica que o build local == site live
#
# Nada é publicado sem aprovação do dono (gate 3 do Builders).
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ "${1:-}" == "--check" ]]; then
  python3 scripts/build.py
  python3 scripts/build.py --check
  exit $?
fi

echo "== 1/3 build =="
python3 scripts/build.py

echo "== 2/3 verificação (build local vs. site live) =="
python3 scripts/build.py --check || {
  echo "AVISO: o build local difere do site live. Revê antes de publicar." >&2
}

echo "== 3/3 envio para aprovação (tivra-publish) =="
tivra-publish dist --name noticias-ia

echo
echo "Enviado para aprovação. O site só fica no ar depois de o dono aprovar na app."
