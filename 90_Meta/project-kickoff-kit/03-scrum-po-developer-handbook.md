---
type: concept
title: "Podręcznik Operacyjny: Procedury Obronne dla Rotującego PO i Dewelopera"
created: 2026-09-29
updated: 2026-09-29
tags: [meta, project-kickoff, scrum, jira, confluence, bitbucket, po-handbook]
up: "[[90_Meta/_index]]"
---

# Podręcznik Operacyjny: Procedury Obronne dla Rotującego PO i Dewelopera

> [!CAUTION]
> **Zasada Główna Oceniania:**
> Prowadzący ocenia **wyłącznie dowody utrwalone w Jira, Confluence i Bitbucket**.
> Niezrealizowanie zadania = obniżenie oceny o **1.0**.
> Nieterminowe lub niepełne zrealizowanie = obniżenie oceny o **0.5**.
> Koszt niezrealizowanego zadania deweloper może spróbować przerzucić na Ciebie (jako PO), twierdząc, że zadanie było nierealistyczne. Poniższy podręcznik zawiera żelazne procedury, które chronią Twoją ocenę **bdb**.

---

## 🛡️ Część 1: Tarcza Obronna Product Ownera (Procedura Anty-Spychologiczna)

Jeśli w Twoim sprincie którykolwiek z deweloperów nie dowiezie zadania i spróbuje wnioskować do prowadzącego o przeniesienie kary na PO, musisz posiadać **zamknięty łańcuch dowodowy**:

```
[PLANNING]                               [W TRAKCIE SPRINTU]                     [REVIEW / RETRO]
Deweloper zatwierdza estymację           Brak zgłoszenia blokera                 Zadanie niedowiezione:
w komentarzu Jira (<= 4h)       ----->   w raportach Daily w Confluence ----->   Wina dewelopera w 100%!
                                                                                 PO zachowuje ocenę BDB.
```

### Krok 1: Żelazna Reguła Rozmiaru Zadania ($\le 4$ godzin)
- Jako PO **nigdy** nie wpuszczasz do sprintu zadania z estymacją większą niż 4 godziny (lub 3 Story Points).
- Jeśli deweloper mówi: *„Muszę napisać cały moduł fakturowania, to zajmie 12 godzin”*, natychmiast rozbijasz to w Jira na podzadania:
  - `NEX-41`: Projekt schematu tabeli faktur i encji (2h)
  - `NEX-42`: Implementacja kalkulatora stawek VAT z testami jednostkowymi (3h)
  - `NEX-43`: Kontroler API wystawiania faktury z walidacją DTO (3h)
  - `NEX-44`: Prosty widok podglądu faktury w UI (4h)
- **Zysk PO:** Nawet jeśli deweloper utknie na widoku UI (`NEX-44`), zadania `41`, `42` i `43` są zamknięte jako `DONE`! Deweloper traci punkty tylko za 1 małe zadanie, a nie za całą funkcjonalność.

### Krok 2: Formuła Potwierdzenia Realizmu na Planningu (Podpis Dewelopera)
Podczas ceremonii Sprint Planningu, w momencie przypisania zadania, deweloper **musi** dodać w zgłoszeniu Jira krótki komentarz:

> *„Potwierdzam zakres zadania, kryteria akceptacji oraz estymację 3.5h jako w pełni realistyczne do wykonania w tym sprincie. [Podpis / Data]”*

Prowadzący (arbiter) widząc taki komentarz, natychmiast odrzuca argument dewelopera, że *„PO narzucił mi nierealistyczny termin”*.

### Krok 3: Zadania Badawcze (*Spike*) na Nieznane Biblioteki
Jeśli deweloper mówi: *„Nigdy nie konfigurowałem biblioteki do generowania PDF / uwierzytelniania OAuth, nie wiem ile to zajmie”*:
- **ZAKAZ:** Nie twórz zadania wdrożeniowego na 10h!
- **NAKAZ:** Utwórz zadanie typu **Spike** na maksymalnie **2 godziny**:
  - *Tytuł:* `NEX-50: [SPIKE] Rozpoznanie biblioteki QuestPDF / konfiguracji OAuth`
  - *Kryterium akceptacji:* Notatka w Confluence z decyzją techniczną (ADR) + miniaturowy prototyp w branchu testowym.
  - Dopiero w kolejnym sprincie planujesz właściwe zadanie wdrożeniowe z precyzyjną estymacją.

---

## 📋 Część 2: Standard Daily Scrum i Szablon Raportu do Confluence (EU2, EU3)

Regulamin wymaga: *„regularne prowadzenie raportu z codziennych spotkań daily scrum”*.

### Krok 2.1: Obieg Informacji (Discord -> Confluence)
1. **Na Discordzie (codziennie do godz. 18:00):** Każdy deweloper wrzuca na kanał `#daily-sync` krótki post:
   - `Co zrobiłem wczoraj:` [Klucze Jira, np. skończyłem NEX-12 (2h)]
   - `Co robię dzisiaj:` [Klucz Jira, np. zaczynam NEX-15 (plan 3h)]
   - `Blokery:` [BRAK lub opis problemu uniemożliwiającego pracę]
