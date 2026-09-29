---
name: kb-pattern-extract
description: "Extracts a reusable engineering pattern from multiple implementations, libraries, or snippets and records its trade-offs."
---

# kb-pattern-extract — ekstrakcja wzorca z grupy snippetów lub bibliotek

## Cel
Analiza powtarzalnych rozwiązań programistycznych zawartych w kilku notatkach lub snippetach i wyekstrahowanie ogólnego, uniwersalnego wzorca architektonicznego/projektowego do szablonu wzorca.

## Kiedy użyć
- Gdy w vaultcie znajduje się 3+ snippetów lub bibliotek realizujących podobne zadanie (np. optymistyczne aktualizacje UI, reaktywne stanówki, pooling połączeń).
- Gdy użytkownik prosi: "wyciągnij z tego wzorzec", "zaabstrakcjonuj to rozwiązanie".

## Kroki
1. **Analiza zestawu wejściowego:** Odczytaj wskazane notatki z `10_Libraries/` lub `40_Snippets/`.
2. **Identyfikacja rdzenia:** Wyodrębnij wspólny problem, kluczową abstrakcję, mechanizm działania oraz powtarzające się pułapki.
3. **Formułowanie wzorca:**
   - Opisz problem niezależnie od konkretnego języka czy biblioteki.
   - Zdefiniuj czyste rozwiązanie oraz sytuacje, kiedy TEGO WZORCA NIE STOSOWAĆ.
4. **Generowanie propozycji:**
   - Wypełnij szablon `.agent/templates/tpl-pattern.md`.
   - Zapisz wynik jako `00_Inbox/_proposals/tpl-pattern-<slug>.md`.
5. **Zgłoszenie do akceptacji:** Przedstaw gotowy draft wzorca użytkownikowi.

## Input
- Wskazanie co najmniej 3 notatek (bibliotek lub snippetów) stanowiących materiał źródłowy.

## Output
- Nowy plik propozycji wzorca w `00_Inbox/_proposals/tpl-pattern-<slug>.md`.

## Guardrails
- **NIGDY nie zapisuj propozycji wzorca bezpośrednio do `20_Patterns/`.** Wszystkie nowe wzorce muszą zostać zatwierdzone przez użytkownika w `_proposals/`.
- Wzorzec musi być technicznie agnostyczny (niezależny od konkretnego frameworka), z przykładami użycia w realnych narzędziach w sekcji "Implementacje w bibliotekach".

## Warianty
- Brak.
