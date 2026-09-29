---
name: kb-archive
description: "Archives or retires stale Vaultie notes safely. Use when reviewing, archiving, or retiring outdated library, pattern, decision, or snippet notes."
---

# kb-archive — archiwizacja nieaktualnych lub wycofanych notatek

## Cel
Przenoszenie zestarzałych, nieużywanych lub wycofanych notatek z folderów produkcyjnych (`10_`–`50_`) do katalogu `99_Archive/` wraz ze spójnym usunięciem ich ze spisów treści i MOC-ów.

## Kiedy użyć
- Gdy notatka uzyska werdykt `verdict: avoid` i nie była aktualizowana od ponad 12 miesięcy.
- Gdy użytkownik prosi: "zarchiwizuj notatkę X", "przenieś do archiwum Y", "usuń przestarzały stack".

## Kroki
1. **Analiza kwalifikacyjna:**
   - Wyryj notatki spełniające kryteria automatycznej archiwizacji (np. z raportu `kb-lint` lub bezpośredniego wskazania).
   - Potwierdź, że plik znajduje się w jednej ze ścieżek `10_` do `50_`.
2. **Prezentacja propozycji:** Zgłoś użytkownikowi listę notatek przewidzianych do archiwizacji i poproś o zatwierdzenie.
3. **Przeniesienie pliku:** Po akceptacji przenieś plik `.md` z dotychczasowej ścieżki produkcyjnej do folderu `99_Archive/`.
4. **Czyszczenie MOC i nawigacji:**
   - Otwórz właściwy plik MOC (np. `10_Libraries/Libraries MOC.md`) i usuń z niego odnośnik `[[...]]` do zarchiwizowanej notatki.
   - Odnotuj archiwizację w dzienniku sesji `90_Meta/sessions/`.
5. **Kompilacja:** Uruchom `kb-compile`, aby przeliczyć statystyki w `90_Meta/_index.md`.

## Input
- Wikilink do notatki lub lista notatek do zarchiwizowania.

## Output
- Przeniesione pliki w folderze `99_Archive/`.
- Zaktualizowane pliki MOC i `_index.md`.

## Guardrails
- **NIGDY nie usuwaj plików trwale z dysku (`rm`). Archiwizacja to wyłącznie przeniesienie do `99_Archive/`.**
- Wymagana wyraźna akceptacja użytkownika przed przeniesieniem któregokolwiek z plików z warstwy produkcyjnej.

## Warianty
- Brak.
