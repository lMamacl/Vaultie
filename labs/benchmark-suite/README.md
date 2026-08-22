# Epistemic A/B Benchmark Suite

Pakiet referencyjny 10 zadań programistycznych do ślepej ewaluacji porównawczej: **Zwykły Agent ReAct (Wariant A)** vs **Epistemic Coding Agent Tier 1 (Wariant B)**.

---

## 1. Cel Metodologiczny

Weryfikacja empiryczna, czy protokół epistemiczny (`Investigator -> Prior Art -> Planner -> Adversarial Critic -> Grounded Test Verification`) osiąga wyższy wskaźnik Pass@1 i eliminuje halucynacje wersji bibliotek (API Drift) w porównaniu do standardowego agenta jednoukładowego.

---

## 2. Instrukcja Przeprowadzenia Ślepego Testu (Dla Nowych Czatów)

> [!IMPORTANT]
> Aby zachować 100% obiektywizmu, testy należy uruchomić w **nowych, czystych oknach czatu** (oddzielna instancja dla Wariantu A i Wariantu B), aby uniknąć zanieczyszczenia kontekstu (Context Contamination).

### Przebieg Wariantu A (Grupa Kontrolna — Czysty ReAct):
1. Otwórz nowy czat w IDE.
2. Wydaj polecenie:
   ```text
   Przejdź do labs/benchmark-suite/task-01-api-drift/. Uruchom 'python test_task.py', zdiagnozuj błąd i napraw kod w 'solution.py' tak, aby test przeszedł na zielono.
   ```
3. Zarejestruj: liczbę prób, czas, zużycie tokenów i czy agent użył przestarzałego API.

### Przebieg Wariantu B (Grupa Badawcza — Epistemic Agent):
1. Otwórz nowy czat w IDE.
2. Wydaj polecenie:
   ```text
   Uruchom kb-epistemic-solve dla zadania w labs/benchmark-suite/task-01-api-drift/. Napraw błąd w 'solution.py' tak, aby test 'python test_task.py' przeszedł na zielono.
   ```
3. Zarejestruj: stan pliku `state.json`, wykorzystanie Context7/Exa, wynik krytyki i ostateczny status testu.

---

## 3. Zestaw Zadań w Piaskownicy

| ID | Katalog | Typ Problemu | Wymagane Źródło Prawdy |
|---|---|---|---|
| **01** | `task-01-api-drift` | API Drift: Metody Pydantic v2 / TanStack Query | Odpytanie Context7 o aktualne API |
| **02** | `task-02-root-cause-auth` | Zależność Upstream: Błąd autoryzacji w Token Generatorze | Root Cause Analysis zamiast maskowania błędu |
| **03** | `task-03-retry-backoff` | Brakujący Wzorzec: Exponential Backoff z Full Jitter | Sprawdzenie wzorca w 20_Patterns / Exa |
| **04-10** | `task-04` ... `task-10` | Refaktoryzacja, parsowanie AST, walidacja transakcyjna | Ugruntowane testy jednostkowe |

---

## 4. Automatyczny Runner Ewaluacyjny

Aby uruchomić wszystkie testy jednostkowe w zestawie benchmarkowym:
```bash
python labs/benchmark-suite/run_benchmark.py
```
