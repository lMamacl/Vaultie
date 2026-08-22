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

W katalogu `.agent/skills/` znajdują się pełne definicje skilli (`kb-query`, `kb-ingest`, `kb-extract`, `kb-lint`, `kb-compile`, `kb-lib-analyze`, `kb-compare`, `kb-scout`, `kb-update`, `kb-archive`, `kb-merge`, `kb-review`, `kb-pattern-extract`, `kb-canvas`, `kb-blackbox`, `kb-lesson-certify`, `kb-epistemic-solve`).


Pomocniczy skrypt integralności i planowania transakcji: `python3 .agent/scripts/vaultie-cli.py`.

## Escape hatch & Koniec sesji

Jeśli zadanie wymaga utworzenia nowej struktury lub wykracza poza znane schematy, agent proponuje wpis do `00_Inbox/_proposals/` przed realizacją.

W trakcie i na koniec sesji: Zaktualizuj `90_Meta/hot.md` i zapisz `90_Meta/sessions/YYYY-MM-DD-HHMM.md`. Potem `git add -A && git commit -m "session: <podsumowanie>"`.
