#!/usr/bin/env python3
"""Checklist de segurança para build.py reconstituído."""

from pathlib import Path
import re
import subprocess
import hashlib

REPO_ROOT = Path("/workspace/builders-blog")
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build.py"
DEPLOY_SCRIPT = REPO_ROOT / "scripts" / "deploy.sh"

def sha256(file_path: Path) -> str:
    """Calcular SHA256 de um ficheiro."""
    return hashlib.sha256(file_path.read_bytes()).hexdigest()

def check_injection_javascript(content: str) -> list:
    """Verificar injecção de links `javascript:`."""
    issues = []
    matches = re.findall(r'href=["\']javascript:([^"\']*)["\']', content)
    if matches:
        issues.append(f"Injecção JavaScript detectada: {matches}")
    return issues

def check_path_traversal(content: str) -> list:
    """Verificar path traversal no slug."""
    issues = []
    matches = re.findall(r'\.\./[^\s"\'<>]+', content)
    if matches:
        issues.append(f"Path traversal possível: {matches}")
    return issues

def check_secrets(content: str) -> list:
    """Verificar segredos (API keys, tokens, passwords)."""
    secrets = [
        r'(api[_-]?key)\s*=\s*["\']?[^"\']+["\']?',
        r'(secret)\s*=\s*["\']?[^"\']+["\']?',
        r'(password)\s*=\s*["\']?[^"\']+["\']?',
        r'(token)\s*=\s*["\']?["\']?[a-zA-Z0-9_-]{20,}["\']?',
        r'Bearer\s+[a-zA-Z0-9_-]{20,}',
        r'BEGIN [A-Z ]*PRIVATE KEY',
    ]
    issues = []
    for pattern in secrets:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            issues.append(f"Padrão verificado: {pattern}")
            issues.append(f"  Encontrado: {matches[:3]}")  # Primeiros 3
    return issues

def check_no_exec_injection(content: str) -> list:
    """Verificar comandos de execução (subprocess, os.system, etc.)."""
    dangerous = [
        r'os\.exec',
        r'os\.system',
        r'subprocess\.call',
        r'subprocess\.run',
        r'subprocess\.Popen',
        r'eval\(',
    ]
    issues = []
    for pattern in dangerous:
        matches = re.findall(pattern, content)
        if matches:
            issues.append(f"Comando de execução encontrado: {pattern}")
    return issues

def main():
    print("=" * 60)
    print("CHECKLIST DE SEGURANÇA — build.py reconstituído")
    print("=" * 60)
    print()

    # 1. Verificar build.py
    print("1. build.py")
    print("-" * 60)
    if BUILD_SCRIPT.exists():
        content = BUILD_SCRIPT.read_text(encoding='utf-8')
        print(f"  ✓ Ficheiro existe ({BUILD_SCRIPT.stat().st_size} bytes, SHA256: {sha256(BUILD_SCRIPT)[:16]}...)")

        issues = []
        issues.extend(check_injection_javascript(content))
        issues.extend(check_path_traversal(content))
        issues.extend(check_secrets(content))
        issues.extend(check_no_exec_injection(content))

        if issues:
            print("  ✗ ACHADOS:")
            for i, issue in enumerate(issues, 1):
                print(f"    [{i}] {issue}")
        else:
            print("  ✓ SEM achados")
    else:
        print("  ✗ Ficheiro não encontrado")
    print()

    # 2. Verificar deploy.sh
    print("2. deploy.sh")
    print("-" * 60)
    if DEPLOY_SCRIPT.exists():
        content = DEPLOY_SCRIPT.read_text(encoding='utf-8')
        print(f"  ✓ Ficheiro existe ({DEPLOY_SCRIPT.stat().st_size} bytes)")

        issues = []
        issues.extend(check_injection_javascript(content))
        issues.extend(check_secrets(content))

        if issues:
            print("  ✗ ACHADOS:")
            for i, issue in enumerate(issues, 1):
                print(f"    [{i}] {issue}")
        else:
            print("  ✓ SEM achados")
    else:
        print("  ✗ Ficheiro não encontrado")
    print()

    # 3. Verificar posts por segredos
    print("3. posts/*.md")
    print("-" * 60)
    posts_found = 0
    posts_with_secrets = 0
    for md_file in REPO_ROOT.glob("posts/*.md"):
        posts_found += 1
        content = md_file.read_text(encoding='utf-8')
        secrets = check_secrets(content)
        if secrets:
            posts_with_secrets += 1
            print(f"  ✗ {md_file.name}: {secrets}")
        else:
            print(f"  ✓ {md_file.name}")
    print(f"  Total: {posts_found} posts, {posts_with_secrets} com segredos")
    print()

    # 4. Verificar dist/ por segredos
    print("4. dist/ por segredos")
    print("-" * 60)
    dist_has_secrets = False
    dist_dir = REPO_ROOT / "dist"
    if dist_dir.exists():
        for file in dist_dir.rglob("*"):
            if file.is_file() and file.suffix in ('.html', '.css', '.js'):
                try:
                    content = file.read_text(encoding='utf-8')
                    secrets = check_secrets(content)
                    if secrets:
                        dist_has_secrets = True
                        print(f"  ✗ {file.relative_to(REPO_ROOT)}: {secrets}")
                except Exception:
                    pass
    if not dist_has_secrets:
        print("  ✓ SEM segredos em dist/")
    print()

    # 5. Verificar se build.py usa html.escape
    print("5. html.escape no build.py")
    print("-" * 60)
    if BUILD_SCRIPT.exists():
        content = BUILD_SCRIPT.read_text(encoding='utf-8')
        if 'html.escape' in content:
            print("  ✓ html.escape presente (escape de input)")
        else:
            print("  ⚠ html.escape não encontrado (input não escapado)")
    print()

    print("=" * 60)
    print("CHECKLIST CONCLUÍDO")
    print("=" * 60)

if __name__ == "__main__":
    main()