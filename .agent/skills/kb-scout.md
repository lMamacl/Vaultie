# kb-scout — automatyczny przwiad i odkrywanie nowych materiałów

## Cel
Cykliczne przeszukiwanie zewnętrznych źródeł (GitHub Releases, RSS, wyszukiwanie w sieci, Hacker News) pod kątem nowych wydań, artykułów i dyskusji zgodnych z definicjami w pliku `.agent/watchlist.yaml`.

## Kiedy użyć
- Gdy użytkownik prosi: "poszukaj nowych materiałów", "sprawdź co nowego", "uruchom auto-research", "wygeneruj digest".
- Automatycznie w ramach zadań cyklicznych (cron/CI).

## Kroki
1. **Wczytanie konfiguracji:** Odczytaj plik `.agent/watchlist.yaml`. Pobierz zdefiniowane tematy (`topics`), źródła (`sources`) oraz daty ostatniego sprawdzenia (`last_checked`).
2. **Odkrywanie (Discover):** Dla każdego tematu z upłyniętym czasem od `last_checked`:
   - `releases`: Odpytaj GitHub API o nowe wydania (Releases) wybranej biblioteki.
   - `feeds`: Pobierz wpisy z kanałów RSS z ostatnich 7 dni.
   - `search`: Użyj narzędzia wyszukiwania (np. Tavily, Firecrawl search lub web search) dla fraz kluczowych (`keywords`).
   - `discussions`: Sprawdź wpisy na Hacker News / Reddit posiadające wymaganą liczbę punktów.
3. **Dedyplikacja (Dedupe):** Odzuć adresy URL oraz tytuły, które istnieją już w `00_Inbox/_clips/` lub w `10_Libraries/` (sprawdź pola `source:` we frontmatterach).
4. **Triage trafności i jakości źródła:**
   - Oceń oddzielnie trafność dla problemu i bezpośredniość źródła (czy to źródło pierwotne, aktualna dokumentacja, standard, badanie z opisaną metodą, techniczne omówienie czy dyskusja społeczności).
   - Preferuj dokumentację/standardy dla faktów o API i zachowaniu normatywnym; dla porównań skuteczności sprawdź metodę, kontekst i ograniczenia badań. Gwiazdki, popularność i pozycja w wyszukiwarce nie są miarą prawdziwości.
   - Zweryfikuj kluczowe twierdzenia w treści źródła, nie tylko w snippecie wyniku wyszukiwarki. Zapisz także czego źródło nie rozstrzyga.
   - Przeanalizuj trafność dla obecnego vaulta; powiązany materiał z werdyktem `adopt` może zwiększać priorytet, ale nie jakość dowodu.
   - Odrzuć pozycje poniżej `min_relevance`; uwzględnij limit `max_clips_per_run`. Nie generuj wniosku „jednoznacznego”, gdy źródła są sprzeczne lub pośrednie.
5. **Zapis klipów:**
   - Wywołaj `kb-extract` dla wybranych wartościowych URL-i.
   - Zapisz klipy do `00_Inbox/_clips/YYYY-MM-DD-<slug>.md` przy użyciu szablonu `.agent/templates/tpl-clip.md`.
6. **Generowanie Digestu:**
   - Utwórz lub zaktualizuj plik podsumowania `90_Meta/digests/YYYY-WW.md` z tabelą zebranych materiałów i rekomendacjami promocji (max 3 pozycje).
7. **Aktualizacja znacznika:** Zaktualizuj pole `last_checked` dla przetworzonych tematów w `.agent/watchlist.yaml`.

## Input
- Konfiguracja z `.agent/watchlist.yaml`.
- Opcjonalny parametr filtra tematu: `--topic=<id>`.

## Output
- Nowe pliki klipów w `00_Inbox/_clips/`.
- Plik podsumowania tygodniowego w `90_Meta/digests/YYYY-WW.md`.
- Zaktualizowany `.agent/watchlist.yaml`.

## Guardrails
- **NIGDY nie zapisuj odnalezionych materiałów bezpośrednio do folderów produkcyjnych (`10_`–`50_`).** Scout produkuje wyłącznie surowy materiał i klipy w `00_Inbox/`.
- Szanuj limity zaryzykowań API i maksymalną liczbę pobieranych klipów (`max_clips_per_run`).

## Warianty
- Standardowy: skanuje wszystkie tematy w watchlist.
- `--topic=<id>`: ogranicza badanie do konkretnego wątku.
