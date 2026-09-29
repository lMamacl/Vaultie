# Lab 2.1 — Paradygmaty Renderowania, Mostek WASM i Runtimes Desktopowe

Laboratorium do lekcji **[[2.1/2.1-website-vs-webapp-rendering-runtimes|Lekcja 2.1 — Website vs Web App, Paradygmaty Renderowania i Środowiska Wykonawcze]]**.  
Kanwa wizualna: **[[lesson-2.1-rendering-runtimes.canvas]]**

---

## Cel ćwiczenia

W tym laboratorium doświadczalnie weryfikujesz mechanizmy wykonawcze:
1. **Zmierzenie narzutu mostka WASM (Bridge Latency Collapse):** Porównanie czasu obliczeń prostych operacji w czystym JavaScript (V8 JIT) z WebAssembly oraz zaobserwowanie zapaści wydajnościowej, gdy funkcja WASM jest wywoływana w pętli z poziomu JS.
2. **Pomiar podatku hydracji i Data Doubling (CSR vs SSR):** Zmierzenie różnicy w czasie generowania na serwerze, rozmiarze transferu sieciowego oraz zjawiska powtórzonego stanu JSON (`<script id="__NEXT_DATA__">`) dla tabeli 5 000 rekordów.
3. **Wzorzec bezpiecznego kontraktu IPC dla Desktopu:** Zbadanie architektonicznego kontraktu TypeScript dla mostków IPC w Electronie (Preload script z `contextBridge`) oraz Tauri v2 (Rust `invoke`).

---

## Struktura katalogu

```text
labs/web-engineering/2.1/
├── README.md                           # Ten plik z opisem i checklistą DoD
├── package.json                        # Skrypty uruchomieniowe (zero ciężkich zależności)
└── benchmarks/
    ├── wasm-bridge.mjs                 # Benchmark JS JIT vs WASM vs Narzut Mostka
    ├── csr-vs-ssr.mjs                  # Benchmark symulacyjny CSR vs SSR (TTFB / Data Doubling)
    └── ipc-contract.ts                 # Wzorzec bezpiecznego kontraktu IPC dla Desktopu
```

---

## Szybki start (uruchomienie benchmarków)

Wymagany jest wyłącznie zainstalowany **Node.js** (v18+ / v20+ / v24+):

```bash
cd labs/web-engineering/2.1

# Uruchomienie pełnego pakietu benchmarków:
npm test

# Lub niezależne uruchamianie poszczególnych skryptów:
npm run bench:wasm      # node benchmarks/wasm-bridge.mjs
npm run bench:render    # node benchmarks/csr-vs-ssr.mjs
```

---

## Co sprawdzić w wynikach benchmarków:

1. **W `wasm-bridge.mjs`:**
   - Obserwacja: pętla 10 000 000 wywołań prostej funkcji dodawania w WASM przez FFI wykonuje się ~5x wolniej niż w V8 Inlined JIT.
   - Wyjaśnienie: narzut marshalingu argumentów i zmiana kontekstu przewyższają czas trwania samej instrukcji procesora.
   - Wniosek: WASM stosujemy dla przetwarzania buforów danych (np. `Float32Array`) w jednym kawałku, a nie dla mikro-wywołań.
2. **W `csr-vs-ssr.mjs`:**
   - Obserwacja: SSR generuje stronę ważącą >1.2 MB w porównaniu do 0.25 KB szkieletu CSR.
   - Wyjaśnienie: ponad 50% wagi strony SSR stanowi powtórzony obiekt JSON ze stanem tabeli (zjawisko **Data Doubling**), który jest niezbędny, by klient mógł zrekonstruować stan komponentów podczas hydracji.
   - Wniosek: dla aplikacji za logowaniem (ERP, CRM, dashboardy) czyste CSR na Vite oszczędza transfer i odciąża procesor serwera.

---

## Definition of Done (DoD)

Ćwiczenie uważa się za zaliczone, gdy spełnione są poniższe kryteria akceptacji:

- [x] **Wykonanie testów:** Polecenie `npm test` wykonuje się bezbłędnie (kod wyjścia 0) i wypisuje wyniki obu benchmarków.
- [x] **Zrozumienie mostka WASM:** Potrafisz wyjaśnić, dlaczego drobne wywołania FFI są wolniejsze od JIT-a oraz jak zorganizować przepływ pamięci przez `SharedArrayBuffer` / `TypedArray`.
- [x] **Zrozumienie podatku hydracji:** Potrafisz wskazać różnicę między FCP a TTI w SSR oraz wymienić 3 inżynieryjne koszty procesu hydracji (Data Doubling, zużycie CPU na urządzeniach mobilnych, ryzyko Hydration Mismatch).
- [x] **Bezpieczeństwo IPC:** Rozumiesz, dlaczego w Electronie zabronione jest `nodeIntegration: true` i jak `contextBridge` chroni aplikację przed atakami XSS.
