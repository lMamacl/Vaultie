# Labs — Vaultie Masterclass

Sandbox z kodem i szablonami do odpalenia przy lekcjach masterclass.

## Struktura

```
labs/
  README.md                 ← ten plik
  web-engineering/
    <lesson-id>/            ← np. 1.1, 2.2, 3.3
      README.md             ← cel labu, kroki, DoD
      ...                   ← pliki ćwiczeniowe
```

## Zasady

1. Lab powstaje **przy realizacji lekcji** (nie hurtowo na zapas).
2. Małe, uruchamialne przykłady; Docker Compose gdy potrzeba DB.
3. Kotwice: TypeScript/Node, Java/Spring, C#/.NET, React, Angular, PostgreSQL.
4. Go/Rust tylko gdy lekcja Vs tego wymaga.
5. Sekrety: tylko `.env.example` — nigdy prawdziwych kluczy w git.

## Artefakty build

Commitujemy źródła labu. Ignorujemy: `node_modules/`, `bin/`, `obj/`, `.env`, artefakty build (patrz root `.gitignore`).

## Start

| Lekcja / Sandbox | Ścieżka | Status |
|---|---|---|
| 1.1 Ideation / FR-NFR | [web-engineering/1.1](web-engineering/1.1/) | Aktywny |
| 1.2+ | — | Po realizacji lekcji |
| Fantasy Map Generator | [Fantasy-Map-Generator-experimental](Fantasy-Map-Generator-experimental/) | Submoduł badawczo-eksperymentalny |
| Poland Statecraft | [poland-statecraft](poland-statecraft/) | Symulator systemowy & Drzewo reform Polski 2026+ |

Mapa lekcji: [`90_Meta/web-engineering-roadmap.md`](../90_Meta/web-engineering-roadmap.md)
