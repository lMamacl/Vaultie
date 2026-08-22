---
type: library
title: "Exa Neural Search — Semantyczna Wyszukiwarka Sieciowa i Wyszukiwarka Kodu dla Agentów AI"
created: 2026-08-22
updated: 2026-08-22
tags: [library, mcp, exa, search, semantic-search, code-search, embeddings]
aliases: [Exa, Exa AI, Metaphor]
up: "[[Libraries MOC]]"
---

# Exa Neural Search (Exa AI)

> [!NOTE]
> **Werdykt:** Wiodący silnik wyszukiwania semantycznego zaprojektowany natywnie dla agentów sztucznej inteligencji. W odróżnieniu od klasycznych wyszukiwarek słów kluczowych (Google/Bing opartych na BM25), Exa wykorzystuje modele transformatorowe trenowane na strukturze linków i cytowań, umożliwiając odnajdywanie wzorców kodu i dokumentacji na podstawie intencji semantycznej.

## 1. Architektura i Różnice Względem Wyszukiwarek Tradycyjnych

```
┌────────────────────────────────────────────────────────────────────────┐
│                   BM25 (Google/Bing) vs. EXA EMBEDDINGS                │
├──────────────────────────────────┬─────────────────────────────────────┤
│ Tradycyjne Wyszukiwanie Słów     │ Wyszukiwanie Semantyczne Exa        │
├──────────────────────────────────┼─────────────────────────────────────┤
│ Dopasowuje dokładne frazy        │ Dopasowuje znaczenie i kontekst     │
│ Podatne na spam SEO i reklamy    │ Oparte na autorytecie linków GitHub │
│ Zwraca fragmenty HTML (snippets) │ Zwraca czysty Markdown / kod źródła │
└──────────────────────────────────┴─────────────────────────────────────┘
```

---

## 2. Dostępne Narzędzia w Serwerze MCP Exa

Serwer MCP udostępniany przez Exa pod adresem `https://mcp.exa.ai/mcp` oferuje wyspecjalizowany zestaw narzędzi:

1. `web_search_exa`: Podstawowe wyszukiwanie semantyczne z obsługą domen, dat i filtrów treści.
2. `get_code_context_exa` / `web_search_advanced_exa`: Narzędzie wyszukiwania fragmentów kodu, sygnatur funkcji i implementacji w publicznych repozytoriach GitHub i StackOverflow.
3. `crawling / deep researcher` (opcjonalne): Wielostopniowe podążanie za powiązaniami.

---

## 3. Konfiguracja Klienta MCP

```json
{
  "mcpServers": {
    "exa": {
      "type": "streamable-http",
      "url": "https://mcp.exa.ai/mcp?tools=web_search_exa,get_code_context_exa"
    }
  }
}
```

Dla autoryzacji z wyższymi limitami zapytań dodaje się nagłówek z kluczem API:
```json
{
  "headers": {
    "x-api-key": "${EXA_API_KEY}"
  }
}
```

---

## 4. Zastosowanie w Pętli Epistemicznej Vaultie

* **Faza Prior Art Search:** Wyszukiwanie sprawdzonych implementacji algorytmów na GitHubie przed rozpoczęciem pisania kodu od zera.
* **Eksploracja Międzytematyczna (Cross-Domain):** Odnajdywanie analogicznych wzorców inżynierskich w innych ekosystemach technologicznych (np. "jak w Rust zarządza się buforowaniem w porównaniu z Node.js Streams").

---

## Powiązane Notatki
- Standard MCP: [[mcp-protocol]]
- Ugruntowanie w Dokumentacji: [[context7]]
- Wzorzec Pętli: [[epistemic-reasoning-loop]]
- Decyzja Architektoniczna: [[2026-08-22-epistemic-coding-agent-architecture]]
