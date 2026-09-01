---
type: meta
title: "Hot Context Buffer — Aktywny Kontekst Sesji"
created: 2026-08-06
updated: 2026-09-01
tags: [meta, context, hot-buffer]
up: "[[90_Meta/_index]]"
---

# Hot Context Buffer

> [!NOTE]
> Plik czytany automatycznie na początku każdej nowej sesji przez agenta w celu błyskawicznego podjęcia kontekstu bez konieczności odczytywania całej historii logów.

## Bieżący Punkt Skupienia
- **Aktywny Wątek:** Audyt Code Review & Physics Audit modułu Aero-Hydro 2.0 (Fate / FMG).
- **Zrealizowane Zadania:**
  1. **Pełny audyt 4-filarowy modułu Aero-Hydro** (algorytmy, edytory, wizualizacja, zgodność z fizyką Ziemi/Fate/Azgaar FMG) → raport: `labs/Fantasy-Map-Generator-experimental/AERO_HYDRO_AUDIT_2026-09-01.md` (18 ustaleń A-01…A-18, backlog P0/P1/P2, plan testów T-*).
  2. **P0 wykryte w audycie:** (a) podejrzenie odwróconego znaku rotacji Ekmana (`ocean-engine.ts:90`), (b) skala geostroficzna w hPa/komórkę → wiatr zależny od rozdzielczości siatki (`atmosphere-engine.ts`), (c) trzy różne stałe prec→mm (40/45/55) rozspajające bilans opad→rzeki→biomy.
  3. **P1 kluczowe:** Coriolis odwrócony przy równiku (geostrofia najsilniejsza przy f→0), Western Intensification od pozycji na mapie zamiast krawędzi basenu, „Fate-izmy" hardkodowane w ścieżkach generycznych (fallback współrzędnych Fate w `temperature-engine.ts`), „Priority-Flood" bez kolejki priorytetowej, `cells.fl` nadpisywane m³/s niezgodnie z semantyką FMG.
  4. Potwierdzone mocne strony: serializacja `data[52]` (wzorcowa), silnik wilgoci (Dijkstra upwind + Smith-Barstad + Föhn), edytor z live recompute żetonów H/L.

## Ostatnio Modyfikowane Notatki i Pliki
- `labs/Fantasy-Map-Generator-experimental/AERO_HYDRO_AUDIT_2026-09-01.md` (**NOWY** — główny wynik sesji)
- `90_Meta/hot.md`
- `90_Meta/sessions/2026-09-01-*.md`

## Następne Kroki
- [ ] Naprawa P0: znak Ekmana (A-01) + skala wiatru w km (A-02) + jedna stała prec→mm (A-03) — z testami T-OC-1, T-AT-4, T-MO-3
- [ ] Dekontaminacja Fate (A-06): generyczne fallbacki `mapCoordinates` + źródła wilgoci dla dowolnej krawędzi mapy
- [ ] Priority-Flood Barnes 2014 zamiast iteracyjnego raise (A-08); rozdzielenie `cells.fl` vs `flAero` (A-09)
- [ ] Prawdziwe izobary (marching squares) zamiast kropek (A-10); RK2 w streamline'ach (A-11)



