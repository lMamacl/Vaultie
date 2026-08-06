# kb-canvas — generowanie wizualnych tablic Obsidian Canvas (.canvas)

## Cel
Automatyczne generowanie interaktywnych plików schematów wizualnych w natywnym formacie Obsidian Canvas (`.canvas`) do graficznego prezentowania powiązań między bibliotekami, wzorcami architektonicznymi oraz decyzjami ADR.

## Kiedy użyć
- Gdy użytkownik prosi: "stwórz wizualną tablicę", "wygeneruj canvas", "zrób schemat graficzny w Obsidian Canvas".
- Przy tworzeniu zestawień przeglądowych dla notatek w `10_Libraries/`, `20_Patterns/` czy `30_Decisions/`.

## Format Pliku `.canvas` (JSON Spec)
Pliki `.canvas` w Obsidianie to zwykły plik JSON zawierający tablice `nodes` oraz `edges`:

```json
{
  "nodes": [
    {
      "id": "node1",
      "type": "file",
      "file": "10_Libraries/react-flow.md",
      "x": 0,
      "y": 0,
      "width": 300,
      "height": 200
    },
    {
      "id": "node2",
      "type": "file",
      "file": "10_Libraries/jointjs.md",
      "x": 400,
      "y": 0,
      "width": 300,
      "height": 200
    },
    {
      "id": "node3",
      "type": "text",
      "text": "## Porównanie Silników Renderowania\n- React Flow: DOM/JSX\n- JointJS: Engine/SVG",
      "x": 200,
      "y": 260,
      "width": 350,
      "height": 160
    }
  ],
  "edges": [
    {
      "id": "edge1",
      "fromNode": "node1",
      "fromSide": "right",
      "toNode": "node2",
      "toSide": "left",
      "label": "alternatywa"
    }
  ]
}
```

## Kroki Execution
1. **Identyfikacja Notatek:** Zbierz wybrane pliki `.md`, które mają znaleźć się na tablicy.
2. **Kalkulacja Współrzędnych (Grid Layout):** Wyznacz pozycje `x` i `y` dla każdego węzła (z zachowaniem odstępów min. 80px).
3. **Stworzenie Połączeń (Edges):** Odczytaj wikilinki `[[...]]` z frontmattera oraz treści notatek i stwórz krawędzie `edges` łączące id węzłów.
4. **Zapis Pliku Canvas:** Zapisz plik z rozszerzeniem `.canvas` (np. `90_Meta/canvases/Diagramming-Engines.canvas` lub bezpośrednio w odpowiednim folderze).
5. **Kompilacja i Raport:** Poinformuj użytkownika o wygenerowaniu tablicy ze wskazaniem ścieżki do otwarcia w Obsidianie.

## Input
- Wskazanienotatek lub MOC (np. `Libraries MOC`, `React Flow vs JointJS`).

## Output
- Nowy plik `.canvas` w katalogu `90_Meta/canvases/` lub we wskazanym folderze dziedzinowym.

## Guardrails
- Dbaj o unikanie nachodzenia na siebie węzłów (kalkulacja $x, y$ na siatce).
- Używaj typów `file` dla notatek z vaulta i typów `text` dla nagłówków/notatek pomocniczych.

## Warianty
- Brak.
