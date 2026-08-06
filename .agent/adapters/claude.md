# Adapter: Claude Code

- Punkt wejścia: `CLAUDE.md` → `.agent/AGENTS.md`
- Skille: opcjonalnie odwzoruj `.agent/skills/*` na `.claude/skills/<nazwa>/SKILL.md` z jedną linią: „Follow `.agent/skills/<nazwa>.md`."
- Shell dostępny: `kb-lint`, `qmd`, git snapshoty działają w pełni
- MCP: jeśli podłączysz Firecrawl MCP lub GitHub MCP, `kb-scout` i `kb-extract` korzystają z nich zamiast z HTTP API — reszta pętli bez zmian
