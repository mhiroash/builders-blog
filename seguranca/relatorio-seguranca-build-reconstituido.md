# Relatório de segurança — build.py reconstituído

**Autor:** Agentes (Tivra)
**Data:** 2026-10-17
**Tarefa:** TASK-2026-10-17-028 — Reconstituir o código-fonte do blog de notícias IA
**Âmbito:** `scripts/build.py` e `scripts/deploy.sh` reconstituídos; `posts/*.md`; `dist/`

## Veredicto

**SEM ACHADOS ALTA.** O `build.py` reconstituído passa o checklist de segurança do relatório anterior (TASK-2026-10-16-011), com as duas defesas que faltavam já implementadas.

## Checklist corrido

| # | Verificação | Resultado |
|---|---|---|
| 1 | Injecção de links `javascript:` | ✓ Bloqueado (`safe_link` remove o href) |
| 2 | Injecção `data:` URI | ✓ Bloqueado (`safe_link` remove o href) |
| 3 | Path traversal no slug | ✓ Bloqueado (`slugify` valida e rejeita `/`, `\`, `.`) |
| 4 | Segredos (API keys, tokens, passwords) | ✓ Zero segredos em `build.py`, `deploy.sh`, `posts/`, `dist/` |
| 5 | HTML injection (tags não escapadas) | ✓ `html.escape` aplicado a todo o input |
| 6 | Execução de comandos arbitrários | ✓ Sem `os.system`, `subprocess`, `eval` no `build.py` |
| 7 | Verificação pré-publicação no `deploy.sh` | ✓ Aborta se detectar segredos ou marcadores `[confirmar]` |

## Achados do relatório anterior (TASK-2026-10-16-011) e estado

O relatório anterior identificou 2 achados ALTA **latentes** no `scripts/build.py` original:

- **A1 — Injecção de links `javascript:`**: o build original inseria o `href` sem validação.
  - **Estado na reconstituição:** CORRIGIDO. A função `safe_link` bloqueia `javascript:` e `data:` e escapa o `href`.
- **A2 — Path traversal no slug**: o slug derivado do título podia conter `../`.
  - **Estado na reconstituição:** CORRIGIDO. A função `slugify` remove caracteres não-alfanuméricos e rejeita slugs com separadores de caminho.

## Testes de segurança executados

```
[seguro] link javascript:: sem tags activas
[seguro] script tag: sem tags activas
[seguro] img onerror: sem tags activas
[seguro] data URI: sem tags activas
```

## Notas

- O `deploy.sh` inclui verificações pré-publicação (grep por segredos e por marcadores `[confirmar]`) que abortam o deploy antes de publicar.
- **Nada foi republicado.** O site live mantém-se intacto; esta reconstituição é apenas do código-fonte.
- O `dist-live/` (HTML descarregado do site) está no `.gitignore` — é artefacto de referência, não fonte.

## Ficheiros

| Ficheiro | SHA256 (prefixo) |
|---|---|
| `scripts/build.py` | ver `git log` |
| `scripts/deploy.sh` | ver `git log` |
| `docs/checklist-seguranca-build.py` | script do checklist |
