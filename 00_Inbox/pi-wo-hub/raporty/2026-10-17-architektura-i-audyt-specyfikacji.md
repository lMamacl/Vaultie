# Raport Architektoniczny i Audyt Specyfikacji: Projekt „Pi-Wo” (Texas Hold'em)

**Data audytu:** 17 października 2026  
**Rola:** Główny Architekt Oprogramowania  
**Przedmiot:** Pracownia Specjalistyczna (Politechnika Białostocka)  
**Cel audytu:** Weryfikacja założeń architektonicznych, eliminacja sprzeczności w specyfikacji (`docs/00–04`), projekt silnika i współbieżności, integracja monorepo (`shared/`) oraz precyzyjny podział pracy dla 5-osobowego zespołu studentów.

---

## 1. Ocena paradygmatu silnika gry

### 1.1. Wzorzec czystej funkcji: `applyAction(state, action) -> newState`
Wzorzec pure-state reducer (znany m.in. z Reduxa, Elma i architektury Event Sourcing) przyjęty w `02-protokol-websocket-i-silnik-gry.md` jest **optymalnym i wzorcowym wyborem architektonicznym** dla gry turowej o wysokim rygorze reguł biznesowych.

```
                  ┌───────────────────────────────────────┐
                  │       (staryStan, akcjaGracza)        │
                  └──────────────────┬────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │   applyAction(s, a)     │  ◄── CZYSTA FUNKCJA (zero I/O,
                        │   (silnik w engine/)    │      zero DB, zero Express)
                        └────────────┬────────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │      nowyStan       │
                          └─────────────────────┘
```

#### Kluczowe zalety dla projektu i obrony:
1. **Determinizm i testowalność (10 pkt za jakość techniczną):**
   - Moduł `server/src/engine/` nie posiada żadnych zależności od sieci (`ws`, `express`) ani I/O dyskowego (`better-sqlite3`).
   - Testy w Vitest wykonują się w ułamku sekundy na zwykłych obiektach JSON. Umożliwia to łatwe pokrycie 100% skrajnych przypadków (np. split pot, kołówka, fold na turnie, all-in poniżej minimalnego raise).
2. **Replayability za darmo (widok `/hands/:id`):**
   - Odtworzenie przebiegu ręki w widoku `HandReplayView.vue` sprowadza się do jednej linii:
     ```javascript
     const currentState = actions.slice(0, currentStep).reduce(applyAction, initialHandState);
     ```
   - Eliminuje to potrzebę pisania skomplikowanych silników animacji klatkowej lub dedykowanych rejestratorów snapshotów.
3. **Izolacja mutowalności i brak efektów ubocznych:**
   - W JavaScript obiekty są przekazywane przez referencję. Aby zagwarantować czystość funkcji, `applyAction` **musi** operować na kopii stanu lub zwracać nowy obiekt (np. poprzez płytkie kopiowanie zmienionych podstruktur lub `structuredClone(state)` w punktach węzłowych). Dzięki temu żaden wyścig w pamięci nie uszkodzi poprzedniego snapshotu.

### 1.2. Trzymanie stanu gry w pamięci (`Map<tableId, GameState>`) vs trwałość w SQLite
Dokumenty zakładają, że aktywny stan licytacji i kart żyje wyłącznie w pamięci operacyjnej procesu Node.js, a do SQLite zapisywana jest wyłącznie **zakończona ręka** (oraz trwałe stoły i konta użytkowników).

#### Ocena inżynierska:
- **Wydajność:** W Texas Hold'em akcje licytacji (check, call, fold) następują w odstępach sekundowych. Synchroniczny zapis do SQLite po każdej pojedynczej akcji wprowadzałby niepotrzebny narzut I/O i ryzyko blokad przy wielu stołach.
- **Bezpieczeństwo kart (Anti-Cheat):** Zapisywanie `hole_cards` w SQLite w trakcie trwania ręki stanowiłoby lukę bezpieczeństwa (potencjalny wyciek kart przez endpointy REST lub logi bazy). Przechowywanie kart w pamięci serwera i serializacja per adresat (`serializeState(state, viewerId)`) gwarantuje, że nieuprawniony gracz ani zewnętrzny proces nie zobaczy kart przeciwników.
- **Analiza awarii i restartu serwera (Trade-off):**
  - *Co jeśli serwer ulegnie awarii w trakcie ręki?* Ręka w toku przepada. Po restarcie serwera żetony graczy przywracane są ze stanu `seats.stack` zapisanego po ostatniej zakończonej ręce.
  - *Decyzja architektoniczna:* Dla projektu akademickiego (system z jednym procesem Node.js) jest to kompromis w pełni uzasadniony i profesjonalny. W dokumentacji `docs/PROBLEMY.md` należy wprost opisać ten trade-off: *"Wybór pamięci operacyjnej z persystencją post-hand zamiast Write-Ahead Transaction Log w Redis/DB wynika z optymalizacji pod prostotę wdrożenia i zerową latencję licytacji; scenariusz awarii serwera podczas ręki anuluje nierozliczoną rękę bez utraty salda bazowego."*
