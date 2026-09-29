---
type: concept
title: "Szablon 1-Pagera Pomysłu i Procedura Cichej Inkubacji (Discord)"
created: 2026-09-29
updated: 2026-09-29
tags: [meta, project-kickoff, ideation, 1-pager, discord, scrum]
up: "[[90_Meta/_index]]"
---

# Szablon 1-Pagera Pomysłu & Procedura Asynchronicznej Inkubacji

> [!NOTE]
> Poniższy materiał został zaprojektowany do bezpośredniego skopiowania na serwer Discord (np. na kanał `#ogłoszenia` lub `#pomysły-zasady`) oraz do wspólnego dokumentu roboczego (Google Docs / Notion / Confluence).

---

## 📢 Wiadomość wprowadzająca na Discord (Do skopiowania i wysłania zespołowi)

```markdown
Hej wszystkim! 👋
Rozpoczynamy przygotowania do naszego projektu zespołowego. Aby uniknąć chaosu, przekrzykiwania się na callu i wyboru przypadkowego pomysłu, zastosujemy sprawdzoną procedurę **cichej inkubacji (Brainwriting asynchroniczny)**.

Mamy przed sobą 2 semestry pracy, a regulamin przedmiotu stawia twarde warunki:
1. **Musimy mieć kontakt z realnym użytkownikiem końcowym** (EU1/EU2 – bez tego tracimy punkty!).
2. **Każdy z nas (6+ osób) musi mieć swój własny, niezależny Epik / grupę funkcjonalności** (EU1).
3. Projekt musi być wykonalny technicznie, ale nie może być banalnym CRUD-em.

### 🗓️ Harmonogram wyboru pomysłu:
- **Krok 1 (do [Wstaw datę: np. za 5 dni]): Ciche myślenie.** Każdy z nas w wolnej chwili wypełnia poniższy szablon 1-pagera dla 1–2 własnych propozycji i wrzuca na kanał `#propozycje-pomysłów`. Nie krytykujemy jeszcze pomysłów innych!
- **Krok 2 (kolejne 2 dni): Lektura i pytania.** Czytamy propozycje na spokojnie, zadajemy pytania w wątkach pod postami.
- **Krok 3 (kolejny dzień): Głosowanie matrycą.** Na wspólnym 30-minutowym callu oceniamy pomysły według matrycy scoringowej i wybieramy zwycięski temat oraz wstępny podział ról.

Poniżej znajduje się oficjalny szablon – skopiujcie go, wypełnijcie dla swojego pomysłu i wrzućcie w osobnym poście! 🚀
```

---

## 📄 Szablon 1-Pagera Pomysłu (Formatka dla każdego członka zespołu)

```markdown
# 💡 [NAZWA ROBOCZA PROJEKTU]

**Autor propozycji:** [Twoje Imię i Nazwisko]  
**Data zgłoszenia:** [YYYY-MM-DD]  

---

### 1. Problem i Cel Biznesowy
*Jaki realny problem rozwiązuje ten system? Dlaczego ktoś miałby z niego korzystać zamiast arkusza Excel lub gotowego programu?*
> [Krótki opis problemu w 2–4 zdaniach]

---

### 2. Użytkownik Końcowy (Kluczowe pod zaliczenie EU1 i EU2!)
*Zgodnie z regulaminem zadania musimy realizować w bezpośrednim kontakcie z końcowym użytkownikiem. Kto nim będzie w naszym projekcie i czy mamy do niego fizyczny dostęp w trakcie semestru?*
- **Grupa docelowa:** [np. pracownicy małej kawiarni / członkowie koła naukowego / koordynatorzy wolontariatu / studenci wydziału]
- **Konkretny kontakt / persona:** [np. „Mój znajomy Jan prowadzi lokalny sklep i zgodził się raz w sprincie testować nasz system i dawać feedback”]
- **Weryfikacja dostępności:** Czy ta osoba zgodzi się na 15-minutową demonstrację pod koniec każdego 2-tygodniowego sprintu? [TAK / NIE]

---

### 3. Wstępna Dekompozycja na 6+ Niezależnych Epików (Dla każdego studenta)
*Każdy członek zespołu musi w dokumencie DIP zdefiniować swój własny Epik (EU1). Czy ten system naturalnie dzieli się na min. 6 odrębnych modułów funkcjonalnych?*

