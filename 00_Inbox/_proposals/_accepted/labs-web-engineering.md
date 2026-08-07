---
type: proposal
title: "Propozycja katalogu labs/web-engineering"
created: 2026-08-06
updated: 2026-08-06
tags: [proposal, labs, sandbox, masterclass, web-engineering]
up: "[[web-engineering-roadmap]]"
status: accepted
accepted: 2026-08-07
---

# Propozycja ACCEPTED → `labs/web-engineering/`

## Cel
Sandbox z kodem do odpalenia przy każdej lekcji masterclass (ID z roadmapy v3). Część pakietu MD + Canvas + labs.

## Docelowa struktura

```
labs/
  README.md                          # jak uruchamiać, wymagania (Node/Docker/JDK/.NET)
  web-engineering/
    1.1/
      README.md                      # cel labu, kroki, DoD
      ...
    1.2/
    ...
    8.3/
```

Każdy katalog lekcji zawiera tylko to, co opisuje pole **Kod / lab** w [[web-engineering-roadmap]] — bez hurtowego generowania wszystkich labs naraz.

## Zasady
1. Labs tworzone **przy realizacji lekcji**, po zaliczonym Blackbox (lub równolegle jako szkielet po briefie).
2. Preferuj małe, uruchamialne przykłady (Docker Compose gdy DB).
3. Kotwice: TypeScript/Node, Java/Spring, C#/.NET, React, Angular, PostgreSQL — zgodnie z lekcją; nie mieszaj zbędnie.
4. Go/Rust tylko jeśli lekcja Vs tego wymaga.
5. Secrets: tylko `.env.example`; żadnych kluczy w git.

## Relacja do vaulta
- `labs/` to **nowa struktura** poza obecną taksonomią `10_`–`50_` — wymaga akceptacji (escape hatch AGENTS.md).
- Artefakty wiedzy nadal lądują w `10_`–`50_` przez `_proposals/`.
- Kanwy: `90_Meta/canvases/` osobno (skill `kb-canvas`).

## Kryteria akceptacji
- [ ] Właściciel akceptuje ścieżkę `labs/web-engineering/`
- [ ] Ustalenie: czy `labs/` jest w `.gitignore` częściowo (build artifacts) czy commitowany w całości (preferencja: commitować źródła labu, ignorować `node_modules`/binaria)
- [ ] Polecenie: „utwórz labs/web-engineering i lab 1.1”

## Pierwszy lab po akceptacji
`labs/web-engineering/1.1/` — szablon `spec-fr-nfr.md` + arkusz latency budget (zgodnie z roadmapą 1.1).
