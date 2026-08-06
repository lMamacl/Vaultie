---
type: moc
title: "Libraries MOC"
created: 2026-08-06
updated: 2026-08-06
tags: [moc, libraries]
up: "[[90_Meta/_index]]"
---

# Map of Content — Biblioteki

Rejestr przeanalizowanych i wykorzystywanych bibliotek oraz narzędzi programistycznych.

```dataview
TABLE lib, ecosystem, version, verdict, confidence
FROM "10_Libraries"
WHERE type = "library"
SORT file.name ASC
```

## Spis bibliotek

- [[react-flow]] — Niezależna biblioteka React do tworzenia edytorów grafów i nieskończonych pól (`adopt`)
- [[jointjs]] — Zaawansowany silnik diagramowania i wizualizacji SVG z wrapperem React (`trial`)
- [[tanstack-query]] — Standard zarządzania stanem serwerowym w React (`adopt`)
