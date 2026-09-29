---
name: kb-update
description: "Updates an existing Vaultie knowledge note using new evidence while preserving its history, links, and accepted context."
---

# kb-update — aktualizacja istniejących notatek produkcyjnych

## Cel
Bezpieczna aktualizacja istniejącej notatki w vaultcie (np. zmiana wersji biblioteki, dodanie nowych gotchas, zaktualizowanie snippetu) na podstawie nowych informacji bez utraty dotychczasowego kontekstu.

## Kiedy użyć
- Gdy pojawia się nowa wersja analizowanej biblioteki.
- Gdy użytkownik prosi: "zaktualizuj notatkę X", "dodaj nowe informacje do Y", "zmień wersję biblioteki Z".

## Kroki
1. **Identyfikacja notatki:** Odnajdź Notatkę Docelową w `10_`–`50_` po nazwie lub wikilinku `[[X]]`.
2. **Pobranie nowego źródła:** Pobierz nową dokumentację lub changelog (za pomocą `kb-extract` lub czytając podany surowiec).
3. **Analiza różnic:** Porównaj dotychczasową treść notatki z nowymi danymi:
   - Zidentyfikuj zmiany w API, deprecacje oraz nowe funkcjonalności.
   - Przygotuj proponowaną nową treść notatki, aktualizując pola `version` i `updated` we frontmatterze.
4. **Wyświetlenie DIFF (Kluczowy Guardrail):**
   - Przedstaw użytkownikowi w oknie czatu dokładne porównanie zmian (format diff z liniami `+` i `-`).
5. **Akceptacja i Zapis:**
   - Po uzyskaniu akceptacji użytkownika nadpisz notatkę produkcyjną nową zawartością.
   - Zaktualizuj powiązany MOC za pomocą `kb-compile`, jeśli uległ zmianie werdykt lub status.

## Input
- Wikilink do notatki docelowej (np. `[[tanstack-query]]`).
- Nowa treść, URL do changelogu lub surowy plik w `00_Inbox/_raw/`.

## Output
- Zaktualizowany plik w folderach `10_`–`50_`.

## Guardrails
- **BEZWZGLĘDNIE ZABRONIONE jest nadpisywanie istniejącej notatki bez wcześniejszego zaprezentowania użytkownikowi podglądu zmian (diffa) i uzyskania jego wyraźnej zgody.**
- Zachowaj autorskie uwagi użytkownika i wcześniej wyciągnięte wnioski z sekcji "Model mentalny" czy "Gotchas".

## Warianty
- Brak.
