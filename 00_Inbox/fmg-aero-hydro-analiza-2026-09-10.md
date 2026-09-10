---
type: deep-analysis
title: "Analiza systemu Aero-Hydro i zależnych komponentów FMG"
created: 2026-09-10
updated: 2026-09-10
tags: [fantasy-map-generator, aero-hydro, architecture, climate, rendering, review]
aliases: []
up: "[[90_Meta/_index]]"
---

# Cel i zakres

Analiza dotyczy modułu Aero-Hydro w `labs/Fantasy-Map-Generator-experimental` oraz
każdego komponentu, który dostarcza mu dane, konsumuje jego wyniki albo wpływa na
interakcję użytkownika. Oceniany jest stan faktyczny kodu, a nie wyłącznie architektura
docelowa opisana w dokumentacji.

System ma obsługiwać dowolną mapę FMG: różne rozdzielczości siatki, szerokości
geograficzne, proporcje lądu i oceanu oraz zapis w istniejącym formacie `.map`.

# 1. Model systemu

## 1.1. Warstwy

Projekt deklaruje cztery warstwy:

1. **Dane świata** — `grid`, `pack`, style i opcje.
2. **Generatory** — deterministyczne obliczenia terenu, klimatu, hydrologii,
   osadnictwa i gospodarki.
3. **Edytory** — kontrolowane zmiany danych świata wywoływane przez użytkownika.
4. **Renderery** — wizualizacja stanu bez modyfikowania modelu.

To jest właściwy kierunek, lecz implementacja nadal korzysta z globalnych obiektów
`window.grid`, `window.pack`, `options`, `style` oraz funkcji legacy z `public/main.js`.
Rozdzielenie jest więc kontraktem architektonicznym, a nie pełną izolacją wykonawczą.

## 1.2. Rola `grid` i `pack`

`grid` jest pierwotną, regularnie rozmieszczoną siatką Voronoi. Przechowuje wysokość,
klimat i dane potrzebne do obliczeń na etapie generowania.

`pack` jest ponownie upakowaną reprezentacją świata używaną przez rzeki, biomy,
kultury, państwa, miasta i gospodarkę. Mapowanie `pack.cells.g` łączy komórkę
upakowaną z komórką `grid`.

Aero-Hydro zapisuje większość pól klimatycznych w `grid.cells`. Jest to poprawne
dla etapu generowania, ale wymaga jawnego odświeżenia danych zależnych w `pack`.
Naruszenie tej kolejności daje mapę, na której klimat i biomy pochodzą z różnych
wersji świata.

# 2. Główny workflow generowania

Kanoniczny przebieg znajduje się w `public/main.js`, w funkcji `generate()`:

1. seed, rozmiar mapy i opcje,
2. siatka oraz wysokość terenu,
3. oceany, jeziora i cechy hydrologiczne,
4. położenie świata i Aero-Hydro,
5. repack do `pack`,
6. rzeki i biomy,
7. lód i warstwy klimatyczne,
8. dobra,
9. ranking komórek i kultury,
10. miasta, państwa, trasy i religie,
11. prowincje i nazewnictwo,
12. gospodarka,
13. wojsko, markery i strefy,
14. finalizacja, statystyki i render.

`AeroHydroModule.generate()` wykonuje kolejno:

`AtmosphereEngine → OceanEngine → TemperatureEngine →
MoistureAdvectionEngine → StreamlineRenderer`.

HydrologyEngine nie jest automatycznie częścią tego potoku. Rzeki produkcyjne nadal
tworzy generator FMG. HydrologyEngine zapisuje dodatkowe pola `flAero` i
`strahlerAero`, dzięki czemu nie niszczy semantyki istniejącego `cells.fl`.

## 2.1. Zależne ścieżki regeneracji

Edycja heightmapy ma dwa warianty:

- pełna regeneracja usuwa osadnictwo i odtwarza późniejsze fazy pipeline’u;
- zachowanie danych remapuje kultury, miasta, państwa i prowincje na nową topologię.

Każdy nowy generator musi być dopisany do obu ścieżek. To obecnie największe ryzyko
regresji: `generate()` jest kanoniczne, ale nie istnieje centralny graf zależności,
który automatycznie wymusza aktualizację replik.

# 3. Analiza modułów

## 3.1. AtmosphereEngine

**Odpowiedzialność:** tworzy pole MSLP, gradient ciśnienia i wektory wiatru.
Łączy profil strefowy, wpływ lądu i morza, żetony baryczne, wskazówki kierunku
wiatru oraz wygładzanie.

**Mocne strony:**

- deterministyczne wejścia i typowane tablice;
- czytelna dekompozycja profilu ciśnienia;
- ograniczenie maksymalnej prędkości i tłumienie na dużych wysokościach;
- testy obejmujące pola ciśnienia, wiatr i zachowanie graniczne.

**Problemy:**

