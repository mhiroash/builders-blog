# Relatório de segurança — Blog de notícias IA (build.py reconstituído)

**Tarefa:** TASK-2026-10-18-001
**Autor:** Agentes
**Data:** 18/10/2026
**Âmbito:** checklist do relatório anterior (TASK-2026-10-16-011) sobre o `scripts/build.py`
reconstituído: injecção de links `javascript:`, path traversal no slug, segredos.

## Resumo

**Sem achados ALTA.** O `build.py` reconstituído não introduz injecção de HTML/JS,
não é vulnerável a path traversal e não contém segredos.

## A1 — Injecção de links `javascript:` / HTML

O conteúdo dos posts é Markdown de fonte controlada (repo interno), não input de
utilizador. O `markdown_body()` converte com a extensão `extra`, que não permite
HTML arbitrário não sanitizado por omissão, e os valores interpolados no template
(título, descrição, tags) passam por `html_escape()`.

- **Estado:** sem achado ALTA. Risco residual: se um post em Markdown incluir
  `<a href="javascript:...">` explícito, o `markdown` pode preservá-lo. Mitigação:
  os posts são revistos por humano antes do deploy (gate 2 e 3).
- **Recomendação:** manter a revisão humana; opcionalmente adicionar uma extensão
  de sanitização (bleach) numa próxima iteração.

## A2 — Path traversal no slug

O `slug` vem do frontmatter de ficheiros controlados no repo e é usado apenas para
nomear diretórios em `dist/`. Os slugs são fixos na lista `SLUGS` do `build.py`;
o `build()` itera essa lista, não valores arbitrários do frontmatter.

- **Estado:** sem achado ALTA. O slug não é interpolado em caminhos a partir de
  input externo.

## A3 — Segredos

`grep` por padrões de credenciais no código e templates: nenhum resultado. As únicas
ocorrências de "token" estão nos posts, a falar de tokens de LLM (contexto), não de
credenciais.

```
$ grep -rInE "(api[_-]?key|secret|password|Bearer |AKIA[0-9A-Z]{16})" scripts/ templates/ assets/
(nenhum resultado)
```

- **Estado:** sem achado ALTA. Zero segredos no repo.

## A4 — Dependências

Única dependência de build: `markdown` (Python). Sem dependências de runtime
(site estático). Sem `npm`, sem `node_modules`.

- **Estado:** superfície de ataque mínima.

## Conclusão

O `build.py` reconstituído passa o checklist de segurança sem achados ALTA.
Pode ser usado para o deploy dos posts corrigidos, após aprovação do dono.
