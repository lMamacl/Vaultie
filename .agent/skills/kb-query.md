# kb-query — inteligentne przeszukiwanie wiedzy w vaultcie

## Cel
Umożliwia agentowi i użytkownikowi szybkie znalezienie odpowiedzi na pytania dotyczące bibliotek, wzorców, decyzji architektonicznych i konceptów bez przeszukiwania całego repozytorium.

## Kiedy użyć
- Gdy użytkownik pyta: "jakie mamy biblioteki do stanu?", "co zdecydowaliśmy w sprawie X?", "gdzie znajdę wzorzec Y?", "jak działa Z?".
- Gdy agent musi odnaleźć istniejące notatki przed stworzeniem nowej, aby zapobiec duplikacji.

## Kroki
Przeszukuj dane według następującego łańcucha (fallback chain):
1. **Index (`90_Meta/_index.md`):** Sprawdź główne Mapy Treści (MOC) i sekcje nawigacyjne.
2. **Nazwane kwerendy (`90_Meta/queries.md`):** Zobacz, czy szukany problem odpowiada jednemu z gotowych widoków (np. `adopt-stack`, `do-oceny`, `decyzje-30-dni`).
3. **Filtry frontmatter:** Użyj wyszukiwania po polach meta w Obsidianie (jeśli dostępne) lub przeczytaj nagłówki YAML notatek z odpowiednich folderów.
4. **Wyszukiwarka wbudowana Obsidian Search:** Wykorzystaj natywne filtry globalne.
5. **Wyszukiwanie semantyczne (qmd):** Jeśli qmd jest zainstalowane, uruchom komendę `qmd search "<fraza>"` w katalogu głównym.
6. **Ripgrep (Grep Search):** Wykonaj niskopoziomowe przeszukanie plików za pomocą narzędzia `grep_search` dla konkretnych słów kluczowych.
7. **Brak wyników:** Poinformuj użytkownika, że informacja nie istnieje w bazie i zaproponuj jej zbadanie.

## Input
- Fraza wyszukiwania, pytanie lub nazwa poszukiwanego komponentu/pojęcia.

## Output
- Lista pasujących notatek z krótkim podsumowaniem ich statusu (np. `adopt`, `trial`, itp.) oraz ścieżek dostępu.

## Guardrails
- NIGDY nie skanuj całego vaulta czytając każdy plik po kolei — to zużywa limit kontekstu i spowalnia działanie.
- Zawsze zaczynaj wyszukiwanie od góry łańcucha fallbacków.

## Warianty
- Brak.
