---
type: moc
title: "Decisions MOC"
created: 2026-08-06
updated: 2026-08-06
tags: [moc, decisions]
up: "[[90_Meta/_index]]"
---

# Map of Content — Decyzje (ADR)

Rejestr kluczowych decyzji architektonicznych i technologicznych.

```dataview
TABLE status, affects, supersedes
FROM "30_Decisions"
WHERE type = "decision"
SORT file.name ASC
```

## Spis decyzji

- [[2026-08-06-state-management-tanstack-query]] — Wybór TanStack Query v5 jako standardu dla stanu serwerowego (`accepted`)