2. **W Confluence (raz na 2–3 dni lub pod koniec tygodnia):** PO kopiuje te wpisy do oficjalnego rejestru sprintu.

### Krok 2.2: Gotowy Szablon Raportu Daily w Confluence

```markdown
# 📅 Raport Daily Scrum — Sprint [Numer]
**Właściciel Produktu (PO):** [Imię i Nazwisko]  
**Okres Sprintu:** [Data od] do [Data do]  

---

### Dzień 3 — [YYYY-MM-DD]
*Forma spotkania:* Asynchroniczna (Discord `#daily-sync`) + 10-minutowy call głosowy.  
*Obecność:* 6/6 członków zespołu.

| Członek Zespołu | Zrealizowane zadania (ostatnie 24h) | Planowane zadania (kolejne 24h) | Zgłoszone Blokery / Uwagi |
|---|---|---|---|
| Jan Kowalski | Zakończono walidację DTO (`NEX-21`, 2.5h) | Implementacja serwisu zamówień (`NEX-22`, 3h) | **Brak** |
| Anna Nowak | Konfiguracja migracji bazy danych (`NEX-14`, 3h) | Testy integracyjne repozytorium (`NEX-15`, 2h) | **Brak** |
| Piotr Wiśniewski | Prace nad formularzem (`NEX-30`, 1.5h) | Dokończenie styli widoku (`NEX-30`, 2h) | **Bloker:** Oczekiwanie na schemat DTO od Anny. *Rozwiązanie: Uzgodniono mock interfejsu na Discordzie.* |
| [...] | [...] | [...] | [...] |

---

### Dzień 5 — [YYYY-MM-DD]
[...]
```

> [!TIP]
> **Dlaczego to kluczowe dla oceny BDB:**
> Prowadzący wchodząc na stronę Confluence widzi pełną, chronologiczną historię zaangażowania każdego studenta. Jeśli student nie wpisze się na Daily przez 3 dni, prowadzący obniża mu ocenę za brak realizacji EU2, a PO ma czyste ręce.

---

## 🎯 Część 3: Sprint Review z Użytkownikiem Końcowym (EU1, EU2, EU5)

Regulamin wymaga: *„zrealizowanie każdego z wyznaczonych zadań w kontakcie z końcowym użytkownikiem”* oraz *„pokaz zrealizowanych funkcjonalności”*.

### Agenda Sprint Review (Czas trwania: 30–45 minut)
1. **Wstęp PO (5 min):** Przedstawienie Celu Sprintu (*Sprint Goal*) oraz listy zadań ukończonych (`DONE`) vs nieukończonych.
2. **Prezentacja Działającego Kodu (20 min):** Każdy deweloper osobiście udostępnia ekran i prezentuje działanie swojego modułu w środowisku uruchomieniowym (zakaz prezentowania suchych slajdów PowerPoint!).
3. **Pętla z Użytkownikiem Końcowym (10–15 min):** Użytkownik przekazuje swoje uwagi, zgłasza co jest nieintuicyjne, a PO zapisuje wnioski bezpośrednio do Backlogu Produktu jako nowe User Stories na kolejne sprinty.

### Szablon Protokołu Odbioru przez Użytkownika (Do Confluence)

```markdown
# 🤝 Protokół ze Sprint Review [Numer] z Użytkownikiem Końcowym
**Data:** [YYYY-MM-DD]  
**Uczestnicy:** Zespół projektowy (6 os.) oraz Użytkownik Końcowy: [Imię i Nazwisko / Rola].

### 1. Zaprezentowane Funkcjonalności
- `NEX-EPIC-2`: Wprowadzanie i edycja pozycji katalogowych (prezentował: [Imię Dewelopera])
- `NEX-EPIC-3`: Rejestracja nowego zamówienia w panelu dyspozytora (prezentował: [Imię Dewelopera])

### 2. Informacja Zwrotna Użytkownika Końcowego (Feedback Loop)
- **Co działa znakomicie:** Formularz dodawania pozycji jest bardzo szybki i czytelny na laptopie.
- **Zgłoszone uwagi / Zmiany wymagań:**
  1. *Uwaga:* W liście zamówień brakuje podglądu numeru telefonu klienta bez wchodzenia w szczegóły.
  2. *Wniosek:* PO utworzył zadanie w Backlogu Produktu: `NEX-62: Dodanie kolumny telefon w widoku tabeli zamówień (Estymacja: 1.5h)`.
