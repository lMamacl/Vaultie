---
type: comparison
title: "<% tp.file.title %>"
options: []
criteria: []
winner: ""
status: draft
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.creation_date("YYYY-MM-DD") %>
tags: []
aliases: []
up: "[[Decisions MOC]]"
---

<!-- AI-INSTRUCTIONS
1. Comparison to SUROWIEC dla Decision (ADR). Po akceptacji → stwórz ADR w 30_Decisions/
2. `options` = nazwy porównywanych bibliotek/narzędzi (min. 2)
3. `criteria` = kryteria oceny (min. 4). Użyj skali: ++ / + / 0 / - / --
4. `winner` = pustego NIE zostawiaj jeśli status != draft. Musi być uzasadniony w Syntezie
5. Macierz musi być FAIR — nie pisz pod z góry wybraną opcję
6. Po akceptacji właściciela: uruchom `kb-compare --promote` → generuje ADR
-->

# <% tp.file.title %>

## Kontekst
<!-- Dlaczego porównujesz? Jaki problem rozwiązujesz? Jakie ograniczenia? -->

## Kryteria oceny
| Kryterium | Waga | Opis |
|-----------|------|------|
<!-- Waga: critical / important / nice-to-have -->

## Macierz porównawcza
| Kryterium | Option 1 | Option 2 | Option 3 |
|-----------|----------|----------|----------|
<!-- Skala: ++ (doskonałe) / + (dobre) / 0 (neutralne) / - (słabe) / -- (eliminujące) -->

## Szczegóły per opcja

### Option 1
<!-- 3-5 zdań: główne zalety, największa wada, dojrzałość ekosystemu -->

### Option 2
<!-- 3-5 zdań: główne zalety, największa wada, dojrzałość ekosystemu -->

## Synteza
<!-- Która opcja i DLACZEGO. Odnieś się do kryteriów z wagi "critical". -->

## Rekomendacja → ADR
<!-- Jedno zdanie w formacie Y-statement:
     "W kontekście [X], facing [Y], wybieram [Z] zamiast [A], aby [B], akceptując [C]." -->
