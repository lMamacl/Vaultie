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

- [[2026-08-06-diagramming-engine-react-flow-vs-jointjs]] — Wybór silnika dla edytora diagramów UML na nieskończonym polu: React Flow vs JointJS vs Alternatywy (`accepted`)
- [[2026-08-06-state-management-tanstack-query]] — Wybór TanStack Query v5 jako standardu dla stanu serwerowego (`accepted`)
- [[2026-08-22-epistemic-coding-agent-architecture]] — Architektura Epistemicznego Agenta Kodującego: Wdrożenie Tier 1 MVP i Integracja MCP vs Odrzucenie 6-Silnikowego Molocha (`accepted`)

