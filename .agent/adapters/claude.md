# Adapter: Claude Code

- Punkt wejścia: `CLAUDE.md` → `.agent/AGENTS.md`
- Skille: definicje źródłowe to `.agent/skills/<nazwa>/SKILL.md`; dla Claude Code przygotuj cienki wrapper `.claude/skills/<nazwa>/SKILL.md`, który wskazuje na tę ścieżkę źródłową.
- Shell dostępny: `kb-lint`, `qmd`, git snapshoty działają w pełni
- MCP: jeśli podłączysz Firecrawl MCP lub GitHub MCP, `kb-scout` i `kb-extract` korzystają z nich zamiast z HTTP API — reszta pętli bez zmian
