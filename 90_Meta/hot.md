---
type: meta
title: "Hot Context Buffer — Aktywny Kontekst Sesji"
created: 2026-08-06
updated: 2026-09-04
tags: [meta, context, hot-buffer]
up: "[[90_Meta/_index]]"
---

# Hot Context Buffer

> [!NOTE]
> Plik czytany automatycznie na początku każdej nowej sesji przez agenta w celu błyskawicznego podjęcia kontekstu bez konieczności odczytywania całej historii logów.

## Bieżący Punkt Skupienia
- **Aktywny Wątek:** Wdrożenie pakietu poprawek P0/P1 dla podsystemu Aero-Hydro w Fantasy Map Generator oraz ustalenie architektury steady-state (odrzucenie sezonowości w silniku fizycznym).
- **Zrealizowane Zadania:**
  1. **Decyzja produktowa:** Potwierdzenie modelu stacjonarnego (steady-state, średniorocznego). Sezonalność odrzucona z silnika fizycznego — ewentualne sezony będą wyłącznie lekką nakładką wizualną (post-process shader/filtr) w przyszłości.
  2. **[A-09] Bezpieczna hydrologia:** Wdrożono zapis fizycznego przepływu $Q$ do dedykowanego `cells.flAero: Float32Array` oraz rzędowości Strahlera do `cells.strahlerAero: Uint8Array`. Ochroniono natywną tablicę `grid.cells.fl` przed korupcją jednostek FMG. Zaktualizowano test jednostkowy `hydrology-engine.test.ts`.
  3. **[A-20] Naprawa buga tęczy podczas dragu:** Zastąpiono błędne `updatePressureColorsOnly` poprawnym rebuildingiem wiader ścieżek `updatePressureHeatmap()` w `draw-pressure.ts`. Wprowadzono koalescencję zdarzeń myszy przez `requestAnimationFrame` (60 FPS podczas ruchu żetonu) oraz statyczny import `drawWinds`.
  4. **[A-21] UI i kontrolki wilgoci:** W `aero-hydro-editor.ts` dodano dedykowaną kontrolkę `condensationRateInput` spiętą z `options.moistureAdvection.condensationRate`, porządkując etykietę dla blokady orograficznej. Zaktualizowano test `aero-hydro-editor.test.ts`.
  5. **Optymalizacja wydajnościowa:** Wyeliminowano alokację 100 000 tablic tymczasowych na klatkę (`Math.max(...neigh.map(...))`) w `atmosphere-engine.ts`.
  6. **Weryfikacja testowa:** Zestaw 55 plików testowych (452 testy) przechodzi w 100% na zielono (`vitest`).

## Ostatnio Modyfikowane Notatki i Pliki
- `src/generators/aero-hydro/hydrology-engine.ts`
- `src/generators/aero-hydro/hydrology-engine.test.ts`
- `src/renderers/aero-hydro/draw-pressure.ts`
- `src/controllers/aero-hydro-editor.ts`
- `src/controllers/aero-hydro-editor.test.ts`
- `src/generators/aero-hydro/atmosphere-engine.ts`
- `90_Meta/hot.md`

## Następne Kroki
- [ ] Priority-Flood Barnes 2014 zamiast iteracyjnego podnoszenia + jeziora endoreiczne (A-08)
- [ ] Gradient FVM Green-Gauss / LSQ na siatce Voronoi w `grid-math.ts` (A-19)
- [ ] Ujednolicenie skali mapy z cos(midLat) we wszystkich silnikach (atmosfera vs wilgoć)
- [ ] Warstwa intencji: piny biomów chronione przed nadpisaniem przy recompute klimatu




