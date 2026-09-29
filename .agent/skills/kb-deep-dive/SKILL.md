---
name: kb-deep-dive
description: "Produces a detailed engineering analysis of how a technology works internally, including architecture, performance limits, and implementation pitfalls."
---

# kb-deep-dive — głęboka analiza technologii / tematu Y

## Cel
Przeanalizowanie wewnętrznego mechanizmu działania technologii Y (architektura under-the-hood, alokacja pamięci, reaktywność, ograniczenia wydajnościowe i pułapki) oraz przygotowanie kompleksowej notatki dydaktyczno-inżynieryjnej.

## Kiedy użyć
- Gdy użytkownik prosi: "zrób deep dive dla tematu Y", "chcę zgłębić jak działa biblioteka Y", "przeanalizuj internals technologii Z".

## Integracja MCP
- **tavily MCP / fetch MCP:** Pobranie oficjalnej dokumentacji, wycieczek po kodzie (code walkthroughs) oraz artykułów "under the hood".
- **github MCP:** Przejrzenie kluczowych plików źródłowych repozytorium (np. core loop, state manager, memory layer).

## Kroki
1. **Identyfikacja rdzenia:** Ustal, jakie są kluczowe moduły technologii Y (np. reconciler, event loop, parser, storage engine).
2. **Pobranie źródeł:** Użyj Tavily i Fetch MCP do zebrania głębokiej wiedzy inżynieryjnej.
3. **Analiza wewnętrzna:** Zdefiniuj zasady działania, wykresy przepływu danych oraz znane pułapki (*gotchas*).
4. **Wygenerowanie Notatki:** Wypełnij szablon `.agent/templates/tpl-deep-analysis.md` lub `tpl-library.md`.
5. **Zapis Propozycji:** Zapisz plik w `00_Inbox/_proposals/tpl-deep-analysis-<slug>.md`.

## Output
- Plik propozycji głębokiej analizy w `00_Inbox/_proposals/tpl-deep-analysis-<slug>.md`.

## Guardrails
- Notatka musi zawierać sekcję "Jak to zastosuję w kodzie" oraz konkrety architektoniczne zamiast ogólników marketingowych.