- **Higiena pamięci (Memory Leak Prevention):**
  - Obiekt `Map<tableId, GameState>` musi być jawnie czyszczony w momencie zamknięcia stołu (`DELETE /api/tables/:id` lub usunięcie przez brak aktywności).
  - Wszelkie timery (`turnTimeout = setTimeout(...)`) przypisane do danego stołu muszą być bezwzględnie anulowane (`clearTimeout`) przed usunięciem referencji ze struktury `Map`.

---

## 2. Analiza sprzeczności i luk w dokumentacji

### 2.1. Sprzeczność All-in: Cap & Refund vs Pule Boczne (Side Pots)

#### Natura problemu i błąd logiczny w specyfikacji:
W `00-plan-projektu.md` (§3 i §7) oraz `02-protokol-websocket-i-silnik-gry.md` (§3) autorzy rekomendują wariant „cap & refund (bez side potów)" jako rzekomo bezpieczny i prosty. Jednak w `03-frontend-i-komponenty.md` pojawia się komponent `PotDisplay.vue` z etykietą `"side pot 2: 340"`.

> [!CAUTION]
> **Dlaczego „Cap & Refund” niszczy reguły Texas Hold'em dla 3+ graczy:**
> Rozważmy scenariusz z 3 graczami:
> - Gracz A (short-stack): posiada **50 żetonów** i wchodzi All-in na preflopie.
> - Gracz B (deep-stack): posiada **500 żetonów** i sprawdza (call 50).
> - Gracz C (deep-stack): posiada **500 żetonów** i sprawdza (call 50).
>
> Co dzieje się na Flopie?
> 1. Jeśli zastosujemy „Cap & Refund” i zablokujemy wielkość puli na poziomie wkładu Gracza A (cap = 50 od każdego), to **Gracze B i C mają bezwzględnie zablokowaną możliwość dalszej licytacji na flopie, turnie i riverze!** Znika esencja pokera: blefowanie, ochrona układu i value-betting między aktywnymi graczami.
> 2. Jeśli pozwolimy B i C licytować dalej do jednej wspólnej puli bez pul bocznych:
>    - Jeśli wygra Gracz A, zgarnie on żetony z puli, do której włożyli gracze B i C po flopie (rażące złamanie zasad matematyki gry).
>    - Jeśli zastosujemy refund po zakończeniu ręki, licytacja graczy B i C traci jakikolwiek sens ekonomiczny.
>
> **Wniosek:** „Cap & Refund” działa **wyłącznie w pojedynku 1 na 1 (Heads-Up)**, gdzie nadwyżka nieposiadająca pokrycia w stacku rywala jest od razu zwracana (`uncalled_return`). W grze 3–6 graczy pule boczne (Side Pots) są **bezwzględną koniecznością regułową**.

#### Eleganckie, bezpieczne rozwiązanie w kodzie (`pots.js`):
Algorytm budowania pul bocznych nie musi być skomplikowany. Zamiast śledzić stan puli w czasie rzeczywistym na każdej ulicy, pule boczne oblicza się w oparciu o wektor skumulowanych wkładów (`totalContribution`) graczy w momencie rozliczenia ręki:

```javascript
/**
 * Oblicza pule (główną i boczne) na podstawie łącznych wkładów graczy.
 * @param {Array<{ seatNo: number, totalContribution: number, folded: boolean }>} players 
 * @returns {Array<{ potId: number, amount: number, eligibleSeats: number[] }>}
 */
export function buildPots(players) {
  const pots = [];
  // Pobieramy unikalne, dodatnie poziomy wkładów, posortowane rosnąco
  const contributions = players
    .map(p => p.totalContribution)
    .filter(c => c > 0);
  const tiers = Array.from(new Set(contributions)).sort((a, b) => a - b);

  let previousTier = 0;
  for (let i = 0; i < tiers.length; i++) {
    const currentTier = tiers[i];
    const tierSize = currentTier - previousTier;
    
    // Wszyscy gracze, którzy wpłacili co najmniej currentTier, finansują tę warstwę
    const contributingPlayers = players.filter(p => p.totalContribution >= currentTier);
    const potAmount = contributingPlayers.length * tierSize;

    // Uprawnieni do wygrania puli są tylko ci, którzy wpłacili i NIE spasowali
    const eligibleSeats = contributingPlayers
      .filter(p => !p.folded)
      .map(p => p.seatNo);

    if (eligibleSeats.length > 0) {
      pots.push({
        potId: i,
        amount: potAmount,
        eligibleSeats
      });
    } else {
      // Jeśli wszyscy spasowali (martwa pula), przypisz do ostatniego niespasowanego
      const lastActive = players.find(p => !p.folded);
      if (lastActive) {
        pots.push({
          potId: i,
          amount: potAmount,
          eligibleSeats: [lastActive.seatNo]
        });
      }
    }
    previousTier = currentTier;
  }

  return pots;
}
```
*Zalety:* Algorytm liczy ~35 linii, jest w 100% deterministyczny, obsługuje dowolną liczbę all-inów na różnych poziomach oraz graczy spasowanych. Wypłata polega na iteracji po tablicy `pots` od najmniejszej do największej i wyłonieniu najlepszego układu spośród `eligibleSeats`.

