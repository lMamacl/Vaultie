# kb-lib-analyze — szczegółowa analiza biblioteki programistycznej

## Cel
Analiza funkcjonalności, przydatności i dojrzałości wybranej biblioteki/narzędzia na bazie jej dokumentacji lub kodu źródłowego, a następnie wygenerowanie ustrukturyzowanej notatki w folderze propozycji.

## Kiedy użyć
- Gdy użytkownik pyta: "przeanalizuj bibliotekę X", "dodaj Zustand do bibliotek", "oceń przydatność pakietu Y".
- Po pobraniu dokumentacji biblioteki za pomocą `kb-extract`.

## Kroki
1. **Pobranie danych:** Wykorzystaj przekazany plik z ekstraktem dokumentacji w `00_Inbox/_raw/` lub pobierz go za pomocą `kb-extract` (jeśli podano URL).
2. **Ekstrakcja informacji:** Przeanalizuj treść dokumentacji pod kątem:
   - Problemu, który biblioteka rozwiązuje.
   - Modelu mentalnego (jak myśleć o jej strukturze i mechanizmie działania).
   - Najważniejszego API (3-5 najczęstszych wywołań).
   - Pułapek (Gotchas), ograniczeń i wydajności.
   - Dostępnych alternatyw.
3. **Generowanie propozycji:**
   - Domyślnie: użyj szablonu `.agent/templates/tpl-library.md`. Zapisz plik jako `00_Inbox/_proposals/tpl-library-<nazwa>.md`.
   - Z flagą `--deep`: użyj szablonu `.agent/templates/tpl-deep-analysis.md` (rekomendowane dla kluczowych komponentów architektury). Zapisz plik jako `00_Inbox/_proposals/tpl-deep-analysis-<nazwa>.md`.
4. **Walidacja:** Upewnij się, że każda sekcja szablonu została uzupełniona rzetelnymi informacjami (żadnych pustych sekcji ani placeholderów).
5. **Zgłoszenie:** Poinformuj użytkownika o wygenerowaniu draftu analizy i poproś o weryfikację.

## Input
- Ścieżka do pliku ekstraktu dokumentacji w `00_Inbox/_raw/` LUB bezpośredni adres URL dokumentacji biblioteki.
- Opcjonalna flaga `--deep` (wymusza pełną, 10-sekcyjną analizę głęboką).

## Output
- Nowy plik propozycji w `00_Inbox/_proposals/` oparty o szablon `tpl-library.md` lub `tpl-deep-analysis.md`.

## Guardrails
- **NIGDY nie zapisuj wyniku bezpośrednio do folderu `10_Libraries/`.** Zawsze generuj plik jako prozycję w `00_Inbox/_proposals/`.
- Każda biblioteka musi mieć zdefiniowane co najmniej 2 alternatywy produkcyjne oraz minimum 1 gotcha (pułapkę).

## Warianty
- `tpl-library.md`: standardowa notatka o bibliotece (domyślnie).
- `--deep`: zaawansowana analiza strukturalna na szablonie `tpl-deep-analysis.md`.
