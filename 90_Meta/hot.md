---
type: meta
title: "Hot Context Buffer — Aktywny Kontekst Sesji"
created: 2026-08-06
updated: 2026-08-22
tags: [meta, context, hot-buffer]
up: "[[90_Meta/_index]]"
---

# Hot Context Buffer

> [!NOTE]
> Plik czytany automatycznie na początku każdej nowej sesji przez agenta w celu błyskawicznego podjęcia kontekstu bez konieczności odczytywania całej historii logów.

## Bieżący Punkt Skupienia
- **Aktywny Wątek:** Wdrożenie infrastruktury **Fazy 1 Epistemicznego Agenta Kodującego** (Tier 1 MVP + elementy Tier 2) w ekosystemie Vaultie.
- **Ostatnie Zadanie:** 
  1. Zaimplementowano skrypt kontrolera i maszyny stanów `.agent/scripts/epistemic_runner.py` z obsługą UTF-8 i guardrailami regex.
  2. Utworzono specyfikację skilla `.agent/skills/kb-epistemic-solve.md` oraz `.agent/skills/kb-epistemic-solve/SKILL.md` i zarejestrowano w `.agent/AGENTS.md`.
  3. Zbudowano pakiet ewaluacji A/B w `labs/benchmark-suite/` ze skryptem `run_benchmark.py` i 3 referencyjnymi zadaniami (API Drift, Root Cause Auth, Exponential Backoff).

## Ostatnio Modyfikowane Notatki
- `.agent/scripts/epistemic_runner.py` — kontroler maszyny stanów, guardrails i runner testów
- `.agent/skills/kb-epistemic-solve.md` — specyfikacja skilla epistemicznego pętli rozwiązywania problemów
- `.agent/skills/kb-epistemic-solve/SKILL.md` — definicja skilla folder-based
- `.agent/AGENTS.md` — zaktualizowany rejestr skilli agenta
- `labs/benchmark-suite/` — pakiet referencyjny benchmarku A/B (README, harness, zadania 01-03)
- `00_Inbox/_proposals/2026-08-22-phase-1-epistemic-agent-implementation.md` — plan wdrożenia Fazy 1

## Otwarte Kwestie / Następne Kroki
- [x] Zbudowano kompletną infrastrukturę Fazy 1 (Runner, Guardrails, Skill, Benchmark Suite)
- [ ] Gotowość do uruchomienia ślepego testu benchmarkowego A/B (w czystych oknach czatu zgodnie z instrukcją w `labs/benchmark-suite/README.md`)
