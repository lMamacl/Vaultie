# Vaultie — Inżynieryjna Baza Wiedzy (v1.0.0)

> Vaultie to usystematyzowana, agentyczna baza wiedzy i drugi mózg (Second Brain) inżyniera oprogramowania stworzony z myślą o efektywnej analizie bibliotek, wzorców, decyzji architektonicznych (ADR) oraz przetestowanych snippetów kodu.

---

## 🌟 Główne Cechy Systemu

- **Struktura Trójwarstwowa:** Ścisły podział na warstwę zarządczą (`.agent/`), treść produkcyjną (`10_`–`50_`) i odtwarzalne kompilaty (`90_Meta/`).
- **Autonomiczne Skille Agenta:** System posiada wbudowane skille CLI/Agent (w tym `kb-query`, `kb-ingest`, `kb-extract`, `kb-lint`, `kb-compile`, `kb-scout`, `kb-update`, `kb-archive`, `kb-merge`, `kb-review`, `kb-pattern-extract`).
- **Standard Technology Radar:** Klasyfikacja narzędzi według 5-poziomowego schematu (`adopt`, `trial`, `assess`, `hold`, `avoid`).
- **Zintegrowany Wygląd i Widoki Obsidian:** Kompatybilny z Obsidian Git, Linter oraz Obsidian Bases (v1.9+).
- **Auto-research & Health Monitoring:** Śledzenie zmian w bibliotekach poprzez `watchlist.yaml` oraz wbudowany `health-dashboard.md`.

---

## 📂 Struktura Vaulta

- `00_Inbox/` — Surowe ekstrakty, klipy ze stron i propozycje do akceptacji (`_proposals/`).
- `10_Libraries/` — Notatki o konkretnych pakietach i bibliotekach.
- `20_Patterns/` — Wzorce projektowe niezależne od języka/frameworka.
- `30_Decisions/` — Rekordy decyzji architektonicznych (ADR).
- `40_Snippets/` — Kod gotowy do wklejenia z oznaczoną flagą weryfikacji.
- `50_Concepts/` — Notatki pojęciowe i teoretyczne.
- `90_Meta/` — Indeksy (`_index.md`), spisy MOC, widoki `.base`, słownik, zapytania i dzienniki.
- `99_Archive/` — Zarchiwizowane i wycofane materiały.
- `.agent/` — Instrukcje wykonawcze, szablony i skille agentowe.

---

## 🚀 Zacznij tutaj

Nie musisz znać układu repozytorium, aby zacząć. Otwórz **[Zacznij tutaj](90_Meta/start-here.md)** w Obsidianie — znajdziesz tam wejścia do rozwiązywania problemów, wyszukiwania wiedzy, nauki i przeglądu materiałów.

Szybkie polecenie: „Przeanalizuj problem: [objaw]. Kontekst: [system i ograniczenia]. Porównaj możliwe rozwiązania, wskaż źródła, założenia i brakujące informacje.”

Dla agentów: przed edycją przeczytaj **[.agent/AGENTS.md](.agent/AGENTS.md)** — źródło prawdy o strukturze i prawach zapisu.
