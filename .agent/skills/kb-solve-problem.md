# kb-solve-problem — poszukiwanie wzorców i rozwiązanie problemu X

## Cel
Przeszukanie istniejących implementacji Open Source oraz artykułów technicznych w celu odkrycia, jak problem X został zadresowany w różnych projektach, a następnie wyekstrahowanie uniwersalnego wzorca architektonicznego.

## Kiedy użyć
- Gdy użytkownik pyta: "Mam problem X, jak to rozwiązano w innych projektach?", "szukam rozwiązań dla problemu Y", "jak obsłużyć X w architekturze".

## Integracja MCP
- **github MCP:** Przeszukaj kody źródłowe i nagłówki funkcji na GitHubie (repozytoria z dużą liczbą gwiazdek).
- **tavily MCP / search:** Pobierz artykuły inżynieryjne z firm technologicznych (np. Uber, Linear, Figma engineering blogs).
- **fetch MCP:** Pobierz pełną treść kluczowych fragmentów dokumentacji.

## Kroki
1. **Analiza problemu:** Zdefiniuj kluczowe frazy zapytania dla GitHub i Tavily (np. `infinite canvas rendering`, `optimistic state sync`).
2. **Skanowanie implementacji (Discover):** Odpytaj serwery MCP o 3-5 popularnych rozwiązań problemu X.
3. **Zapis materiałów surowych:** Wygeneruj pliki klipów w `00_Inbox/_clips/YYYY-MM-DD-problem-<slug>.md` z linkami i wycinkami kodu.
4. **Formułowanie Wzorca:** Wyekstrahuj wspólne podejścia, trade-offy oraz pułapki.
5. **Wygenerowanie Propozycji Wzorca:** Wypełnij szablon `.agent/templates/tpl-pattern.md` i zapisz wynik jako `00_Inbox/_proposals/tpl-pattern-<slug>.md`.

## Output
- Klipy źródłowe w `00_Inbox/_clips/`.
- Plik propozycji wzorca w `00_Inbox/_proposals/tpl-pattern-<slug>.md`.

## Guardrails
- Nie zapisuj notatki bezpośrednio w `20_Patterns/`. Przedstaw diff/draft użytkownikowi.
