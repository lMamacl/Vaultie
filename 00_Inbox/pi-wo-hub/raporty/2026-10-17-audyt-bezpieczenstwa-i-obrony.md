# Raport Audytu: Bezpieczeństwo, Logika Gry i Integralność Akademicka Projektu „Pi-Wo”

**Data audytu:** 2026-10-17  
**Rola:** Audytor Bezpieczeństwa i Integralności Akademickiej  
**Projekt:** „Pi-Wo” (Poker Texas Hold'em w przeglądarce)  
**Uczelnia:** Politechnika Białostocka (Pracownia Specjalistyczna)  
**Skład zespołu (5 osób):** Maciej Cyuńczyk (Lider), Michał Pączkowski, Michał Małecki, Miłosz Szymczuk, Miłosz Pawlaczyk  

---

## CZĘŚĆ I: AUDYT BEZPIECZEŃSTWA I LOGIKI GRY (KRYTERIUM 5 PKT)

### 1. Maskowanie kart (Fog of War) w protokole WebSocket
- **Zagrożenie:** Otwarcie DevTools (zakładka Network -> WS) i podsłuchiwanie pakietów. Jeżeli serwer wysyła obiekt gracza z polem `holeCards` zamaskowanym jedynie na poziomie UI/CSS/Vue, następuje całkowita deanonimizacja kart przeciwników (Critical Information Disclosure).
- **Rozwiązanie architektoniczne:**
  1. **Autorytatywna projekcja stanu (Viewer Projection):** Serwer posiada w RAM pełny stan (`InternalGameState`). Przy tworzeniu payloadu dla danego gniazda serwer wykonuje funkcję transformującą `serializeStateForViewer(state, viewerUserId)`.
  2. **Reguła maskowania:**
     ```javascript
     const isMe = player.userId === viewerUserId;
     const isShowdown = (state.phase === 'showdown' || state.phase === 'settled');
     const shouldReveal = isShowdown && player.status !== 'folded' && player.showed;
     
     serializedPlayer.holeCards = (isMe || shouldReveal) ? player.holeCards : null;
     ```
  3. **Showdown vs Spasowanie (Fold/Muck):** Karty gracza, który spasował (`status === 'folded'`), NIGDY nie są ujawniane, nawet na showdownie. W przypadku, gdy wszyscy poza jednym graczem spasują (uncontested pot), ręka zwycięzcy również NIE jest ujawniana w protokole, chyba że gracz dobrowolnie wyśle akcję `hand:showCards`.
  4. **Oddzielenie zdarzeń:** Broadcast `hand:started` informuje jedynie o miejscach, dealerze i blindach. Karty własne trafiają do gracza w osobnym dedykowanym evencie prywatnym `hand:holeCards: { cards: ['Ah', 'Kd'] }` wysyłanym wyłącznie do socketu właściciela (`ws.send`).
  5. **Baza danych:** Karty trafiają do SQLite (`hand_players.hole_cards`) DOPIERO w transakcji zamykającej rękę. W trakcie gry istnieją wyłącznie w pamięci RAM serwera.

### 2. Ochrona salda żetonów (`ledger` + `users.chips` + `seats.stack`) i concurrency w SQLite
- **Zagrożenia:**
  1. *Double-spending / Race Condition:* Równoczesne dołączenie do dwóch stołów przy stanie konta wystarczającym na jeden buy-in.
  2. *Ujemne stany konta:* Zmniejszenie salda poniżej zera przy równoległych żądaniach HTTP/WS.
  3. *Desynchronizacja pamięci i bazy przy Leave/Disconnect:* Próba natychmiastowego wycofania stacka w trakcie trwającej licytacji lub podwójna wypłata przy rozłączeniu.
- **Rozwiązanie architektoniczne:**
  1. **Konfiguracja SQLite dla współbieżności:**
     - `PRAGMA journal_mode = WAL;` (pozwala na jednoczesne czytanie i zapis bez blokad odczytu).
     - `PRAGMA busy_timeout = 5000;` (zapobiega natychmiastowym błędom `SQLITE_BUSY`).
     - `PRAGMA foreign_keys = ON;`
     - Ograniczenia bazodanowe: `CHECK (chips >= 0)` w `users` oraz `CHECK (stack >= 0)` w `seats`.
  2. **Atomowe transakcje finansowe (`better-sqlite3`):**
     Operacje finansowe (buy-in, cash-out, settle) są zamykane w synchronicznych transakcjach `db.transaction()`:
     ```javascript
     // Atomowe pobranie żetonów z portfela:
     const res = db.prepare(`
       UPDATE users SET chips = chips - ? WHERE id = ? AND chips >= ?
     `).run(buyIn, userId, buyIn);
     if (res.changes === 0) throw new AppError('INSUFFICIENT_FUNDS', 422, 'Brak środków');
     ```
  3. **Zasada Cash-out podczas gry:**
     - Jeżeli gracz opuszcza stół lub zrywa połączenie w trakcie trwania ręki (`phase !== 'waiting'` oraz gracz bierze udział w rozdaniu):
       - Stan gracza zmienia się na `sitting_out` / `leaving`.
       - Włożone żetony (`totalContribution`) POZOSTAJĄ w puli.
       - Tury gracza są automatycznie pasowane (auto-fold / auto-check po upływie `turnDeadline`).
       - Zwrot pozostałego stacka do portfela `users.chips` i usunięcie z `seats` następuje DOPIERO w transakcji `settleHand` po zakończeniu ręki.
  4. **Księga audytowa (`ledger`):**
     Każda zmiana salda rejestruje typ operacji (`bonus`, `buy_in`, `cash_out`, `hand_result`, `refund`), kwotę delta oraz `balance_after`. Saldo nigdy nie jest modyfikowane bez powiązanego wpisu w `ledger`.
  5. **Mutex na stół (In-Memory Queue):** Każdy stół posiada asynchroniczną kolejkę poleceń (per-table command queue), gwarantującą, że akcje graczy i rozliczenia są przetwarzane sekwencyjnie.

### 3. Autoryzacja i tokeny (Cykl życia JWT & WebSocket)
- **Zagrożenia:**
  1. Wygaśnięcie access tokena (TTL 15 min) w trakcie 40-minutowej partii pokera, prowadzące do odrzucenia akcji gracza lub zerwania gniazda w kluczowym momencie (np. all-in na riverze).
  2. Przechowywanie tokenów w `localStorage` (podatność na kradzież via XSS).
  3. Nieautoryzowane połączenia do protokołu WebSocket.
- **Rozwiązanie architektoniczne:**
  1. **Dual-Token Pattern:**
     - `accessToken`: krótkożyjący (15 min), przechowywany **wyłącznie w pamięci operacyjnej aplikacji** (Pinia store `auth.accessToken`). Brak zapisu w `localStorage`!
     - `refreshToken`: długożyjący (7 dni), przechowywany w ciasteczku z flagami **`httpOnly; Secure; SameSite=Strict`** pod ścieżką `/api/auth`.
  2. **Handshake WebSocket z walidacją JWT:**
     - Podczas zdarzenia HTTP `upgrade` serwer parsuje token z query stringu `/ws?token=...` lub nagłówka.
     - Weryfikacja: `jwt.verify(token, env.JWT_ACCESS_SECRET)`.
     - W przypadku błędu: socket zostaje odrzucony statusem `401 Unauthorized` (`socket.destroy()`).
     - Po poprawnym handshaku do gniazda przypisywany jest identyfikator `ws.userId = decoded.sub`.
  3. **Obsługa wygasania tokena w 40-minutowej partii:**
     - **Socket jest stanowy:** Po ustanowieniu połączenia tożsamość gniazda jest już potwierdzona. Serwer nie weryfikuje podpisu JWT przy każdej akcji `game:action` – sprawdza jedynie, czy `ws.userId === seat.userId`.
     - **Silent Refresh w tle (po REST):** Frontend w `App.vue` / `services/api.js` uruchamia timer (co 10 minut) wywołujący `POST /api/auth/refresh` (z httpOnly cookie). Zwrócony nowy `accessToken` trafia do pamięci Pinia.
     - **Odporność na reconnect:** Jeżeli po 35 minutach gry nastąpi chwilowy lag sieci i socket zostanie zerwany, klient natychmiast łączy się ponownie, używając aktualnego (cicho odświeżonego) tokena z pamięci.

### 4. Walidacja wejścia w akcjach gry (Game Rule Validation & Anti-Exploit)
- **Zagrożenia:**
  Próby manipulacji stawkami przez DevTools: ujemny raise, bet większy niż stack gracza, nielegalny check przy istniejącym zakładzie, wysłanie akcji poza kolejnością lub na podstawie przestarzałego stanu.
- **Rozwiązanie architektoniczne:**
  1. **Walidacja schematu (Zod):**
     Każdy przychodzący pakiet `game:action` jest rygorystycznie sprawdzany:
     `z.object({ tableId: z.number().int().positive(), stateVersion: z.number().int().nonnegative(), type: z.enum(['fold','check','call','raise','all_in']), amount: z.number().int().positive().optional() })`.
     Odrzuca: ujemne liczby, liczby zmiennoprzecinkowe, NaN, nieznane typy akcji.
  2. **Optymistyczna ochrona współbieżności (`stateVersion`):**
     Klient musi przesłać `stateVersion`, na którym bazował swoją decyzję. Jeżeli `payload.stateVersion !== state.stateVersion`, serwer odrzuca akcję kodem `STALE_STATE` i odsyła aktualny `table:snapshot`. Chroni to gracza przed przypadkowym checkiem w sytuacji, gdy milisekundę wcześniej przeciwnik zagrał all-in.
  3. **Walidacja reguł Hold'ema w `engine/betting.js`:**
     - *Tura:* Sprawdzenie `state.turnSeat === seat.seatNo`.
     - *Check:* Dozwolony TYLKO gdy `seat.bet === state.currentBet`.
     - *Call:* Wymaga wyrównania do `state.currentBet`. Kwota: `min(currentBet - seat.bet, seat.stack)`.
     - *Raise:*
       - `amount` musi spełniać: `amount >= state.currentBet + state.minRaise` (chyba że jest to all-in za cały pozostały stack).
       - `amount <= seat.bet + seat.stack` (bezwzględna blokada przekroczenia własnego stacka).
       - Aktualizacja: `state.minRaise = Math.max(state.minRaise, amount - state.currentBet)`.
       - **Reset `hasActed`:** Każde podbicie zeruje flagę `hasActed = false` dla wszystkich pozostałych graczy, gwarantując im prawo do odpowiedzi.

---

## CZĘŚĆ II: INTEGRALNOŚĆ AKADEMICKA I OCHRONA PRZED ZARZUTEM PLAGIATU / AI

### 1. Model współpracy z AI (Architekt/Konsultant vs 100% Własna Implementacja)
Regulamin pracowni kategorycznie zabrania kopiowania kodu bez zrozumienia oraz fragmentów generowanych przez AI bez pełnego zrozumienia i obrony pod rygorem niezaliczenia przedmiotu.
- **Rola AI:** Dopuszczalna jako partner konsultacyjny do:
  - Projektowania architektury (diagramy encji, maszyna stanów, specyfikacja kontraktu API i protokołu WS).
  - Brainstormingu przypadków brzegowych (np. zasady kołówki A-2-3-4-5, side poty, reconnect).
  - Wsparcia w tworzeniu mocków testowych.
- **Zasada 100% samodzielności implementacyjnej:**
  - **Zakaz gotowych bibliotek pokerowych:** Kategoryczny zakaz instalowania bibliotek typu `poker-evaluator` z npm. Evaluator musi być autorskim kodem zespołu (`C(7,5)` kombinacji + system wag bitowych).
  - **Wewnętrzny filtr Peer Review ("Explain in 60s"):** Żaden commit ani PR nie trafia do gałęzi `main`/`develop` bez weryfikacji przez drugiego członka zespołu. Jeśli autor nie potrafi wyjaśnić działania kodu linijka po linijce, PR zostaje odrzucony.
  - **Dziennik `docs/PROBLEMY.md`:** Dokumentowanie realnych problemów i prób ich rozwiązania (np. błąd `SQLITE_BUSY`, problem z timeoutem WS) stanowi bezdyskusyjny dowód autentycznej pracy inżynierskiej.

---

### 2. Zestaw 10 pytań obronnych dla 5 członków zespołu (Etap 7)
W oparciu o skład z `labs/projects/pi-wo/README.md` oraz role A, B, C, D, E z `docs/04`:

#### OSOBA A: Maciej Cyuńczyk (Lider — Backend Core & WebSocket Architecture)
- **Pytanie 1:** *„Jak w protokole WebSocket zabezpieczyliście aplikację przed wyścigami (race conditions) i desynchronizacją, gdy dwóch graczy kliknie akcję w tej samej milisekundzie?”*
  - **Odpowiedź studenta:** Wytłumaczenie mechanizmu `stateVersion` i per-table async mutex (command queue). Każda akcja wysyłana z klienta zawiera wersję stanu, na której gracz widział stół. Serwer przetwarza akcje sekwencyjnie w kolejce. Jeśli wersja nie zgadza się z aktualną na serwerze, akcja jest odrzucana kodem `STALE_STATE`, a klient otrzymuje pełny `table:snapshot`.
  - **Na tablicy:** Rysunek osi czasu: Serwer (State v4) -> Gracz 1 wysyła Bet (v4) -> Serwer inkrementuje do v5 -> Gracz 2 wysyła Call bazowany na starej v4 -> Serwer odrzuca akcję Gracza 2 i wysyła resync snapshot.
- **Pytanie 2:** *„W jaki sposób uwierzytelniane jest połączenie WebSocket i co dzieje się, gdy gracz gra przez godzinę, a access token wygasa po 15 minutach?”*
  - **Odpowiedź studenta:** Handshake WS parsuje JWT z parametru zapytania przy `upgrade` i weryfikuje podpis. Po udanym połączeniu socket staje się stanowy i serwer wiąże z nim `userId`. W tle frontend cyklicznie (co 10 min) odświeża token access przez REST (`POST /api/auth/refresh`) przy użyciu httpOnly cookie. Gniazdo WS nie jest zrywane, a w razie reconnectu klient dysponuje świeżym tokenem.
  - **Na tablicy:** Schemat handshake'u HTTP 101 Switching Protocols z nagłówkiem/query tokenem oraz równoległa pętla REST Silent Refresh z ciasteczkiem Refresh Token.

#### OSOBA B: Miłosz Pawlaczyk (Silnik Gry / Game Engine & Evaluator)
- **Pytanie 3:** *„Jak działa wasz algorytm oceny układu 7 kart i jak matematycznie rozstrzygacie, który gracz wygrywa przy dwóch takich samych układach (np. dwie pary u obu graczy)?”*
  - **Odpowiedź studenta:** Wytłumaczenie kombinatoryki $C(7,5) = 21$. Algorytm generuje 21 podzbiorów 5-kartowych, ocenia każdy funkcją `evaluate5`, kodując układ w jedną 32-bitową liczbę całkowitą (`score = (kategoria << 20) | (r1 << 16) | (r2 << 12) | ...`). Porównanie układów to proste `scoreA > scoreB`. Kicker jest zapisany na niższych bitach, co automatycznie rozstrzyga wygraną bez konieczności pisania skomplikowanych drabinek warunkowych.
  - **Na tablicy:** Schemat wag bitowych liczby `score`: `[Kategoria (4 bity)][Karta główna 1 (4 bity)][Karta główna 2 (4 bity)][Kicker 1 (4 bity)][Kicker 2 (4 bity)]` oraz przykład dwóch par Asów i Króli z kickerem Dama vs Walet.
- **Pytanie 4:** *„W którym momencie dokładnie kończy się runda licytacji i dlaczego flaga `hasActed` jest kluczowa dla poprawnego działania Hold'ema?”*
  - **Odpowiedź studenta:** Runda kończy się, gdy wszyscy aktywni gracze zrównali najwyższy zakład (`bet === currentBet`) ORAZ każdy miał okazję wykonać ruch po ostatnim podbiciu (`hasActed === true`). Bez `hasActed`, na preflopie po samym sprawdzeniu blindów runda zamknęłaby się przed ruchem Big Blinda, co łamałoby fundamentalne reguły pokera.
  - **Na tablicy:** Maszyna stanów rundy licytacji z uwzględnieniem resetu `hasActed = false` przy każdym zdarzeniu `raise`/`bet`.

#### OSOBA C: Michał Małecki (Baza Danych, Transakcje & Ledger)
- **Pytanie 5:** *„Pokaż i wyjaśnij transakcję zamykającą rękę w SQLite. Co gwarantuje, że przy awarii serwera nikt nie straci żetonów ani nie powstanie ujemne saldo?”*
  - **Odpowiedź studenta:** Omówienie synchronicznej transakcji `db.transaction()`: w jednym bloku ACID następuje `INSERT INTO hands`, `INSERT INTO hand_players`, `UPDATE seats SET stack`, `INSERT INTO ledger` oraz aktualizacja `stats`. Zastosowanie constraintu `CHECK (stack >= 0)` i `CHECK (chips >= 0)` wyklucza ujemne salda. Awaria w trakcie operacji powoduje natychmiastowy `ROLLBACK`.
  - **Na tablicy:** Sekwencja transakcyjna: `BEGIN IMMEDIATE` -> Zapis wyniku ręki -> Aktualizacja stacków -> Zapis do ledgera -> `COMMIT` wraz ze strzałką błędu prowadzącą do `ROLLBACK`.
- **Pytanie 6:** *„Dlaczego zdecydowaliście się na tryb WAL w SQLite i jak zapobiegacie błędowi `SQLITE_BUSY` przy równoległych żądaniach z REST API?”*
  - **Odpowiedź studenta:** Domyślny tryb rollback journal blokuje całą bazę przy zapisie. WAL (Write-Ahead Logging) pozwala na współbieżne czytanie podczas trwania zapisu. Dodatkowo ustawienie `PRAGMA busy_timeout = 5000;` powoduje, że wątek czeka do 5 sekund na zwolnienie blokady zamiast od razu rzucać wyjątkiem `SQLITE_BUSY`. Całość działa w jednym procesie Node.js.
  - **Na tablicy:** Architektura SQLite: plik bazy `.db`, plik `.db-wal` oraz rola checkpointingu i timeoutu.

#### OSOBA D: Michał Pączkowski (Frontend Stołu, Canvas & Komponenty)
- **Pytanie 7:** *„Jak matematycznie obliczacie pozycje graczy wokół owalnego stołu w composable `useSeatLayout` i jak zapewniacie responsywność bez używania bibliotek typu Three.js?”*
  - **Odpowiedź studenta:** Wytłumaczenie równania parametrycznego elipsy: $x_i = 50\% + R_X \cdot \cos(\alpha_i)$, $y_i = 50\% + R_Y \cdot \sin(\alpha_i)$, gdzie kąt $\alpha_i = 90^\circ + (360^\circ / N) \cdot i$. Kąt $90^\circ$ pozycjonuje lokalnego gracza na samym dole ekranu. Wartości w procentach sprawiają, że stół skaluje się płynnie do dowolnego okna.
  - **Na tablicy:** Rysunek elipsy stołu w układzie współrzędnych, zaznaczenie promieni $R_X, R_Y$, kąta $\alpha$ oraz wyprowadzenie wzoru na współrzędne procentowe.
- **Pytanie 8:** *„W jaki sposób zaimplementowaliście trzy różne widoki stołu (Classic, Hero, Compact) i dlaczego nie wymagało to powielania logiki w JavaScript?”*
  - **Odpowiedź studenta:** Zastosowano CSS Grid z nazwanymi obszarami (`grid-template-areas`). Zmiana układu to jedynie przełączenie klasy na głównym kontenerze (np. `.table--hero`), co redefiniuje siatkę i rozmiar komponentów `PlayingCard`, podczas gdy cała logika komponentów i nasłuchiwania WS w `stores/game.js` pozostaje w 100% nienaruszona.
  - **Na tablicy:** Trzy szkice siatki CSS: Classic (oval/ring), Hero (duże karty gracza na dole, przeciwnicy zwinięci na górze) oraz Compact (widok kolumnowy na telefon).

#### OSOBA E: Miłosz Szymczuk (Frontend Aplikacji, Sieć & Web Worker Equity)
- **Pytanie 9:** *„Dlaczego kalkulator szans (equity) został wydzielony do Web Workera i jak wygląda wymiana danych między wątkiem głównym a workerem?”*
  - **Odpowiedź studenta:** Symulacja Monte Carlo wykonuje od 10 000 do 20 000 iteracji oceny rozdań. Na głównym wątku JavaScript zamroziłoby to pętlę zdarzeń (Event Loop), animacje CSS oraz licznik tury (20s). Komunikacja opiera się na asynchronicznym API `postMessage`: wysyłane są tylko karty gracza i stół, worker liczy equity w tle i odsyła wynik `{ win, tie, iterations }` bez blokowania UI.
  - **Na tablicy:** Diagram dwóch wątków: Main Thread (UI/Pinia/WS) <--- `postMessage` / `onmessage` ---> Worker Thread (Monte Carlo Loop).
- **Pytanie 10:** *„Jak zaprojektowaliście odporność warstwy sieciowej na zerwanie połączenia WebSocket (reconnect) oraz jak interfejs komunikuje stany przejściowe użytkownikowi?”*
  - **Odpowiedź studenta:** Moduł `services/socket.js` implementuje wykładniczy backoff (1s, 2s, 4s... max 30s) z losowym jitterem oraz heartbeat ping/pong (co 15s). Po udanym reconnect klient automatycznie wysyła `table:subscribe`, odbierając świeży stan. W UI status reprezentowany jest 4 stanami: zielony badge (połączono), żółty spinner (łączenie/resync), czerwony toast (błąd krytyczny) oraz transparentny resync bez wyrzucania gracza ze stołu.
  - **Na tablicy:** Maszyna stanów połączenia klienta: `CONNECTED` -> `DISCONNECTED` -> `BACKOFF_DELAY` -> `RECONNECTING` -> `SUBSCRIBING` -> `SYNCED`.
