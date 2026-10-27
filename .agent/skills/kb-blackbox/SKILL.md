---
name: kb-blackbox
description: "Runs a closed-book teach-back quiz for a Vaultie lesson. Use when checking understanding of a lesson or preparing to accept a lesson artifact."
---

# kb-blackbox — Guard-Rail Verification Protocol

## Cel
Wymuszenie głębokiej notatki dydaktycznej w **nowej instancji czata** (ze źródeł), potem quiz otwarty jako brama do kolejnej lekcji masterclass. Chroni przed skracaniem i „hand-waving” AI.

## Kiedy użyć
- Wywołanie: „uruchom kb-blackbox dla \<ID\>” (np. `1.1`, `2.2`, `3.3`).
- Przed akceptacją artefaktu lekcji do `10_`–`50_`.
- Po drafcie lekcji, gdy właściciel ma zaliczyć zrozumienie.
- **Zalecane:** po `kb-lesson-certify` ze statusem `certified` (Faza A). Bez certify — ostrzeż właściciela.

## Kroki
1. **Sprawdź certify:** jeśli lekcja ma `certification_status` ≠ `certified`|`screened`, ostrzeż i wskaż „uruchom kb-lesson-certify dla \<ID\>”. Kontynuuj tylko na życzenie właściciela.
2. **Wczytaj lekcję ID** z `90_Meta/web-engineering-roadmap.md` (sprawozdanie) oraz — jeśli istnieje — pełną lekcję w `90_Meta/lessons/`.
3. **Wygeneruj Brief Blackbox** zawierający:
   - ID i tytuł lekcji
   - cel dydaktyczny
   - listę źródeł (z roadmapy + oficjalna dokumentacja)
   - **zakaz skracania** / hand-waving
   - ścieżkę artefaktu i typ Vaultie (`concept` / `library` / `comparison` / `decision` / `snippet`)
   - 3–4 pytania otwarte + rubrykę zaliczenia (z roadmapy)
4. **Poproś właściciela** o otwarcie **nowego czata Cursor** i wklejenie briefu. Ta instancja pisze głęboką notatkę wyłącznie ze źródeł z briefu.
5. **Po drafcie:** zbierz odpowiedzi na quiz (wklejone przez właściciela do sesji masterclass lub Blackbox).
6. **Oceń wg rubryki:**
   - Zaliczone: przepływ / trade-off / „kiedy użyć” + ≥1 konkret techniczny
   - Do poprawy: ogólniki, pomylone pojęcia, brak „dlaczego nie X”
   - **Próg:** ≥3/4; przy 2/4 — rozbudowa notatki + retake (bez przejścia do kolejnego ID)
7. **Przy fail:** wypisz braki, wygeneruj brief rozbudowy; **nie** przechodź do następnego ID.
8. **Przy pass:** ustaw `certification_status: screened` jeśli lekcja istnieje; utwórz/zaktualizuj propozycję w `00_Inbox/_proposals/` (typ zgodny z artefaktem lekcji) albo — jeśli właściciel już zaakceptował promote — wskaż ścieżkę zapisu do `10_`–`50_`.

## Input
- ID lekcji masterclass (wymagane), np. `1.1`.
- Opcjonalnie: ścieżka do draftu z Blackboxa (jeśli już istnieje).

## Output
- Brief Blackbox (do wklejenia w nowym czacie).
- Ocena quizu (pass/fail + uzasadnienie per pytanie).
- Przy pass: plik w `00_Inbox/_proposals/` lub wskazanie promote.

## Guardrails
- **Brak przejścia do następnego ID bez zaliczenia quizu.**
- Draft Blackbox opiera się na źródłach z roadmapy + oficjalnej dokumentacji z briefu — nie na „ogólnej wiedzy bez cytatu”.
- Nie zapisuje bezpośrednio do `10_`–`50_` bez akceptacji właściciela.
- Nie edytuje `.agent/` poza tym skillem (już zdefiniowanym).
- Język nauczyciela: pełne wyjaśnienia, bez „m.in.” / „itd.” bez listy.

## Warianty
- Standard: brief + ocena quizu.
- `--retake`: tylko brief rozbudowy po fail, bez nowego spisu źródeł (chyba że źródła były niewystarczające).
