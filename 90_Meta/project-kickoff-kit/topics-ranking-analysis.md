---
type: concept
title: "Ranking, Audyt i Dekompozycja 13 Tematów Projektu Zespołowego PB"
created: 2026-10-05
updated: 2026-10-05
tags: [meta, project-kickoff, topics-ranking, scrum, pb, architecture, epics]
up: "[[90_Meta/_index]]"
---

# Ranking, Audyt i Dekompozycja 13 Tematów Projektu Zespołowego (Politechnika Białostocka)

> [!IMPORTANT]
> **Metodologia i Kontekst Oceny:**
> Niniejsza analiza powstała w oparciu o twarde kryteria sylabusa przedmiotu *Projekt Zespołowy* (Semestr 1 & 2):
> - **EU1 & EU2:** Wymóg bezpośredniej współpracy z **kończącym użytkownikiem** w każdym sprincie oraz terminowość.
> - **Zasada 6+ Epików:** Każdy student w zespole **musi** osobiście przygotować i odpowiadać za swoją grupę funkcjonalności (Epik).
> - **Klauzula Spychologiczna:** Kara -1.0 za niezrealizowane zadanie, z prawem przeniesienia winy na rotującego Product Ownera, jeśli zadanie okaże się „nierealistyczne”.
> - **Inżynieria ponad Hype:** Tematy oparte o modne technologie (Blockchain, GenAI/LLM) niosą skrajne ryzyko poślizgów w małych, studenckich zespołach Scrumowych.

---

## 🏆 Tabela Zbiorcza i Ranking Główny

| Miejsce | Nr | Nazwa Tematu | Użytkownik (25%) | 6 Epików (20%) | Feasibility (20%) | Scrum/PO (15%) | Logika (10%) | CV (10%) | Wynik (0-100) | Kategoria Rekomendacji |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **🥇 1** | **#4** | **System ocen pracowniczych Politechniki Białostockiej** | **98** | **95** | **95** | **92** | **90** | **85** | **94.2** | 🟢 **Złoty Standard (Top 1)** |
| **🥈 2** | **#13** | **System wybierania tematów prac dyplomowych** | **96** | **95** | **92** | **90** | **88** | **85** | **92.2** | 🟢 **Złoty Standard (Top 2)** |
| **🥉 3** | **#8** | **Rozliczanie delegacji zagranicznych** | **88** | **90** | **90** | **85** | **92** | **82** | **87.9** | 🟢 **Złoty Standard (Top 3)** |
| **4** | **#7** | **Obsługa delegacji krajowych** | **88** | **85** | **92** | **88** | **78** | **75** | **84.9** | 🟡 **Bardzo Bezpieczny** |
| **5** | **#12** | **System układania obciążeń nauczycieli (Pensum)** | **85** | **85** | **75** | **78** | **95** | **85** | **82.8** | 🟡 **Silny Inżyniersko (Uwaga na solver)** |
| **6** | **#11** | **Zarządzanie hospitacjami nauczycieli akademickich** | **85** | **80** | **88** | **85** | **75** | **75** | **81.9** | 🟡 **Solidny i Prosty** |
| **7** | **#5** | **Platforma dla organizacji NGO (Wolontariat)** | **82** | **75** | **78** | **78** | **72** | **80** | **77.9** | 🟡 **Solidny Społecznie (Mobile)** |
| **8** | **#1** | **Platforma oceny jakości danych pod AI (AI Act)** | **55** | **85** | **70** | **65** | **90** | **98** | **72.1** | 🟠 **Ambitny / Ryzykowny EU1** |
| **9** | **#9** | **Nowy w firmie – Platforma onboardingowa** | **70** | **70** | **85** | **75** | **60** | **70** | **71.8** | 🟠 **Płytka Logika (Ryzyko Trello)** |
| **10** | **#2** | **Aplikacja "car pooling" / "ridesharing"** | **78** | **65** | **62** | **62** | **75** | **82** | **69.8** | 🟠 **Ryzyko Płatnych API Map** |
| **11** | **#6** | **Platforma ESG dla budownictwa (LLM / GenAI)** | **45** | **75** | **55** | **55** | **80** | **92** | **62.7** | 🔴 **Wysokie Koszty & Niedeterminizm** |
| **12** | **#10** | **Zero Waste - Świat z mniejszą ilością odpadów** | **60** | **55** | **68** | **60** | **50** | **65** | **59.3** | 🔴 **Rozmyte Wymagania (Brak Klienta)** |
| **13** | **#3** | **Certyfikacja żywności w łańcuchu (Blockchain)** | **35** | **70** | **35** | **40** | **85** | **88** | **50.5** | 🔴 **Czerwona Flaga (Overengineering)** |

