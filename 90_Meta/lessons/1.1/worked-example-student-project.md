---
type: meta
title: "Przykład kompletny — VaultCollab (Lekcja 1.1)"
created: 2026-08-07
updated: 2026-08-07
tags: [lesson, example, fr, nfr, student-project]
up: "[[1.1-ideation-fr-nfr]]"
---

# Worked Example: VaultCollab

> **Fikcyjny projekt uczelniany** ilustrujący pełny łańcuch: Problem → FR → NFR → PoC/MVP → Latency budget.  
> **Nie kopiuj 1:1** — użyj jako wzorca struktury i głębokości.

---

## 1. Problem Statement

**Użytkownik:** Zespół 4 studentów realizujących 2-semestralny projekt inżynierski (web app).

**Kontekst:** Praca rozproszona (hybrid), promotor wymaga dokumentacji architektury i działającego demo online.

**Ból:** Decyzje giną w Discordzie; README nieaktualne; przed demo ręczny deploy „u Kuby na laptopie”; promotor nie widzi ADR.

**Obecne obejście:** Notion + Discord + ręczne skrypty deploy.

**Sukces:** Promotor otwiera publiczny URL, widzi listę zadań i ADR w repo; zespół ma jeden source of truth; deploy z `main` automatyczny.

---

## 2. Interesariusze

| Interesariusz | Wpływ |
|---|---|
| Student (członek zespołu) | FR: zadania, ADR, status |
| Promotor | FR: read-only widok postępu; NFR: docs, stabilne demo |
| Zespół dev | NFR: maintainability, CI |

---

## 3. Functional Requirements (skrót)

### MUST (MVP S1)

| ID | FR | Akceptacja (skrót) |
|---|---|---|
| FR-001 | Rejestracja / logowanie email+hasło | Dashboard po login; błąd bez ujawniania istnienia konta |
| FR-002 | CRUD projektów zespołowych | Owner + członkowie; max 1 owner |
| FR-003 | CRUD zadań w projekcie | Status: todo / doing / done |
| FR-004 | ADR jako Markdown w repo | Render w UI; link do pliku w Git |
| FR-005 | Publiczny link read-only dla promotora | Token URL bez logowania promotora |

### SHOULD (S2)

| ID | FR |
|---|---|
| FR-010 | Komentarze przy zadaniu |
| FR-011 | Powiadomienie email przy przypisaniu |

### WON'T

- Natywna apka iOS/Android  
- Płatności / subskrypcje  
- Realtime chat (tylko komentarze async w S2)

---

## 4. Non-Functional Requirements (skrót)

| ID | NFR | Cel |
|---|---|---|
| NFR-PERF-001 | GET /api/projects p95 | ≤ 250 ms @ 20 RPS |
| NFR-PERF-002 | LCP strony dashboard | ≤ 2.5 s (3G Fast) |
| NFR-SEC-001 | Hasła | Argon2id, cost skonfigurowany |
| NFR-SEC-002 | Transport | HTTPS only prod |
| NFR-SEC-003 | Autoryzacja | Użytkownik widzi tylko projekty, do których należy |
| NFR-MAINT-001 | CI | Lint + test na każdy PR |
| NFR-OPS-001 | Backup DB | Codzienny dump przed obroną S2 |

---

## 5. Macierz FR ↔ NFR (fragment)

| FR | NFR | Dlaczego |
|---|---|---|
| FR-001 | NFR-SEC-001 | Rejestracja = przechowywanie hasła |
| FR-005 | NFR-SEC-003 | Token read-only nie może ujawniać mutacji |
| FR-002 | NFR-PERF-001 | Lista projektów = pierwszy ekran po login |

---

## 6. PoC / MVP / Production

### PoC?

**Nie.** Stack znany: TypeScript + NestJS + PostgreSQL + React. Brak ryzykownego algorytmu.

### MVP (koniec S1 — tydzień 15)

- FR-001 … FR-005 MUST  
- NFR: SEC-001, SEC-002, SEC-003 (baseline), PERF-001 (pomiar ręczny), MAINT-001 (CI podstawowe)  
- Demo: promotor otwiera magic link → widzi projekt + 1 ADR

### Production-Ready (koniec S2)

- + FR-010, FR-011  
- + NFR-OPS-001 backup, rate limit login (lekcja 5.2), OTel basic (7.2)  
- OWASP checklist (5.1) w DoD

---

## 7. Feasibility (S1)

```
Zespół: 4 osoby × 15 tyg × 3 dni × 3h × 0.7 ≈ 378 h ≈ 47 osobodni

FR MUST (5 epików) × ~6 osobodni = 30 osobodni
Bufor + NFR/CI ≈ 10 osobodni
Zostaje ~7 osobodni na bugfix/demo → OK
```

**Ryzyko:** jedna osoba zna tylko Angular — **mitygacja:** ADR 2.4 wybór React+TS dla spójności.

---

## 8. Latency budget — `GET /api/projects`

**Cel NFR-PERF-001:** p95 ≤ 250 ms

| Warstwa | ms |
|---|---|
| Sieć (demo LAN/cloud) | 25 |
| JWT verify middleware | 35 |
| Use case (mapowanie) | 25 |
| SQL + indeks `owner_id` | 90 |
| JSON | 15 |
| Margines | 60 |
| **SUMA** | **250** |

**Decyzja architektoniczna wynikająca z budżetu:** pagination max 50 projektów; indeks na `(member_id)` — inaczej SQL przekroczy 90 ms (→ lekcja 4.1).

---

## 9. Jak ten przykład łączy się z kanwą

Na [[lesson-1.1-ideation-fr-nfr.canvas]] każdy węzeł w strefie FR/NFR możesz zastąpić treścią z tego przykładu i porównać ze swoim projektem side-by-side.

---

*Reference only — VaultCollab nie istnieje jako repo; służy nauce 1.1*
