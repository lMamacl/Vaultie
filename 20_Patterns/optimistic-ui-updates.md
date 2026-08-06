---
type: pattern
title: "Optimistic UI Updates"
created: 2026-08-06
updated: 2026-08-06
tags: [ui-pattern, UX, async, state-management]
aliases: [Optymistyczne Aktualizacje UI]
up: "[[Patterns MOC]]"
---

<!-- AI-INSTRUCTIONS
Instrukcje dotyczące wzorca:
- Wzorzec musi być uniwersalny (niezależny od konkretnej biblioteki).
- Sekcja "Rozwiązanie" powinna opisywać przepływ i kroki (np. cancel queries -> rollback snapshot -> mutate -> invalidate).
-->

# Optimistic UI Updates

Wzorzec projektowy polegający na natychmiastowym zaktualizowaniu interfejsu użytkownika przed otrzymaniem potwierdzenia sukcesu z serwera API.

## Problem

Tradycyjny przepływ żądań HTTP powoduje opóźnienia w interfejsie (spinners), co obniża subiektywne odczucie szybkości aplikacji (perceived performance).

## Rozwiązanie

1. Anuluj wychodzące zapytania re-fetchowe, aby zapobiec nadpisaniu stanu lokalnego.
2. Zapisz snapshot poprzedniego stanu (na przypadek wycofania zmian).
3. Zaktualizuj stan w pamięci klienta natychmiast na podstawie danych wysyłanych w mutacji.
4. W przypadku błędu (error rollback) przywróć poprzednio zapisany snapshot.
5. Po zakończeniu mutacji (onSettled) przeprowadź ponowną synchronizację z serwerem (`invalidateQueries`).

## Pułapki i Gotchas

- Należy pamiętać o generowaniu tymczasowych ID (np. `crypto.randomUUID()`) dla nowo dodawanych elementów.

## Odnośniki
- Biblioteka: [[tanstack-query]]
- Snippet: [[use-tanstack-query-optimistic]]
