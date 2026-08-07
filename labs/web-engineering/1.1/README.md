# Lab 1.1 — Ideation, Feasibility & Scope (FR / NFR)

> **Lekcja:** [[1.1-ideation-fr-nfr]] · **Concept:** [[project-initiation-fr-nfr]] · **Roadmapa:** ID `1.1`

## Cel

Wypełnisz specyfikację FR/NFR i arkusz latency budget dla **własnego** (lub przykładowego) projektu 2-semestralnego — zanim napiszesz kod aplikacji.

## Wymagania

- Edytor Markdown (Obsidian / Cursor).
- Brak runtime — to lab dokumentacyjny.

## Kroki

1. Skopiuj `spec-fr-nfr.md` → wypełnij Problem Statement, interesariuszy, FR (MUST/SHOULD/WON'T), NFR, macierz FR↔NFR, decyzję PoC/MVP/Prod.
2. Skopiuj `latency-budget.md` → wypełnij budżet ms dla **2** kluczowych endpointów powiązanych z NFR-PERF.
3. Porównaj z reference: `90_Meta/lessons/1.1/worked-example-student-project.md` (VaultCollab).
4. DoD (poniżej) — self-check.

## Pliki w tym labie

| Plik | Opis |
|---|---|
| [`spec-fr-nfr.md`](spec-fr-nfr.md) | Główna specyfikacja do wypełnienia |
| [`latency-budget.md`](latency-budget.md) | Budżet latencji per endpoint |

Szablony źródłowe (Vaultie Meta): `90_Meta/lessons/1.1/`

## Definition of Done

- [ ] Min. 5 FR MUST z kryteriami akceptacji
- [ ] Min. 5 NFR mierzalnych (w tym 1 PERF + 1 SEC)
- [ ] Macierz FR↔NFR (min. 3 powiązania)
- [ ] Jawna decyzja: PoC tak/nie + uzasadnienie
- [ ] Latency budget dla 2 endpointów (suma ≤ cel p95)
- [ ] Out of Scope / WON'T wypisane

## Po labie

1. Quiz Blackbox w lekcji 1.1 (lub: `uruchom kb-blackbox dla 1.1`).
2. Opcjonalnie: skopiuj wypełniony `spec-fr-nfr.md` do repo projektu uczelnianego jako `docs/spec-fr-nfr.md`.
3. Następna lekcja: **1.2** (WBS / RACI) — FR MUST → zadania na tablicy.
