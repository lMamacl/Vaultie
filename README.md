# Vaultie

Inżynierska baza wiedzy: nauka i analiza bibliotek, wzorców, decyzji architektonicznych oraz snippetów kodu przeznaczonych do codziennej pracy programistycznej.

## Quick Start

1. Otwórz ten folder jako vault w Obsidianie (`File` → `Open folder as vault`).
2. Włącz plugin Bases: `Settings` → `Core plugins` → `Bases`.
3. Ustaw `90_Meta/_index.md` jako notatkę startową.
4. Upewnij się, że zainstalowano i włączono wymagane pluginy (`Obsidian Git`, `Templater`, `Linter`).

## Dla agenta AI

Przeczytaj `.agent/AGENTS.md` jako jedyne źródło prawdy o strukturze i regułach tego vaulta, a następnie otwórz `90_Meta/_index.md`.

## Architektura i struktura

- `.agent/` — WARSTWA 1: Zarządzanie (AGENTS.md, skille, szablony, adaptery)
- `00_Inbox/` — WARSTWA 2: Surowiec (extrakty, klipy, propozycje)
- `10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/` — WARSTWA 2: Treść produkcyjna
- `90_Meta/` — WARSTWA 3: Kompilaty (index, MOC-i, queries, bases, sesje, mefisty)
- `99_Archive/` — Przestarzałe notatki
- `_assets/` — Załączniki i pliki binarne
