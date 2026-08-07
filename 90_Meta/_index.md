---
type: moc
title: "Vaultie — Główna Mapa Treści i Punkt Wejścia"
created: 2026-08-06
updated: 2026-08-07
tags: [moc, index, meta]
up: ""
---

# Vaultie — Inżynieryjna Baza Wiedzy

> Wersja: v1.1.0 | Status: Produkcyjny | Ostatnia pełna kompilacja: 2026-08-07

---

## 🗺️ Mapa Treści (MOC)

| Warstwa / Katalog | Przeznaczenie | Notatek | Punkt wejścia |
|---|---|---|---|
| `10_Libraries/` | Analizy bibliotek i narzędzi (verdict, gotchas) | 3 | [[Libraries MOC]] |
| `20_Patterns/` | Wzorce projektowe i architektoniczne | 2 | [[Patterns MOC]] |
| `30_Decisions/` | Decyzje architektoniczne (ADR) | 2 | [[Decisions MOC]] |
| `40_Snippets/` | Sprawdzony, przetestowany kod (verified) | 1 | [[Snippets MOC]] |
| `50_Concepts/` | Teoria, edukacja i pojęcia domenowe | 2 | [[Concepts MOC]] |
| `labs/` | Sandbox ćwiczeń masterclass | — | `labs/web-engineering/` |
| `00_Inbox/` | Surowiec, klipy, propozycje draftów | — | `00_Inbox/` |
| `99_Archive/` | Zarchiwizowane notatki | 0 | `99_Archive/` |

---

## ⚡ Szybki Start & Przepływy Wyszukiwania

- Gotowe zapytania przekrojowe: **[[queries]]**
- Slownik i pojęcia: **[[glossary]]**
- Historia zmian i wersji bazy: **[[changelog]]**
- Raporty i audyty: **[[.agent/health-dashboard|Health Dashboard]]**

---

## 🎯 Ostatnie Decyzje (ADR)

- [[2026-08-06-diagramming-engine-react-flow-vs-jointjs]] — Wybór silnika dla edytora diagramów UML na nieskończonym polu (`accepted`)
- [[2026-08-06-state-management-tanstack-query]] — Wybór TanStack Query v5 jako standardu dla stanu serwerowego (`accepted`)

---

## 📌 Wybrane Notatki Produkcyjne

- **Biblioteki:** [[react-flow]], [[jointjs]], [[tanstack-query]]
- **Wzorce:** [[infinite-canvas-architecture]], [[optimistic-ui-updates]]
- **Snippety:** [[use-tanstack-query-optimistic]]
- **Koncepcje:** [[project-initiation-fr-nfr]], [[optimistic-updates]]
- **Masterclass:** [[web-engineering-roadmap]] · Lekcja [[1.1-ideation-fr-nfr]] · Lab `labs/web-engineering/1.1/`
