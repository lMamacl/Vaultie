---
type: proposal
title: "Integracja Prime Agent Harness & Python-Executable Skills z Vaultie"
created: 2026-08-11
updated: 2026-08-11
tags: [proposal, prime-agent, architecture, python-skills, harness]
up: "[[90_Meta/_index]]"
---

# Proposal: Integracja Prime Agent Harness & Architektura Hybrydowa dla Vaultie

## 1. Kontekst & Problem

Współczesne systemy agentowe borykają się z **przeładowaniem okna kontekstowego (Context Window Bloat)**. Tradycyjne skille zdefiniowane wyłącznie w Markdownie zmuszają LLM do przetwarzania setek linii instrukcji, co zmniejsza precyzję modelu i podnosi koszty.

**Prime Agent Harness** (od Prime Intellect) rozwiązuje ten problem poprzez:
- **IPython REPL Kernel**: Skille są wywoływanym kodem Pythona (`await skill.run()`), a nie wielkimi prompami tekstu.
- **Stan Trwały Harnessu**: $H = (\rho, G, K, M)$ (System prompt, Sub-agents, Skills, Memory) z pętlą samodoskonalenia `/refine`.
- **Sub-agenci jako funkcje**: Delegowanie zadań odbywa się asynchronicznie poprzez funkcje w REPL (`await rlm(...)`).

---

## 2. Architektura Hybrydowa: Antigravity + Prime Agent

Przeanalizowaliśmy oficjalną strukturę kodu `PrimeIntellect-ai/prime-agent`. Wynika z niej idealny podział ról w ekosystemie Vaultie:

```
+-----------------------------------------------------------------------+
|                            ANTIGRAVITY IDE                            |
|             (Główny Architekt & Pair Programmer w GUI)                |
|  - Tworzy specyfikacje, przegląda diffy, rozmawia z użytkownikiem    |
|  - Zarządza strukturą wiedzy w 10_-50_ i decyzjami ADR                |
+-----------------------------------+-----------------------------------+
                                    |
                 Wywołanie przez run_command / MCP Bridge
                                    |
                                    v
+-----------------------------------------------------------------------+
|                         PRIME AGENT HARNESS                           |
|            (Autonomiczny Silnik Sandbox & REPL w tle)                 |
|  - Wykonuje złożone pętle TDD i ćwiczenia w labs/                     |
|  - Wykorzystuje pętlę /refine do uczenia się i zapisu wniosków       |
|  - Działa w odizolowanym terminalu/konkontenerze                     |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                    WSPÓLNA WARSTWA NAWIGACJI (.agent/)                |
|  - `.agent/scripts/*.py` — Skrypty Pythonowe jako skille (wykonawcze) |
|  - `.agent/AGENTS.md` — Jedno źródło prawdy o regułach vaulta        |
+-----------------------------------------------------------------------+
```

---

## 3. Zastosowanie Python-Executable Skills w Vaultie

Każdy skrypt w `.agent/scripts/` (jak istniejący `vaultie-cli.py`) staje się **wykonawczym skillem**:

1. **`vaultie-cli.py lint`**: Deterministyczny audyt linków Wikilinks, braku frontmattera i sierot.
2. **`vaultie-cli.py plan`**: Generowanie atomowych planów transakcyjnych SHA-256 przed zapisem do `10_`–`50_`.
3. **Nowy `vaultie-certify.py`**: Automatyczna weryfikacja zgodności lekcji z *Lesson Quality Contract v1*.

---

## 4. Plan Wdrożenia (Action Plan)

1. **Instalacja CLI Prime Agent**:
   ```bash
   curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
   ```
2. **Uruchamianie zadań tle z poziomu Antigravity**:
   Wykonywanie autonomicznych serii testowych w `labs/` przez `run_command` w tle.
3. **Ekspansja `.agent/scripts/`**:
   Przenoszenie ciężkich procedur weryfikacyjnych z tekstu promptów do czystego Pythona.
