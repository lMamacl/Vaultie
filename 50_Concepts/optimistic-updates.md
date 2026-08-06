---
type: concept
title: "Koncepcja Optymistycznego Interfejsu (Optimistic UI)"
created: 2026-08-06
updated: 2026-08-06
tags: [ux, concept, performance]
aliases: [Perceived Performance]
up: "[[Concepts MOC]]"
domain: frontend
prerequisite: "Asynchroniczne ładowanie danych"
difficulty: intermediate
---

# Koncepcja Optymistycznego Interfejsu (Optimistic UI)

Optymistyczne interfejsy opierają się na zaaproszeniu, że zdecydowana większość żądań użytkownika w sieci kończy się sukcesem (często > 99%).

## Kluczowe założenia
- Zamiast wywoływać stan ładowania (`spinner`), UI odpowiada natychmiastowo tak, jakby operacja się powiodła.
- Tworzy to złudzenie natychmiastowej reakcji aplikacji.
- W rzadkim przypadku niepowodzenia interfejs wycofuje stan i powiadamia użytkownika (np. toast notifications).

## Powiązania
- Wzorzec: [[optimistic-ui-updates]]
- Snippet: [[use-tanstack-query-optimistic]]
