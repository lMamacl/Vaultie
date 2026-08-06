---
type: library
title: "<% tp.file.title %>"
lib: ""
ecosystem: js
version: ""
verdict: assess
alternatives: []
confidence: low
used_in: []
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.creation_date("YYYY-MM-DD") %>
tags: []
aliases: []
up: "[[Libraries MOC]]"
---

<!-- AI-INSTRUCTIONS
Wypełniając ten szablon:
1. `lib` = oficjalna nazwa pakietu (npm/pip/cargo name)
2. `version` = wersja, na której ROBISZ analizę (nie "latest")
3. `verdict` startuje jako `assess`. Zmień na `trial` po testach, `adopt` po użyciu w projekcie
4. `alternatives` = minimum 2, nawet jeśli oczywiste
5. `confidence` = `low` jeśli czytałeś tylko docs, `medium` po hello-world, `high` po produkcji
6. Każda sekcja MUSI mieć treść. Puste sekcje = notatka niekompletna = `kb-lint` ją zgłosi
7. Sekcja "API którego naprawdę używam" — NIE kopiuj dokumentacji. Pokaż 3-5 najczęstszych wywołań
8. Sekcja "Gotchas" — minimum 1 wpis. Jeśli nie znasz, napisz "do zbadania"
-->

# <% tp.file.title %>

## Verdict w jednym zdaniu
<!-- Max 2 zdania. Format: "[Nazwa] robi [co] lepiej niż [alternatywa] bo [dlaczego]." -->

## Problem, który rozwiązuje
<!-- 3-5 zdań. Jaki ból adresuje? Czym się różni od natywnego rozwiązania? -->

## Model mentalny
<!-- Jak MYŚLEĆ o tej bibliotece — 3-5 zdań, NIE streszczenie docsów. Analogie, kluczowa abstrakcja, czym to "jest" konceptualnie. -->

## API, którego naprawdę używam
```ts
// 3-5 najczęstszych wywołań z komentarzami
```

## Gotchas
<!-- Lista bullet-pointów. Rzeczy, które Cię zaskoczyły lub mogą zaskoczyć. -->
- 

## Jak użyć u mnie
<!-- Konkretnie: w którym projekcie, zamiast czego, co trzeba zmienić. Jeśli jeszcze nie wiesz — napisz hipotezę z "?" na końcu. -->

## Alternatywy i dlaczego nie
| Alternatywa | Dlaczego odrzucona |
|---|---|

## Benchmark / Performance
<!-- Opcjonalne. Jeśli wydajność jest istotna — porównanie z alternatywami. Format: metryka, warunki, wynik. Bez danych = "nie mierzone". -->

## Źródła
<!-- Linki do oficjalnych docsów, artykułów, postów. Minimum 2. -->
- 
