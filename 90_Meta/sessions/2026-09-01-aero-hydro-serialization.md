# Sesja 2026-09-01 — Aero-Hydro: serializacja stanu fizycznego + seeding prądów

## Kontekst

Kontynuacja analizy mapy `Fate 2026-08-31-20-24.map` (34,5 MB, 70 550 komórek).
Z diagnozy: pola fizyczne (pressure/windU/V/oceanU/V/sstAnomaly/moisture) nie były
serializowane do `.map` — każde wczytanie gubiło klimat; prądy morskie seedyły się
15× rzadziej niż wiatr (2173:15) przez sztywne progi m/s w streamline-rendererze.

## Co zrobiono (commit `8cc30f1b` w `labs/Fantasy-Map-Generator-experimental`)

1. **`src/services/io/aero-hydro-state.ts`** (nowy) — sekcja `data[52]` w `.map`:
   JSON `{v:1, fields:{pressure:"<b64 Float32>",...}}`. Pola: pressure, windU/V,
   oceanU/V, sstAnomaly, sstLandInfluence, moisture. `windSpeed` pochodna — nie
   serializowany. Pola zerowe pomijane (lean saves); sekcja opcjonalna (kompatybilność
   wstecz ze starymi plikami); garda długości przy load (zmieniony grid → skip).
2. **`save.ts` / `load.ts`** — podpięta sekcja 52; load loguje przywrócenie stanu.
3. **`streamline-renderer.ts`** — progi adaptacyjne dla oceanu: start 25% maksimum
   pola (min 0.05), stop 8% (min 0.01); krok śledzenia w px ekranowych (10–24)
   skalowany prędkością relatywną zamiast fizycznej (prądy mają 0.05–0.5 m/s).
4. **Testy** (`aero-hydro-state.test.ts`, 5 przypadków): round-trip bez utraty
   precyzji, lean-save, brak gridu, garda wersji, mismatch długości.

## Walidacja

- Vitest: **428/428** (50 plików) — pełna suita zielona.
- `tsc --noEmit`: jedyny błąd to pre-istniejący `@types/d3-path` w node_modules.
- Uwaga środowiskowa: matcher `toContain` w tym setupie vitest rzuca
  `TypeError: instanceof is not callable` — w testach używać `includes().toBe(true)`.

## Otwarte (backlog z diagnozy)

- Kalibracja lodowców (7,4% lądu w Fate — możliwy za niski próg glaciacji).
- Decyzja: hydrology-engine (Priority-Flood/Strahler) do auto-pipeline po reGraph.
- GPU particles (wzorzec mapbox/webgl-wind) dla warstwy wiatru — dalsza optymalizacja.
- Rebase na upstream FMG v1.149 (klimat upstreamu nieruszany od v1.9 / 2023).