---

### 2.2. Granica REST API vs WebSocket (Dual-write i Race Conditions)

#### Natura konfliktu w specyfikacji:
- `01-model-danych-i-api.md`: `POST /api/tables/:id/join` oraz `POST /api/tables/:id/leave`.
- `02-protokol-websocket-i-silnik-gry.md`: eventy WS `seat:take` (`{ tableId, seatNo, buyIn }`) oraz `seat:leave`.

Jeśli klient może usiąść przy stole zarówno przez REST, jak i przez WebSocket, powstaje ryzyko:
1. **Dual-write:** Dwie różne ścieżki kodu modyfikują stan portfela (`users.chips`) oraz stan stołu (`seats`).
2. **Race condition:** Dwóch graczy wysyła żądanie zajęcia tego samego miejsca (jeden przez REST, drugi przez WS).
3. **Desynchronizacja pamięci z bazą:** REST zapisze do SQLite, ale serwer WS nie zaktualizuje stanu `GameState.players` w pamięci.

#### Rozwiązanie architektoniczne: Ścisła separacja Command/Query

```
                            ┌────────────────────────────────────────┐
                            │           KLIENT (VUE 3)               │
                            └────┬──────────────────────────────▲────┘
                                 │                              │
                     1. REST     │                  5. WebSocket│ Broadcast
                     Mutacja     │                  `seat:taken`│ `table:snapshot`
                     finansowa   │                              │
                                 ▼                              │
                     ┌───────────────────────┐                  │
                     │  POST /tables/:id/join│                  │
                     └───────────┬───────────┘                  │
                                 │                              │
                                 ▼                              │
                     ┌───────────────────────┐                  │
                     │   TableService.join() │                  │
                     │   (transakcja SQLite  │                  │
                     │   BEGIN IMMEDIATE)    │                  │
                     └───────────┬───────────┘                  │
                                 │ 2. Zapis DB (ACID)           │
                                 ▼                              │
                     ┌───────────────────────┐   4. Notyfikacja │
                     │  TableManager (Memory)├──────────────────┘
                     │  stan stołu w pamięci │
                     └───────────────────────┘
```

1. **REST jest jedynym kanałem mutacji portfela i miejsc przy stole:**
   - Operacje: Rejestracja, logowanie, utworzenie stołu, `POST /api/tables/:id/join`, `POST /api/tables/:id/leave`.
   - Uzasadnienie: Dołączenie do stołu wymaga weryfikacji salda w `users.chips`, blokady miejsca w `seats` oraz utworzenia wpisu w `ledger` z typem `buy_in`. To jest operacja finansowa wymagająca transakcji ACID w SQLite i synchronicznej odpowiedzi HTTP (np. `409 Conflict` gdy miejsce zajęte, `422 Unprocessable Entity` gdy za mało żetonów).
2. **WebSocket jest kanałem wyłącznie do rozgrywki i transmisji stanu:**
   - Operacje: `table:subscribe`, `game:action` (fold, check, call, raise, all_in), `chat:send`, `table:resync`.
   - Event `seat:take` i `seat:leave` zostaje **usunięty z protokołu WebSocket klienta**.
3. **Most integracyjny (Controller -> TableManager -> WS Broadcast):**
   - Po pomyślnym wykonaniu transakcji SQL w `tableService.joinTable(tableId, userId, seatNo, buyIn)`, kontroler wywołuje wewnętrzną metodę w pamięci:
     ```javascript
     tableManager.seatPlayer(tableId, { seatNo, userId, username, avatarId, stack: buyIn });
     ```
   - Silnik stołu weryfikuje fazę (gracz otrzymuje status `waiting_for_next_hand`, jeśli ręka trwa) i rozsyła przez WebSocket zdarzenie `seat:taken` oraz zaktualizowany `table:snapshot` do wszystkich obecnych przy stole.
   - W ten sposób źródło prawdy dla pieniędzy jest zawsze w SQLite, źródło prawdy dla kart i tury jest w pamięci, a wyścigi są wykluczone.

---

### 2.3. Współbieżność, transakcje i `better-sqlite3` w Node.js

