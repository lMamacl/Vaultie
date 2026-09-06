---
type: meta
title: "Hot Context Buffer — Aktywny Kontekst Sesji"
created: 2026-08-06
updated: 2026-09-06
tags: [meta, context, hot-buffer]
up: "[[90_Meta/_index]]"
---

# Hot Context Buffer

> [!NOTE]
> Plik czytany automatycznie na początku każdej nowej sesji przez agenta w celu błyskawicznego podjęcia kontekstu bez konieczności odczytywania całej historii logów.

## Bieżący Punkt Skupienia
- **Aktywny Wątek:** `labs/HitTimline/` — rejestracja projektu gry muzycznej na Androida jako submodułu Git w `labs/`.
- **Zrealizowane Zadania:**
  1. **Podpięcie submodułu:** Skonfigurowano `git submodule add https://github.com/cyunczykg/HitTimline.git labs/HitTimline`.
  2. **Aktualizacja spisu:** Zaktualizowano `labs/README.md` oraz `.gitmodules`.
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
- `public/main.js`
- `src/generators/aero-hydro/index.ts`
- `src/generators/aero-hydro/hydrology-engine.ts`
- `src/generators/aero-hydro/hydrology-engine.test.ts`
- `src/generators/aero-hydro/moisture-advection-engine.ts`
- `src/generators/biomes-generator.ts`
- `src/utils/binary-heap.ts`
- `src/utils/binary-heap.test.ts`
- `90_Meta/hot.md`

## Następne Kroki
- [ ] Opcjonalne wsparcie dla basenów bezodpływowych (endorheic sinks) przy skrajnym ujemnym bilansie wodnym
- [ ] Ujednolicenie skali mapy z cos(midLat) w `moisture-advection-engine.ts`
- [ ] Warstwa intencji: piny biomów chronione przed nadpisaniem przy recompute klimatu





