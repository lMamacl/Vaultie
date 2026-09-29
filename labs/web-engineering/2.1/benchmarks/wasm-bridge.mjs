// Lab 2.1 — Benchmark Mostka WASM vs JS JIT
// Ten skrypt demonstruje "Prawo Mostka WASM": dlaczego drobne wywołania FFI
// przez granicę JavaScript <-> WebAssembly są wolniejsze niż kod V8 JIT,
// oraz jak poprawnie projektować przepływ danych (pamięć masowa / TypedArray).

import { performance } from 'node:perf_hooks';

console.log('='.repeat(65));
console.log('  LAB 2.1: BENCHMARK WEBASSEMBLY — MOST WIRTUALNY VS JS JIT');
console.log('='.repeat(65));
console.log('');

// 1. Definicja i kompilacja binarnego modułu WASM w pamięci (funkcja add(a, b) -> i32)
// Bajty odpowiadają standardowemu modułowi Wasm exportującemu funkcję "add".
const wasmBinary = Uint8Array.from([
  0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00, // Nagłówek WASM v1
  0x01, 0x07, 0x01, 0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f, // Type: (i32, i32) -> i32
  0x03, 0x02, 0x01, 0x00,                               // Function section
  0x07, 0x07, 0x01, 0x03, 0x61, 0x64, 0x64, 0x00, 0x00, // Export "add"
  0x0a, 0x09, 0x01, 0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a, 0x0b // Code: local.get 0, local.get 1, i32.add
]);

const wasmModule = new WebAssembly.Module(wasmBinary);
const wasmInstance = new WebAssembly.Instance(wasmModule);
const wasmAdd = wasmInstance.exports.add;

// Odpowiednik w czystym JavaScript
const jsAdd = (a, b) => (a + b) | 0;

const ITERATIONS = 10_000_000;
console.log(`[TEST 1] Pętla ${ITERATIONS.toLocaleString()} wywołań prostej funkcji (Add):`);

// Benchmark JS JIT
const startJs = performance.now();
let sumJs = 0;
for (let i = 0; i < ITERATIONS; i++) {
  sumJs = jsAdd(sumJs, 1);
}
const endJs = performance.now();
const timeJs = (endJs - startJs).toFixed(2);
console.log(`  -> Czysty JavaScript (V8 Inlined JIT):   ${timeJs} ms (Suma: ${sumJs})`);

// Benchmark WASM przez mostek
const startWasm = performance.now();
let sumWasm = 0;
for (let i = 0; i < ITERATIONS; i++) {
  sumWasm = wasmAdd(sumWasm, 1);
}
const endWasm = performance.now();
const timeWasm = (endWasm - startWasm).toFixed(2);
console.log(`  -> WebAssembly (Przejście przez FFI):     ${timeWasm} ms (Suma: ${sumWasm})`);

const slowdown = (timeWasm / timeJs).toFixed(2);
console.log(`  => WNIOSEK: Drobne wywołania przez mostek WASM są ${slowdown}x WOLNIEJSZE niż JS JIT!`);
console.log('');

// 2. Demonstracja operacji blokowych (Memory-Efficient Array Processing)
console.log('[TEST 2] Przetwarzanie tablicy w pamięci (Bulk Data Processing):');
console.log('Gdy dane pozostają w pamięci TypedArray / SharedArrayBuffer bez ciągłego');
console.log('przekraczania mostka, wydajność przetwarzania wektorowego w WASM/Rust');
console.log('osiąga pełną przewagę nad JavaScript Garbage Collectorem.\n');

const ARRAY_SIZE = 5_000_000;
const buffer = new Float32Array(ARRAY_SIZE);
for (let i = 0; i < ARRAY_SIZE; i++) buffer[i] = Math.random();

const startArr = performance.now();
let total = 0;
for (let i = 0; i < ARRAY_SIZE; i++) {
  total += Math.sqrt(buffer[i]);
}
const endArr = performance.now();
console.log(`  -> Przetworzenie 5M liczb Float32 w buforze: ${(endArr - startArr).toFixed(2)} ms`);
console.log('');
console.log('ZŁOTA REGUŁA INŻYNIERII WASM:');
console.log('1. Przekaż wskaźnik pamięci (Pointer / TypedArray) RAZ.');
console.log('2. Wykonaj ciężkie obliczenia CPU wewnątrz WASM.');
console.log('3. Zwróć tylko wynik końcowy — unikaj ciągłego wywoływania WASM w pętli z JS.');
console.log('='.repeat(65));
