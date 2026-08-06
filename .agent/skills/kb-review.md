# kb-review — generowanie tygodniowego przeglądu wiedzy (Weekly Review)

## Cel
Automatyczna synteza i przygotowanie zestawienia aktywności w vaultcie z ostatniego tygodnia: nowych i zaktualizowanych notatek, klipów czekających na decyzję oraz nieprzetestowanych snippetów.

## Kiedy użyć
- Gdy użytkownik prosi: "zrób tygodniowy przegląd", "wygeneruj weekly review", "podsumuj ten tydzień".
- Pod koniec tygodnia (np. w każdy piątek/niedzielę).

## Kroki
1. **Pobranie aktywności Git:** Przeanalizuj historię zmian w repozytorium (`git log --since="7 days ago" --name-status`) i znajdź utworzone oraz zmodyfikowane notatki w folderach `10_`–`50_`.
2. **Kolekcja klipów:** Odczytaj pliki w `00_Inbox/_clips/` o statusie `relevance >= 4` dodane w tym tygodniu.
3. **Kolekcja decyzji:** Wyciągnij propozycje decyzji z `30_Decisions/` ze stanem `status: proposed`.
4. **Kolekcja niesprawdzonych kodów:** Znajdź snippety w `40_Snippets/` ze stanem `verified: false` starsze niż 7 dni.
5. **Generowanie raportu:**
   - Wypełnij szablon `.agent/templates/tpl-review.md`.
   - Zapisz wynikowy dokument jako `90_Meta/sessions/review-YYYY-WW.md`.
6. **Prezentacja:** Przedstaw najważniejsze wnioski i rekomendacje do dalszej nauki/rozwoju bezpośrednio w oknie konwersacji.

## Input
- Brak (automatycznie pobiera dane z git log i vaulta za ostatnie 7 dni).

## Output
- Nowy dokument tygodniowego przeglądu w `90_Meta/sessions/review-YYYY-WW.md`.

## Guardrails
- Skill jest wyłącznie procesem generowania raportu podsumowującego. Nie dokonuje modyfikacji wpisów produkcyjnych.

## Warianty
- Brak.