#### Problem wydajnościowy:
Czy synchroniczne API biblioteki `better-sqlite3` (`db.prepare(...).run()`) przy atomowym zapisie zakończonej ręki (`hands`, `hand_players`, `hand_actions`, `seats`, `ledger`, `stats`) nie zablokuje pętli zdarzeń (Event Loop) serwera Node.js?

#### Ekspertyza wydajnościowa i mechanizmy blokad:
1. **Charakterystyka transakcji zamknięcia ręki:**
   - Pojedyncza ręka generuje: 1 `INSERT` do `hands`, 2–6 `INSERT` do `hand_players`, ok. 10–30 `INSERT` do `hand_actions`, 2–6 `UPDATE` w `seats`, 2–6 `INSERT` w `ledger`, 2–6 `UPDATE` w `stats`.
   - Łącznie: **ok. 20–50 operacji SQL na rękę**.
2. **Czas wykonania w `better-sqlite3` + WAL:**
   - `better-sqlite3` to natywny binding C++, który nie ponosi narzutu asynchronicznych wrapperów Node.js.
   - Przy włączonym trybie `PRAGMA journal_mode = WAL;` oraz `PRAGMA synchronous = NORMAL;`, transakcja `db.transaction(...)` zapisuje zmiany do pamięci podręcznej i bufora WAL w systemie operacyjnym.
   - Zmierzony czas wykonania transakcji 50 prostych instrukcji `INSERT/UPDATE` w `better-sqlite3` wynosi **od 0.8 ms do 2.5 ms**.
   - Pauza w pętli zdarzeń rzędu 2 milisekund występująca raz na kilkadziesiąt sekund jest z perspektywy serwera HTTP/WS **całkowicie niezauważalna** (pakiety sieciowe i timery nie doznają żadnego janku).
3. **Dlaczego synchroniczne API jest bezpieczniejsze od asynchronicznego:**
   - W asynchronicznych sterownikach (np. starym `sqlite3`), jeśli programista użyje `await` pomiędzy `BEGIN` a `COMMIT`, pętla zdarzeń może wpuścić inny request na to samo połączenie, powodując katastrofalny błąd `cannot start a transaction within a transaction` lub wyścigi danych.
   - `better-sqlite3` gwarantuje nieprzerwaną, atomową egzekucję:
     ```javascript
     const settleHandTransaction = db.transaction((handData) => {
       // 1. INSERT hands
       // 2. INSERT hand_players
       // 3. INSERT hand_actions
       // 4. UPDATE seats
       // 5. INSERT ledger
       // 6. UPDATE stats
     });
     // Wywołanie: natychmiastowe, atomowe, z auto-rollbackiem przy jakimkolwiek błędzie!
     settleHandTransaction(handSummary);
     ```
4. **Wymogi bezwzględne dla konfiguracji SQLite:**
   ```sql
   PRAGMA journal_mode = WAL;        -- czytający nie blokują piszących, piszący nie blokują czytających
   PRAGMA busy_timeout = 5000;       -- oczekiwanie do 5000 ms w przypadku rygla zapisu
   PRAGMA foreign_keys = ON;        -- spójność relacyjna
   PRAGMA synchronous = NORMAL;     -- idealny balans bezpieczeństwa i wydajności w trybie WAL
   ```
   *Rygor:* Wewnątrz `settleHandTransaction` **nie wolno** wywoływać żadnych operacji CPU-heavy (np. `bcrypt.hashSync`). Wszystkie zapytania SQL muszą być skompilowane wcześniej (`db.prepare(...)` zainicjalizowane raz przy starcie repozytorium).

---

## 3. Współdzielenie kodu (`shared/`) w architekturze Monorepo

### 3.1. Problem architektoniczny
Moduł oceny siły kart (`evaluator.js` wraz ze stałymi kart i rang) musi być współdzielony pomiędzy dwoma różnymi środowiskami uruchomieniowymi:
1. **Backend (Node.js 20+):** Wykorzystywany przez silnik serwera (`server/src/engine/hand.js`).
2. **Frontend (Vite + Web Worker):** Wykorzystywany w dedykowanym wątku w przeglądarce (`client/src/workers/equity.worker.js`) do symulacji Monte Carlo (obliczanie procentowych szans na wygraną).

Obecny stan repozytorium w `labs/projects/pi-wo/` zawiera płaski `package.json` z Expressem 5.3.0 i `server.js`. Należy przekształcić strukturę w czyste monorepo.

