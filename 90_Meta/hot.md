---
type: meta
title: "Hot Context Buffer — Aktywny Kontekst Sesji"
created: 2026-08-06
updated: 2026-10-12
tags: [meta, context, hot-buffer]
up: "[[90_Meta/_index]]"
---

# Hot Context Buffer

> [!NOTE]
> Plik czytany automatycznie na początku każdej nowej sesji przez agenta w celu błyskawicznego podjęcia kontekstu bez konieczności odczytywania całej historii logów.

## Bieżący Punkt Skupienia
- **Aktywny Wątek (2026-10-12):** Redakcja językowa, strukturalna i typograficzna zestawu dokumentów startowych w `90_Meta/project-kickoff-kit/` (`tematy przykłądowe.md`, `instrukcje.md`, `wymagania uczelniane.md`). Wprowadzono standaryzację Markdown (nagłówki `#`, `##`, `###`, alerty, tabele, linki), usunięto liczne błędy ortograficzne i fleksyjne ze źródeł uczelnianych, zachowując 100% pierwotnej treści merytorycznej, wymagań sylabusowych i reguł oceniania.
- **Poprzedni Wątek (2026-09-29):** Opracowanie kompleksowego aneksu inżynieryjnego [[appendix-system-architecture-kuchnia-cygana|Appendix 2.2 (Architektura Systemowa i Analiza Przepływów Wielomodułowych „Kuchnia u Cygana”)]]: dogłębny audyt architektury, odwrócenie zależności (DIP), analiza brakujących FK, blokady pesymistyczne UPDLOCK, pełne studium przepływu orkiestracji M1-M2-M3 (Generowanie Planu Produkcji i Rozchód FEFO), rekonstrukcja w 4 alternatywnych paradygmatach, macierz trade-offów i rozszerzone tematy badawcze.
- **Poprzedni Wątek (2026-09-29):** Rejestracja 20 natywnych skills Antigravity: kanoniczne foldery `SKILL.md`, opisy wyzwalające, walidator i aktualizacja adapterów. Szczegóły: [[2026-09-29-1252]].
- **Poprzedni Wątek (2026-09-29):** Druga iteracja UX/researchu: jawna sekcja decyzji i odrzuconych alternatyw; rewizja lekcji 2.2 i jej relacji, źródeł oraz statusu Phase A / human review. Szczegóły: [[2026-09-29-1231]].
- **Poprzedni Wątek (2026-09-29):** Pierwsza iteracja poprawy UX i researchu Vaultie: `90_Meta/start-here.md`, solution brief, metadane źródeł, lint + CI oraz pilot retry. Szczegóły: [[2026-09-29-1145]].
- **Poprzedni Aktywny Wątek (2026-09-29):** Opracowanie kompletnego zestawu startowego dla 2-semestralnego projektu inżynierskiego zespołowego 6+ osób (*Project Kickoff Kit*):
  1. Szablon 1-pagera na Discorda i procedura cichej asynchronicznej inkubacji pomysłów (`01-discord-ideation-1pager.md`).
  2. Oficjalny szablon Dokumentu Inicjującego Projekt (DIP) dla Confluence z mapowaniem 6+ Epików na Bounded Contexts Modularnego Monolitu (`02-confluence-dip-template.md`).
  3. Podręcznik operacyjny rotującego Product Ownera i Dewelopera w Jira/Confluence/Bitbucket z procedurą obronną przed zrzucaniem winy za niedowiezione zadania, szablonami Daily, Review z użytkownikiem końcowym oraz Retro z analizą delty i burndown (`03-scrum-po-developer-handbook.md`).
