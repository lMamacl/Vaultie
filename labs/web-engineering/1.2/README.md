# Lab 1.2 — WBS, Metodyki i RACI w Zespole Inżynieryjnym

> **Zadanie:** Na podstawie specyfikacji FR/NFR z Lekcji 1.1 przeprowadź dekompozycję projektu na drzewo WBS, utwórz konfigurację tablicy Kanban w YAML, skonfiguruj macierz odpowiedzialności RACI w CSV oraz uzasadnij wybór metodyki i obronę przed zjawiskami grupowymi.

---

## 📂 Struktura Plików Labu

| Plik | Rola / Opis |
|---|---|
| `wbs-template.md` | Szablon dekompozycji WBS z estymacjami i Mnożnikami Ryzyka (Risk Multipliers) oraz ścieżką krytyczną. |
| `board.yaml` | Konfiguracja tablicy projektowej (Kanban / Shape Up) z limitem WIP, kolumnami oraz etykietami. |
| `raci.csv` | Tabela macierzy RACI (Responsible, Accountable, Consulted, Informed) dla zespołu 3–5 osób. |
| `README.md` | Niniejsza instrukcja labu i lista kryteriów odbioru (Definition of Done). |

---

## 🎯 Kryteria Odbioru (Definition of Done)

Aby zaliczyć Lab 1.2, Twój artefakt w folderze labu musi spełniać poniższe wymogi:

- [ ] **WBS (w `wbs-template.md`):** Min. 3 produkty końcowe (deliverables) rozbite na pakiety pracy (work packages) i atomowe zadania (≤ 16 godzin / 1–2 dni).
- [ ] **Estymacja i Mnożnik Ryzyka (Risk Multiplier):** Przypisanie Mnożnika Ryzyka (`×1.2` znany stack, `×1.5` nowa baza/architektura, `×2.0` customowe/zewnętrzne API) do każdego zadania oraz wyliczenie estymacji skorygowanej.
- [ ] **Ścieżka Krytyczna & Dług Techniczny:** Wyznaczenie zadań na ścieżce krytycznej (Critical Path) oraz alokacja bufora na dług techniczny (min. 15% budżetu czasu).
- [ ] **Tablica Kanban (w `board.yaml`):** Poprawny składniowo plik YAML definiujący kolumny przepływu, twarde limity WIP (np. 2 zadania na osobę w `in_progress`) oraz taksonomię tagów (`kind/*`, `area/*`, `effort/*`).
- [ ] **Macierz RACI (w `raci.csv`):** Plik CSV pokrywający min. 5 głównych modułów/zadań i min. 3–4 role. Zgodność z regułą **Accountability Singularity** (dokładnie **jeden** `A` w każdym wierszu).
- [ ] **Uzasadnienie Metodyki i Psychologia Zespołu:** Wybór metodyki (Kanban / Shape Up / Scrum) poparty analizą dostępności czasowej oraz wdrożenie mechanizmu obrony przed *Groupthink* (*Egoless Programming* / *Adwokat Diabła*).

---

## 💡 Jak Uruchomić i Weryfikować?

1. Wypełnij plik `wbs-template.md` danymi swojego projektu studenckiego/inżynieryjnego.
2. Dostosuj pliki `board.yaml` oraz `raci.csv`.
3. Uruchom skrypt certyfikujący vaulta:
   ```bash
   python .agent/scripts/vaultie-certify.py 1.2
   ```
