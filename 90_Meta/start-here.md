---
type: moc
title: "Zacznij tutaj — Vaultie"
created: 2026-09-29
updated: 2026-09-29
tags: [meta, start, guide]
aliases: [Start, Start here]
up: "[[90_Meta/_index]]"
---

# Zacznij tutaj

Vaultie pomaga **rozwiązywać problemy inżynierskie na podstawie wiedzy, źródeł i jawnych założeń**. Nie musisz znać układu katalogów ani nazw wszystkich skillsów.

## Co chcesz zrobić?

### Rozwiązać konkretny problem
Opisz problem, kontekst i ograniczenia zwykłym językiem. Możesz użyć takiego polecenia:

> Przeanalizuj problem: retry do zewnętrznego API może powodować podwójne wykonanie operacji. Kontekst: Node.js, checkout, timeout po wysłaniu żądania. Porównaj rozwiązania, wskaż źródła, założenia i brakujące informacje.

W Antigravity wpisz `/kb-solve-problem` (albo wybierz skill po wpisaniu `/`) dla otwartego problemu programistycznego lub architektonicznego. Oczekuj jawnej decyzji, dlaczego wybrano tę opcję, dlaczego odrzucono istotne alternatywy i co zmieniłoby wybór — wraz ze źródłami, trade-offami i następnym krokiem. Jeśli odpowiedź zależy od nieznanych danych, agent powinien je ujawnić — nie zgadywać.

### Znaleźć istniejącą wiedzę
W Antigravity użyj `/kb-query` lub wybierz go po wpisaniu `/`; możesz też po prostu poprosić agenta o wyszukanie w Vaultie. Korzystaj z zapytań z [[queries]]. Zaczynaj od słów opisujących **problem i efekt**, nie tylko nazwy technologii. Sprawdź też [[_index|mapę treści]] oraz powiązane linki w znalezionej notatce.

### Zbadać nowe źródła
Użyj `kb-scout` do odkrywania materiałów z watchlisty albo `kb-extract` do zebrania konkretnej strony. Nowe materiały trafiają do `00_Inbox/` — są surowcem do oceny, nie zatwierdzoną wiedzą ani automatyczną rekomendacją.

### Uczyć się i ćwiczyć
Otwórz [[web-engineering-roadmap]] i wybierz lekcję. Laby znajdują się w `labs/web-engineering/`; opis labu wskazuje cel, kroki i kryteria ukończenia.

### Przejrzeć materiały czekające na decyzję
Nowe ekstrakty i propozycje znajdziesz w `00_Inbox/`. Przed przeniesieniem materiału do zatwierdzonej wiedzy sprawdź źródła, trafność, aktualność oraz proponowane powiązania.

## Jak opisać problem, żeby dostać lepszą odpowiedź

Podaj, o ile wiesz:

- **objaw lub cel** — co się dzieje albo co chcesz osiągnąć;
- **kontekst** — język, framework, architektura i istotny fragment systemu;
- **ograniczenia** — zespół, infrastruktura, termin, budżet, kompatybilność;
- **wymagania niefunkcjonalne** — np. bezpieczeństwo, dostępność, wydajność;
- **próby i ich wyniki** — co już sprawdziłeś;
- **rodzaj wyniku** — diagnoza, porównanie, rekomendacja, plan migracji albo szkic ADR.

Nie musisz znać odpowiedzi na wszystkie te pytania. Agent powinien odróżnić brak danych od faktu i wskazać, które brakujące informacje mogą zmienić rekomendację.

## Jak czytać rekomendację

- **Fakt ze źródła** powinien mieć możliwe do sprawdzenia odwołanie.
- **Synteza** to wniosek agenta z kilku źródeł lub materiałów Vaultie.
- **Rekomendacja** zależy od podanego kontekstu i może nie pasować do innego projektu.
- **Niepewność** powinna być jawna; brak dowodów nie oznacza, że hipoteza jest prawdziwa.
- **Propozycja** nie staje się zatwierdzoną notatką produkcyjną bez akceptacji.

## Szybkie linki

- [[_index|Mapa treści]] · [[queries|Zapytania]] · [[web-engineering-roadmap|Roadmapa lekcji]]
- [[00_Inbox/_index|Inbox — materiały do przeglądu]] · [[.agent/health-dashboard|Health Dashboard]]
- [Instrukcje agenta](../.agent/AGENTS.md) · [Repozytorium i szybki start](../README.md)
