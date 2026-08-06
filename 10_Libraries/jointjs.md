---
type: library
title: "JointJS (i JointJS React Wrapper)"
created: 2026-08-06
updated: 2026-08-06
tags: [jointjs, diagramming, svg-engine, enterprise, graph-visualization]
aliases: [JointJS Core, JointJS React]
up: "[[Libraries MOC]]"
lib: "jointjs"
ecosystem: js
version: "4.0.0"
verdict: trial
alternatives: ["react-flow", "gojs", "maxgraph"]
confidence: high
used_in: ["Zaawansowane Edytory Schematów", "Systemy CAD/UML"]
---

<!-- AI-INSTRUCTIONS
Zasady dotyczące notatki biblioteki JointJS:
- Opisuj dokładnie architekturę silnikową (Model-View) odseparowaną od drzewa React.
- Wskazuj zalety przy skali 10k+ obiektów oraz specyfikę dostosowywania SVG.
-->

# JointJS (i JointJS React Wrapper)

Dojrzały, wydajny silnik diagramowania i wizualizacji grafów w języku JavaScript oparty na modelu MVC/Model-View i renderowaniu SVG.

## Podsumowanie i Verdict

- **Verdict:** `trial` — Zalecany w projektach enterprise, gdzie kluczowa jest wydajność przy dziesiątkach tysięcy elementów, automatyczne trasowanie krawędzi (orthogonal routing), gotowe palety narzędzi oraz ścisłe standardy diagramowania (BPMN, UML, ERD).
- **Zastosowanie:** Skomplikowane edytory inżynieryjne, zaawansowane modelowanie UML, systemy przemysłowe.

## Architektura i Separacja Stanu

JointJS oddziela model grafu (`joint.dia.Graph`) od widoku kanwy (`joint.dia.Paper`). Wstawienie wrappera Reacta polega na osadzeniu punktu montowania widoku `Paper` i synchronizowaniu zdarzeń zdarzeniami silnika:

```typescript
import * as joint from 'jointjs';

// 1. Utworzenie modelu danych (Graph)
const graph = new joint.dia.Graph({}, { cellNamespace: joint.shapes });

// 2. Utworzenie widoku renderującego (Paper)
const paper = new joint.dia.Paper({
  el: document.getElementById('canvas-container'),
  model: graph,
  width: '100%',
  height: '100%',
  gridSize: 10,
  drawGrid: true,
  cellViewNamespace: joint.shapes,
});

// 3. Dodanie elementu UML
const umlClass = new joint.shapes.standard.Rectangle();
umlClass.position(100, 100);
umlClass.resize(180, 100);
umlClass.attr({
  body: { fill: '#f8f9fa', stroke: '#343a40', strokeWidth: 2 },
  label: { text: 'UserEntity\n+ id: UUID\n+ name: string', fill: '#212529' }
});
graph.addCell(umlClass);
```

## Pułapki i Gotchas

1. **Stroma krzywa uczenia i stylizowanie SVG:** Tworzenie niestandardowych węzłów nie odbywa się za pomocą czystego JSX, lecz poprzez szablony SVG lub fabryki widoków, co wymaga innej mentalności niż klasyczny rozwój komponentów w React.
2. **Synchronizacja Stanu:** Gdy edytor używa zewnętrznego magazynu (np. Redux/Zustand), należy uważać na pętle synchronizacji między stanem `joint.dia.Graph` a stanem aplikacji.
3. **Wersja Płatna (JointJS+/Rappid):** Większość zaawansowanych gotowych komponentów UI (palety drag-and-drop, minimapy, inspektory właściwości, ulepszone routingi) znajduje się w komercyjnym pakiecie JointJS+.

## Odnośniki
- Alternatywa: [[react-flow]]
- Wzorzec: [[infinite-canvas-architecture]]
- Decyzja ADR: [[2026-08-06-diagramming-engine-react-flow-vs-jointjs]]
