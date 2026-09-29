---
name: kb-solution-blueprint
description: "Designs a solution architecture for a stated engineering problem, compares options and risks, and prepares a decision brief or ADR proposal."
---

# kb-solution-blueprint — projektowanie rozwiązania Z, komponentów i decyzji ADR

## Cel
Zaprojektowanie optymalnej architektury dla nowego rozwiązania Z, wskazanie wymaganych komponentów, identyfikacja ryzyk i wąskich gardeł, zderzenie z alternatywami (inne języki/biblioteki) i przygotowanie formalnej decyzji architektonicznej (ADR).

## Kiedy użyć
- Gdy użytkownik prosi: "chcę zbudować rozwiązanie Z", "zaprojektuj architekturę dla Z", "jakie komponenty i biblioteki wybrać do Z".

## Integracja MCP
- **tavily MCP / search:** Weryfikacja dojrzałości rynkowej komponentów, benchmarków i opinii społeczności.
- **github MCP:** Ocena aktywności repozytoriów, wskaźników maintenance, znanych nierozwiązanych problemów w wyznaczonych bibliotekach.

## Kroki
1. **Doprecyzowanie wymagań:** Zdefiniuj kluczowe wymagania funkcjonalne i niefunkcjonalne (FR / NFR) dla rozwiązania Z.
2. **Dobór komponentów & alternatyw:** Wybierz 2-3 warianty stosu technologicznego (np. TypeScript vs Rust vs Go, Postgres vs DuckDB).
3. **Analiza Ryzyk Architektonicznych:** Zidentyfikuj potencjalne wyzwania (skalowalność, synchronizacja stanu, koszty utrzymania).
4. **Wygenerowanie Macierzy Porównawczej:** Wypełnij szablon `.agent/templates/tpl-comparison.md`.
5. **Wygenerowanie Rekomendacji ADR:** Wypełnij szablon `.agent/templates/tpl-decision.md` wskazując uzasadnienie wyboru i konsekwencje.
6. **Zapis Propozycji:** Zapisz pliki w `00_Inbox/_proposals/tpl-comparison-<slug>.md` oraz `tpl-decision-YYYY-MM-DD-<slug>.md`.

## Output
- Plik propozycji porównania w `00_Inbox/_proposals/`.
- Plik propozycji decyzji ADR w `00_Inbox/_proposals/`.

## Guardrails
- Przestrzegaj zasad tworzenia decyzji ADR: jasno wskaż zrezygnowane alternatywy i negatywne konsekwencje wyboru.