- gradient historycznie był skalowany na komórkę, więc wynik zależał od rozdzielczości;
- człon geostroficzny wymaga ostrożnego wygaszania przy równiku;
- dokumentacja nazywa prosty estymator sąsiedzki gradientem Green-Gaussa;
- komentarz o polu bezrozbieżnościowym nie odpowiada pełnej matematyce składowej wirowej.

**Ocena:** dobry moduł do ukierunkowanego ulepszenia. Nie wymaga rewrite’u, ponieważ
jego wejścia, wyjścia i dekompozycja są użyteczne. Należy ujednolicić jednostki,
zabezpieczyć zachowanie przy równiku i testować niezależność od rozdzielczości.

## 3.2. OceanEngine

**Odpowiedzialność:** prądy oceaniczne, anomalia temperatury powierzchni morza
oraz wpływ oceanu na temperaturę lądu.

**Mocne strony:**

- osobne pola `oceanU`, `oceanV`, `sstAnomaly` i `sstLandInfluence`;
- wyraźna granica między cyrkulacją atmosferyczną i oceaniczną;
- możliwość wizualizacji przepływu bez zmiany podstawowej geometrii mapy.

**Problemy:**

- western intensification nie może zależeć wyłącznie od globalnej pozycji `x`;
- reguła powinna rozpoznawać zachodnią krawędź konkretnego basenu oceanicznego;
- model musi działać także dla map z małym oceanem, oceanem na wschodzie albo
  wieloma basenami.

**Ocena:** redesign lokalny. Należy zachować interfejs i pola wyjściowe, ale zmienić
wyznaczanie odległości od krawędzi basenu oraz dodać testy dla różnych układów mapy.

## 3.3. TemperatureEngine

**Odpowiedzialność:** temperatura z profilu szerokości geograficznej, wysokości
oraz wpływu SST.

**Mocne strony:**

- wynik trafia do jednego źródła danych przed klasyfikacją biomów;
- uwzględnia lapse rate i wpływ morza;
- istnieją testy profilu temperatury oraz przypadków brzegowych.

**Problemy:**

- parametry wysokości muszą korzystać z ustawień FMG, a nie z niezależnego
  wykładnika i ograniczenia właściwego tylko dla jednego scenariusza;
- należy wyraźnie oddzielić temperaturę klimatyczną od ręcznej intencji użytkownika.

**Ocena:** ulepszenie kontraktu parametrów i testów, bez przebudowy silnika.

## 3.4. MoistureAdvectionEngine

**Odpowiedzialność:** adwekcja wilgoci, opady, recykling lądowy, efekt orograficzny
i zapis ciągłego `precipMm`.

**Mocne strony:**

- używa ciągłego pola `Float32Array`, eliminując sztuczne progi wynikające
  z kwantyzacji starego `prec`;
- uwzględnia kierunek wiatru, transport i teren;
- posiada testy konfiguracji, opadów i klifów orograficznych.

**Problemy:**

- konfiguracja musi być dostępna w edytorze, inaczej część modelu jest ukryta;
- skala odległości geograficznej powinna być wspólna z atmosferą;
- przepływ powinien mieć jawny kontrakt jednostek i jawne wartości domyślne.

**Ocena:** zachować i ulepszyć. To jeden z najbardziej wartościowych elementów
modułu, ale wymaga pełnego okablowania ustawień i dokumentacji jednostek.

## 3.5. HydrologyEngine

**Odpowiedzialność:** wypełnianie depresji, kierunek spływu, akumulacja,
rzędowość Strahlera oraz parametry koryta.

**Mocne strony:**

- Priority-Flood z kolejką priorytetową ma właściwy model złożoności;
- używa `precipMm` z fallbackiem dla starszych map;
- nie nadpisuje starego `cells.fl`, tylko zapisuje `flAero`;
- wynik jest użyteczny do analizy i diagnostyki.

**Problemy:**

- automatyczne włączenie do produkcyjnego generatora rzek zmieniłoby semantykę FMG;
- przepływ fizyczny i historyczne `cells.fl` muszą pozostać rozdzielone;
- obsługa zlewisk bezodpływowych powinna być jawna, a nie ukryta w sztucznym spadku.

**Ocena:** zachować jako niezależny silnik analityczny. Integrację produkcyjną można
rozważyć dopiero po osobnej migracji formatu i porównaniu wyników z istniejącymi rzekami.

## 3.6. AeroHydroModule

Koordynator ma poprawną kolejność silników i rejestruje kompatybilne globalne wywołania
`calculateTemperatures`, `generatePrecipitation` oraz `generateAeroHydro`.

**Ryzyko:** `flowFeatures` i wywołanie `Biomes.define()` są efektami ubocznymi,
a globalne rejestracje utrudniają testowanie i śledzenie zależności.

