---
type: snippet
title: "Optymistyczna mutacja w TanStack Query v5"
created: 2026-08-06
updated: 2026-08-06
tags: [react, tanstack-query, snippet, optimistic-ui]
aliases: []
up: "[[Snippets MOC]]"
lib: "@tanstack/react-query"
language: typescript
version: "5.0.0"
verified: true
---

# Optymistyczna mutacja w TanStack Query v5

Sprawdzony wzorzec implementacji optymistycznej aktualizacji listy elementów w z wykorzystaniem `useMutation`.

```typescript
import { useMutation, useQueryClient } from '@tanstack/react-query';

export function useAddTodo() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateTodoApi,
    onMutate: async (newTodo) => {
      await queryClient.cancelQueries({ queryKey: ['todos'] });
      const previousTodos = queryClient.getQueryData(['todos']);

      queryClient.setQueryData(['todos'], (old: any) => [...(old || []), newTodo]);

      return { previousTodos };
    },
    onError: (err, newTodo, context) => {
      queryClient.setQueryData(['todos'], context?.previousTodos);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] });
    },
  });
}
```

## Powiązania
- Biblioteka: [[tanstack-query]]
- Wzorzec: [[optimistic-ui-updates]]