---

## 🎯 Szczegółowa Analiza 13 Tematów

---

### #4: System ocen pracowniczych Politechniki Białostockiej (Ocena: 94.2 / 100) — 🥇 NAJLEPSZY WYBÓR

#### 1. Dlaczego wygrywa?
- **Prowadzący SAM JEST UŻYTKOWNIKIEM:** Nauczyciele akademiccy PB (w tym Twój prowadzący zajęcia, recenzenci i dziekan) podlegają okresowej ocenie pracowniczej z art. 115 Ustawy. Każdy z nich nienawidzi ręcznego wypełniania arkuszy punktowych w Excelu. Prowadzący widząc ten projekt, będzie osobiście zaangażowany i bez problemu udzieli feedbacku co 2 tygodnie (100% gwarancja EU1 i EU2).
- **Czysta domena inżynierska:** Zero zewnętrznych płatnych API, zero problemów z gas fee blockchaina czy losowością modeli językowych. Czysty, elegancki Modularny Monolit z silnikiem reguł punktowych i dwuetapowym workflow akceptacji.

#### 2. Dekompozycja na 6 Epików (Podział dla 6 studentów):
1. **Epik 1 (Moduł Struktury Uczelni i Uprawnień RBAC):** Wydziały, katedry, role (Nauczyciel, Kierownik Katedry, Dziekan, Członek Komisji, Dział Kadr), profile i historia zatrudnienia.
2. **Epik 2 (Silnik Parametryzacji Kryteriów i Minimów Regulaminowych):** Definiowanie kryteriów oceny (3 główne filary: naukowa, dydaktyczna, organizacyjna), progi punktowe, wagi, obsługa zmian w regulaminie bez konieczności re-deployu.
3. **Epik 3 (Kreator Hierarchicznego Wniosku Pracowniczego):** Dynamiczne drzewo osiągnięć (obszar $\to$ kategoria $\to$ osiągnięcie), auto-uzupełnianie danych z profilu, kalkulator punktów na żywo, walidacja kompletności przed wysłaniem.
4. **Epik 4 (Dwuetapowy Workflow Weryfikacji i Korekt):** Etap 1: Kierownik bezpośredni (korekta punktów, uwagi, zatwierdzenie), Etap 2: Uczelniana/Wydziałowa Komisja Oceniająca. Powiadomienia e-mail i in-app.
5. **Epik 5 (Moduł Odwołań, Historii i Porównywania Ocen):** Ścieżka odwoławcza pracownika, wersjonowanie wniosków, porównywanie wyników z poprzednich okresów oceny (delta postępu naukowego).
6. **Epik 6 (Moduł Analityczny i Raportowania dla Dziekanatu/Kadr):** Zbiorcze rankingi wydziałowe, statystyki spełnienia minimów, generowanie urzędowych protokołów PDF, eksport zestawień do Excela.

---

### #13: System wybierania tematów prac dyplomowych (Ocena: 92.2 / 100) — 🥈 TOP TIER

#### 1. Dlaczego jest wybitny?
- **Zespół doskonale zna domenę:** Każdy z Was jest studentem i przeszedł lub przechodzi przez koszmar poszukiwania promotora, ustalania tematu i zatwierdzania go przez Radę Wydziału.
- **Użytkownicy na wyciągnięcie ręki:** Wszyscy Wasi koledzy ze studiów, promotorzy i pracownicy dziekanatu są dostępni codziennie na korytarzach PB.
- **Naturalna sekwencja stanowa:** Przepiękne wzorce maszyn stanów (*Draft $\to$ Katedra $\to$ Dziekan $\to$ Opublikowany $\to$ Zarezerwowany $\to$ Przypisany*).