- **Status akceptacji przyrostu:** Zaakceptowano z uwagami do wdrożenia w Sprincie [Kolejny].
```

---

## 📈 Część 4: Sprint Retrospective z Wykresem Burndown i Analizą Delty (EU3, EU4, EU5)

Dla oceny **bdb** dla roli PO regulamin wymaga:
- *„regularne prowadzenie diagramu wypalania w zakresie godzin pracy i zadań”*,
- *„odniesienie się do różnic w czasie realizacji zadań: oszacowanym i rzeczywistym”*.

### Krok 4.1: Eksport Wykresu Wypalania (Burndown Chart)
Na koniec sprintu PO wchodzi w Jira: `Raporty` -> `Wykres wypalania (Burndown Chart)` dla zakończonego sprintu.
- Robi zrzut ekranu wykresu (pokazującego linię idealną vs linię rzeczywistego spalania godzin/zadań).
- Wkleja zrzut ekranu do raportu Retro w Confluence.

### Krok 4.2: Tabela Analizy Delty Czasowej (Wymóg BDB na Retrospektywie)

```markdown
# 🔄 Raport z Retrospektywy — Sprint [Numer]
**Prowadzący PO:** [Imię i Nazwisko]  
**Wykres Burndown:** [Tutaj wklej zrzut ekranu z Jira]

### Analiza Odchyleń Czasowych (Czas Oszacowany vs Czas Rzeczywisty)

| Klucz Jira | Zadanie | Wykonawca | Estymacja (h) | Czas Rzecz. (h) | Odchylenie ($\Delta$) | Analiza Przyczyny & Wnioski na Przyszłość |
|---|---|---|:---:|:---:|:---:|---|
| `NEX-12` | Walidacja rejestracji | Jan Kowalski | 3.0 h | 3.5 h | +0.5 h | Drobne rozszerzenie testów jednostkowych o przypadek pustego maila. Odchylenie w normie (< 20%). |
| `NEX-15` | Konfiguracja CORS i JWT | Anna Nowak | 4.0 h | 7.5 h | **+3.5 h** | **Niedoszacowanie technologiczne:** Niespodziewany błąd z nagłówkami `Set-Cookie` w przeglądarce. *Wniosek:* Nowe mechanizmy bezpieczeństwa muszą być poprzedzone 2h zadaniem badawczym (*Spike*). |
| `NEX-18` | Szablon e-mail | Piotr Wiśniewski | 2.5 h | 1.5 h | -1.0 h | Wykorzystano gotowy szablon HTML, co skróciło czas kodowania styli. |
| `NEX-20` | Rezerwacja stanu | Tomasz Zieliński | 4.0 h | 4.0 h | 0.0 h | Idealne trafienie w estymację. |

### Podsumowanie Metryczne Sprintu:
- **Suma godzin oszacowanych:** 42.0 h
- **Suma godzin przepracowanych:** 46.5 h
- **Ogólne odchylenie sprintu:** +10.7% (Wynik w dopuszczalnym buforze ryzyka $\le 15\%$).
- **Główny wniosek procesowy zespołu:** W kolejnym sprincie zmniejszamy pulę zadań o 4 godziny, aby zrekompensować czas potrzebny na dokładniejsze Code Review w Bitbuckecie.
```

---

## 💻 Część 5: Żelazna Checklista Dewelopera na Ocenę BDB (EU2, EU5, EU6)

Jako członek zespołu (deweloper), aby otrzymać ocenę **bdb** i nie stracić 0.5–1.0 stopnia, wykonujesz następujące kroki dla każdego przypisanego zadania:

### 1. Rozpoczęcie Pracy w Bitbucket (EU2)
- Przeciągasz zadanie w Jira ze statusu `TO DO` do `IN PROGRESS`.
- Tworzysz gałąź w Git z poziomu Jira lub terminala z zachowaniem klucza zadania:
  `git checkout -b feature/NEX-22-order-service`
- Każdy commit musi zawierać numer zadania:
  `git commit -m "NEX-22: add domain validation for order items"`

### 2. Zgłaszanie Pracy na Daily (EU2)
- Codziennie wpisujesz status na Discordzie.
- W zadaniu w Jira logujesz przepracowany czas (*Log Work*, np. `2h 30m`).

### 3. Zakończenie Pracy i Pull Request (EU2, EU6)
- Wypychasz gałąź na Bitbucket i otwierasz **Pull Request (PR)** do gałęzi `develop` / `main`.
- **Wymóg opisu PR:**
  - Link do zadania w Jira (`NEX-22`).
  - Zrzut ekranu lub animacja GIF potwierdzająca działanie w UI (lub wynik zielonych testów).
  - Oznaczenie co najmniej 1 recenzenta (innego członka zespołu).
- Zakaz samodzielnego merge'owania bez akceptacji!

### 4. Dokumentacja w Confluence (EU6)
- Otwierasz stronę swojego modułu w Confluence (np. `04_Moduły -> Moduł Zamówień`).
- Dopisujesz krótki akapit: jak działa nowa funkcja, jakie są kody błędów, jak przetestować endpoint.
- Dopiero po wykonaniu tych 4 kroków przeciągasz zadanie w Jira do kolumny **`DONE`**.
