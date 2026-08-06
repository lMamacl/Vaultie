---
type: moc
title: "Snippets MOC"
created: 2026-08-06
updated: 2026-08-06
tags: [moc, snippets]
up: "[[90_Meta/_index]]"
---

# Map of Content — Snippety

Baza przetestowanych i zweryfikowanych fragmentów kodu.

```dataview
TABLE lib, language, verified
FROM "40_Snippets"
WHERE type = "snippet"
SORT file.name ASC
```

## Spis snippetów

- [[use-tanstack-query-optimistic]] — Optymistyczna mutacja w TanStack Query v5 (`verified: true`)
