# kb-compare — porównanie bibliotek i technologii

## Cel
Porównanie dwóch lub więcej technologii lub bibliotek na podstawie ich dojrzałości, wydajności, ergonomii i zgodności z architekturą, a następnie wygenerowanie notatki porównawczej.

## Kiedy użyć
- Gdy użytkownik pyta: "co lepsze: Zustand czy Redux?", "porównaj Fastify z Express", "wybierz silnik bazy danych".
- Przed podjęciem kluczowej decyzji architektonicznej (ADR).

## Kroki
1. **Analiza wejścia:** Zweryfikuj, czy porównywane biblioteki posiadają już swoje notatki w `10_Libraries/` lub pliki w `00_Inbox/_raw/`. Jeśli nie, pobierz informacje o nich za pomocą `kb-extract` i `kb-lib-analyze`.
2. **Kompilacja kryteriów:** Zdefiniuj kryteria oceny (np. bundle size, łatwość testowania, typowanie TS, wsparcie społeczności, wydajność).
3. **Tworzenie macierzy:** Zbuduj tabelę porównawczą (Macierz Kryteriów) na podstawie szablonu `.agent/templates/tpl-comparison.md`.
4. **Zapis propozycji:** Zapisz plik jako `00_Inbox/_proposals/tpl-comparison-<slug>.md`.
5. **Generowanie decyzji (ADR) z flagą `--promote`:**
   - Wygeneruj zarys decyzji architektonicznej na szablonie `tpl-decision.md` i umieść go w `00_Inbox/_proposals/tpl-decision-YYYY-MM-DD-<slug>.md` wskazując rekomendowany wybór i uzasadnienie.

## Input
- Lista nazw bibliotek lub technologii do porównania (minimum 2).
- Opcjonalna flaga `--promote` (generuje powiązany plik decyzji ADR w `_proposals/`).

## Output
- Nowy plik propozycji porównania w `00_Inbox/_proposals/`.
- Opcjonalnie: nowy plik propozycji decyzji ADR (`tpl-decision.md`) w `00_Inbox/_proposals/`.

## Guardrails
- Porównanie musi być obiektywne i opierać się na faktach (benchmarki, oficjalne dane), a nie na subiektywnej opinii agenta.
- Rekomendacja końcowa (synteza) musi jasno wskazywać zwycięzcę w określonym kontekście projektowym.

## Warianty
- Standardowe porównanie: Zapisuje `tpl-comparison` w `_proposals/`.
- `--promote`: Dodatkowo generuje propozycję decyzji ADR `tpl-decision` w `_proposals/`.
