#!/usr/bin/env python3
"""Push off-site do repo builders-blog via conector GitHub (tivra-team).

Usado pelo backup.sh quando o `git push` falha por falta de credenciais git no
ambiente. O conector GitHub está autenticado como mhiroash.

CORRIGIDO em 20/10/2026: a versão anterior enviava TODOS os ficheiros num único
argumento de linha de comandos. Com ~800 KB de conteúdo, o `execve` rebentava com
"OSError: [Errno 7] Argument list too long" e o push off-site falhava em silêncio
(o backup ficava só no disco local — exactamente o que falhou no apagão de 17/10).

Agora envia em lotes: cada chamada leva poucos ficheiros e fica sempre abaixo de
MAX_PAYLOAD bytes de JSON. O limite real do kernel é 128 KB por argumento
(MAX_ARG_STRLEN); ficamos com margem.

Uso: python3 scripts/push_github.py [--dry-run]
Saída: 0 = tudo empurrado; 1 = pelo menos um lote falhou.
"""
import json
import os
import subprocess
import sys

REPO = "/workspace/builders-blog"
OWNER = "mhiroash"
REMOTE_REPO = "builders-blog"
BRANCH = "main"

# Limite por lote. 80 KB deixa margem folgada para o JSON e para o ambiente.
MAX_PAYLOAD = 80_000

# Ficheiros que interessam para recuperação (o dist/ é reconstruível pelo build.py).
INCLUDE_DIRS = ["posts", "scripts", "templates", "assets", "docs", "seguranca", "reconstituicao"]
INCLUDE_FILES = ["README.md", "PROGRESSO.md", ".gitignore"]
SKIP_SUFFIX = (".bak-markdown", ".copy")
# O dist-live é cópia do que está publicado; pesa e não é fonte de verdade.
SKIP_PREFIX = ("reconstituicao/dist-live/",)


def collect_files():
    files = []
    for d in INCLUDE_DIRS:
        base = os.path.join(REPO, d)
        if not os.path.isdir(base):
            continue
        for root, _dirs, names in os.walk(base):
            if ".git" in root:
                continue
            for name in sorted(names):
                if name.endswith(SKIP_SUFFIX):
                    continue
                full = os.path.join(root, name)
                rel = os.path.relpath(full, REPO)
                if any(rel.startswith(p) for p in SKIP_PREFIX):
                    continue
                try:
                    with open(full, encoding="utf-8") as f:
                        files.append({"path": rel, "content": f.read()})
                except (UnicodeDecodeError, OSError):
                    continue
    for name in INCLUDE_FILES:
        full = os.path.join(REPO, name)
        if os.path.isfile(full):
            with open(full, encoding="utf-8") as f:
                files.append({"path": name, "content": f.read()})
    return files


def batches(files, limit=MAX_PAYLOAD):
    """Agrupa ficheiros em lotes cujo JSON não passa de `limit` bytes."""
    cur, size = [], 0
    for f in files:
        # custo aproximado deste ficheiro no JSON (path + conteúdo + pontuação)
        cost = len(json.dumps(f, ensure_ascii=False)) + 2
        if cost > limit:
            # um ficheiro sozinho já é grande: vai num lote só para ele
            if cur:
                yield cur
                cur, size = [], 0
            yield [f]
            continue
        if size + cost > limit and cur:
            yield cur
            cur, size = [], 0
        cur.append(f)
        size += cost
    if cur:
        yield cur


def push(chunk, index, total, dry_run=False):
    payload = {
        "owner": OWNER,
        "repo": REMOTE_REPO,
        "branch": BRANCH,
        "message": f"backup automático via conector GitHub (lote {index}/{total})",
        "files": chunk,
    }
    blob = json.dumps(payload, ensure_ascii=False)
    if dry_run:
        print(f"  lote {index}/{total}: {len(chunk)} ficheiros, {len(blob)} bytes (dry-run)")
        return True
    out = subprocess.run(
        ["tivra-team", "connector-call", "github", "push_files", blob],
        capture_output=True, text=True,
    )
    ok = out.returncode == 0 and ("sha" in out.stdout or "commit" in out.stdout.lower())
    if ok:
        print(f"  lote {index}/{total}: {len(chunk)} ficheiros, {len(blob)} bytes — OK")
    else:
        err = (out.stderr or out.stdout or "").strip().splitlines()
        print(f"  lote {index}/{total}: FALHOU — {err[-1] if err else 'sem saída'}", file=sys.stderr)
    return ok


def main():
    dry = "--dry-run" in sys.argv
    files = collect_files()
    if not files:
        print("nada para empurrar", file=sys.stderr)
        return 1
    chunks = list(batches(files))
    total = len(chunks)
    print(f"push off-site: {len(files)} ficheiros em {total} lote(s)")
    failures = 0
    for i, chunk in enumerate(chunks, 1):
        if not push(chunk, i, total, dry):
            failures += 1
    if failures:
        print(f"push off-site INCOMPLETO: {failures}/{total} lote(s) falharam", file=sys.stderr)
        return 1
    print(f"push off-site OK ({len(files)} ficheiros, {total} lote(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
