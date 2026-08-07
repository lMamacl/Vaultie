---
type: meta
title: "Szablon Latency Budget (Lekcja 1.1)"
created: 2026-08-07
updated: 2026-08-07
tags: [template, lesson, performance, latency, nfr]
up: "[[1.1-ideation-fr-nfr]]"
---

# Latency Budget — budżet latencji per endpoint

> **Instrukcja:** Dla każdego endpointu z NFR-PERF wypełnij tabelę. **Suma warstw ≤ cel p95 z NFR.**  
> Jeśli suma przekracza cel — zmieniasz architekturę (cache, indeks, SSR), nie „liczysz na szczęście”.

---

## Endpoint: `GET /api/_______________`

| Pole | Wartość |
|---|---|
| **Powiązane FR** | FR-___ |
| **Powiązane NFR** | NFR-PERF-___ |
| **Cel p95** | ___ ms |
| **Szacowane RPS (demo)** | ___ |

### Rozkład budżetu (ms)

| # | Warstwa | Budżet (ms) | Opis / co tu się dzieje | Jak zmierzyć |
|---|---|---|---|---|
| 1 | DNS + TCP/TLS (client → edge) | | Pierwsze połączenie vs keep-alive | DevTools Network |
| 2 | CDN / reverse proxy | | Nginx, Cloudflare, Vercel edge | `X-Response-Time` header |
| 3 | Auth / middleware | | JWT verify, session lookup | log `auth_ms` |
| 4 | Handler / use case | | logika biznesowa bez I/O | log `handler_ms` |
| 5 | ORM + SQL | | query + mapowanie | log `db_ms`, EXPLAIN |
| 6 | Cache read (jeśli jest) | | Redis hit | log `cache_ms` |
| 7 | Serializacja JSON | | stringify response | log `serialize_ms` |
| 8 | **Margines (GC, kolejka)** | | 15–20% buforu | p99 − p95 |
| | **SUMA** | | **≤ cel p95** | |

### Werdykt

- [ ] Suma ≤ cel p95 — **OK na papierze** (weryfikacja w lekcji 7.2)
- [ ] Suma > cel — **wymaga zmiany:** <!-- indeks / cache / mniejszy payload / pagination -->

### Notatki po pomiarze (wypełnij później)

| Data | p50 | p95 | p99 | Narzędzie | Uwagi |
|---|---|---|---|---|---|
| | | | | k6 / logs | |

---

## Endpoint: `POST /api/_______________`

| Pole | Wartość |
|---|---|
| **Cel p95** | ___ ms |
| **Uwaga** | POST często wolniejsze (walidacja + zapis + side effects) |

| # | Warstwa | Budżet (ms) | Opis |
|---|---|---|---|
| 1 | Sieć | | |
| 2 | Auth | | |
| 3 | Walidacja (Zod/class-validator) | | |
| 4 | Transakcja DB | | |
| 5 | Side effects (email, event) | | async vs sync? |
| 6 | Response | | |
| 7 | Margines | | |
| | **SUMA** | | |

---

## Mapowanie budżetu → decyzje architektoniczne

| Jeśli przekroczony budżet w warstwie… | Rozważ (lekcja) |
|---|---|
| SQL / ORM | Indeks, query rewrite (4.1), pagination |
| Auth | Cache session, krótszy JWT path (3.3) |
| Serializacja | Mniejszy DTO, compression |
| Sieć / TTFB | SSR vs SSG (2.1), CDN (7.2) |
| Handler | Przenieś CPU do job queue (późniejsze) |

---

## Przykład wypełniony (reference)

**Endpoint:** `GET /api/orders` · **Cel p95:** 300 ms

| Warstwa | Budżet |
|---|---|
| Sieć | 30 |
| Auth | 40 |
| Handler | 30 |
| SQL | 120 |
| JSON | 20 |
| Margines | 60 |
| **SUMA** | **300** |

---

*Użyj razem z [[spec-fr-nfr-template]] i lekcją [[1.1-ideation-fr-nfr#7. Pod maską]]*
