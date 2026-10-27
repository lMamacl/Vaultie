---
name: kb-compile
description: "Rebuilds Vaultie indexes, maps of content, navigation, and context buffers after approved knowledge changes."
---

# kb-compile — kompilacja indeksów, nawigacji i bufora kontekstu

## Cel
Automatyczne przebudowanie całej warstwy nawigacyjnej i kompilatów (`90_Meta/_index.md`, wszystkich plików MOC, bufora `90_Meta/hot.md` oraz manifestów) na podstawie aktualnego stanu notatek w katalogach produkcyjnych (`10_`–`50_`).

## Kiedy użyć
- Po zatwierdzeniu i przeniesieniu nowych notatek z `00_Inbox/_proposals/` do folderów produkcyjnych.
- Po zarchiwizowaniu lub usunięciu notatki.
- Na koniec sesji roboczej przed zrobieniem finałowego commita.

## Kroki
1. **Git Snapshot (Przed):** Sprawdź stan Git. Zrób automatyczny commit roboczy (`git add -A && git commit -m "pre-compile: stash work"`), jeśli w drzewie roboczym są niezatwierdzone zmiany.
2. **Aktualizacja MOC-ów:**
   - Przeskanuj podfoldery `10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/`.
   - Zaktualizuj plik MOC w każdym z tych folderów (np. `10_Libraries/Libraries MOC.md`). Wstaw sekcję ze spisem Notatek przypisanych do tego folderu (na podstawie pola `up:` wskazującego na dany MOC).
3. **Regeneracja `_index.md`:**
   - Przelicz liczbę notatek w każdym katalogu.
   - Odczytaj najnowsze rekordy decyzji z `30_Decisions/` (status `accepted`) i umieść je w sekcji "Ostatnie Decyzje".
   - Podepnij odnośniki do `Libraries MOC`, `Patterns MOC`, `Decisions MOC`, `Snippets MOC`, `Concepts MOC`.
4. **Aktualizacja Hot Buffer (`90_Meta/hot.md`):**
   - Odczytaj ostatnio dodane lub zmodyfikowane notatki z repozytorium.
   - Zaktualizuj w sekcji "Bieżący Punkt Skupienia" oraz "Ostatnio Modyfikowane Notatki".
5. **Generowanie manifestu:**
   - Zaktualizuj `.vault-meta/manifest.json` zawierający listę wszystkich notatek wraz z ich typami i tagami.
6. **Git Snapshot (Po):** Zatwierdź wszystkie zmiany wygenerowane przez proces kompilacji (`git add -A && git commit -m "compile: rebuild index, MOCs, hot buffer and manifest"`).

## Input
- Brak (działa na całym vaultcie).

## Output
- Zaktualizowany `90_Meta/_index.md`.
- Zaktualizowany `90_Meta/hot.md`.
- Zaktualizowane pliki MOC we wszystkich folderach.
- Zaktualizowany manifest w `.vault-meta/manifest.json`.

## Guardrails
- **NIE modyfikuj treści samej notatki w folderach `10_`–`50_`.** Kompilacja zmienia WYŁĄCZNIE pliki w `90_Meta/`, pliki MOC w folderach oraz pliki manifestu.
- Pamiętaj o wykonaniu snapshotu Git przed i po kompilacji.

## Warianty
- Brak.
