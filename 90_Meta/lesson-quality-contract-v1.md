---
type: moc
title: "Lesson Quality Contract v1 — bramki jakości lekcji AI"
created: 2026-08-10
updated: 2026-08-10
tags: [moc, lesson, quality-gate, blackbox, pedagogy, masterclass]
up: "[[web-engineering-roadmap]]"
status: active
version: "1.0.0"
---

# Lesson Quality Contract v1

> **Cel:** zanim lekcja trafi do screeningu człowieka / Blackbox quizu właściciela, musi przejść Formalny Quality Gate.  
> **Zasada nadrzędna:** lekcja jest dobra wtedy, gdy niezależny uczeń potrafi z niej wykonać poprawne działanie bez pomocy autora — nie wtedy, gdy tekst „wygląda poprawnie”.  
> **Zakres:** masterclass w [[web-engineering-roadmap]] + ogólne lekcje programowania w vaultcie.  
> **Powiązania:** [[1.1-lesson-quality-audit]], propozycja `kb-lesson-certify`, skill [[kb-blackbox]].

---

## 1. Synteza trzech analiz (GPT / Grok / Claude)

| Źródło | Brać | Odrzucić / odłożyć |
|---|---|---|
| **GPT 5.6 SOL** | Knowledge Spec ≠ prose; bramki bez średniej; drabina ćwiczeń; code execution jako prawda; Learning Atoms; curriculum compiler | Full V3–V4 multi-agent na start; Canvas jako DB |
| **Grok 4.5** | MUST/SHOULD; Creator production rules; statusy Obsidian; pętla Learner | „OPTEQ” jako nazwany standard (niesprawdzalne); same wymiary eval są OK |
| **Claude Sonnet** | ICAP/PRIMM/notional machine/Diátaxis; teach-back + osobny Judge; deletion test; PL stylometria bez EN progów; Reflexion ≤N | Samodzielny self-grade; angielskie progi burstiness „z półki” |

**Wspólny werdykt:** AI Curriculum Compiler + Learning Verification, nie „AI Course Generator”.

### Uzasadnienie badawcze (skrót)

