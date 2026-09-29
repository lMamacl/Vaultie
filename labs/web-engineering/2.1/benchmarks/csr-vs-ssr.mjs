// Lab 2.1 — Symulacja i Pomiar: CSR vs SSR vs Podatek Hydracji
// Porównanie narzutu sieciowego, czasu generowania oraz zjawiska Data Doubling.

import { performance } from 'node:perf_hooks';

console.log('='.repeat(65));
console.log('  LAB 2.1: BENCHMARK RENDEROWANIA — CSR VS SSR VS HYDRACJA');
console.log('='.repeat(65));
console.log('');

// 1. Generator danych testowych (10 000 transakcji bankowych)
function generateTransactions(count = 10_000) {
  const list = [];
  for (let i = 1; i <= count; i++) {
    list.push({
      id: `TX-${i.toString().padStart(6, '0')}`,
      date: '2026-09-28',
      amount: (Math.random() * 1000).toFixed(2),
      currency: 'PLN',
      status: i % 5 === 0 ? 'PENDING' : 'COMPLETED',
      recipient: `Kontrahent ${i} Sp. z o.o.`
    });
  }
  return list;
}

const data = generateTransactions(5_000);

// --- SCENARIUSZ A: CSR (Client-Side Rendering) ---
console.log('[SCENARIUSZ A] Client-Side Rendering (CSR / SPA):');
const startCsr = performance.now();
const csrHtml = `<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>Bank Dashboard (CSR)</title>
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
  <div id="root"></div>
  <script src="/assets/app-bundle.js"></script>
</body>
</html>`;
const endCsr = performance.now();
const csrPayloadBytes = Buffer.byteLength(csrHtml, 'utf-8');
const csrServerTime = (endCsr - startCsr).toFixed(3);

console.log(`  -> Czas generowania na serwerze:   ${csrServerTime} ms`);
console.log(`  -> Rozmiar HTML z serwera:         ${(csrPayloadBytes / 1024).toFixed(2)} KB`);
console.log(`  -> FCP (Widoczna treść):           Opóźniony (pusty ekran do pobrania app-bundle.js)`);
console.log(`  -> Narzut procesora serwera:       Znikomy (~0 CPU)`);
console.log('');

// --- SCENARIUSZ B: SSR (Server-Side Rendering z pełną hydracją) ---
console.log('[SCENARIUSZ B] Server-Side Rendering (SSR + Hydration State):');
const startSsr = performance.now();

// 1. Serwer generuje pełną tabelę HTML
let rowsHtml = '';
for (const tx of data) {
  rowsHtml += `<tr><td>${tx.id}</td><td>${tx.date}</td><td>${tx.amount} ${tx.currency}</td><td>${tx.status}</td><td>${tx.recipient}</td></tr>`;
}

// 2. Serwer serializuje ten sam stan do JSON, aby klient mógł go zhydratować (Data Doubling)
const stateJson = JSON.stringify(data);

const ssrHtml = `<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>Bank Dashboard (SSR)</title>
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
  <div id="root">
    <h1>Historia Transakcji</h1>
    <table>
      <thead><tr><th>ID</th><th>Data</th><th>Kwota</th><th>Status</th><th>Odbiorca</th></tr></thead>
      <tbody>${rowsHtml}</tbody>
    </table>
  </div>
  <script id="__NEXT_DATA__" type="application/json">${stateJson}</script>
  <script src="/assets/app-bundle.js"></script>
</body>
</html>`;
const endSsr = performance.now();

const ssrPayloadBytes = Buffer.byteLength(ssrHtml, 'utf-8');
const htmlOnlyBytes = Buffer.byteLength(rowsHtml, 'utf-8');
const stateOnlyBytes = Buffer.byteLength(stateJson, 'utf-8');
const ssrServerTime = (endSsr - startSsr).toFixed(2);

console.log(`  -> Czas renderowania na serwerze:   ${ssrServerTime} ms (Koszt CPU per żądanie!)`);
console.log(`  -> Całkowity rozmiar strony HTML:   ${(ssrPayloadBytes / 1024).toFixed(2)} KB`);
console.log(`     - Sam kod tabeli HTML:           ${(htmlOnlyBytes / 1024).toFixed(2)} KB`);
console.log(`     - Stan JSON (Data Doubling):     ${(stateOnlyBytes / 1024).toFixed(2)} KB`);
console.log(`  -> FCP (Widoczna treść):            Błyskawiczny (użytkownik widzi dane natychmiast)`);
console.log(`  -> TTI (Czas do klikalności):       Wstrzymany do zparsowania JSON i hydracji DOM`);
console.log('');

// Podsumowanie
console.log('PODSUMOWANIE INŻYNIERYJNE:');
console.log(`1. W SSR serwer wysyła ${(ssrPayloadBytes / csrPayloadBytes).toFixed(0)}x WIĘCEJ danych przez sieć niż w CSR.`);
console.log(`2. Zjawisko DATA DOUBLING: ${((stateOnlyBytes / ssrPayloadBytes) * 100).toFixed(0)}% wagi HTML-a w SSR to ten sam stan powtórzony jako JSON dla hydracji.`);
console.log('3. Wniosek: Dla dashboardu za logowaniem CSR (SPA) oszczędza CPU serwera i transfer.');
console.log('   SSR stosuj tam, gdzie kluczowe jest SEO i pierwszy podgląd dla robotów wyszukiwarek.');
console.log('='.repeat(65));
