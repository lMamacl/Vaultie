# Szablon Dekompozycji WBS i Estymacji Effortu (Lab 1.2)

**Projekt:** VaultCollab / [Nazwa Twojego Projektu]  
**Wersja:** 1.0.0  
**Data:** 2026-08-11  

---

## 1. Drzewo Dekompozycji WBS (Work Breakdown Structure)

```text
1.0 System VaultCollab
│
├── 1.1 Moduł Autentykacji i Sesji (Deliverable 1)
│   ├── 1.1.1 Config & Schema Auth (Work Package)
│   │   ├── 1.1.1.1 Schema tabeli users i ról w Supabase (Task, 4h, Risk ×1.2 = 4.8h) [Critical Path]
│   │   └── 1.1.1.2 Konfiguracja RLS (Row Level Security) (Task, 6h, Risk ×1.5 = 9.0h) [Critical Path]
│   └── 1.1.2 Auth Endpoints & Handlers (Work Package)
│       ├── 1.1.2.1 Endpoint POST /api/auth/register (Task, 6h, Risk ×1.2 = 7.2h)
│       └── 1.1.2.2 Endpoint POST /api/auth/login + JWT Refresh (Task, 8h, Risk ×1.2 = 9.6h)
│
├── 1.2 Moduł Canvas Editor (Deliverable 2)
│   ├── 1.2.1 Wyświetlanie Nieskończonej Siatki (Work Package)
│   │   ├── 1.2.1.1 Integracja React Flow Viewport (Task, 8h, Risk ×1.2 = 9.6h)
│   │   └── 1.2.1.2 Wirtualizacja obiektów na canvasie (Task, 12h, Risk ×1.5 = 18.0h)
│   └── 1.2.2 Zapis Stanu i Synchroniczne Konflikty (Work Package)
│       └── 1.2.2.1 Optimistic Updates dla węzłów canvasa (Task, 14h, Risk ×2.0 = 28.0h) [Critical Path]
│
└── 1.3 Infrastruktura i Jakość (Deliverable 3)
    ├── 1.3.1 Pipeline CI/CD (Work Package)
    │   └── 1.3.1.1 Konfiguracja GitHub Actions z linterem i buildem (Task, 6h, Risk ×1.2 = 7.2h)
    └── 1.3.2 Dług Techniczny i Refaktoryzacja (Work Package)
        └── 1.3.2.1 Alokacja bufora długu technicznego (Task, 16h, Risk ×1.0 = 16.0h)
```

---

## 2. Tabela Estymacji z Mnożnikami Ryzyka (Risk Multipliers)

| ID Zadania | Nazwa Zadania | Szacunek Bazowy (h) | Mnożnik Ryzyka (×) | Uzasadnienie Mnożnika | Skorygowany Effort (h) | Ścieżka Krytyczna? |
|---|---|---|---|---|---|---|
| `1.1.1.1` | Schema users i ról | 4.0 | ×1.2 | Standardowy PostgreSQL w Supabase | 4.8 h | **TAK** |
| `1.1.1.2` | Konfiguracja polityk RLS | 6.0 | ×1.5 | Wymaga znajomości reguł Supabase RLS | 9.0 h | **TAK** |
| `1.1.2.1` | Endpoint POST /api/auth/register | 6.0 | ×1.2 | Znany wzorzec FastAPI / Pydantic | 7.2 h | NIE |
| `1.1.2.2` | Endpoint POST /api/auth/login | 8.0 | ×1.2 | Standardowy token JWT | 9.6 h | NIE |
| `1.2.1.1` | React Flow Viewport Integration | 8.0 | ×1.2 | Gotowa biblioteka react-flow | 9.6 h | NIE |
| `1.2.1.2` | Wirtualizacja obiektów canvas | 12.0 | ×1.5 | Wymaga optymalizacji renderowania 60fps | 18.0 h | NIE |
| `1.2.2.1` | Optimistic Updates nodów | 14.0 | ×2.0 | Złożony stan serwerowy, customowy rollback | 28.0 h | **TAK** |
| `1.3.1.1` | GitHub Actions CI/CD Pipeline | 6.0 | ×1.2 | Standardowe skrypty yaml | 7.2 h | NIE |
| `1.3.2.1` | Bufor na Dług Techniczny (20%) | 16.0 | ×1.0 | Rezerwa czasowa na refaktoryzację | 16.0 h | NIE |
| **SUMA** | | **78.0 h** | — | — | **109.4 h** | — |

---

## 3. Ścieżka Krytyczna (Critical Path) i Wyznaczanie Długu Technicznego

1. **Ścieżka Krytyczna:** `1.1.1.1` (4.8h) → `1.1.1.2` (9.0h) → `1.2.2.1` (28.0h).  
   *Łączny czas ścieżki krytycznej:* **41.8 h**. Opóźnienie któregokolwiek z tych zadań bezpośrednio opóźnia termin oddania MVP.
2. **Budżet Długu Technicznego:** Zgodnie z zasadą 15–20% czasu pracy zespołu, wydzielono 16h w zadaniu `1.3.2.1` przeznaczone wyłącznie na refaktoryzację kodu, automatyzację testów oraz poprawianie zidentyfikowanego długu.

---

## 4. Wybór Metodyki i Psychologia Zespołu

- **Wybrana Metodyka:** **Kanban z twardym limitowaniem WIP (Max 1 zadanie/osobę w `in_progress`).**  
  *Uzasadnienie:* Zespół studencki pracuje w nieregularnych godzinach (zajęcia, praca). Usztywnione 2-tygodniowe sprinty Scruma prowadziłyby do "teatru statusów". Kanban umożliwia ciągły przepływ (continuous flow) i wymusza kończenie rozpoczętych zadań przed pobraniem nowych.
- **Obrona przed Groupthink (Egoless Programming & Adwokat Diabła):**  
  Do każdego Code Review wyznaczana jest osoba pełniąca rolę *Adwokata Diabła*, której zadaniem jest znalezienie min. 2 potencjalnych punktów awarii lub ograniczeń wydajnościowych w propozycji architektonicznej. Kod jest własnością całego zespołu (*Egoless Programming*), a krytyka dotyczy wyłącznie rozwiązań technicznych, nie osób.
