---
type: concept
title: "Inicjacja projektu — FR, NFR, PoC/MVP"
domain: architecture
prerequisite: []
difficulty: intermediate
created: 2026-08-07
updated: 2026-08-07
tags: [concept, fr, nfr, requirements, mvp, poc, ideation]
aliases: [FR NFR, project initiation, PoC vs MVP]
up: "[[Concepts MOC]]"
---

# Inicjacja projektu — FR, NFR, PoC/MVP

## What — o co chodzi?

Inicjacja projektu webowego to przekształcenie pomysłu w **specyfikację inżynierską**: Functional Requirements (co system robi), Non-Functional Requirements (jak dobrze), feasibility (czy się da w czasie i zespole) oraz świadoma decyzja PoC / MVP / Production — **zanim padnie pierwsza linia kodu**.

## Why — dlaczego to ważne?

- Bez FR nie ma testów akceptacyjnych ani sensownego WBS (lekcja 1.2).
- Bez NFR architektura, baza i security to zgadywanie (etapy 2–5 masterclass).
- Mylenie PoC z produktem to antypattern **Prototype in Production** — dług techniczny od tygodnia 1.

## Mental Model

**Budowa domu:**
- **FR** = „3 sypialnie, kuchnia, łazienka” (co budujemy).
- **NFR** = „ogrzewanie do 20°C, ściany odporne na wiatr” (jak dobrze).
- **PoC** = „sprawdzenie, czy grunt wytrzyma piwnicę” (jedno ryzyko techniczne).
- **MVP** = „dom z jedną łazienką, można w nim mieszkać zimą” (najmniejsza wartość użytkowa).
- **Production** = „dom z certyfikatem, ubezpieczeniem, serwisem” (przeżyje obciążenie i czas).

## How — jak to działa?

```
Pomysł → Problem Statement → Interesariusze
       → FR (MUST/SHOULD/COULD/WON'T) + Out of Scope
       → NFR (mierzalne: p95, HTTPS, CI…)
       → Macierz FR ↔ NFR
       → Feasibility (tech / czas / org)
       → PoC? → MVP (S1) → Production (S2)
       → Latency budget (NFR perf → ms per warstwa)
       → docs/spec-fr-nfr.md
```

| Horyzont | Pytanie walidacyjne | Typowy czas (uczelnia) |
|---|---|---|
| PoC | Czy da się technicznie? | 1–2 tyg., throwaway |
| MVP | Czy użytkownik chce? | 4–8 tyg. (Semestr 1) |
| Production | Czy przeżyje ruch i ataki? | Semestr 2 + hardening |

**Werdykt:** PoC tylko przy ryzyku technicznym. MVP = start S1. Production checklist = cel końca S2. Nie wgrywaj kodu PoC jako fundamentu demo bez rewrite.

## Powiązane koncepty

- Lekcja: [[1.1-ideation-fr-nfr]]
- Szablony: [[spec-fr-nfr-template]], [[latency-budget-template]]
- Przykład: [[worked-example-student-project]]
- Roadmapa: [[web-engineering-roadmap]]
- Lab: `labs/web-engineering/1.1/`

## Źródła

- Lekcja Masterclass 1.1 (Vaultie)
- [Google SRE Book — SLOs](https://sre.google/sre-book/service-level-objectives/)
- [roadmap.sh/full-stack](https://roadmap.sh/full-stack)
