---
type: meta
title: "Szablon spec-fr-nfr (Lekcja 1.1)"
created: 2026-08-07
updated: 2026-08-07
tags: [fr, lesson, nfr, spec, template]
up: "[[1.1-ideation-fr-nfr]]"
---

# Specyfikacja projektu — FR / NFR

> **Instrukcja:** Wypełnij sekcje po kolei. Usuń komentarze `<!-- ... -->` po ukończeniu.
> **Wersja dokumentu:** 0.1.0
> **Data:** YYYY-MM-DD
> **Zespół:** [imiona, role]

---

## 1. Metadane projektu

| Pole | Wartość |
|---|---|
| **Nazwa robocza** | |
| **Typ** | Web app / Website / Desktop + web backend |
| **Horyzont** | 2 semestry (S1 MVP / S2 Production) |
| **Stack (propozycja — ADR w 2.4)** | Backend: TS / Java / C# · Frontend: React / Angular · DB: Postgres / SQLite |

---

## 2. Problem Statement

**Użytkownik:**
<!-- np. student 3 roku, zespół 4 osób -->

**Kontekst:**
<!-- np. projekt inżynierski, brak centralnego miejsca na decyzje -->

**Problem:**
<!-- co jest frustrujące dziś -->

**Obecne obejście:**
<!-- Discord, Notion, Excel — konkurencja -->

**Sukces wygląda tak:**
<!-- mierzalny efekt końcowy -->

---

## 3. Interesariusze

| Interesariusz | Rola | Wpływ na wymagania |
|---|---|---|
| | Użytkownik | |
| | Promotor | |
| | Zespół dev | |

---

## 4. Functional Requirements (FR)

### FR — MUST (MVP Semestr 1)

#### FR-001: [Tytuł]

- **Opis:**
- **Kryterium akceptacji:**
  1.
  2.
- **Interesariusz:**

#### FR-002: [Tytuł]

- **Opis:**
- **Kryterium akceptacji:**
  1.
- **Interesariusz:**

<!-- Dodaj FR-003 … FR-00N -->

### FR — SHOULD (Semestr 1 koniec / Semestr 2)

#### FR-0XX: [Tytuł]

- **Opis:**
- **Kryterium akceptacji:**

### FR — COULD (jeśli zostanie czas)

#### FR-0XX: [Tytuł]

### WON'T (świadomie poza scope)

- 
- 

---

## 5. Out of Scope (MVP)

<!-- Lista rzeczy, których NIE robimy w S1 — chroni przed scope creep -->

- 
- 

---

## 6. Non-Functional Requirements (NFR)

### NFR-PERF (Wydajność)

#### NFR-PERF-001: [Tytuł]

- **Metryka:**
- **Cel:** p95 ≤ ___ ms / LCP ≤ ___ s
- **Warunki pomiaru:** ___ użytkowników, ___ RPS
- **Powiązane FR:** FR-___
- **Sposób pomiaru:** <!-- middleware, k6, Lighthouse -->

### NFR-SEC (Bezpieczeństwo)

#### NFR-SEC-001: [Tytuł]

- **Wymaganie:** <!-- np. Argon2id, HTTPS only -->
- **Powiązane FR:**

### NFR-OPS (Operacyjność)

#### NFR-OPS-001: [Tytuł]

- **Wymaganie:** <!-- backup, deploy, healthcheck -->

### NFR-MAINT (Utrzymywalność)

#### NFR-MAINT-001: [Tytuł]

- **Wymaganie:** <!-- CI, ADR, docs w repo -->

### NFR-A11Y (Dostępność — SHOULD S2)

#### NFR-A11Y-001: [Tytuł]

---

## 7. Macierz traceability FR ↔ NFR

| FR ID | NFR ID | Uzasadnienie powiązania |
|---|---|---|
| FR-001 | NFR-SEC-001 | |
| FR-002 | NFR-PERF-001 | |

---

## 8. Decyzja PoC / MVP / Production

### Czy potrzebujemy PoC?

- [ ] **Tak** — ryzyko techniczne: <!-- opisz -->
- [ ] **Nie** — stack i integracje znane

### Definicja MVP (koniec Semestru 1)

**FR MUST w MVP:** FR-001, FR-002, …
**NFR w MVP (minimum):**
**Demo dla promotora (happy path):**
<!-- 1 akapit: co kliknę na obronie S1 -->

### Definicja Production-Ready (koniec Semestru 2)

**Dodatkowe FR:**
**Dodatkowe NFR:**
**Checklist:** CI green, backup DB, OWASP baseline, docs ADR

---

## 9. Feasibility

| Filtr | Ocena (OK / Ryzyko / Bloker) | Komentarz |
|---|---|---|
| Techniczna (stack, integracje) | | |
| Czasowa (FR MUST vs osobodni) | | |
| Organizacyjna (promotor, wymogi uczelni) | | |

**Szacunek osobodni S1:** ___ / dostępne ___
**Bufor 20%:** ___

---

## 10. Ryzyka (top 3)

| Ryzyko | Prawdop. | Wpływ | Mitygacja |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## 11. Latency budget (skrót)

Szczegóły: [[latency-budget-template]]

| Endpoint | NFR cel p95 | Suma budżetu | Status |
|---|---|---|---|
| GET /api/... | ms | ms | OK / OVER |

---

## 12. Zatwierdzenie zespołu

| Rola | Imię | Data | Podpis (GitHub issue/PR) |
|---|---|---|---|
| Accountable (1 osoba) | | | |
| Responsible dev | | | |

---

*Szablon lekcji 1.1 — skopiuj do repo projektu jako `docs/spec-fr-nfr.md`*