- **Poprzedni Wątek (2026-09-28):** Wdrożenie i pełna certyfikacja jakościowa lekcji 2.2 Masterclass (*Paradygmaty Architektoniczne Systemów: Architektura Warstwowa, Hexagonalna / Ports & Adapters, Onion, Clean Architecture, Modular Monolith vs Mikroserwisy*).
- **Poprzedni Wątek (2026-09-28):** Opracowanie kompleksowego aneksu inżynieryjnego [[appendix-aspnet-mvc-kuchnia-cygana|Appendix 2.1 (ASP.NET Core MVC, HTMX i Studium Projektu „Kuchnia u Cygana”)]].
- **Bieżące artefakty:** `90_Meta/lessons/2.2/appendix-system-architecture-kuchnia-cygana.md`, `90_Meta/project-kickoff-kit/`, `90_Meta/lessons/2.2/2.2-system-architecture-paradigms.md`, `labs/web-engineering/2.2/`, `90_Meta/lessons/2.1/appendix-aspnet-mvc-kuchnia-cygana.md`
- **Zrealizowane Zadania:**
  1. **Weryfikacja stanu:** potwierdzono naprawy P0 z audytu 2026-09-01 (Ekman, skala wiatru w km, jedna stała 55, Barnes Priority-Flood, izolacja `flAero`, delegacja temp/opadu, `precipMm` w biomach); podzbiór krytyczny 12 plików / 69 testów przechodzi w 100%.
  2. **Dokumenty i Analizy Modułowe:** Skompletowano i zaktualizowano wszystkie 6 analiz modułowych (`00_Inbox/aero-hydro-analizy/`), tworząc pełną specyfikację techniczną dla agentów i bazę do audytu kodu źródłowego.
  3. **[MODUŁ 1 / P0/P1] Wdrożenie AtmosphereEngine v2.1:**
     - Zaimplementowano dynamiczne sferyczne centra baryczne (półkula N/S, pasy podzwrotnikowe i subpolarne).
     - Wdrożono detekcję połączonych mas lądowych (Connected Components) dla niezależnych centrów termicznych wielu kontynentów.
     - Wdrożono wariancję z ziarna PRNG (`seed`) z zachowaniem budżetu fizycznego (jitter $\pm 10\%$, $\Delta P$, promień $R$).
     - Dodano ekstrapolację brzegową Ghost Domain (`getBoundaryLandFractions`, Land Continuity).
     - Wprowadzono metodę `updatePressureLive()` dla płynnego przeciągania żetonów w UI (60 FPS).
     - Wszystkie 13 testów modułu oraz 56 plików testowych (461 testów) w całym repozytorium przechodzą w 100% na zielono.
  4. **[MODUŁ 2 / P0/P1] Wdrożenie OceanEngine v2.1:**
     - Zaimplementowano uniwersalne wzmocnienie brzegowe w basenie oparte o wirowość wiatru (`detectOceanBasins`, Wind Stress Curl / Stommel), eliminując sztywne powiązanie z lewą krawędzią ekranu.
     - Wdrożono filtrację małych jezior śródlądowych (< 25 komórek) — brak sztucznych prądów w jeziorach górskich.
     - Wdrożono punkty brzegowe zasilania prądów morskich (`OceanInflowSpawner`).
     - Wdrożono tłumienie naprężenia wiatrowego pod pokrywą lodu morskiego ($T \le -2^\circ\text{C}$).
     - Wprowadzono kierunkową bramkę wiatru on-shore w `propagateSstToLand()` — transfer ciepła na wybrzeże zachodzi tylko przy wietrze wiejącym z morza.
     - Wszystkie 12 testów modułu oraz 56 plików testowych (465 testów) w repozytorium przechodzą w 100% na zielono.
  5. **[MODUŁ 3 / P0/P1/P2] Wdrożenie TemperatureEngine v2.1:**
     - Zaimplementowano adiabatyczne ogrzanie fenowe (Föhn heating bonus $+2$ do $+5^\circ\text{C}$) po zawietrznej stronie pasm górskich, sprzężone z `cells.foehnShadow` oraz geometrycznym opadaniem mas powietrza.
     - Wprowadzono ciągłe pole Float32Array `cells.tempC` (dla bezschodkowej ewapotranspiracji i fizyki parowania) przy zachowaniu kompatybilnego `cells.temp` (Int8Array).
     - Wdrożono fizyczny model kontynentalizmu: wygaszanie buforu oceanicznego oraz radiacyjne wypromieniowanie ciepła w suchym powietrzu (nasycenie kolumny Clausius-Clapeyron w strefach umiarkowanych/borealnych), eliminując sztuczne wzory empiryczne.
     - Wdrożono próg zlodowacenia morskiego ($-2^\circ\text{C}$) z flagą `cells.seaIce`.
     - Zaimplementowano obsługę blokad użytkownika (`userLocks` / `tempLock`).
     - Zamknięto sprzężenie zwrotne w `AeroHydro.generate()` (refinement termiczny po wyliczeniu wilgoci i cienia fenowego).
     - Wszystkie 10 testów modułu oraz 56 plików testowych (471 testów) w repozytorium przechodzą w 100% na zielono.
  6. **[MODUŁ 4 / P0/P1] Wdrożenie MoistureAdvectionEngine v2.1:**
     - Poprawiono skalę geograficzną na osi X: dodano współczynnik sferycznego zwężenia południków $\cos(\text{midLat})$, eliminując błąd dwukrotnego przeszacowania odległości na szerokościach subpolarnych.
     - Wdrożono odcięcie parowania oceanicznego dla wód zlodowaconych ($T \le -2^\circ\text{C}$ / `cells.seaIce === 1`), tworząc realistyczną suchą pustynię polarną.
     - Zaimplementowano lokalne parowanie jezior śródlądowych zasilające wilgocią obszary zawietrzne.
     - Wdrożono wielokierunkowy napływ brzegowy z Ghost Domain (wiatry zachodnie, pasaty wschodnie, monsuny południowe, wiatry północne) sterowany `grid.boundaryLandFraction`.
     - Obliczono fizyczne pola bilansu wodnego: `cells.petMm` (Potencjalna Ewapotranspiracja Holdridge/Thornthwaite), `cells.waterBalanceMm` ($P - \text{PET}$) oraz `cells.aridityIndex` ($P/\text{PET}$), trwale rozwiązując paradoks tajgi i pustyni.
     - Wszystkie 15 testów modułu oraz 56 plików testowych (476 testów) w repozytorium przechodzą w 100% na zielono.
  7. **[MODUŁ 5 / P0/P1] Wdrożenie HydrologyEngine v2.1 & BiomesGenerator:**
     - Wdrożono algorytm Priority-Flood (Barnes 2014) z obsługą zlewisk bezodpływowych (Endorheic Basins): w suchych strefach ($P \ll \text{PET}$, `waterBalanceMm < -50` lub `aridityIndex < 0.6`) lokalne depresje są rejestrowane jako naturalne ujścia (`cells.endorheicSinks`), zapobiegając sztucznemu wyrównywaniu do poziomu oceanu.
     - Wdrożono skalowanie wilgoci biomów w oparciu o wskaźnik aridity Holdridge'a / PET (`effectiveMm = baseMm * (PET_REF / max(120, petMm))`), co rozwiązuje paradoks fałszywych pustyń w strefach zimnych (tajga ma wilgotność efektywną lasu mimo niskiego opadu sumarycznego).
     - Zaimplementowano strefę buforową korytarzy rzecznych (Riparian Buffer): sąsiedzi dużych rzek (flux >= 30, |Δh| <= 2) otrzymują bonus infiltracji aluwialnej do +150 mm, tworząc oazy nadrzeczne (efekt doliny Nilu / zielonego Mazowsza).
     - Wpięto `HydrologyEngine.generate()` bezpośrednio do głównego pipeline'u `AeroHydro.generate()` przed rekalkulacją biomów `Biomes.define()`.
     - Wszystkie 11 testów `hydrology-engine.test.ts`, 7 testów `biomes-generator.test.ts` i 56 plików testowych (479 testów) w repozytorium przechodzą w 100% na zielono.
  8. **[MODUŁ 6 / P0/P1] Wdrożenie Architecture & User Intent Layer:**
     - Utworzono moduł `IntentStore` (`src/services/intent-store.ts`) zarządzający blokadami użytkownika (`userLocks`: ręcznie malowane biomy, zablokowane rzeki, piny wyżów/niżów barycznych).
     - Zintegrowano `IntentStore` w `BiomesGenerator.define()` i `BiomesEditor.applyBiomesChange()`: komórki zmodyfikowane ręcznie pędzlem są chronione przed nadpisaniem podczas ponownych rekalkulacji klimatu.
     - Zaimplementowano dwupoziomowy cykl reaktywny UI: płynne przeciąganie w 60 FPS (`updatePressureLive()`) bez lagów w `draw-pressure.ts`, z pełnym recompute fizycznym po upuszczeniu żetonu (`AeroHydro.generate()` na zdarzeniu `dragend`).
     - Rozszerzono serializację `.map` w sekcji 52 (`aero-hydro-state.ts`) o nowe pola fizyczne (`tempC`, `precipMm`, `petMm`, `waterBalanceMm`, `aridityIndex`, `flAero`, `foehnShadow`) oraz trwały zapis blokad użytkownika `userLocks`.
     - Wszystkie 57 plików testowych (484 testy) w całym repozytorium przechodzą w 100% na zielono.
  9. **[KALIBRACJA OROGRAFII / BUGFIX & ROLLBACK PRZECHODZENIA WILGOCI]:**
     - Zachowano opływanie pasma po bokach (*Flow Splitting / Mountain Blocking*): nasycenie pionowej prędkości wznoszenia $W = 2.5 \tanh(W_{\text{raw}} / 2.5)$ zapobiega nieliniowej eksplozji gradientu na stromych klifach.
     - Zachowano fizyczny sufit opadu orograficznego (max ~4200 mm/rok), likwidując sztuczne wartości rzędu 17 000+ mm.
     - **Cofnięto sztuczne przechodzenie wilgoci ponad górami:** przywrócono fizyczną barierowość pasm górskich (odcięcie ubytku do 70% w rainoutcie orograficznym, standardowe 1-przebiegowe wygładzenie dyspersyjne bez wymuszonego spilloveru za grań, wygaszanie wilgoci w cieniu fenowym $\times 0.50$).
  10. **[FIZYKA KLIMATU / NAPRAWA ANOMALII PUSTYŃ I POTOPU NIZIN (FATE MAP AUDIT)]:**
     - **Punkt 1 (Bramka nizinna / Grounded Lowland Gating):** Wyciszono sztuczne wznoszenie orograficzne na płaskich nizinach przybrzeżnych ($h < 28$, nachylenie $< 5\text{ m/km}$). Nizina $h=21$ nie generuje już 3000 mm z powodu rozlanego `elevMacro`. Komórka 94779 spadła z 3078 mm do 235 mm!
     - **Punkt 2 (Przeniesienie wznoszenia na stoki i grzbiety):** Szczyty i granie ($h \ge 45$) dziedziczą składową wznoszenia ze stoku nawietrznego (`upwindInflow`), dzięki czemu grzbiety górskie zyskują 250–1500 mm (śnieg, lodowce, lasy górskie) zamiast 60 mm suszy. Odsetek szczytów o opadzie $< 200\text{ mm}$ spadł z 99.5% do 64%.
     - **Punkt 3 & Blokowanie gór w Dijkstrze (Mountain Blocking):** W algorytmie Dijkstry wprowadzono opór orograficzny wspinania pod górę ($\Delta z \times 0.2\text{ km/m}$). Wilgoć obiega pasma górskie przez doliny i przełęcze. Komórki za grzbietem nie dostają wilgoci na wskroś przez szczyt 3700 m, lecz opływowo.
     - **Punkt 4 (Likwidacja uskoków brzegowych / Upwind Leakage):** W kroku adwekcji wilgoć transportowana jest wyłącznie z wiatrem ($\vec{V} \cdot \vec{n} > 0.02$). Wyeliminowano zasysanie morskiej wilgoci pod wiatr, co zlikwidowało pionowy uskok na granicy lądu (komórka 52716 i 53081: zamiast 1107 mm $\leftrightarrow$ 172 mm jest 546 mm $\leftrightarrow$ 657 mm).
     - Wszystkie 57 plików testowych (486 testów) przechodzą w 100% na zielono, a `npm run build` kompiluje się bezbłędnie.
  11. **Sesja:** `90_Meta/sessions/2026-09-11-1245.md`. Zmiany niecommitowane na prośbę użytkownika.
