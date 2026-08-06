# Vault Operating Manual

Ten plik jest jedynym źródłem prawdy o strukturze i regułach tego vaulta.
Każdy agent czyta go na starcie sesji. Adaptery w `.agent/adapters/` tylko tu wskazują.

## Czym jest ten vault

Inżynierska baza wiedzy: nauka i analiza bibliotek oraz rozwiązań, które właściciel wykorzystuje w codziennej pracy programistycznej. Nie jest to dziennik ani ogólny second brain. Każda notatka musi odpowiadać na pytanie „jak to zastosuję w kodzie".

## Warstwy

1. `.agent/` — zarządcza. Reguły, skille, szablony, adaptery. Modyfikacja tylko na wyraźne polecenie.
2. `00_Inbox/`, `10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/`, `99_Archive/` — treść.
3. `90_Meta/` — kompilaty. Generowane, w pełni odtwarzalne z warstwy 2.

## Prawa zapisu

| Ścieżka | Agent |
|---|---|
| `00_Inbox/` (`_raw/`, `_clips/`, `_batch/`) | zapis swobodny |
| `90_Meta/` | zapis swobodny (to kompilaty) |
| `10_`–`50_` | propozycja w `00_Inbox/_proposals/` + akceptacja właściciela |
| `99_Archive/` | archiwizacja za akceptacją |
| `.agent/` | tylko na wyraźne polecenie |

Zabronione bezwarunkowo: usuwanie plików z `10_`–`50_`, `git push --force`, nadpisywanie notatki bez pokazania diffa.

## Punkt wejścia

NIE czytaj całego vaulta. Zawsze w kolejności:

1. `90_Meta/_index.md` — mapa i punkty wejścia
2. `90_Meta/queries.md` — gotowe zapytania, jeśli szukasz przekrojowo
3. dopiero potem konkretne notatki

## Taksonomia

- `10_Libraries/<nazwa>.md` — jedna biblioteka/narzędzie. Verdict, API, gotchas, wersja.
- `20_Patterns/<nazwa>.md` — wzorzec niezależny od biblioteki. Problem, rozwiązanie, pułapki.
- `30_Decisions/YYYY-MM-DD-<temat>.md` — ADR. Co wybrano i dlaczego, z linkami do 10/20.
- `40_Snippets/<nazwa>.md` — sprawdzony kod. Zawsze z wersją i flagą `verified`.
- `50_Concepts/<nazwa>.md` — notatka edukacyjna/koncepcyjna (np. event loop, GC, CAP theorem).
- `00_Inbox/` — surowiec: dumpy docsów, logi błędów, klipy z auto-researchu, extrakty.
- `99_Archive/` — przestarzałe notatki (`verdict: avoid` lub nieużywane >12 miesięcy).

## Frontmatter — obowiązkowy

```yaml
---
type: library | pattern | decision | snippet | concept | clip | moc | raw-extract | comparison | deep-analysis | review
title: string
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [lista]
aliases: []
up: "[[nadrzędna notatka]]"      # breadcrumb, wymagany poza MOC
---
```

Dla `type: library` dodatkowo:
```yaml
lib: string                       # nazwa pakietu
ecosystem: js | python | rust | go | dotnet | other
version: string                   # wersja, na której robiono analizę
verdict: adopt | trial | assess | hold | avoid
alternatives: [lista]
confidence: low | medium | high
used_in: [lista projektów]
```

Dla `type: decision`: `status: proposed | accepted | superseded | deprecated`, `supersedes`, `affects`.
Dla `type: snippet`: `lib`, `language`, `version`, `verified: true | false`.
Dla `type: concept`: `domain: frontend | backend | devops | architecture | data | security | other`, `prerequisite`, `difficulty: beginner | intermediate | advanced`.
Dla `type: clip`: `source` (URL), `retrieved`, `relevance: 1-5`, `topic`.
Dla `type: raw-extract`: `source`, `extracted`, `extractor`, `content_type`, `language`, `word_count`.