#### 2. Dekompozycja na 6 Epików:
1. **Epik 1 (Katalog Tematów i Kreator Promotora):** Wprowadzanie propozycji tematów inżynierskich/magisterskich, słowa kluczowe, wymagania kompetencyjne, wersje robocze (Drafts).
2. **Epik 2 (Wieloetapowy Workflow Zatwierdzania Tematów):** Ścieżka akceptacji: Promotor $\to$ Kierownik Katedry $\to$ Kolegium Dziekańskie z mechanizmem uwag i cofania do poprawy.
3. **Epik 3 (Wyszukiwarka i Portal Aplikacyjny Studenta):** Zaawansowane filtry (promotor, katedra, technologie), system rezerwacji tematów indywidualnych oraz zespołowych (z deklaracją składu zespołu).
4. **Epik 4 (Panel Zarządzania Promotora i Pilnowanie Limitów):** Rozpatrywanie aplikacji studentów, akceptacja/odrzucenie, automatyczne pilnowanie pensum dyplomantów (np. max 5 prac inżynierskich na promotora).
5. **Epik 5 (Moduł Harmonogramów, Deadlinów i Komunikacji):** Odliczanie do terminów zgłaszania i wyboru, automatyczne alerty mailowe, bezpieczny czat wewnętrzny promotor-student w kontekście wybranego tematu.
6. **Epik 6 (Integracja Uczelniana i Raportowanie USOS):** Eksport zatwierdzonych par Student-Promotor-Temat do formatów kompatybilnych z USOS (CSV/XML), statystyki obciążenia katedr, generowanie uchwał zatwierdzających w PDF.

---

### #8: Rozliczanie delegacji zagranicznych (Ocena: 87.9 / 100) — 🥉 TOP TIER

#### 1. Dlaczego jest znakomity?
- **Prawdziwe zarządzenie PB:** Posiada gotową, precyzyjną specyfikację prawną (Zarządzenie Rektora PB nr 61/2024 oraz Rozporządzenie MPiPS).
- **Ciekawa logika walutowa:** Integracja z publicznym, w 100% darmowym i niezawodnym API Narodowego Banku Polskiego (NBP Web API). Przeliczenia kursów z dnia poprzedzającego dzień rozliczenia/zaliczki.
- **Użytkownicy:** Nauczyciele wyjeżdżający na zagraniczne konferencje naukowe i staże Erasmus+.

#### 2. Dekompozycja na 6 Epików:
1. **Epik 1 (Wnioskowanie i Planowanie Podróży):** Formularz wniosku o wyjazd zagraniczny (cel, środek transportu, państwa docelowe, wnioskowane zaliczki wielowalutowe).
2. **Epik 2 (Integrator NBP i Silnik Walutowy):** Automatyczne pobieranie tabel kursowych NBP (Tabela A i C), obsługa przeliczeń wielowalutowych (EUR, USD, GBP, CHF) wg dat transakcji.
3. **Epik 3 (Kalkulator Diet Zagranicznych i Limitów Hotelowych):** Tabela stawek diet i limitów noclegowych per kraj, odliczanie zapewnionego wyżywienia (śniadanie -15%, obiad -30%, kolacja -30%).
4. **Epik 4 (Workflow Akceptacji i Kwestura):** Ścieżka akceptacji: Przełożony $\to$ Dziekan $\to$ Dział Współpracy Międzynarodowej $\to$ Kwestura. Rejestracja wypłaty zaliczki.
5. **Epik 5 (Moduł Rozliczenia Końcowego i Rachunków):** Wprowadzanie rachunków, faktur za hotele, biletów lotniczych, kilometrówki zagranicznej, kalkulacja zwrotu lub dopłaty pracownika.
6. **Epik 6 (Moduł Finansowo-Księgowy i Integracja FK):** Przypisywanie kosztów do projektów badawczych/grantów, generowanie oficjalnych formularzy rozliczeniowych PDF, raportowanie budżetowe dla Kwestury.

---

### #7: Obsługa delegacji krajowych (Ocena: 84.9 / 100)
- **Zalety:** Bardzo bezpieczny, proste reguły, Zarządzenie PB.
- **Dlaczego przegrywa z zagranicznymi?** Brak walut i tabel NBP sprawia, że system jest mniej imponujący inżyniersko (zwykły kalkulator kilometrówki i diet krajowych 45 zł).

---

### #12: System układania obciążeń nauczycieli (Pensum) (Ocena: 82.8 / 100)
- **Zalety:** Bardzo ważny dla wydziału, wagi zajęć, podział przedmiotów.
- **Główne Ryzyko (PO Hazard):** Jeśli prowadzący zażąda „automatycznego algorytmu optymalizującego przydział zajęć”, zespół wpadnie w pułapkę problemu NP-trudnego (Constraint Satisfaction Problem / ILP). Deweloperzy utkną na solverze, co zagrozi ocenom w sprintach!
- **Warunek bezpieczeństwa:** Realizować wyłącznie jako **narzędzie ewidencyjno-bilansujące dla kierownika katedry** (manualny przydział z walidacją reguł pensum na żywo), a nie automatyczny generator harmonogramu.

