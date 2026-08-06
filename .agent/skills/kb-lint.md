# kb-lint — automatyczny audyt spójności i walidacja schematów

## Cel
Weryfikacja jakości, kompletności i spójności logicznej notatek w vaultcie w celu wykrywania błędów struktury, pustych sekcji, martwych linków oraz sprzecznych metadanych.

## Kiedy użyć
- Gdy użytkownik prosi o: "zrób porządki", "sprawdź vault", "uruchom lintera", "znajdź błędy".
- Automatycznie jako element weryfikacji przed zakończeniem sesji roboczej.

## Kroki
Przeskanuj pliki w folderach `10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/` oraz `00_Inbox/` pod kątem następujących reguł:

1. **Sieroty (Orphans):**
   - Notatki z typów `library`, `pattern`, `decision`, `snippet`, `concept` nieposiadające poprawnie zdefiniowanego pola `up:` we frontmatterze AND brak jakichkolwiek linków wchodzących do tej notatki z innych plików.
2. **Martwe linki (Dead Links):**
   - Wyszukaj odnośniki typu `[[Nazwa Pliku]]` prowadzące do nieistniejących notatek w vaultcie.
3. **Brakujący/Niekompletny Frontmatter:**
   - Porównaj frontmatter każdej notatki z jej schematem (zdefiniowanym w `.agent/AGENTS.md` oraz szablonach). Upewnij się, że kluczowe pola (np. `type`, `title`, `created`, `updated`, `up`) istnieją i mają poprawny format.
4. **Stale Versions (Przestarzałe wersje bibliotek):**
   - Dla notatek o typie `library`: zgłoś te, w których pole `updated` jest starsze niż 6 miesięcy. Wymagają one zweryfikowania, czy nie pojawiła się nowa wersja biblioteki.
5. **Verdict Consistency (Spójność decyzji):**
   - Zgłoś sytuację, w której `verdict` to `adopt` (rekomendacja produkcyjna), ale `confidence` wynosi `low` (brak wystarczającego doświadczenia).
6. **Missing Alternatives (Brak alternatyw):**
   - Notatki typu `library` z pustą listą alternatyw (`alternatives: []`). Każda biblioteka powinna mieć wymienione co najmniej 2 alternatywy.
7. **Unverified Snippets (Nieweryfikowane snipety):**
   - Snippety o statusie `verified: false`, które zostały utworzone lub zmodyfikowane dawniej niż 30 dni temu.
8. **Puste Sekcje (Empty Sections):**
   - Nagłówki Markdown (np. `## Gotchas` lub `## Model mentalny`), pod którymi nie ma żadnej treści (lub znajduje się tylko placeholder szablonowy typu `<!-- ... -->` albo `- `).
9. **Zalegający Surowiec (Stale Raw Files):**
   - Pliki w `00_Inbox/_raw/` starsze niż 14 dni, które nie zostały przetworzone ani usunięte.

### Generowanie raportu:
Stwórz plik raportu w lokalizacji `90_Meta/sessions/lint-YYYY-MM-DD.md`. Raport powinien zawierać:
- Podsumowanie liczby sprawdzonych plików i wykrytych naruszeń.
- Tabelaryczną listę wykrytych problemów (Ścieżka do pliku | Typ błędu | Opis i rekomendacja).

## Input
- Brak (skanuje cały vault).

## Output
- Raport z audytu zapisany w `90_Meta/sessions/lint-YYYY-MM-DD.md`.
- Wypisanie najważniejszych błędów bezpośrednio w oknie czatu/terminala.

## Guardrails
- Skill jest wyłącznie procesem walidacyjnym (read-only). Nie modyfikuje ani nie usuwa żadnych plików w vaultcie poza zapisaniem raportu.

## Warianty
- Brak.