- **Poprzedni Wątek:** Modernizacja i audyt globalnych skilli Antigravity IDE (AAS v17.0.0 + Context7).
- **Zrealizowane Zadania:**
  1. **Audyt i czyszczenie:** Wykonano pełen backup `skills_backup_20260909` (196 starych folderów). Usunięto martwe i zduplikowane skille, zwolniono zablokowany budżet kontekstu tokenów.
  2. **Wyłączenie pluginu `science`:** Przeniesiono 32 nieużywane w codziennym kodowaniu skille bioinformatyczne do `plugins_disabled/science`.
  3. **Wdrożenie AAS v17.0.0:** Pobrano oficjalne repozytorium do `skills_repo/` i zsynchronizowano pełną bibliotekę 2017+ skilli w `skills_library/`.
  4. **Instalacja `context-7`:** Wdrożono skill wyszukiwania bieżącej dokumentacji REST API (z natywnym wrapperem Python + bash).
  5. **Aktywacja wyselekcjonowanego zestawu (113 skilli):** Wdrożono paczki Essentials, Web Wizard, Systems Programming, Architecture, Security, DDD, OSS Maintainer, Mobile oraz zachowano skille customowe (`academic-thesis-auditor`, `tauri-ipc-architecture`, `canvas-performance`).
  6. **Narzędzia zarządzania:** Utworzono skrypty `scripts/activate-skills.bat` oraz `scripts/manage-skills.ps1` do szybkiego przełączania i warstwowania paczek.