---

### #11: Zarządzanie hospitacjami nauczycieli akademickich (Ocena: 81.9 / 100)
- **Zalety:** Prosty, gotowy użytkownik na wydziale, przejrzysty obieg protokołu hospitacji.
- **Wada:** Mały zakres funkcjonalny. Przy 6 osobach w zespole możecie mieć trudność ze sztucznym rozdmuchiwaniem Epików na 2 semestry, żeby każdy miał co robić.

---

### #5: Platforma dla organizacji NGO (Wolontariat) (Ocena: 77.9 / 100)
- **Zalety:** Bardzo przyjemny temat, łatwo znaleźć fundację lub koło naukowe do roli użytkownika.
- **Wada:** Silny nacisk na aplikację mobilną (push notifications, kalendarz smartfona). Wymaga sprawnego zespołu w technologiach mobilnych (React Native / Flutter) i problemów z deploymentem na telefony 6 osób.

---

### #1: Platforma oceny jakości danych pod AI (AI Act) (Ocena: 72.1 / 100)
- **Zalety:** Najlepszy temat do CV, europejski AI Act to absolutny hit rynkowy.
- **Główna Pułapka EU1:** **Kto będzie Waszym użytkownikiem końcowym?** Czy macie znajomego Data Stewarda lub Compliance Officera w dużej spółce giełdowej, który co 2 tygodnie zaloguje się do Waszego systemu i odbierze sprint? Jeśli nie, prowadzący obetnie ocenę za brak weryfikacji z użytkownikiem!

---

### #9: Nowy w firmie – Platforma onboardingowa (Ocena: 71.8 / 100)
- **Zalety:** Grywalizacja, odznaki, intuicyjny proces.
- **Wada:** Ryzyko sprowadzenia projektu do „ładniejszego Trello z checklistą zadań”. Prowadzący może uznać, że projekt jest za prosty na 2-semestralny projekt inżynierski.

---

### #2: Car pooling / Ridesharing miejski (Ocena: 69.8 / 100)
- **Zalety:** Użytkownikami mogą być sami studenci dojeżdżający na PB.
- **Wady i Pułapki:** 
  1. Zależność od zewnętrznych map (Google Maps API wymaga podpięcia karty kredytowej i generuje koszty; darmowy OpenStreetMap wymaga własnego serwera kafelków lub OSRM).
  2. Złożoność algorytmu dopasowywania tras po drodze (*Point-to-Route matching*).

---

### #6: Platforma ESG dla budownictwa (LLM) (Ocena: 62.7 / 100)
- **Zalety:** Wykorzystanie AI i GPT-4.
- **Czerwone Flagi:**
  - Płatne tokeny OpenAI przy intensywnym testowaniu przez 6 studentów.
  - Brak powtarzalności w testach jednostkowych (niedeterminizm LLM psuje pipeline CI w Bitbuckecie).
  - Brak realnego użytkownika z branży budowlanej.

---

### #10: Zero Waste (Mniejsza ilość odpadów) (Ocena: 59.3 / 100)
- **Czerwona Flaga:** **Zbyt rozmyte wymagania.** Opis tematu to luźny esej bez konkretów. Spędzicie 6 tygodni na ustalaniu zakresu w DIP i każdy w zespole będzie miał inną wizję.

---

### #3: Certyfikacja żywności (Blockchain) (Ocena: 50.5 / 100) — 🔴 CZERWONA FLAGA
- **Dlaczego to pułapka?**
  - **Przerost formy nad treścią (Overengineering):** Blockchain, smart contracts w Solidity, portfele MetaMask, gas fees.
  - **Ryzyko spychologii:** Jeśli deweloper dostanie zadanie zintegrowania sieci testowej Ethereum i utknie na 2 tygodnie, natychmiast oskarży PO o narzucenie nierealistycznego zadania. Prowadzący obniży ocenę.
  - **Brak użytkownika:** Żaden rolnik ani inspektor GIJHARS nie przyjdzie na Wasze demo sprintowe.
