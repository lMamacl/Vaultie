# Adapter: Antigravity

- **Workspace root:** root katalog otwartego workspace; unikaj ścieżek zależnych od konkretnego komputera.
- **Instrukcje projektu:** root `AGENTS.md` → `.agent/AGENTS.md`.
- **Natywne skille workspace:** `.agent/skills/<skill-name>/SKILL.md`; każdy `SKILL.md` musi mieć YAML `name` i `description`.
- **Wywołanie:** `/kb-query`, `/kb-scout`, `/kb-solve-problem` itd. Można też opisać cel naturalnym językiem, aby agent dobrał skill.
- **Odświeżenie:** po instalacji/zmianie rejestru rozpocznij nową sesję albo odśwież workspace, jeśli polecenie nie pojawi się w menu `/`.
- **Web research:** używaj dostępnego narzędzia wyszukiwania sieciowego w `kb-scout`, `kb-extract` i `kb-solve-problem`; nie zakładaj, że konkretne MCP jest zawsze skonfigurowane.
- **Shell:** wybierz PowerShell lub shell udostępniony przez środowisko; ścieżki i komendy mają być względem workspace.