1. **Epik 1 (np. Moduł Tożsamości i Uprawnień):** [Krótki opis 1 zdaniem: rejestracja, role, audit log, profile]
2. **Epik 2 (np. Moduł Katalogu / Zasobów):** [Krótki opis 1 zdaniem: ewidencja, kategoryzacja, wyszukiwarka, stany]
3. **Epik 3 (np. Moduł Procesowy / Transakcyjny):** [Krótki opis 1 zdaniem: rezerwacje, zamówienia, maszyna stanów procesu]
4. **Epik 4 (np. Moduł Magazynowy / Realizacji):** [Krótki opis 1 zdaniem: przepływ towaru/zadań, kolejkowanie, przypisywanie obsługi]
5. **Epik 5 (np. Moduł Finansowy / Raportowy):** [Krótki opis 1 zdaniem: rozliczenia, generowanie PDF, wskaźniki analityczne]
6. **Epik 6 (np. Moduł Komunikacji i Powiadomień):** [Krótki opis 1 zdaniem: mailing, alerty systemowe, push/in-app notyfikacje]
*(Jeśli zespół liczy >6 osób, dopisz kolejne: Epik 7 Moduł Helpdesk/Reklamacji, Epik 8 Moduł Integracji zewnętrznych)*

---

### 4. Specyfika Techniczna i Złożoność Logiki
*Projekt nie może być trywialnym formularzem wprowadzania danych. Gdzie kryje się ciekawa logika inżynierska?*
- **Nietrywialna logika biznesowa:** [np. algorytm optymalnego przydziału zadań / walidacja konfliktów czasowych w rezerwacjach / kalkulator kosztów / automatyczne reguły eskalacji]
- **Wymagania niefunkcjonalne (NFR):** [np. czas odpowiedzi < 200 ms przy generowaniu raportu / pełna audytowalność zmian / responsywność na smartfonach]

---

### 5. Analiza Ryzyk i Zależności Zewnętrznych
*Co może nas zabić w trakcie semestru?*
- Czy projekt wymaga zewnętrznych, płatnych API? [NIE / TAK: jakie?]
- Czy wymaga dedykowanego hardware'u (np. mikrokontrolery, czytniki NFC)? [NIE / TAK]
- Czy domena wymaga skomplikowanej wiedzy prawnej/księgowej, której nikt z nas nie ma? [NIE / TAK]
```

---

## 📊 Matryca Scoringowa do Oceny Pomysłów (Arkusz Głosowania)

Podczas spotkania selekcyjnego każdy członek zespołu przyznaje każdemu pomysłowi punkty w skali **1 do 5** w poniższych kategoriach. 

$$\text{Wynik Końcowy} = (K1 \times 3) + (K2 \times 3) + (K3 \times 2) + (K4 \times 1) - \text{Kary Ryzyka}$$

| Kryterium | Waga | Opis weryfikacji | Skala ocen (1–5) |
|---|:---:|---|---|
| **K1: Dostępność Użytkownika Końcowego (EU1/EU2)** | **x 3** | Czy mamy pewnego, żywego człowieka, który zgodzi się na regularny feedback i odbiór sprintów? | 1 = Użytkownik hipotetyczny<br>3 = Użytkownik ogólny (np. inni studenci)<br>5 = Konkretna, potwierdzona osoba z branży |
| **K2: Czysty podział na 6+ Epików (EU1)** | **x 3** | Czy każdy student może wziąć 1 Epik bez wchodzenia w paradę innym i bez blokad w Git? | 1 = Wszyscy modyfikują tę samą tabelę<br>3 = Granice lekko zatarte<br>5 = Idealny Modular Monolith / 6 Bounded Contexts |
| **K3: Wykonalność w 2 semestry (Feasibility)** | **x 2** | Czy zakres prac jest realny do dowiezienia przy 4–6h pracy tygodniowo na osobę? | 1 = Zbyt rozległy / wymaga AI Researchu<br>3 = Wymagający, ale realny<br>5 = Bardzo dobrze dopasowany do możliwości |
| **K4: Wartość do Portfolio / Resume** | **x 1** | Czy ten projekt dobrze wygląda w CV i pozwala pochwalić się nowoczesnym stosem? | 1 = Nudny system szkolny z 2005 r.<br>3 = Standardowa aplikacja webowa<br>5 = Imponujący projekt biznesowy z ciekawą architekturą |
| **Kara: Ryzyko zewnętrzne (Red Flag)** | **-5 pkt** | Wymóg płatnych API, zewnętrznego hardware'u lub niejasnych licencji. | Odejmij 5 punktów, jeśli występuje! |

---

## 🛡️ Lista Pytań Filtrujących (Decyzja GO / NO-GO)

Zanim jakikolwiek pomysł zostanie ogłoszony zwycięzcą, zespół musi odpowiedzieć **„TAK”** na wszystkie 4 pytania:

1. **Czy jesteśmy w stanie wyznaczyć imiennego opiekuna dla każdego z 6+ Epików przed rozpoczęciem semestru?**
2. **Czy do 2. tygodnia semestru możemy przeprowadzić co najmniej 1 wywiad z użytkownikiem końcowym na temat jego potrzeb?**
3. **Czy architektura systemu pozwala na zaimplementowanie go w postaci jednego repozytorium (Monorepo) z wydzielonymi modułami?**
4. **Czy jeśli jeden z członków zespołu zachoruje lub zawali sprint, pozostałe moduły będą mogły nadal działać i kompilować się bez przeszkód?**
