---
type: library
title: "React Flow (@xyflow/react)"
created: 2026-08-06
updated: 2026-08-06
tags: [react, diagramming, ui-library, infinite-canvas, graph-visualization]
aliases: [XYFlow, ReactFlow]
up: "[[Libraries MOC]]"
lib: "@xyflow/react"
ecosystem: js
version: "12.0.0"
verdict: adopt
alternatives: ["jointjs", "tldraw", "gojs", "konva"]
confidence: high
used_in: ["Edytor Przepływów", "Diagramy Interaktywne"]
---

<!-- AI-INSTRUCTIONS
Zasady dotyczące notatki biblioteki React Flow:
- Opisuj dokładnie podejście DOM-based i wyzwania przy dużej skali.
- Podawaj gotchas związane z wirtualizacją i niepotrzebnymi re-renderami.
-->

# React Flow (@xyflow/react)

Wysoce dostosowywalna biblioteka React do tworzenia interaktywnych edytorów grafów, schematów blokowych i interfejsów typu nieskończone pole (infinite canvas).

## Podsumowanie i Verdict

- **Verdict:** `adopt` — Domyślny i najlepszy wybór dla projektów opartych na React, gdzie priorytetem jest szybki czas wytwarzania (DX), bogaty interfejs użytkownika wewnątrz węzłów oraz natywna dostępność (A11y).
- **Zastosowanie:** Edytory workflow (np. n8n, Langflow), wyznaczniki procesów, interaktywne panele edycji logiki.

## Kluczowa Architektura i API

React Flow opiera swoje renderowanie na natywnych elementach HTML/SVG zarządzanych bezpośrednio przez drzewo komponentów Reacta:

```tsx
import React, { useCallback } from 'react';
import { ReactFlow, useNodesState, useEdgesState, addEdge } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

const initialNodes = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'Klasa UML 1' } },
  { id: '2', position: { x: 0, y: 150 }, data: { label: 'Klasa UML 2' } },
];

export function UMLCanvas() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onlyRenderVisibleElements={true}
      />
    </div>
  );
}
```

## Pułapki i Gotchas (Performance & Scaling)

1. **Wąskie gardło przy 10 000 węzłach:** Ponieważ każdy węzeł to natywny element DOM Reacta, przy > 1000 węzłach bez wirtualizacji wydajność drastycznie spada.
2. **"Pułapka Pomniejszenia" (Zoom-Out Trap):** Włączenie `onlyRenderVisibleElements={true}` odciąża przeglądarkę tylko wtedy, gdy rzutnia pokazuje fragment wykresu. Przy maksymalnym pomniejszeniu (Zoom Out), gdy w rzutni widać 10k obiektów, wirtualizacja ulega wyłączeniu i następuje spadek płynności FPS.
3. **Memoizacja Węzłów:** Niestandardowe komponenty węzłów **muszą być opakowane w `React.memo`**, a procedury obsługi zdarzeń w `useCallback`, inaczej każda zmiana stanu układu powoduje masowe re-rendery całego drzewa.

## Odnośniki
- Alternatywa: [[jointjs]]
- Wzorzec: [[infinite-canvas-architecture]]
- Decyzja ADR: [[2026-08-06-diagramming-engine-react-flow-vs-jointjs]]
