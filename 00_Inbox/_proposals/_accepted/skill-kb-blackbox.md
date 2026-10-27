---
type: proposal
title: "Propozycja skillu kb-blackbox"
created: 2026-08-06
updated: 2026-08-06
tags: [proposal, skill, blackbox, guardrail, masterclass]
up: "[[web-engineering-roadmap]]"
status: accepted
accepted: 2026-08-07
---

# Propozycja ACCEPTED → `.agent/skills/kb-blackbox/SKILL.md`

## Cel
Ustandaryzować Guard-Rail Verification Protocol z [[web-engineering-roadmap]]: brief → **nowa instancja czata** → draft ze źródeł → quiz otwarty → brama zaliczenia → propozycja do `10_`–`50_`.

## Docelowa lokalizacja
- Definicja: `.agent/skills/kb-blackbox/SKILL.md` (**tylko po wyraźnym poleceniu właściciela** — `.agent/` jest chronione)
- Wywołanie: „uruchom kb-blackbox dla \<ID lekcji\>” (np. `1.1`)

## Zachowanie skillu (szkic)
1. Wczytaj sprawozdanie lekcji ID z `90_Meta/web-engineering-roadmap.md`.
2. Wygeneruj **Brief Blackbox** (cele, źródła, zakaz skracania, rubryka 3–4 Q, ścieżka artefaktu, typ Vaultie).
3. Poproś właściciela o otwarcie nowego czata i wklejenie briefu.
4. Po drafcie: przeprowadź ocenę odpowiedzi quizu wg rubryki (próg ≥3/4).
5. Przy fail: wypisz braki i wygeneruj brief rozbudowy (bez przejścia do kolejnego ID).
6. Przy pass: utwórz/zaktualizuj propozycję w `00_Inbox/_proposals/` zgodną z typem artefaktu lekcji.

## Guardrails
- Brak przejścia do następnego ID bez zaliczenia.
- Draft w Blackboxie opiera się na źródłach z roadmapy + oficjalnej dokumentacji wskazanej w briefie — nie na „ogólnej wiedzy bez cytatu”.
- Nie zapisuje bezpośrednio do `10_`–`50_` bez akceptacji.

## Kryteria akceptacji propozycji
- [ ] Właściciel zatwierdza treść skillu
- [ ] Właściciel wydaje polecenie: zaimplementuj skill w `.agent/skills/`
- [ ] Opcjonalnie: cienki wskaźnik w `.claude/skills/` jeśli używane

## Powiązania
- Roadmapa: sekcja „Protokół Blackbox Verification”
- Inspiracje edu (adaptacja, nie fork): vibe-learn, LearnKit, learn-something Feynman explain-back