| Idea | Źródło |
|---|---|
| Backward design: cele → assessment → treść | [Carpentries Lesson Design](https://carpentries.github.io/lesson-development-training/lesson-design.html) |
| Epizody 20–60 min, 2–4 LO | Carpentries Episodes |
| PRIMM | Sentance & Waite 2017 |
| Worked examples + self-explanation → transfer | ACM TOCE (m.in. 10.1145/3732791, review 10.1145/3560266) |
| Notional machine | Sorva, ACM TOCE 2013 |
| Diátaxis (nie mieszać trybów) | [docs.divio.com/documentation-system](https://docs.divio.com/documentation-system/) |
| LLM łapie formę wzorca; potrzebny oversight | Sarsa, Denny, Hellas, Leinonen — ICER 2022 |
| Curriculum map (opcjonalnie) | [CS2023](https://csed.acm.org/) |
| LLM-as-judge biases | Zheng et al., MT-Bench 2023 |
| Repair z werbalną refleksją | Reflexion / Self-Refine |

---

## 2. Warstwy artefaktów (Vaultie)

```text
Roadmapa (Course Graph)
        ↓
Knowledge Spec  (YAML — nie dla ucznia)
        ↓
Lesson Markdown + Lab + Canvas
        ↓
Quality Gate (static → student-sim → judge)
        ↓
status: certified
        ↓
Human Blackbox quiz  (kb-blackbox)
        ↓
Promote 10_–50_  (za akceptacją)
```

| Warstwa | Ścieżka | Rola |
|---|---|---|
| Curriculum | `90_Meta/web-engineering-roadmap.md` | Co / kiedy / źródła / quiz właściciela |
| Knowledge Spec | `90_Meta/lessons/<id>/spec.yaml` | Kompletność wiedzy i testów |
| Lekcja | `90_Meta/lessons/<id>-….md` | Artefakt dydaktyczny |
| Lab | `labs/web-engineering/<id>/` | Dowód proceduralny |
| Canvas | `90_Meta/canvases/…` | Nawigacja / mapa — **nie** SoT |
| Cert report | `90_Meta/lessons/<id>/quality-report.yaml` | Wynik bramki |

**Markdown = źródło prawdy treści. Canvas = widok.**

---

## 3. Knowledge Spec (schemat v1)

Plik: `90_Meta/lessons/<lesson_id>/spec.yaml`

```yaml
id: "1.1"                         # ID z roadmapy
title: "Ideation, Feasibility & Scope (FR / NFR)"
diataxis: tutorial                # tutorial | how-to | reference | explanation
audience: "student 2-semestralny / junior engineer"
level: novice                     # novice | intermediate | advanced
threshold_concept: false

prerequisites: []                 # lista ID lub [[wikilinki]]

learning_objectives:              # czasowniki działania, mierzalne
  - "odróżnić FR od NFR i zapisać oba w formacie z kryterium akceptacji / metryką"
  - "zdecydować PoC vs MVP vs Production dla własnego scope"
  - "wypełnić latency budget dla 2 endpointów powiązanych z NFR-PERF"

critical_competencies:            # 100% wymagane do PASS teach-back
  - fr_vs_nfr
  - poc_not_production
  - p95_latency_budget
  - mvp_nfr_tradeoff_security_baseline

mental_models:
  - id: requirements_split
    claim: "FR = co system robi; NFR = jak dobrze; technologia ≠ FR"
  - id: horizon_maturity
    claim: "PoC waliduje ryzyko; MVP wartość; Production przeżywalność"

misconceptions:
  - "NFR to walidacja pola formularza"
  - "PoC można wypchnąć na demo jako gotowy produkt"
  - "średnia latencji wystarczy zamiast percentyli"

decision_points:
  - "Czy potrzebujemy PoC przed MVP?"
  - "Które NFR wolno okroić w MVP, a których nie?"

procedures:                       # chain-of-action
  - name: draft_spec_fr_nfr
    trigger: ["nowy pomysł projektu", "brak spec przed kodem"]
    steps:
      - problem_statement
      - stakeholders
      - fr_moscow
      - nfr_smart
      - fr_nfr_matrix
      - poc_mvp_prod_decision
      - latency_budget
      - lab_dod_self_check

examples:
  minimal: required
  real_world: required            # np. VaultCollab
  misleading: recommended
  broken: recommended

assessment_ladder:                # które szczeble MUST dla tego ID
  explain: required
  worked_example: required
  predict: optional               # N/A gdy brak kodu runtime
  complete: optional
  modify: optional
  create: required                # lab: własna spec
  debug: optional
  transfer: required              # zastosuj do własnego projektu

sources:
  normative:
    - "Google SRE Book — SLIs/SLOs"
    - "SWEBOK / IEEE requirements concepts"
  pedagogical:
    - "Carpentries backward design"
  counterexample: []

project_spine_link: "spec-fr-nfr.md → 1.2 WBS → … → 8.3 blueprint"
```

**Reguła:** Writer **nie** zaczyna prose, dopóki Spec nie ma: LO, critical_competencies, misconceptions (≥1), assessment_ladder, sources.normative (≥1), procedures lub decision_points.

---

## 4. Lesson Markdown — kontrakt sekcji

### 4.1 Frontmatter (rozszerzenie)

```yaml
---
type: moc                          # lub concept gdy promote
title: "…"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [lesson, masterclass, …]
up: "[[web-engineering-roadmap]]"
lesson_id: "1.1"
diataxis: tutorial
certification_status: draft        # draft | static-fail | teachback-fail | certified | needs-human | screened
spec_path: "90_Meta/lessons/1.1/spec.yaml"
duration: "90-120 min"
---
```

### 4.2 Sekcje MUST (kolejność)

1. **Cel** — umiejętność/decyzja, nie lista tematów  
2. **Model mentalny** — jawny (dla runtime: notional machine)  
3. **Worked example** — pełny + „dlaczego”  
4. **Misconceptions** — min. 1; threshold concept → 2–3  
5. **Aktywność generatywna** — predict / self-explain / lab fill / Parsons (wg ladder w Spec)  
6. **Chain of action** — tabela `Sytuacja | Objaw | Akcja | Dlaczego` (nie proza)  
7. **Ćwiczenie samodzielne / lab** z DoD  
8. **Transfer** — nowy kontekst bez kopiowania przykładu  
9. **Retrieval / Blackbox quiz** — pytania bez od razu widocznej odpowiedzi  
10. **Kiedy NIE** / trade-offy  
11. **Powiązane** + **Źródła**

Jedna notatka = **jeden** tryb Diátaxis. Jeśli miesza tutorial z reference → FAIL strukturalny (rozbić).

### 4.3 AI-filler (kara stylu)

Bez uzasadnienia / „show me” zabronione m.in.:  
`w dzisiejszym świecie`, `warto zauważyć`, `nie da się ukryć`, `holistyczny`, `kluczowy` (puste), `ekosystem` (ozdobne), `leverage`, `robust`, `seamless`, `powerful`, `best practice` bez kryterium, `delve`, `tapestry`, `realm`.

**Deletion test:** usunięcie akapitu musi usuwać konkret (nazwę, liczbę, mechanizm, decyzję). Jeśli nic nie ginie → FAIL substancji.

Progi stylometrii EN **nie** obowiązują; baseline PL budujemy później na korpusie vaulta.

---

## 5. Quality Gate

### 5.1 Zasada scoringu

**Nie średnia.**  
`correctness=0.98` + `depth=0.42` → **REJECT**.

PASS wymaga jednocześnie:

```text
PASS ⇔
  wszystkie MUST strukturalne = true
  AND wszystkie MUST dydaktyczne = true
  AND static/code gates = pass
  AND teach-back:
        ≥ 90% competencies
        AND 100% critical_competencies
        AND transfer = pass
        AND zero major misconception
  AND language hard-fails = 0
```

### 5.2 MUST — struktura

- [ ] Frontmatter: `lesson_id`, `diataxis`, `certification_status`, `spec_path`, `up`
- [ ] Spec istnieje i jest kompletny (sekcja 3)
- [ ] Sekcje MUST obecne (4.2); puste H2 = FAIL
- [ ] Wikilinki prereq / related nie są martwe (lub jawnie TODO)
- [ ] Lab path zgodny z roadmapą (gdy `create` wymagane)

### 5.3 MUST — dydaktyka

- [ ] Cel jako umiejętność/decyzja
- [ ] Model mentalny obecny
- [ ] ≥1 worked example z „dlaczego”
- [ ] ≥1 misconception zaadresowane
- [ ] ≥1 zadanie generatywne + transfer
- [ ] Chain-of-action jako tabela
- [ ] Alignment: każda critical competency ma pokrycie w treści **i** w assessment

### 5.4 MUST — technika / groundedness

- [ ] Twierdzenia techniczne → źródło w Spec / sekcji Źródła
- [ ] Bloki kodu: uruchamialne **lub** oznaczone `pseudocode` / `non-exec`
- [ ] Lab DoD checklistowalny

### 5.5 MUST — język

- [ ] Brak AI-filler bez „show me”
- [ ] Deletion test na ≥3 losowych akapitach prozy (nie tabele/kod)
- [ ] Brak „badania pokazują” bez cytatu

### 5.6 SHOULD (nie blokuje sam)

- Faded / Parsons gdy kod
- Project-spine link jawny
- Spaced repetition `Pytanie::Odpowiedź`
- Analogia zakotwiczona w mechanizmie
- Engagement (scenariusz realny)

### 5.7 Raport (`quality-report.yaml`)

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
failures: []          # WHERE / WHAT / HOW_DETECTED / FIX
verdict: certified|needs-human|static-fail|teachback-fail
judge_model_family: "…"   # ≠ writer_model_family
writer_model_family: "…"
```

---

## 6. Pipeline agentów i orkiestracja

### 6.1 Role

| Rola | Cel | Nie wolno |
|---|---|---|
| Spec Builder | Zbudować Knowledge Spec z roadmapy + źródeł | Pisać pełną lekcję |
| Writer | Skompilować MD/lab/canvas ze Spec | Oceniać siebie; pomijać Spec |
| Static Validator | Schema, linki, sekcje, code extract | „Opinia pedagogiczna” |
| Student Agent | Nauczyć się **tylko** z lekcji; rozwiązać zadania | Widzieć Spec; wystawiać PASS |
| Judge | Porównać artefakty Studenta ze Spec; 0/1 + WHERE/WHAT/FIX | Być tą samą rodziną modelu co Writer (preferencja) |
| Human | Akceptacja Spec; Blackbox quiz; promote; kolejne ID | — |

### 6.2 Orkiestracja: skill-driven (nie autonomiczne self-call)

```text
Human: „uruchom kb-lesson-certify dla <ID>”
  → Spec (load|build)
  → Human akceptuje Spec          ← twarde
  → pętla ≤3: Writer → Static → Student → Judge
  → certified | needs-human
Human: „uruchom kb-blackbox dla <ID>”   ← dopiero po certified (zalecane)
  → Brief → nowy czat → quiz właściciela
  → pass → proposal 10_–50_
Human: decyzja o następnym ID         ← nigdy auto
```

**Wewnątrz skilla:** tak — sekwencja finished→verify z limitem 3.  
**Między lekcjami / bez człowieka:** nie.  
**Writer nie odpala Judge’a poza orkiestratorem.**

### 6.3 Mapowanie na istniejący Blackbox

| Faza | Skill | Wynik |
|---|---|---|
| A — Certify | `kb-lesson-certify` (propozycja) | `certification_status: certified` |
| B — Human verify | `kb-blackbox` (istniejący) | zaliczenie quizu → promote |

Blackbox **nie znika**. Certify go **poprzedza**, żeby człowiek nie był pierwszym miejscem wykrywania luk.

---

## 7. Creator Agent — reguły produkcji

1. Najpierw wypełnij Spec (backward design).  
2. Preferuj czasowniki nad przymiotnikami.  
3. Każdy claim abstrakcyjny → przykład / pomiar / counterexample albo osłab.  
4. Chain-of-action tylko jako tabela.  
5. Zakaz AI-filler (sekcja 4.3).  
6. Few-shot: styl [[1.1-ideation-fr-nfr]] jako golden sample tonu (konkret, tabele, lab).  
7. Po FAIL Judge: naprawiaj **tylko** sekcje z FIX — nie przepisuj całej lekcji.

---

## 8. Adaptacja typów lekcji masterclass

| Typ ID | diataxis | Ladder nacisk | Spec notes |
|---|---|---|---|
| Dokumentacyjna (1.1, 1.2, 8.1) | tutorial / how-to | explain, create (lab), transfer | predict/code optional |
| Mechanika runtime (3.1, 3.3, 4.1) | explanation + lab tutorial | predict, debug, transfer + notional machine | threshold często true |
| Vs / stack (2.3x, 2.4, 6.3) | explanation | decision table, transfer | misconceptions o „zawsze X” |
| Capstone (8.3) | how-to | create, transfer | project spine |

---

## 9. MVP wdrożenia (kolejność)

1. Ten kontrakt + delta w roadmapie + audyt 1.1 — **done w tej sesji**.  
2. Spec.yaml dla 1.1 (retrospektywa) przy następnym certify.  
3. Akceptacja propozycji `kb-lesson-certify` → implementacja w `.agent/skills/` **tylko na polecenie**.  
4. V2: Adversarial Agent, PL style linter baseline, automatyczny code runner w labach z runtime.

---

## 10. Definicje statusów

| Status | Znaczenie |
|---|---|
| `draft` | Treść w trakcie |
| `static-fail` | Padła bramka deterministyczna |
| `teachback-fail` | Student-sim nie zaliczył; iteracja < max lub eskalacja |
| `certified` | Gotowe do Human Blackbox / screeningu |
| `needs-human` | Max iteracji lub krytyczna niejednoznaczność |
| `screened` | Właściciel przejrzał / quiz zaliczony |

---

*Lesson Quality Contract v1 · Vaultie · 2026-08-10*