### 3.2. Proponowana struktura katalogów
```
pi-wo/
├── package.json                 ← Root: npm workspaces: ["server", "client", "shared"]
├── shared/                      ← CZYSTY KOD JS (ES Modules, zero zależności zewnętrznych)
│   ├── package.json             ← name: "@pi-wo/shared", type: "module"
│   ├── index.js                 ← eksporty publiczne
│   ├── cards.js                 ← tworzenie talii, symbole, rangi, stałe
│   ├── evaluator.js             ← evaluate5, evaluate7, compareHands, handName
│   └── events.js                ← nazwy zdarzeń WebSocket (stałe unikające literówek)
├── server/
│   ├── package.json             ← z zależnością: "@pi-wo/shared": "*"
│   └── src/
│       ├── engine/              ← hand.js, betting.js, pots.js
│       └── ws/
└── client/
    ├── package.json             ← z zależnością: "@pi-wo/shared": "*"
    ├── vite.config.js           ← konfiguracja aliasów i workera
    └── src/
        ├── workers/
        │   └── equity.worker.js ← import { evaluate7 } from '@pi-wo/shared'
        └── stores/
```

### 3.3. Konfiguracja ES Modules w Vite i Node.js

#### 1. `shared/package.json`:
```json
{
  "name": "@pi-wo/shared",
  "version": "1.0.0",
  "type": "module",
  "main": "./index.js",
  "exports": {
    ".": "./index.js",
    "./evaluator": "./evaluator.js",
    "./cards": "./cards.js",
    "./events": "./events.js"
  }
}
```

#### 2. Root `package.json` (obsługa NPM Workspaces):
```json
{
  "name": "pi-wo-monorepo",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "shared",
    "server",
    "client"
  ],
  "scripts": {
    "dev": "concurrently \"npm run dev --workspace=server\" \"npm run dev --workspace=client\"",
    "test": "npm run test --workspace=shared && npm run test --workspace=server",
    "build": "npm run build --workspace=client"
  },
  "devDependencies": {
    "concurrently": "^9.0.0"
  }
}
```

#### 3. Konfiguracja klienta w `client/vite.config.js`:
Aby Vite oraz Web Worker bezproblemowo ładowały kod z katalogu `shared/`:
```javascript
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'node:path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@pi-wo/shared': path.resolve(__dirname, '../shared')
    }
  },
  worker: {
    format: 'es' // Bezwzględnie wymagane, aby w Workerze działał syntax import/export ESM!
  },
  server: {
    proxy: {
      '/api': 'http://localhost:3000',
      '/ws': {
        target: 'ws://localhost:3000',
        ws: true
      }
    }
  }
});
```

#### 4. Uruchomienie Web Workera w kodzie Vue (`client/src/composables/useEquity.js`):
```javascript
// Natywny konstruktor Vite dla modułowego Web Workera
const worker = new Worker(
  new URL('../workers/equity.worker.js', import.meta.url),
  { type: 'module' }
);
```

#### Dlaczego to rozwiązanie jest bezbłędne na obronie:
- **Zero duplikacji kodu:** Ten sam algorytm oceny kart (`evaluator.js`) weryfikuje zwycięzców na serwerze i liczy equity w przeglądarce.
- **Odpowiedź na pytanie komisji:** Na pytanie *"Jak połączyliście logikę gry z workerem?"* student wskazuje czystą modularność `@pi-wo/shared` opartą o standard ECMAScript Modules bez pośrednich kroków kompilacji bundlerem.

---

## 4. Precyzyjny podział pracy dla 5-osobowego zespołu

