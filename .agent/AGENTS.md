# Vault Operating Manual

Ten plik jest jedynym źródłem prawdy o strukturze i regułach tego vaulta.
Każdy agent czyta go na starcie sesji. Adaptery w `.agent/adapters/` tylko tu wskazują.

## Czym jest ten vault

Inżynierska baza wiedzy: nauka i analiza bibliotek oraz rozwiązań, które właściciel wykorzystuje w codziennej pracy programistycznej. Nie jest to dziennik ani ogólny second brain. Każda notatka musi odpowiadać na pytanie „jak to zastosuję w kodzie".

## Warstwy

1. `.agent/` — zarządcza. Reguły, skille, szablony, skrypty transakcyjne, adaptery. Modyfikacja tylko na wyraźne polecenie.
2. `00_Inbox/`, `10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/`, `99_Archive/` — treść.
3. `labs/` — sandbox ćwiczeń masterclass (`labs/web-engineering/<lesson-id>/`). Źródła commitowane; artefakty build w `.gitignore`.
4. `90_Meta/` — kompilaty, bufor kontekstu (`hot.md`), wizualne kanwy (`canvases/`), lekcje (`lessons/`). Generowane, w pełni odtwarzalne z warstwy 2.

## Prawa zapisu

| Ścieżka | Agent |
|---|---|
| `00_Inbox/` (`_raw/`, `_clips/`, `_batch/`) | zapis swobodny |
| `90_Meta/` | zapis swobodny (to kompilaty i bufor `hot.md`) |
| `labs/` | zapis po akceptacji struktury; laby przy realizacji lekcji |
| `10_`–`50_` | propozycja w `00_Inbox/_proposals/` + akceptacja właściciela |
| `99_Archive/` | archiwizacja za akceptacją |
| `.agent/` | tylko na wyraźne polecenie |

Zabronione bezwarunkowo: usuwanie plików z `10_`–`50_`, `git push --force`, nadpisywanie notatki bez pokazania diffa.

## Punkt wejścia

Dla użytkownika nowym ekranem startowym jest `90_Meta/start-here.md` — opisuje wejścia do rozwiązywania problemów, wyszukiwania i nauki. Agent nadal stosuje poniższy punkt wejścia; strona dla użytkownika nie zastępuje tych instrukcji.

NIE czytaj całego vaulta. Zawsze w kolejności:

1. `90_Meta/hot.md` — błyskawiczny bufor aktywnej sesji i ostatnich zadań
2. `90_Meta/_index.md` — mapa i punkty wejścia
3. `90_Meta/queries.md` — gotowe zapytania, jeśli szukasz przekrojowo
4. dopiero potem konkretne notatki

## Taksonomia

- `10_Libraries/<nazwa>.md` — jedna biblioteka/narzędzie. Verdict, API, gotchas, wersja.
- `20_Patterns/<nazwa>.md` — wzorzec niezależny od biblioteki. Problem, rozwiązanie, pułapki.
- `30_Decisions/YYYY-MM-DD-<temat>.md` — ADR. Co wybrano i dlaczego, z linkami do 10/20.
- `40_Snippets/<nazwa>.md` — sprawdzony kod. Zawsze z wersją i flagą `verified`.
- `50_Concepts/<nazwa>.md` — notatka edukacyjna/koncepcyjna.
- `90_Meta/canvases/<nazwa>.canvas` — wizualne tablice powiązań w formacie Obsidian Canvas.
- `00_Inbox/` — surowiec: dumpy docsów, logi błędów, klipy z auto-researchu.
- `99_Archive/` — przestarzałe notatki.

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

## Skille i Narzędzia

Każdy natywny skill znajduje się w `.agent/skills/<skill-name>/SKILL.md` z wymaganym YAML frontmatter (`name`, `description`). W Antigravity wywołuj go jako `/<skill-name>` albo opisz zadanie, aby agent dobrał go automatycznie. Skille są instrukcjami/workflowami dla agenta; nie zakładaj, że każdy z nich odpowiada samodzielnemu CLI.

Dostępne skille: `kb-archive`, `kb-blackbox`, `kb-canvas`, `kb-compare`, `kb-compile`, `kb-deep-dive`, `kb-epistemic-solve`, `kb-extract`, `kb-ingest`, `kb-lesson-certify`, `kb-lib-analyze`, `kb-lint`, `kb-merge`, `kb-pattern-extract`, `kb-query`, `kb-review`, `kb-scout`, `kb-solution-blueprint`, `kb-solve-problem`, `kb-update`.


Pomocniczy skrypt integralności i planowania transakcji: `python3 .agent/scripts/vaultie-cli.py`.

## Escape hatch & Koniec sesji

Jeśli zadanie wymaga utworzenia nowej struktury lub wykracza poza znane schematy, agent proponuje wpis do `00_Inbox/_proposals/` przed realizacją.

W trakcie i na koniec sesji: Zaktualizuj `90_Meta/hot.md` i zapisz `90_Meta/sessions/YYYY-MM-DD-HHMM.md`. Potem `git add -A && git commit -m "session: <podsumowanie>"`.
