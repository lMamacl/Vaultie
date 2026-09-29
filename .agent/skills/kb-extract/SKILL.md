---
name: kb-extract
description: "Extracts a webpage, documentation, release note, PDF, or local source into a traceable raw item in the Vaultie Inbox."
---

# kb-extract — automatyczna ekstrakcja stron internetowych i dokumentacji

## Cel
Pobieranie zawartości stron internetowych, dokumentacji, changelogów lub plików lokalnych i konwertowanie ich na czysty, ustrukturyzowany markdown zapisywany w `00_Inbox/_raw/`.

## Kiedy użyć
- Gdy użytkownik chce: "pobierz dokumentację X", "wyciągnij treść z URL", "przeszukaj sieć pod kątem Y i pobierz wyniki", "przekonwertuj plik PDF".

## Kroki

### Tryb 1: Pojedynczy URL (url)
1. Sprawdź, czy URL nie był już przetwarzany (szukaj pola `source:` we frontmatterze w całym vaultcie).
2. Pobierz zawartość:
   - Użyj natywnego narzędzia agenta `read_url_content` (najszybsza i bezkosztowa metoda).
   - W przypadku trudności z renderowaniem JS lub blokadą: skorzystaj z API Jina Reader (`r.jina.ai/{url}`) lub Firecrawl scrape API (`/v2/scrape`).
3. Wyczyść tekst: usuń reklamy, skrypty śledzące, menu nawigacyjne, stopki i banery cookies.
4. Wygeneruj plik `00_Inbox/_raw/YYYY-MM-DD-<slug>.md` za pomocą szablonu `tpl-raw-extract.md`. Zachowaj URL, tytuł, autora/organizację, datę publikacji (jeśli jest dostępna), datę pobrania i wersję/sekcję źródła, jeśli istotne.
5. Oddziel wierne streszczenie źródła od syntezy agenta. Zaznacz ograniczenia i nie przypisuj źródłu wniosków, których nie zawiera.
6. Uruchom `kb-ingest` na zapisanym pliku, aby wygenerować propozycję; nie promuj automatycznie do treści produkcyjnej.

### Tryb 2: Lista URL-i (batch)
1. Odczytaj plik z listą adresów URL.
2. Dla każdego adresu po kolei uruchom kroki z **Trybu 1**.
3. Ogranicz liczbę jednoczesnych żądań, aby uniknąć rate-limitów i zablokowania IP.

### Tryb 3: Crawl dokumentacji (docs-crawl)
1. Użyj narzędzia takiego jak Firecrawl crawl API (`/v2/crawl`) lub Crawl4AI do pobrania całej witryny (np. dokumentacji biblioteki).
2. Zbierz pobrane podstrony w jeden ustrukturyzowany dokument lub serię powiązanych plików w `00_Inbox/_raw/`.
3. Dodaj odpowiednie tagi relacji i kolejności.

### Tryb 4: Wyszukiwanie sieciowe (search)
1. Użyj wyszukiwarki internetowej (np. Google/Tavily/Firecrawl search API) do znalezienia najnowszych publikacji dla określonej frazy.
2. Wybierz 3-5 najbardziej pasujących stron i dokonaj ich ekstrakcji wg **Trybu 1**.

## Input
- URL, ścieżka do pliku lokalnego, lista URL-i lub zapytanie wyszukiwania.
- Parametr trybu: `--mode=url|batch|docs-crawl|search`.

## Output
- Pliki ekstraktów z frontmatterem `type: raw-extract` zapisane w katalogu `00_Inbox/_raw/`.

## Guardrails
- **NIGDY nie zapisuj pobranych danych bezpośrednio do folderów `10_`–`50_` ani do `00_Inbox/_clips/`.** Dane z ekstrakcji zawsze muszą najpierw trafić jako surowiec do `00_Inbox/_raw/`.
- Zawsze usuwaj z pobranego kodu HTML zbędny kod znaczników, style i skrypty reklamowe przed zapisaniem do markdown.

## Warianty
- `--mode=url`: Pobiera pojedynczą stronę (domyślnie).
- `--mode=batch`: Pobiera listę stron z pliku tekstowego.
- `--mode=docs-crawl`: Pełzanie po domenie dokumentacji.
- `--mode=search`: Wyszukiwanie w sieci i ekstrakcja najlepszych linków.
