---
type: moc
title: "Audyt vaultie-certify.py — luki i plan naprawy"
created: 2026-08-11
updated: 2026-08-11
tags: [meta, quality-gate, certifier, audit]
up: "[[lesson-quality-contract-v1]]"
---

# Audyt weryfikatora lekcji — 2026-08-11

> **Kontekst:** Lekcja 1.3 miała status `draft`, niekompletny lab i quiz ze spoilerami, a stary `vaultie-certify.py` zwracał **PASS**. Ten dokument wyjaśnia dlaczego i co zostało naprawione.

---

## 1. Werdykt (przed / po)

| Lekcja | Stary certifier | Nowy certifier (extended Phase A) |
|---|---|---|
| 1.3 (przed poprawkami) | PASS (fałszywy) | FAIL — lab, canvas, quiz spoilers, brak transfer/rubryki |
| 1.3 (po poprawkach) | — | PASS (strict) |
| 1.2 | PASS | PASS |
| 1.1 | PASS (luźny) | WARN/FAIL zależnie od canvas/lab linków |

---

## 2. Dlaczego stary certifier nie wychwytywał braków

Implementacja v1.0.0 sprawdzała **tylko**:

1. Pola frontmatter (`type`, `title`, …) — bez `lesson_id`, `certification_status`
2. Luźne regex nagłówków Diátaxis (`Wprowadzenie`, `Kod`, …) — 1.3 je miała mimo luk merytorycznych
3. Obecność `|` w body gdy jest „Chain of Action” — przechodziła tabela z roadmapy
4. Słowa kluczowe z `spec.yaml` — **false positive** (wystarczyło wspomnieć „lockfile”)

**Nie sprawdzało:**

| Luka | Skutek |
|---|---|
| Lab `labs/…` — pliki, lockfile, Husky | PASS mimo pustego monorepo |
| Canvas `.canvas` istnieje i jest linkowany | Brak mapy wizualnej undetected |
| Quiz bez inline odpowiedzi | Spoiler psuje Blackbox |
| Rubryka zaliczenia w quizie | Brak progu ≥3/4 |
| Sekcja Transfer | Brak weryfikacji transferu |
| Duplikaty `##` H2 | Numeracja 8/8 undetected |
| Link lekcji w roadmapie | Roadmap bez `[[1.3/…]]` OK |
| `quality-report.yaml` vs `certification_status` | Rozjazd statusów |
| **Phase B** teach-back / Judge | **W ogóle nie zaimplementowane** |

Dodatkowo: próg `WARN` gdy `<3 issues` — pojedyncze luki nie blokowały.

---

## 3. Co dodano w extended Phase A (2026-08-11)

Skrypt: `.agent/scripts/vaultie-certify.py`

| Bramka | Opis |
|---|---|
| Frontmatter rozszerzony | `lesson_id`, `diataxis`, `certification_status`, `spec_path` |
| Duplicate H2 | Wykrywa powtórzone nagłówki sekcji |
| Blackbox spoilers | Wzorce `*Odpowiedź:`, `**Odpowiedź:` w bloku quizu |
| Rubryka | Wymaga słowa „Rubryka” w sekcji Blackbox |
| Transfer | Wymaga sekcji Transfer |
| Canvas | Wikilink `*.canvas` + plik w `90_Meta/canvases/` |
| Lab artifacts | pnpm-workspace, lockfile, Husky, CI, apps/web, packages/shared |
| Spec completeness | LO, competencies, mental_models, sources.normative, … |
| Roadmap link | Sekcja `## 1.x` musi linkować pełną lekcję |
| quality-report | Spójność ze `certification_status: certified` |
| `--strict` | Exit code 1 gdy nie PASS |

---

## 4. Co nadal NIE jest zaimplementowane (Phase B+)

Zgodnie z [[lesson-quality-contract-v1]] sekcja 6:

| Faza | Status | Narzędzie |
|---|---|---|
| A — Static Validator | **Częściowo** (extended) | `vaultie-certify.py` |
| B — Student Agent | ❌ | kb-lesson-certify (propozycja) |
| C — Judge / teach-back | ❌ | osobny model, porównanie ze Spec |
| D — Human Blackbox | ✅ osobno | [[kb-blackbox]] skill |
| Deletion test / AI-filler | ❌ | wymaga LLM lub korpusu PL |
| Uruchamialność kodu w MD | ❌ | wymaga sandbox exec |
| Martwe wikilinki globalne | ❌ | wymaga parsera vaulta |

**Rekomendacja:** `certification_status: certified` z Phase A oznacza „gotowe do Blackbox człowieka”, nie „zaliczone przez ucznia”.

---

## 5. Jak uruchomić

```bash
python .agent/scripts/vaultie-certify.py 1.3 --strict
python .agent/scripts/vaultie-certify.py 1.2 --strict
python .agent/scripts/vaultie-certify.py        # wszystkie lekcje
```

---

## 6. Powiązane

- [[lesson-quality-contract-v1]]
- [[1.1-lesson-quality-audit]]
- `.agent/scripts/vaultie-certify.py`
- [[1.3/1.3-repo-monorepo-git-workflow]] — case study fałszywego PASS
