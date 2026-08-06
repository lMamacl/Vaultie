---
type: library
title: "TanStack Query v5"
created: 2026-08-06
updated: 2026-08-06
tags: [state-management, react, async-data, frontend]
aliases: [React Query, React Query v5]
up: "[[Libraries MOC]]"
lib: "@tanstack/react-query"
ecosystem: js
version: "5.0.0"
verdict: adopt
alternatives: ["swr", "rtk-query"]
confidence: high
used_in: ["Portal Klienta", "Dashboard Analytics"]
---

<!-- AI-INSTRUCTIONS
Zasady edycji tej notatki:
- W sekcji "Podsumowanie i Verdict" podawaj zwięzłe uzasadnienie biznesowo-techniczne.
- Sekcja "Gotchas i Pułapki" powinna zawierać wyłącznie sprawdzone w praktyce pułapki.
-->

# TanStack Query v5

Standard przemysłowy w ekosystemie React do obsługi pobierania, keszowania oraz synchronizacji stanu serwerowego z klientem.

## Podsumowanie i Verdict

- **Verdict:** `adopt` — rekomendowany domyślny wybór dla wszystkich projektów React.
- **Dlaczego:** Świetna automatyczna inwalidacja keszu, doskonałe typowanie w TS, natywne wsparcie dla Suspense oraz szerokie wsparcie społeczności.

## Kluczowe API

```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const { data, isLoading } = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodos,
});
```

## Gotchas i Pułapki

1. **Wersja v5 wymaga przekazywania pojedynczego obiektu konfiguracyjnego** do `useQuery`.
2. **Query Key musi być tablicą** — string nie jest już dozwolony jako samodzielny klucz.

## Odnośniki i Powiązania
- Wzorzec: [[optimistic-ui-updates]]
- Decyzja: [[2026-08-06-state-management-tanstack-query]]
