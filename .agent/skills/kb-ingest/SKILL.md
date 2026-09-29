---
name: kb-ingest
description: "Triages and converts raw Inbox material into a sourced, structured proposal or clip for Vaultie."
---

# kb-ingest — kategoryzacja i przetwarzanie surowca z Inboxu

## Cel
Automatyczne przekształcanie surowych danych i ekstraktów zebranych w `00_Inbox/_raw/` w uporządkowane notatki oparte o szablony i umieszczanie ich w folderze `00_Inbox/_proposals/` lub `00_Inbox/_clips/`.

## Kiedy użyć
- Gdy użytkownik prosi o: "zaimportuj artykuły z raw", "przetwórz pobrany plik", "przenieś surowy ekstrakt do bazy", "uruchom triage".

## Kroki
1. **Analiza źródła:** Odczytaj pliki w `00_Inbox/_raw/`. Sprawdź pole `content_type` oraz `extractor` we frontmatterze surowego ekstraktu.
2. **Dobór szablonu i kategoryzacja:**
   - Jeśli `content_type` = `article` lub `discussion` LUB plik pochodzi z auto-researchu jako artykuł prasowy/blogowy:
     - Użyj szablonu `.agent/templates/tpl-clip.md`.
     - Zapisz wynik jako `00_Inbox/_clips/YYYY-MM-DD-<slug>.md`.
   - Jeśli `content_type` = `docs` lub `changelog` LUB dotyczy oficjalnej dokumentacji nowej biblioteki:
     - Użyj szablonu `.agent/templates/tpl-library.md`.
     - Zapisz wynik jako propozycję: `00_Inbox/_proposals/tpl-library-<slug>.md`.
   - Jeśli `content_type` = `tutorial` lub `api-reference` LUB zawiera przydatne fragmenty kodu:
     - Użyj szablonu `.agent/templates/tpl-snippet.md` lub `.agent/templates/tpl-concept.md`.
     - Zapisz wynik jako propozycję: `00_Inbox/_proposals/tpl-snippet-<slug>.md` LUB `00_Inbox/_proposals/tpl-concept-<slug>.md`.
3. **Kompilacja i formatowanie:** Wypełnij sekcje nowo utworzonego pliku na podstawie danych z pliku źródłowego. Zachowaj komentarze `<!-- AI-INSTRUCTIONS -->`.
4. **Czyszczenie surowca:** Po udanej konwersji i zapisaniu nowego pliku, usuń oryginalny plik z `00_Inbox/_raw/` (lub przenieś do `99_Archive/` jeśli jest tam cenna treść historyczna).
5. **Zgłoszenie do akceptacji:** Przedstaw użytkownikowi listę wygenerowanych propozycji w `00_Inbox/_proposals/` i poproś o decyzję o wdrożeniu do warstwy produkcyjnej (`10_`–`50_`).

## Input
- Jeden lub więcej surowych plików z rozszerzeniem `.md` znajdujących się w folderze `00_Inbox/_raw/`.

## Output
- Nowy plik klipu w `00_Inbox/_clips/` lub propozycji w `00_Inbox/_proposals/`.

## Guardrails
- **NIGDY nie zapisuj wygenerowanych notatek bezpośrednio do folderów produkcyjnych (`10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/`)** bez wyraźnej akceptacji użytkownika. Zawsze przechodź przez proces propozycji (`_proposals/`).
- Wypełniaj wszystkie sekcje szablonu. Puste sekcje zostaną odrzucone przez `kb-lint`.

## Warianty
- Brak.