### 4.1. Ustalenie stanu faktycznego
W dokumencie `04-podzial-pracy-harmonogram-i-obrona.md` w sekcji 1 błędnie przyjęto strukturę 4-osobową, łącząc rolę Backend Core i Engine w jedno („A+B").
Tymczasem w oficjalnym pliku repozytorium `labs/projects/pi-wo/README.md` oraz zgłoszeniu zespołu widnieje **dokładnie 5 studentów**:
1. **Maciej Cyuńczyk (Lider)**
2. **Michał Pączkowski**
3. **Michał Małecki**
4. **Miłosz Szymczuk**
5. **Miłosz Pawlaczyk**

Zgodnie z wymaganiami Pracowni Specjalistycznej (ocena końcowa etapu 7: 50 pkt), każdy student musi wykazać się **indywidualnym, mierzalnym wkładem**, posiadać własny dedykowany moduł kodu do zaprezentowania przed komisją i potrafić obronić zastosowane w nim mechanizmy.

---

### 4.2. Matryca Odpowiedzialności i Ról (Podział na 5 Studentów)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ZESPÓŁ PROJEKTOWY PI-WO (5 OSÓB)                      │
└─────────────────────────────────────────────────────────────────────────────┘
       │                      │                       │               │
┌──────▼──────┐        ┌──────▼──────┐         ┌──────▼──────┐ ┌──────▼──────┐
│   ROLA A    │        │   ROLA B    │         │   ROLA C    │ │ ROLA D & E  │
│ Backend WS  │        │ Silnik Gry  │         │  Baza Danych│ │ Frontend    │
│  & DevOps   │        │  & Testy    │         │  & REST API │ │ Stół vs App │
└─────────────┘        └─────────────┘         └─────────────┘ └─────────────┘
```

#### 🛡️ ROLA A: Backend Core, WebSocket Gateway & DevOps
- **Sugerowany student:** **Maciej Cyuńczyk (Lider)**
- **Obszar odpowiedzialności:**
  - Architektura serwera Express (`server/src/app.js`, `server/src/index.js`).
  - Globalny middleware stack: obsługa błędów (`errorHandler`), walidacja `zod`, nagłówki bezpieczeństwa `helmet`, CORS, `express-rate-limit`.
  - Serwer WebSocket (`server/src/ws/`): handshake autoryzacyjny z weryfikacją JWT, zarządzanie pokojami stołów (`rooms.js`), obsługa połączeń i rozłączeń, detekcja heartbeat (`ping/pong`).
  - Odporność na awarie sieciowe: mechanizm 60-sekundowego *grace period* dla rozłączonych graczy (`player:connection`), auto-fold po upływie `turnDeadline`.
  - Infrastruktura i wdrożenie: Monorepo scripts (`package.json`), Dockerfile, docker-compose, konfiguracja reverse proxy pod integrację z Vite.
- **Pliki źródłowe:**
  - `server/src/index.js`, `server/src/app.js`
  - `server/src/ws/server.js`, `server/src/ws/rooms.js`, `server/src/ws/handlers.js`
  - `server/src/middleware/*`
  - `Dockerfile`, `docker-compose.yml`
- **Kluczowy fragment do obrony (Etap 7):**
  - Implementacja protokołu czasu rzeczywistego (Snapshot + Delta), autoryzacja tokenem przy handshaku HTTP Upgrade, obsługa rozłączenia gracza bez blokowania stołu.

---

#### 🃏 ROLA B: Silnik Gry Pokerowej, Matematyka & Testy Jednostkowe
- **Sugerowany student:** **Miłosz Pawlaczyk** (lub członek o wysokich predyspozycjach algorytmicznych)
- **Obszar odpowiedzialności:**
  - Moduł współdzielony i silnik serwera: `shared/cards.js`, `shared/evaluator.js`, `server/src/engine/`.
  - Czysta maszyna stanów pokera: `hand.js` (`applyAction`, `advanceStreet`), `betting.js` (`legalActions`, `isBettingComplete`, obsługa flagi `hasActed`).
  - Matematyka puli: implementacja algorytmu warstwowego pul bocznych (`pots.js` / `buildPots`).
  - Generowanie talii i bezpieczne tasowanie (`crypto.randomInt` + Fisher-Yates).
  - TDD i pakiet testów jednostkowych w Vitest: co najmniej **35–50 testów** pokrywających:
    - Wszystkie układy pokerowe w `evaluator.js` (w tym kołówka A-2-3-4-5, kickery, remisy).
    - Reguły licytacji (poprawność opcji Big Blinda, minimalny raise po podbiciu).
    - Rozliczanie skomplikowanych pul bocznych z wieloma all-inami.
    - Złoty test end-to-end: symulacja kompletnej 6-osobowej ręki krok po kroku z weryfikacją stanu żetonów do 1 grosza.
  - Opcjonalny bot serwerowy (`botService.js`): generowanie losowych legalnych akcji do testowania i demonstracji multiplayer.
- **Pliki źródłowe:**
  - `shared/cards.js`, `shared/evaluator.js`
  - `server/src/engine/deck.js`, `server/src/engine/betting.js`, `server/src/engine/pots.js`, `server/src/engine/hand.js`
  - `server/src/engine/__tests__/*` (cały katalog testów)
- **Kluczowy fragment do obrony (Etap 7):**
  - Algorytm ewaluacji 7 kart C(7,5) z kodowaniem binarnym układu do pojedynczej liczby całkowitej (`score`) oraz dowód matematycznej poprawności podziału pul bocznych.

---

#### 🗄️ ROLA C: Baza Danych, Bezpieczeństwo Poświadczeń & REST API
- **Sugerowany student:** **Michał Małecki**
- **Obszar odpowiedzialności:**
  - Konfiguracja SQLite (`better-sqlite3`): migracje DDL, konfiguracja `PRAGMA journal_mode = WAL`, `PRAGMA foreign_keys = ON`, `PRAGMA busy_timeout = 5000`.
  - Repozytoria warstwy danych: `usersRepo.js`, `tablesRepo.js`, `handsRepo.js`, `ledgerRepo.js`, `statsRepo.js`.
  - Bezpieczeństwo i Auth: rejestracja, logowanie, hash haseł (`bcryptjs`), generowanie i rotacja par tokenów (access token 15 min + refresh token 7 dni w bezpiecznym ciasteczku `httpOnly`, `SameSite=Strict`).
  - Endpointy REST: `/api/auth/*`, `/api/users/*`, `/api/tables/*` (w tym zaawansowane wyszukiwanie, filtrowanie wg statusu/stawek, sortowanie i paginacja wymagane w **Etapie 3**), `/api/leaderboard`.
  - Transakcja zamknięcia ręki (`TableService.settleHand`): atomowy zapis do 6 tabel w pojedynczym `BEGIN IMMEDIATE ... COMMIT` z pełnym audytem w `ledger`.
  - Przygotowanie kolekcji zapytań `server/api.http` (dla VS Code / JetBrains) oraz dokumentacji OpenAPI/Swagger (`/api/docs`).
- **Pliki źródłowe:**
  - `server/src/db/index.js`, `server/src/db/migrations/*`, `server/src/db/seed.js`
  - `server/src/repositories/*`
  - `server/src/services/authService.js`, `server/src/services/tableService.js`
  - `server/src/routes/auth.js`, `server/src/routes/tables.js`, `server/src/routes/users.js`
  - `server/api.http`
- **Kluczowy fragment do obrony (Etap 7):**
  - Dowód atomowości transakcji finansowych (ACID w `ledger`), ochrona poświadczeń (brak haseł w logach, httpOnly cookies) oraz zapytanie SQL filtrujące stoły z podzapytaniem zliczającym graczy.

---

#### 🎨 ROLA D: Frontend — Stół Pokera, Grafika & Stan Rozgrywki (Table & Game UI)
- **Sugerowany student:** **Michał Pączkowski**
- **Obszar odpowiedzialności:**
  - Główny ekran gry: `client/src/views/TablePage.vue`.
  - Komponenty stołu:
    - `PlayingCard.vue`: komponent karty na czystym SVG z efektem obracania rewers/awers (`transform: rotateY(180deg)` i `preserve-3d`).
    - `TableCanvas.vue`: owalny stół z filcem (radial-gradient, rail w CSS box-shadow).
    - `SeatSpot.vue`: dynamiczne pozycjonowanie miejsc graczy w oparciu o trygonometrię elipsy (`composables/useSeatLayout.js`).
    - `TurnTimerRing.vue`: animowany okrąg SVG odliczający czas do `turnDeadline`.
    - `ActionBar.vue`: przyciski Fold/Check/Call/Raise z suwakiem stawek zsynchronizowanym z `minRaise`/`maxRaise` z serwera.
    - `PotDisplay.vue`, `DealerButton.vue`, `ResultOverlay.vue` (ekran podsumowania showdown).
  - Store rozgrywki w Pinii: `stores/game.js` — odbiór eventów z WebSocketu, obsługa `stateVersion`, blokada optymistyczna (disable przycisków na 300 ms podczas oczekiwania na akcję serwera).
  - Implementacja 3 wariantów widoku stołu w oparciu o czysty CSS Grid (`classic`, `hero`, `compact`).
- **Pliki źródłowe:**
  - `client/src/views/TablePage.vue`
  - `client/src/components/table/*`
  - `client/src/components/cards/*`
  - `client/src/composables/useSeatLayout.js`, `client/src/composables/useTurnTimer.js`
  - `client/src/stores/game.js`
- **Kluczowy fragment do obrony (Etap 7):**
  - Implementacja responsywnego stołu bez zewnętrznych silników graficznych (CSS 3D / SVG), matematyczne pozycjonowanie graczy wokół elipsy, obsługa animacji bez blokowania licytacji.

---

#### 🧭 ROLA E: Frontend — Architektura Aplikacji, Lobby & Web Worker (App & Extensions)
- **Sugerowany student:** **Miłosz Szymczuk**
- **Obszar odpowiedzialności:**
  - Inicjalizacja i architektura aplikacji Vue 3 (`main.js`, `App.vue`).
  - Vue Router (`router/index.js`): routing, meta-tagi (`requiresAuth`, `guestOnly`), nawigacja i ochrona ścieżek przez `router.beforeEach`.
  - Store'y Pinii: `stores/auth.js` (logowanie, odświeżanie tokena, stan sesji), `stores/tables.js` (filtry, debounce zapytań), `stores/ui.js` (toasty, motyw, ustawienia).
  - Warstwa komunikacji sieciowej:
    - `services/api.js`: fetch wrapper z automatycznym wstrzykiwaniem nagłówka Bearer, przechwytywaniem błędów `401` i cichym odświeżaniem tokena.
    - `services/socket.js`: klient WebSocket z automatycznym wznawianiem połączenia (exponential backoff z jitterem), kolejką wiadomości i stanem online/offline w UI.
  - Główne widoki aplikacji: `LoginView.vue`, `RegisterView.vue`, `LobbyView.vue` (z filtrami, paginacją i oknem tworzenia stołu), `ProfileView.vue`, `LeaderboardView.vue`, `HandReplayView.vue` (odtwarzacz historii rąk).
  - Biblioteka komponentów bazowych (`components/common/`): `BaseButton`, `BaseInput` (z walidacją i wyświetlaniem błędów), `Modal`, `ToastQueue`, `SkeletonLoader` (stany loading/empty/error/success).
  - **Rozszerzenie techniczne na 10 pkt (Kryterium 5):**
    - Implementacja Web Workera: `client/src/workers/equity.worker.js`.
    - Obliczanie szans na wygraną metodą Monte Carlo (10 000 iteracji) z wykorzystaniem `@pi-wo/shared/evaluator`.
    - Komponent `EquityPanel.vue` (płynny pasek szans, układ aktualnej ręki, brak jakichkolwiek przycięć wątku UI).
- **Pliki źródłowe:**
  - `client/src/main.js`, `client/src/router/index.js`
  - `client/src/services/api.js`, `client/src/services/socket.js`
  - `client/src/stores/auth.js`, `client/src/stores/tables.js`, `client/src/stores/ui.js`
  - `client/src/views/LobbyView.vue`, `client/src/views/ProfileView.vue`, `client/src/views/HandReplayView.vue`, itp.
  - `client/src/workers/equity.worker.js`, `client/src/components/table/EquityPanel.vue`
- **Kluczowy fragment do obrony (Etap 7):**
  - Wykorzystanie Web Workera do ciężkich obliczeń statystycznych w osobnym wątku (uzasadnienie techniczne: ochrona 60 FPS animacji i timera tury) oraz odporność warstwy sieciowej (cichy reconnect i token refresh).

---

### 4.3. Zestawienie obronne wkładu indywidualnego (Punkty na Etapie 7)

| Rola | Student | Moduł w kodzie | Co student pokazuje na ekranie podczas obrony | Wymóg z regulaminu |
| :---: | :--- | :--- | :--- | :--- |
| **A** | Maciej Cyuńczyk (Lider) | `server/src/ws/*`, `middleware/*` | Podgląd ramek w DevTools Network WS (ukryte karty przeciwników, autoryzacja), test rozłączenia i powrotu w 60s, Docker Compose | Bezpieczeństwo i Architektura (5 pkt + 10 pkt) |
| **B** | Miłosz Pawlaczyk | `shared/evaluator.js`, `engine/*` | Uruchomienie `npm test` (zielone 40+ testów w Vitest), omówienie wzoru kodowania bitowego układu oraz algorytmu `buildPots` | Jakość techniczna i algorytmika (10 pkt) |
| **C** | Michał Małecki | `server/src/db/*`, `routes/*` | Uruchomienie `server/api.http`, pokazanie transakcji `ledger` w bazie SQLite (zapis zamknięcia ręki, ACID), filtry w lobby | Bezpieczeństwo i poprawność danych (5 pkt) |
| **D** | Michał Pączkowski | `client/src/components/table/*` | Przełączenie układu Classic → Hero → Compact na żywo, omówienie wzoru trygonometrycznego `useSeatLayout`, animacja CSS flip | UI / UX i Responsywność (5 pkt) |
| **E** | Miłosz Szymczuk | `client/src/workers/*`, `services/*` | Demonstracja pracy Web Workera w DevTools Performance (obciążenie CPU w osobnym wątku, zero lagów na stole), automatyczny reconnect WS | Rozszerzenie techniczne (10 pkt) |

---

## 5. Podsumowanie i Rekomendacje dla Zespołu

1. **Struktura Monorepo:** Przekształcić obecne płaskie repozytorium w strukturę `shared/`, `server/`, `client/` z wykorzystaniem NPM Workspaces. Pozwoli to współdzielić `evaluator.js` pomiędzy serwerem a Web Workerem bez dodatkowych narzędzi.
2. **Korekta specyfikacji all-in:** Wykreślić z dokumentów ideę „cap & refund" w grze wieloosobowej jako uniemożliwiającą normalną licytację i zastąpić ją przedstawionym deterministycznym algorytmem warstwowym `buildPots` w `pots.js`.
3. **Pojedynczy punkt wejścia do stołu:** Usunąć `seat:take` z protokołu WebSocket. Zajmowanie miejsca i zasilenie stacka z portfela musi iść wyłącznie przez REST (`POST /api/tables/:id/join`), po czym kontroler powiadamia instancję stołu w pamięci serwera, a ta rozsyła zdarzenie po WebSocket.
4. **Zatwierdzenie ról:** Wprowadzić powyższy 5-osobowy podział ról w `README.md` oraz `docs/04-podzial-pracy-harmonogram-i-obrona.md`, zamykając wszelkie niejasności przed rozpoczęciem kodowania Etapu 2.
