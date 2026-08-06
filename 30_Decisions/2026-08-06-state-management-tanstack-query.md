---
type: decision
title: "Wybiór TanStack Query v5 jako standardu dla stanu serwerowego"
created: 2026-08-06
updated: 2026-08-06
tags: [adr, architecture, state-management, react]
aliases: [ADR-001 TanStack Query]
up: "[[Decisions MOC]]"
status: accepted
supersedes: ""
affects: ["Portal Klienta", "Dashboard Analytics"]
---

# Wybór TanStack Query v5 jako standardu dla stanu serwerowego

## Kontekst

Aplikacje frontendowe w organizacji wymagały spójnego mechanizmu pobierania, keszowania oraz unieważniania danych pobieranych z API GraphQL i REST.

## Rozważane Alternatywy

1. **TanStack Query v5**
2. **SWR**
3. **Custom Redux / RTK Query**

## Wybrana Opcja i Uzasadnienie

Wybór pada na **TanStack Query v5**.

- Zapewnia najdoskonalsze wsparcie dla TypeScript.
- Domyślnie obsługuje dedykowane wzorce reaktywne oraz optymistyczne aktualizacje UI.
- Posiada dojrzałe devtoolsy ułatwiające inspekcję keszu.

## Powiązane Notatki
- Biblioteka: [[tanstack-query]]
- Wzorzec: [[optimistic-ui-updates]]