`verdict` używa 5-poziomowej skali Technology Radar:
- `adopt` — sprawdzona w produkcji, domyślny wybór
- `trial` — testowana w projektach pilotażowych
- `assess` — obiecująca, warto zbadać (default przy tworzeniu)
- `hold` — nie stosować w nowych projektach
- `avoid` — aktywnie odradzana

## Naming conventions

- **Pliki notatek**: `kebab-case.md` (np. `tanstack-query.md`)
- **Pliki decyzji**: `YYYY-MM-DD-kebab-case.md` (np. `2026-08-06-state-management.md`)
- **Pliki klipów**: `YYYY-MM-DD-slug.md` (np. `2026-08-06-zustand-v5-release.md`)
- **Foldery**: `NumerPrefix_PascalCase` (np. `10_Libraries`)
- **Tagi**: `kebab-case`, flat (np. `#state-management`, `#performance`)
- **Aliasy**: `aliases: []` w frontmatter
- **Pola YAML**: `snake_case`
- **Linki**: wikilinks `[[nazwa]]`, NIE markdown links `[]()`
- **Język**: frontmatter + tagi EN, treść sekcji PL
- **Diagramy**: Mermaid inline, NIE Excalidraw

## Co NIE trafia do vault

- Klucze API, hasła, sekrety, credetials
- Całe repozytoria kodu źródłowego (kod żyje w Git)
- Automatycznie generowana dokumentacja API (TypeDoc/Javadoc)
- Tymczasowe logi i notatki z sesji debugowania (chyba że w `00_Inbox/_raw/` z `.gitignore`)
- Dane prywatne i wrażliwe

## Pluginy

Wymagane:
- **Obsidian Git**: automatyczny commit i synchronizacja
- **Templater**: tworzenie notatek z szablonów
- **Linter**: automatyczne formatowanie i porządek YAML
- **Bases** (core): natywne widoki tabelaryczne (Obsidian 1.9+)

Opcjonalne:
- **Dataview**: zaawansowane zapytania DQL
- **Propsec** / **Metadata Validator**: walidacja schematów frontmatter w tle
- **Tag Wrangler**: zarządzanie tagami

## Skille

| Skill | Kiedy |
|---|---|
| `kb-scout` | „poszukaj nowych materiałów", cykliczny digest |
| `kb-extract` | „pobierz tę stronę", „ściągnij dokumentację", ekstrakcja stron |
| `kb-ingest` | surowiec z `00_Inbox` → właściwy folder/propozycja |
| `kb-lib-analyze` | analiza jednej biblioteki → `10_Libraries` |
| `kb-compare` | porównanie 2+ bibliotek → `30_Decisions` |
| `kb-query` | odpowiedź na pytanie na podstawie vaulta |
| `kb-compile` | odbudowa `_index.md` i MOC-ów |
| `kb-lint` | audyt spójności i walidacja schematów |
| `kb-update` | aktualizacja istniejącej notatki o nowe wersje |
| `kb-archive` | przeniesienie przestarzałych notatek do `99_Archive` |
| `kb-merge` | scalenie duplikatów notatek |
| `kb-review` | wygenerowanie tygodniowego przeglądu (weekly review) |
| `kb-pattern-extract` | wyciągnięcie wzorca z grupy snippetów/bibliotek |

Definicje w `.agent/skills/<nazwa>.md`.

## Escape hatch & Koniec sesji

Jeśli zadanie wymaga utworzenia nowej struktury lub wykracza poza znane schematy, agent proponuje wpis do `00_Inbox/_proposals/` przed realizacją.

W trakcie i na koniec sesji: Zapisz `90_Meta/sessions/YYYY-MM-DD-HHMM.md`: co zrobiono, co utworzono/zmieniono, co zostało otwarte. Potem `git add -A && git commit -m "session: <podsumowanie>"`. Snapshot commit ZAWSZE przed `kb-compile` i `kb-reindex`.
