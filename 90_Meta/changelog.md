---
type: raw-extract
title: "Changelog Vaultie"
created: 2026-08-06
updated: 2026-08-06
tags: [changelog, meta]
up: "[[90_Meta/_index]]"
---

# Changelog Vaultie

Wszystkie znaczące zmiany w strukturze i automatyzacjach bazy wiedzy Vaultie.

---

## [v1.0.0] - 2026-08-06

### Dodane
- **Struktura katalogów i konwencje:** Pełna architektura warstwowa (`00_Inbox/`, `10_Libraries/` – `50_Concepts/`, `90_Meta/`, `99_Archive/`, `.agent/`).
- **Standardy i zasady (AGENTS.md):** Zarządczy manual określający prawa zapisu, nazewnictwo i konwencje frontmattera.
- **Szablony notatek (Templates):** 11 kompletnych szablonównotatek w `.agent/templates/` zawierających instrukcje `<!-- AI-INSTRUCTIONS -->`.
- **Kompilaty i Widoki (Bases & MOCs):** 5 widoków Obsidian Bases (`.base`), Mapy Treści (MOC) dla każdego folderu, `_index.md`, `queries.md` oraz `glossary.md`.
- **Skille Core i Advanced:** Zbiór 13 autorskich skilli agentowych (`kb-query`, `kb-ingest`, `kb-extract`, `kb-lint`, `kb-compile`, `kb-lib-analyze`, `kb-compare`, `kb-scout`, `kb-update`, `kb-archive`, `kb-merge`, `kb-review`, `kb-pattern-extract`).
- **Auto-research i Monitorowanie:** Wbudowana konfiguracja `watchlist.yaml`, wskaźnik wyszukiwania semantycznego `qmd-config.json` oraz `health-dashboard.md`.
- **Weryfikacja E2E:** Pierwsza przykładowa linia notatek (`tanstack-query`, `optimistic-ui-updates`, ADR, snippet, concept) potwierdzająca pełne działanie systemu.
