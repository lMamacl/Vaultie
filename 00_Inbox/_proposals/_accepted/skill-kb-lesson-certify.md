---
type: proposal
title: "Propozycja skillu kb-lesson-certify"
created: 2026-08-10
updated: 2026-08-10
tags: [proposal, skill, certify, quality-gate, blackbox, masterclass]
up: "[[lesson-quality-contract-v1]]"
status: accepted
accepted: 2026-08-10
---

# Propozycja ACCEPTED → `.agent/skills/kb-lesson-certify/SKILL.md`

## Cel
Automatyczna **Faza A** weryfikacji lekcji masterclass według [[lesson-quality-contract-v1]]: Knowledge Spec → static gates → Student-sim → Judge → `certified` | `needs-human`, przed `kb-blackbox` (Faza B).

## Docelowa lokalizacja
- Definicja: `.agent/skills/kb-lesson-certify/SKILL.md` (**zaimplementowane 2026-08-10**)
- Wywołanie: „uruchom kb-lesson-certify dla \<ID\>”

## Kryteria akceptacji
- [x] Właściciel zatwierdza treść skillu
- [x] Właściciel wydaje polecenie implementacji w `.agent/skills/`
- [x] Roadmapa wskazuje ten skill
- [ ] Smoke test / re-certify `1.1` (w toku po akceptacji)

## Powiązania
- Skill: `.agent/skills/kb-lesson-certify/SKILL.md`
- [[lesson-quality-contract-v1]]
- `.agent/skills/kb-blackbox/SKILL.md`
- [[web-engineering-roadmap]]
