---
name: kb-solve-problem
description: "Researches how comparable projects solve an engineering problem, then proposes a context-specific solution with sources and rejected alternatives."
---

# kb-solve-problem — poszukiwanie wzorców i rozwiązanie problemu X

## Cel
Przeszukanie istniejących implementacji Open Source oraz artykułów technicznych w celu odkrycia, jak problem X został zadresowany w różnych projektach, a następnie wyekstrahowanie uniwersalnego wzorca architektonicznego.

## Kiedy użyć
- Gdy użytkownik pyta: "Mam problem X, jak to rozwiązano w innych projektach?", "szukam rozwiązań dla problemu Y", "jak obsłużyć X w architekturze".

## Integracja MCP
- **github MCP:** Szukaj implementacji i testów w porównywalnych projektach; gwiazdki repozytorium pomagają znaleźć przykłady, ale nie są dowodem poprawności ani jakości wzorca.
- **tavily MCP / search:** Pobierz artykuły inżynieryjne z firm technologicznych (np. Uber, Linear, Figma engineering blogs).
- **fetch MCP:** Pobierz pełną treść kluczowych fragmentów dokumentacji.

## Przebieg pracy

### 1. Zrozum problem
- Zapisz objaw/cel, kontekst systemu, ograniczenia i to, co już zostało sprawdzone.
- Wskaż brakujące informacje, które mogą zmienić wybór (np. idempotencja, wymagania dostępności, skala zespołu).
- Jeśli bez nich rekomendacja byłaby myląca, zadaj krótkie pytania. W pozostałych przypadkach podaj jawne założenia i warianty warunkowe.

### 2. Przeszukaj Vaultie przed siecią
- Użyj `kb-query` oraz indeksu, aby znaleźć powiązane biblioteki, wzorce, ADR-y, lekcje, snippety i wcześniejsze analizy.
- Szukaj po problemie i symptomach, nie tylko po nazwie technologii.
- Odróżnij brak wyników od dowodu, że rozwiązanie nie istnieje.

### 3. Zdecyduj, czy potrzebny jest research zewnętrzny
Uruchom research, gdy lokalna wiedza nie wystarcza do potwierdzenia istotnego twierdzenia, gdy wersja/API mogły się zmienić lub gdy źródła w Vaultie są sprzeczne. Preferuj w tej kolejności: dokumentację/RFC/specyfikację/źródło pierwotne, badanie lub pomiar opisujący metodę, a następnie techniczne omówienie. Popularność artykułu ani liczba gwiazdek repozytorium nie są same w sobie dowodem jakości rozwiązania.

### 4. Porównaj rozwiązania
- Zakończ jednoznaczną decyzją: co wybierasz, dla jakiego kontekstu i na podstawie jakich kryteriów.
- Dla każdej istotnej odrzuconej alternatywy napisz krótko, dlaczego nie wybrano jej w tym przypadku oraz jaki fakt zmieniłby tę decyzję. Nie pozostawiaj uzasadnienia wyłącznie w tabeli trade-offów.
- Nie twierdź, że źródło potwierdza więcej, niż faktycznie mówi. Oznacz syntezę agenta jako syntezę.
- Jeśli materiału dowodowego brakuje, wynik ma to powiedzieć i zaproponować test lub dalsze pytanie badawcze.

### 5. Pokaż źródła przy twierdzeniach
Dla każdego kluczowego twierdzenia podaj odnośnik do źródła oraz lokalizację (sekcja, strona, wersja lub fragment). Podaj pełny URL, tytuł, autora/organizację i datę dostępu; datę publikacji/wersję, jeśli jest dostępna. Cytaty dosłowne ogranicz do niezbędnego minimum. Odróżniaj dokumentację bieżącego API od dowodu na skuteczność praktyki architektonicznej.

### 6. Zwróć użyteczny brief
Użyj `.agent/templates/tpl-solution-brief.md`. W czacie przedstaw najpierw krótką rekomendację, potem założenia, alternatywy, dowody, ryzyka, pewność i kolejny krok. Zapisz brief wyłącznie jako propozycję w `00_Inbox/_proposals/` po uzgodnieniu lub gdy użytkownik prosi o zapis. Nie zapisuj automatycznie do `10_`–`50_`.

### 7. Wzorzec dopiero po analizie
Jeśli problem prowadzi do wzorca wielokrotnego użytku, przygotuj osobną propozycję na bazie `.agent/templates/tpl-pattern.md`. Nie uogólniaj jednego przypadku lub pojedynczego artykułu do „uniwersalnego wzorca” bez porównania zastosowań i przeciwwskazań.

## Output
- Najpierw odpowiedź w czacie według struktury solution brief.
- Opcjonalny solution brief w `00_Inbox/_proposals/` po prośbie lub uzgodnieniu z użytkownikiem.
- Klipy źródłowe w `00_Inbox/_clips/` lub ekstrakty w `00_Inbox/_raw/` tylko wtedy, gdy wykonano research i zapis jest potrzebny.
- Osobna propozycja wzorca tylko wtedy, gdy analiza wskazuje wzorzec wielokrotnego użytku.

## Guardrails
- Nie zapisuj ani nie promuj notatek bezpośrednio do `10_`–`50_`; pokaż draft/diff do akceptacji.
- Nie przedstawiaj braku wyników jako dowodu nieistnienia rozwiązania.
- Nie przypisuj źródłu twierdzeń, których ono nie popiera; ujawnij sprzeczne dowody i niewiadome.
- Nie obiecuj jednoznacznego rozstrzygnięcia, gdy źródła są niewystarczające.
