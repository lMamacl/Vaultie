---
name: kb-lesson-certify
description: "Runs the available static quality gates for a Vaultie masterclass lesson and reports whether human review or teach-back remains."
---

# kb-lesson-certify — Faza A Quality Gate (przed Blackbox)

## Cel
Certyfikacja lekcji masterclass według [[lesson-quality-contract-v1]] **zanim** właściciel odpali `kb-blackbox` (Faza B). Pipeline: Knowledge Spec → static gates → Student-sim teach-back → Judge → `certified` | `needs-human`.

## Kiedy użyć
- Wywołanie: „uruchom kb-lesson-certify dla \<ID\>” (np. `1.1`, `1.2`).
- Przed draftem / po drafcie lekcji w `90_Meta/lessons/`, zawsze przed zalecanym Blackboxem.
- Przy re-certify po zmianie kontraktu lub treści lekcji.

## Relacja do kb-blackbox

| Skill | Faza | Bramka |
|---|---|---|
| `kb-lesson-certify` | A | Spec + static + teach-back |
| `kb-blackbox` | B | Quiz właściciela ≥3/4 → promote `10_`–`50_` |

Bez `certified` (lub jawnej akceptacji `needs-human` przez właściciela) — **ostrzeż** przed Blackboxem, nie blokuj na siłę.

## Kroki

1. **Wczytaj kontekst**
   - Sprawozdanie ID z `90_Meta/web-engineering-roadmap.md`
   - Kontrakt: `90_Meta/lesson-quality-contract-v1.md`
   - Lekcja (jeśli istnieje): `90_Meta/lessons/<id>-*.md` lub ścieżka podana przez użytkownika
   - Spec: `90_Meta/lessons/<id>/spec.yaml`

2. **Knowledge Spec (twarda brama człowieka)**
   - Jeśli brak Spec: zbuduj draft YAML z pól roadmapy (cele, źródła, quiz → critical competencies, ladder wg typu lekcji).
   - Jeśli Spec istnieje: wczytaj i wypisz skrót (LO, critical, misconceptions, ladder).
   - **Zatrzymaj się** i poproś właściciela o akceptację Spec (`akceptuję Spec` / lista poprawek).
   - Nie przechodź do Writer/static bez akceptacji (chyba że właściciel w tym samym komunikacie już zaakceptował, np. re-certify znanego Spec).

3. **Draft lekcji**
   - Jeśli brak pliku lekcji: wskaż, że Writer/Blackbox-draft to osobny krok (nowa instancja czata ze źródeł Spec + roadmapy). Nie mieszaj Writer+Judge w jednej roli bez briefu.
   - Jeśli lekcja istnieje: przejdź do static.

4. **Static validator** (deterministycznie / checklist)
   - Frontmatter: `lesson_id`, `up`, `diataxis`, `certification_status`, `spec_path`
   - Sekcje MUST z kontraktu (cel, model mentalny, worked example, misconceptions, generatywne, chain-of-action jako tabela, lab/DoD, transfer, retrieval/quiz, kiedy NIE lub trade-off, źródła)
   - Puste H2 = fail
   - Lab path zgodny ze Spec; `exec: true` → uruchom lub jawny skip z powodem
   - AI-filler heurystyka (lista z kontraktu §4.3)
   - Wikilinki krytyczne (prereq / lab) — zgłoś martwe

5. **Student-sim (teach-back)**
   - Preferencyjnie **osobny kontekst / inna rodzina modelu** niż Writer.
   - Student dostaje **tylko** treść lekcji (bez Spec).
   - Produkuje: (a) wyjaśnienie modelu mentalnego własnymi słowami, (b) odpowiedzi na critical competencies / assessment_ladder, (c) listę luk/niejasności.
   - **Nie** wystawia PASS/FAIL.

6. **Judge**
   - Preferencyjnie inna rodzina modelu niż Writer.
   - Porównuje artefakty Studenta ze Spec; rubryka **0/1** per critical competency + transfer + major misconception.
   - PASS wymaga: ≥90% competencies **oraz** 100% critical **oraz** transfer pass **oraz** zero major misconception **oraz** static pass.
   - FAIL zapisuj jako: `WHERE` / `WHAT` / `HOW_DETECTED` / `FIX` (konkretna sekcja lekcji).

7. **Repair loop**
   - `max_iterations: 3`
   - Przy FAIL i iteration < 3: zapisz patch (lista FIX) → popraw **tylko** wskazane sekcje lekcji → wróć do static.
   - Przy FAIL i iteration == 3: `certification_status: needs-human`, pełna historia w raporcie.

8. **Wynik PASS**
   - Ustaw we frontmatterze lekcji `certification_status: certified` (lub pozostaw `screened` jeśli właściciel już zaliczył Blackbox i tylko re-certify — wtedy zapytaj).
   - Zapisz `90_Meta/lessons/<id>/quality-report.yaml`
   - Przypomnij: „uruchom kb-blackbox dla \<ID\>” (jeśli jeszcze nie `screened`).

## Input
- ID lekcji (wymagane), np. `1.1`
- Opcjonalnie: ścieżka draftu, `--skip-spec-gate` tylko gdy właściciel wprost potwierdził Spec w tej sesji
- Opcjonalnie: `--static-only` (bez Student-sim; status nie może być `certified` — max `draft` z notatką)

## Output
- Zaakceptowany / zaktualizowany `spec.yaml`
- `quality-report.yaml`
- Zaktualizowany `certification_status` w lekcji
- Werdykt + lista FIX albo przypomnienie Blackbox

## Guardrails
- Orkiestracja **skill-driven**: pętla ≤3 wewnątrz jednego wywołania; **brak** auto-start kolejnego ID.
- Writer nie ocenia siebie; Student nie wystawia sobie zaliczenia.
- Nie zapisuje do `10_`–`50_` (to Blackbox + akceptacja właściciela).
- Nie edytuje innych skilli w `.agent/` poza utrzymaniem tego pliku.
- Kod: nie uznawaj poprawności „na oko” — exec lub jawny skip.
- Język raportów: konkret, bez AI-filler.

## Warianty
- Standard: pełny pipeline po akceptacji Spec.
- `--retake`: po `needs-human` / fail — tylko lista FIX + jedna iteracja naprawy.
- `--static-only`: checklista strukturalna bez teach-back (nie daje `certified`).

## Schemat quality-report.yaml (minimalny)

```yaml
lesson_id: "1.1"
iteration: 1
max_iterations: 3
gates:
  structure: pass|fail
  pedagogy: pass|fail
  technical: pass|fail
  language: pass|fail
  teachback: pass|fail|skipped
failures: []
verdict: certified|needs-human|static-fail|teachback-fail
writer_model_family: "…"
judge_model_family: "…"
notes: ""
```
