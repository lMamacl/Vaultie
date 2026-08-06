# kb-compile — kompilacja indeksów, MOC-ów i manifestów

## Cel
Automatyczna aktualizacja warstwy kompilatów (`90_Meta/` i MOC-y) na bazie zawartości warstwy treści produkcyjnej (`10_`–`50_`). Zapewnia spójność nawigacji i statystyk.

## Kiedy użyć
- Po przeniesieniu nowej notatki do folderu produkcyjnego.
- Na koniec sesji roboczej przed wykonaniem finalnego commita.
- Gdy użytkownik poprosi: "skompiluj vault", "odśwież indeksy", "przebuduj MOC".

## Kroki
1. **Git Snapshot (Przed):** Sprawdź stan Git. Zrób automatyczny commit roboczy (`git add -A && git commit -m "pre-compile: stash work"`), jeśli w drzewie roboczym są niezatwierdzone zmiany.
2. **Aktualizacja MOC-ów:**
   - Przeskanuj foldery produkcyjne (`10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/`).
   - Odczytaj z frontmattera każdej notatki pole `up: "[[Nazwa MOC]]"`.
   - Zaktualizuj plik MOC (np. `10_Libraries/Libraries MOC.md`) wpisując listę powiązanych notatek do odpowiednich sekcji tematycznych (np. podział na ekosystemy).
3. **Regeneracja `_index.md`:**
   - Zlicz liczbę notatek w każdym z folderów produkcyjnych.
   - Wpisz te statystyki do sekcji "Statystyki i ostatnie akcje" w `90_Meta/_index.md`.
   - Zbierz 5 najnowszych decyzji z `30_Decisions/` (posortowanych po `created` malejąco) i wklej je jako listę do sekcji "Ostatnie decyzje" w `90_Meta/_index.md`.
   - Zlicz pliki w `00_Inbox/_clips/` i wstaw informację o zaległościach.
4. **Generowanie manifestu:**
   - Stwórz lub zaktualizuj plik `90_Meta/_manifest.json`.
   - Zapisz tam listę wszystkich plików w vaultcie z ich rozmiarami, tagami, typami i datami modyfikacji (`updated`). Służy to do optymalizacji wyszukiwania i szybkiego wykrywania zmian.
5. **Git Snapshot (Po):** Zatwierdź wszystkie zmiany wygenerowane przez proces kompilacji (`git add -A && git commit -m "compile: rebuild index, MOCs and manifest"`).

## Input
- Brak (analizuje stan całego vaulta).

## Output
- Zaktualizowany `90_Meta/_index.md`.
- Zaktualizowane pliki `Libraries MOC.md`, `Patterns MOC.md`, `Decisions MOC.md`, `Snippets MOC.md`, `Concepts MOC.md`.
- Zaktualizowany `90_Meta/_manifest.json`.

## Guardrails
- **NIGDY nie edytuj ręcznych notatek produkcyjnych (`10_`–`50_`) poza samymi plikami MOC.**
- Modyfikacja plików MOC powinna dotyczyć wyłącznie list odnośników w wyznaczonych sekcjach. Nie nadpisuj nagłówków i opisów obszarów zdefiniowanych przez użytkownika.

## Warianty
- Brak.
