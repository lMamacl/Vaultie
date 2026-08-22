---
type: decision
title: "Architektura Epistemicznego Agenta Kodującego: Wdrożenie Tier 1 MVP i Integracja MCP vs Odrzucenie 6-Silnikowego Molocha"
created: 2026-08-22
updated: 2026-08-22
tags: [adr, architecture, agents, epistemic, mcp, reasoning, decision]
aliases: [ADR-003 Epistemic Coding Agent Architecture]
up: "[[Decisions MOC]]"
status: accepted
supersedes: ""
affects: ["System Rozumowania Agenta", "Ekosystem Vaultie", "Baza Wiedzy", "Laboratoria Labs"]
---

# Architektura Epistemicznego Agenta Kodującego: Wdrożenie Tier 1 MVP i Integracja MCP

## Kontekst i Problem Decyzyjny

Tradycyjne modele agentów programistycznych (reaktywny ReAct / jednoprzebiegowy prompting) wykazują krytyczne ograniczenia poznawcze:
1. **Pochopne działanie (Premature Action):** Natychmiastowe modyfikowanie kodu bez zbadania fundamentalnych niewiadomych,
2. **Ignorowanie zależności (Causal Blindness):** Próba łatania objawu zamiast przyczyny źródłowej (Root Cause),
3. **Zjawisko API Drift:** Halucynowanie nieaktualnych sygnatur metod i przestarzałych wzorców bibliotek zewnętrznych,
4. **Brak ugruntowania wykonawczego:** Poleganie na werbalnej samousprawiedliwiającej się autorefleksji zamiast na twardym wyniku testów i kompilatora.

Otrzymano propozycję budowy zaawansowanego systemu opartego na 6 oddzielnych "silnikach" (Investigator, Planner, Challenger, Executor, Verifier, Problem Parser) z numerycznymi wskaźnikami pewności (`confidence: 0.94`) oraz wielomiesięczną persystencją grafu problemu w bazie danych.

---

## Analiza Opcji Architektonicznych

### Opcja 1: Pełna Implementacja 6-Silnikowej Architektury Koncepcyjnej
- **Charakterystyka:** 6 wywołań LLM w sekwencji, numeryczny wzór przyrostu informacji, baza grafowa dla problemów.
- **Wady:** 300–500% wyższy koszt obliczeniowy, wysoka latencja (60–120s na krok), podatność na wspólne martwe punkty poznawcze tego samego modelu bazowego, fikcyjna kalibracja liczb pewności.

### Opcja 2: Status Quo (Standardowy Agent ReAct bez Protokołu Epistemicznego)
- **Charakterystyka:** Standardowe zapytania do modeli, poleganie na bieżącej pamięci roboczej.
- **Wady:** Częste regresje w kodzie, brak dyscypliny weryfikacji dokumentacji, wysokie ryzyko wprowadzania halucynacji do bazy wiedzy.

### Opcja 3: Architektura Pragmatyczna (Tier 1 MVP + Elementy Tier 2 i Protokół MCP) — WYBRANA
- **Charakterystyka:**
  - Redukcja ról do deterministycznej maszyny stanów: **Investigator (Triage niewiadomych) $\to$ Prior Art Search (Exa/Context7) $\to$ Planner $\to$ Adversarial Critic $\to$ Grounded Execution (Kompilator/Testy)**.
  - Zastąpienie liczb trójstanową logiką prawdy: `verified / inferred / assumed`.
  - Twardy budżet w kodzie Pythona (max 3 iteracje, max 10 wywołań narzędzi).
  - Integracja serwerów MCP **Exa** (kod i semantyka) oraz **Context7** (eliminacja API drift).
  - Deterministyczne guardraile regex dla bezpieczeństwa powłoki.

---

## Decyzja i Uzasadnienie

Przyjęto do realizacji **Opcję 3 (Architektura Pragmatyczna Tier 1 + 2)**.

### Główne Czynniki Decyzyjne:
1. **Rygor Dowodowy:** Z badań (Reflexion, CRITIC, SWE-bench) wynika jednoznacznie, że fizyczne uruchomienie testu jednostkowego daje wielokrotnie silniejszy sygnał epistemiczny niż jakakolwiek liczba rund werbalnej autorefleksji LLM.
2. **Efektywność Kosztowa:** Ograniczenie sekwencji do 1 kroku krytyka i 1 tury ugruntowania eliminuje zjawisko *Multi-Agent Compute Tax* przy zachowaniu 80% korzyści poznawczych.
3. **Kompatybilność z Vaultie:** Płaski model stanu (`state.json` / Markdown w `00_Inbox/_proposals/`) idealnie mapuje się na strukturę repozytorium.

---

## Konsekwencje i Zobowiązania

### Pozytywne:
- Całkowita eliminacja halucynacji wersji API dzięki Context7 MCP.
- Znaczący wzrost wskaźnika Pass@1 w trudnych zadaniach inżynierskich.
- Bezpieczeństwo bazy wiedzy Vaultie przed zaśmieceniem niesprawdzonymi faktami.

### Wymagane Działania:
- Skonfigurowanie serwerów MCP Exa i Context7 w środowisku.
- Opracowanie skilla `.agent/skills/kb-epistemic-solve/`.
- Wdrożenie skryptu kontrolera `.agent/scripts/epistemic_runner.py`.

---

## Powiązane Notatki
- Wzorzec Architektoniczny: [[epistemic-reasoning-loop]]
- Koncepcja Metapoznania: [[epistemic-agency]]
- Tryby Awarii Agentów: [[agentic-failure-modes]]
- Standard MCP: [[mcp-protocol]]
- Narzędzie Context7: [[context7]]
- Narzędzie Exa Search: [[exa-search]]
- Pełny Dokument Zbiorczy: [[00-MASTER-SYNTHESIS-AND-VERDICT]]