**Ocena:** redesign kontraktu, nie rewrite. Docelowo powinien przyjmować jawny obiekt
świata i zwracać raport zmian, lecz adapter globalny należy utrzymać do czasu migracji
`public/main.js`.

## 3.7. Biomy i zależne generatory

Biomy konsumują temperaturę i ciągłe `precipMm`, a następnie przekazują wynik do
hydrologii, osadnictwa i ekonomii. To poprawia ciągłość modelu, ale każda ponowna
klasyfikacja może nadpisać ręczne decyzje użytkownika.

**Ocena:** ulepszyć przez warstwę intencji. Dane proceduralne i ręczne piny powinny
być przechowywane osobno, a recompute powinien respektować blokady użytkownika.

# 4. Renderowanie i warstwa wizualna

## 4.1. Rejestr warstw

`LayersRegistry` centralizuje kolejność, widoczność, tworzenie grup SVG, draw i erase.
Jest to dobry istniejący wzorzec i powinien pozostać źródłem prawdy dla warstw.

Problemem są grupy Aero-Hydro tworzone poza rejestrem oraz różne mechanizmy życia
warstw. Każda warstwa powinna mieć identyfikator, stan widoczności, renderer i
jednoznaczne zasady czyszczenia.

## 4.2. ViewportRenderer

`ViewportRenderer` posiada overscan, guard pixels, harmonogramowanie przez
`requestAnimationFrame`, bounds i częściową materializację. To realna podstawa
skalowania, lepsza niż pełne przerysowanie każdego obiektu.

Należy rozszerzyć ją o indeks przestrzenny dopiero wtedy, gdy pomiary pokażą, że
iterowanie sceny jest wąskim gardłem. Najpierw należy wykorzystać obecny kontrakt
warstw i dodać metryki czasu renderowania.

## 4.3. Renderer hybrydowy

Prototyp Cartographer Studio słusznie rozdziela:

- Canvas dla ciężkich danych rastrowych i terenu,
- osobny Canvas dla animowanych przepływów,
- SVG dla etykiet, emblematów i interakcji.

Nie jest to jeszcze renderer WebGL: etykieta „WebGL MDOW” opisuje funkcję, której
kod nie implementuje. Dodatkowo bufor offscreen tworzony przy każdym renderze
powinien być utrzymywany i zmieniany tylko po zmianie rozmiaru.

## 4.4. Renderer ciśnienia i animacje

Izobary muszą być liniami wynikającymi z konturów pola, a nie punktami co kilka
hektopaskali. Wstęgi i cząstki powinny używać czasu z `requestAnimationFrame`,
uwzględniać DPR oraz otrzymywać transformację viewportu przez jawny kontekst,
zamiast czytać globalne `viewX`, `viewY` i `scale`.

# 5. Edytor i UX

Istniejący wzorzec jest trafny:

- lewy toolbar narzędzi,
- kontekstowy dock parametrów,
- prawy dock warstw i inspektora,
- minimapa,
- skróty klawiaturowe,
- undo/redo,
- ostrzeżenie przed regeneracją.

Największa luka polega na tym, że interfejs nie udostępnia wszystkich parametrów
modelu Aero-Hydro. Użytkownik widzi efekt, ale nie może wyjaśnić ani kontrolować
części przyczyn. Panel powinien rozdzielać:

1. parametry klimatu,
2. parametry oceanu,
3. parametry opadów,
4. parametry hydrologii,
5. diagnostykę i wersję modelu.

Każda zmiana powinna mieć zakres: tylko wizualizacja, recompute klimatu albo pełna
regeneracja zależnych danych. Przed pełną regeneracją system musi pokazać, które
warstwy zostaną zmienione.

# 6. Najważniejsze zależności i ryzyka

1. Zmiana klimatu wpływa na temperaturę, opady, biomy, hydrologię, roślinność,
   ranking komórek, osadnictwo i ekonomię.
2. Zmiana heightmapy może zmienić topologię `pack`, więc wymaga remapowania danych.
3. `public/main.js` pozostaje punktem wejścia legacy i może ponownie wywołać stare
   procedury, jeśli delegacja nie zostanie utrzymana.
4. Globalny stan utrudnia równoległe obliczenia i testy izolowane.
5. SVG jest właściwy dla etykiet i interakcji, lecz kosztowny dla ciężkich warstw.
6. Deklarowany WebGL nie może być traktowany jako istniejąca funkcja.

# Wniosek

System ma wystarczająco dobry fundament, aby rozwijać go inkrementalnie. Największą
wartość przyniosą: formalny kontrakt danych Aero-Hydro, ujednolicenie jednostek,
jawny graph zależności regeneracji, warstwa intencji użytkownika oraz hybrydowy
renderer z prawdziwym pomiarem wydajności. Pełna przebudowa byłaby kosztowna,
ryzykowałaby kompatybilność `.map` i nie rozwiązałaby sama problemu kolejności
generatorów.