- **Poprzedni Wątek:** `labs/HitTimline/` — rejestracja projektu gry muzycznej na Androida jako submodułu Git w `labs/`.
- **Poprzedni Wątek:** `labs/poland-statecraft/` — uruchomienie symulatora systemowego i drzewa reform polityczno-społecznych Polski (Polska 2026+).
- **Zrealizowane Zadania:**
  1. **Audyt ustaleń `review(1)` (CV-1 do CV-9):**
     - Zweryfikowano status każdego ustalenia z nowego modułu `CodeVerification`: CV-1 (unifikacja MM_PER_PREC=55), CV-3 (heurystyka zachodniego brzegu vs Stommel), CV-4 (saturacja Michaelisa-Mentena orografii), CV-6 (decay SST 375 km).
     - Utrzymano twardą regułę właściciela: **odrzucenie sezonowości fizycznej (Pivot 3 / F-09)** na rzecz modelu steady-state.
  2. **[CV-2 / P0] Likwidacja nadpisywania klimatu w `public/main.js`:**
     - Zidentyfikowano i usunięto krytyczny błąd: `public/main.js` w funkcji `generateMap()` wywoływało `generateAeroHydro()`, a natychmiast potem uruchamiało legacy `calculateTemperatures()` i `generatePrecipitation()`, które nadpisywały wyliczone pola `cells.temp` i `cells.prec` starymi procedurami z 2018 roku.
     - Zarejestrowano `TemperatureEngine` i `MoistureAdvectionEngine` na obiekcie `window` i `globalThis` w `src/generators/aero-hydro/index.ts`.
     - Zaktualizowano `calculateTemperatures()` i `generatePrecipitation()` w `public/main.js`, aby delegowały do nowych silników fizycznych.
  3. **[CV-5 / F-05 / P1] Ciągłe pole Float32 `precipMm` w Biomach i Hydrologii:**
     - Zmodyfikowano `BiomesGenerator.define()` w `biomes-generator.ts`, aby bezpośrednio konsumowało pole `grid.cells.precipMm` (Float32Array) z AeroHydro, eliminując skokową kwantyzację 55 mm i sztuczne przeskoki na progach pustyń (124/125 mm).
     - Zaktualizowano `HydrologyEngine` do czytania `precipMm` z pełną precyzją.
  4. **[CV-7 / F-02 / P1] Barnes (2014) Priority-Flood w `HydrologyEngine`:**
     - Zastąpiono uproszczony 30-przebiegowy relaksator pełnym algorytmem Priority-Flood Barnesa (2014) opartym na min-kopcu `BinaryHeap` ($O(N \log N)$).
     - Wypełnianie depresji gwarantuje brak bezodpływowych dziur, eliminuje sztuczny spadek `+0.05` i zapewnia monotoniczny drenaż do oceanu.
     - Wyekstrahowano czystą klasę narzędziową `src/utils/binary-heap.ts` wraz z testami `binary-heap.test.ts`.
  5. **Weryfikacja testowa:**
     - Wszystkie 56 plików testowych (456 testów) przechodzi w 100% na zielono w `vitest`.
     - Zmiany zatwierdzone commitem `6f423328` w repozytorium `labs/Fantasy-Map-Generator-experimental`.

