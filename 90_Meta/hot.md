---
type: meta
title: "Hot Context Buffer — Aktywny Kontekst Sesji"
created: 2026-08-06
updated: 2026-08-31
tags: [meta, context, hot-buffer]
up: "[[90_Meta/_index]]"
---

# Hot Context Buffer

> [!NOTE]
> Plik czytany automatycznie na początku każdej nowej sesji przez agenta w celu błyskawicznego podjęcia kontekstu bez konieczności odczytywania całej historii logów.

## Bieżący Punkt Skupienia
- **Aktywny Wątek:** Wdrożenie i pełna walidacja fizycznego modelu klimatu Aero-Hydro 3.0 (Fate / FMG).
- **Zrealizowane Zadania:**
  1. **Dynamiczny, chaotyczny wiatr z deflekcją orograficzną (`atmosphere-engine.ts`):** Wskaźnik wiatru w UI to jedynie łagodne tło; wiatr dynamicznie reaguje na gradient ciśnienia MSLP, omija grzbiety górskie (projekcja styczna $\vec{V}_\parallel$), przyspiesza w przełęczach (efekt Venturiego $+35\%$) i meandruje dzięki synoptycznej wirowości (divergence-free curl noise).
  2. **Skala alpejska szczytów $4800\text{ m}$ (`temperature-engine.ts`):** Kalibracja $h=100 \rightarrow 4800\text{ m}$ n.p.m. ($\Delta T = -31.2^\circ\text{C}$), generująca realne lodowce górskie i strefę subalpejską.
  3. **Adwekcja ciepła SST w głąb lądu (`ocean-engine.ts`):** Anomalia termiczna prądów morskich jest przenoszona wiatrem wzdłuż linii prądu na odległość 800–1200 km.
  4. **Fizyczny model opadów Smith-Barstad i cień fenowy (`moisture-advection-engine.ts`):** Usunięto limit 25% ubytku; pełny bilans skraplania orograficznego, silne wysuszenie adiabatyczne (Foehn) i spadek opadów na zawietrznej na dystansie 150–350 km, zasilanie krawędzi nawietrznej (Ghost Domain) i ciągłe osiadanie zwrotnikowe (Hadley cell).
  5. **Płynna matryca biomów (`biomes-generator.ts`):** Skalibrowano progi opadów (<90 mm pustynia, <225 mm zarośla, <450 mm step/trawy, <850 mm zadrzewienia, <1600 mm lasy), eliminując problem załamania kontynentu w pustynię przy obniżaniu opadów.
  6. **Wszystkie 423 testy jednostkowe Vitest (49 plików testowych) przechodzą w 100%.**
  7. **Naprawiono ładowanie plików `.map` z końcami linii LF (`load.ts`):** Parser został uodporniony na pliki zapisane/znormalizowane z zakończeniami linii Unix LF (`\n`). Blok SVG jest izolowany przed podziałem, dzięki czemu mapa `Fate 2026-08-30-18-29.map` ładuje się bez błędu "Invalid file".

## Ostatnio Modyfikowane Notatki i Pliki
- `labs/Fantasy-Map-Generator-experimental/src/generators/aero-hydro/atmosphere-engine.ts`
- `labs/Fantasy-Map-Generator-experimental/src/generators/aero-hydro/temperature-engine.ts`
- `labs/Fantasy-Map-Generator-experimental/src/generators/aero-hydro/ocean-engine.ts`
- `labs/Fantasy-Map-Generator-experimental/src/generators/aero-hydro/moisture-advection-engine.ts`
- `labs/Fantasy-Map-Generator-experimental/src/generators/biomes-generator.ts`
- `labs/Fantasy-Map-Generator-experimental/src/generators/aero-hydro/fate-world-physics.test.ts`
- `00_Inbox/_proposals/2026-08-31-climate-aero-hydro-analysis.md`
- `90_Meta/hot.md`

## Następne Kroki
- [x] Pełne wdrożenie fizyki Aero-Hydro 3.0 w silnikach TypeScript
- [x] Pokrycie testami Vitest weryfikującymi cień opadowy i płynne skalowanie biomów
- [ ] Przetestowanie w przeglądarce i interaktywnym UI generatora przez użytkownika