## Ostatnio Modyfikowane Notatki i Pliki
- `90_Meta/lessons/2.2/appendix-system-architecture-kuchnia-cygana.md` (kompleksowy aneks inżynieryjny: audyt architektury, studium przepływu M1-M2-M3 i rekonstrukcja paradygmatów)
- `90_Meta/project-kickoff-kit/01-discord-ideation-1pager.md` (szablon 1-pagera na Discorda i procedura cichej inkubacji pomysłów)
- `90_Meta/project-kickoff-kit/02-confluence-dip-template.md` (szablon Dokumentu Inicjującego Projekt DIP dla Confluence pod 6+ Epików)
- `90_Meta/project-kickoff-kit/03-scrum-po-developer-handbook.md` (podręcznik operacyjny rotującego PO i dewelopera w Jira/Bitbucket/Confluence)
- `90_Meta/lessons/2.2/2.2-system-architecture-paradigms.md` (kompletna lekcja 2.2: paradygmaty, notional machine, DIP, pipeline decyzyjny)
- `90_Meta/lessons/2.2/spec.yaml` (pełny Knowledge Spec lekcji 2.2)
- `90_Meta/lessons/2.2/quality-report.yaml` (raport walidacji certyfikacyjnej: status certified)
- `90_Meta/lessons/2.1/appendix-aspnet-mvc-kuchnia-cygana.md` (kompleksowy aneks architektoniczny i studium przypadku Kuchnia u Cygana)
- `90_Meta/canvases/lesson-2.2-system-architecture.canvas` (wizualna kanwa architektoniczna z rurociągiem decyzji)
- `labs/web-engineering/2.2/` (referencyjny kod: moduły orders/catalog, ports & adapters, testy reguł architektonicznych)
- `90_Meta/_index.md` (rejestracja lekcji 2.2 w mapie bazy wiedzy)
- `90_Meta/web-engineering-roadmap.md` (rejestracja lekcji 2.2 jako certified w roadmapie)
- `90_Meta/hot.md`

## Następne Kroki
- [ ] Zastosowanie zestawu startowego (`project-kickoff-kit`) przy tworzeniu serwera Discord i zbieraniu 1-pagerów pomysłów w zespole.
- [ ] Przed startem semestru: przeprowadzenie cichej inkubacji, głosowanie matrycą scoringową i obsadzenie 6 Epików w szablonie DIP.
- [ ] Po starcie semestru: wklejenie DIP do Confluence, konfiguracja tablicy Jira i odpalenie procedury pierwszego sprintu wg podręcznika PO.



