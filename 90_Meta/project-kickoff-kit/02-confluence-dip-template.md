---
type: concept
title: "Szablon Dokumentu Inicjującego Projekt (DIP) dla Confluence"
created: 2026-09-29
updated: 2026-09-29
tags: [meta, project-kickoff, dip, confluence, scrum, requirements, epics]
up: "[[90_Meta/_index]]"
---

# Dokument Inicjujący Projekt (DIP)

> [!IMPORTANT]
> **Szablon oficjalny dla przestrzeni Confluence.**  
> Zgodnie z kryteriami przedmiotu: *„przygotowanie założeń projektu i wstępnych grup funkcjonalności nie jest odrębnie oceniane ale jest obowiązkowe - brak realizacji skutkuje oceną niedostateczną”*.  
> Każdy student w zespole **musi** być wpisany jako autor jednego Epiku (EU1).

---

## 📋 Metadane Dokumentu

| Pole | Wartość |
|---|---|
| **Nazwa Projektu** | [Pełna nazwa systemu, np. NexusCore - Platforma Zarządzania Zleceniami Gastronomicznymi] |
| **Klucz Projektu w Jira** | `[np. NEX]` |
| **Wersja Dokumentu** | `v1.0 (Zatwierdzona)` |
| **Data Zatwierdzenia** | `[YYYY-MM-DD]` |
| **Prowadzący / Scrum Master** | [Tytuł, Imię i Nazwisko Prowadzącego] |
| **Skład Zespołu Projektowego** | 1. [Imię Nazwisko] (Lider Inicjalny / PO Sprintu 1) — Właściciel Epiku 1<br>2. [Imię Nazwisko] — Właściciel Epiku 2<br>3. [Imię Nazwisko] — Właściciel Epiku 3<br>4. [Imię Nazwisko] — Właściciel Epiku 4<br>5. [Imię Nazwisko] — Właściciel Epiku 5<br>6. [Imię Nazwisko] — Właściciel Epiku 6<br>*(opcjonalnie 7–8 dla większych zespołów)* |

---

## 1. Wstęp, Kontekst Biznesowy i Cele Systemu

### 1.1. Problem Biznesowy
[Opisz w 2–3 akapitach bieżący stan i problem, z jakim mierzy się użytkownik docelowy. Np. brak centralizacji danych, ręczna obsługa zamówień w arkuszach Excel, opóźnienia w komunikacji, błędy stanów magazynowych, brak audytowalności zmian].

### 1.2. Cel Projektu i Wartość Dodana
Celem 2-semestralnego projektu jest zaprojektowanie, implementacja, przetestowanie oraz wdrożenie kompletnego systemu informatycznego [aplikacji webowej / desktopowej / mobilnej], który:
- Zautomatyzuje proces [główny proces biznesowy].
- Zapewni jedno źródło prawdy dla danych procesowych, magazynowych i finansowych.
- Zredukuje czas obsługi pojedynczego incydentu / zamówienia o minimum [np. 40%].
- Zapewni bezbłędną współpracę w zespole wieloosobowym w oparciu o architekturę modułową i metodykę SCRUM.

### 1.3. Ograniczenia i Założenia Projektowe
- **Środowisko:** Uczelniany stos Atlassian (Jira, Confluence, Bitbucket).
- **Ramy czasowe Semestru 1:** [np. 15 tygodni dydaktycznych, podzielonych na cykle sprintów 2-tygodniowych].
- **Budżet czasowy zespołu:** Nominalnie 4–6 godzin roboczych tygodniowo na każdego członka zespołu.

---

## 2. Użytkownik Końcowy i Pętla Walidacji (EU1, EU2)

Regulamin przedmiotu wymaga realizacji zadań w bezpośrednim kontakcie z użytkownikiem końcowym.

### 2.1. Profil Użytkownika Końcowego (Persona)
- **Rola / Stanowisko:** [np. Kierownik Zmiany / Właściciel Małej Firmy / Koordynator Magazynu]
- **Dane reprezentanta:** [Imię, Nazwisko lub Nazwa Podmiotu Zewnętrznego, np. Pan Jan Kowalski, kawiarnia X]
- **Główne bolączki (Pains):** [Czasochłonne raportowanie, pomyłki przy wprowadzaniu stanów, brak dostępu do danych w czasie rzeczywistym].
- **Oczekiwane korzyści (Gains):** [Przejrzysty dashboard, natychmiastowe alerty o brakach, eksport zestawień do PDF/CSV].

### 2.2. Plan Współpracy i Odbioru Sprintów
1. **Faza Inicjacji:** Wywiad wstępny z użytkownikiem celem weryfikacji założeń niniejszego dokumentu DIP.
2. **Pętla Sprintowa:** Na zakończenie każdego sprintu (podczas ceremonii Sprint Review), zespół prezentuje użytkownikowi (lub deweloper odpowiedzialny za dane zadanie przeprowadza sesję weryfikacyjną) działający przyrost funkcjonalności.
3. **Ślad Audytowy:** Każda sesja z użytkownikiem końcowym kończy się krótką notatką w Confluence (protokół odbioru / feedback loop), co stanowi podstawę zaliczenia efektu EU2 i EU5.

---

## 3. Wizja Architektoniczna i Strategia Techniczna

Aby zapobiec konfliktom w zespole 6+ osób, system projektowany jest w paradygmacie **Modularnego Monolitu (Modular Monolith)** z wyraźnymi granicami modułów domenowych (Bounded Contexts) i architekturą Ports & Adapters wewnątrz kluczowych podsystemów.

```
+------------------------------------------------------------------------------------+
|                         WARSTWA PREZENTACJI (UI / API Gateway)                     |
+------------------------------------------------------------------------------------+
       |                           |                           |
       v                           v                           v
+------------------+       +------------------+       +------------------+
| Moduł Epiku 1    |       | Moduł Epiku 2    |       | Moduł Epiku 3    |
| (Katalog/Zasoby) |<----->| (Zamówienia)     |<----->| (Finanse/Faktury)|
| Właściciel: Stud1|       | Właściciel: Stud2|       | Właściciel: Stud3|
+------------------+       +------------------+       +------------------+
       |                           |                           |
       v                           v                           v
+------------------+       +------------------+       +------------------+
| Moduł Epiku 4    |       | Moduł Epiku 5    |       | Moduł Epiku 6    |
| (Magazyn/Stany)  |       | (Notyfikacje)    |       | (Raporty/Audyt)  |
| Właściciel: Stud4|       | Właściciel: Stud5|       | Właściciel: Stud6|
+------------------+       +------------------+       +------------------+
+------------------------------------------------------------------------------------+
|          WSPÓLNY KONTRAKT: Publiczne DTO i Zdarzenia Domenowe w Pamięci            |
|       (Żaden moduł nie odpytuje bezpośrednio tabel bazy danych innego modułu!)      |
+------------------------------------------------------------------------------------+
```

- **Izolacja kodu:** Każdy student posiada wydzielony katalog modułu (`src/modules/<nazwa_modułu>/`).
- **Komunikacja:** Wyłącznie przez publiczne interfejsy serwisowe lub wewnętrzną szynę zdarzeń w procesie (*In-Memory Event Bus*).
- **Trwałość danych:** Tabele bazy danych są logicznie separowane prefiksami domenowymi (np. `cat_*`, `ord_*`, `fin_*`). Zakaz kluczy obcych cross-module bez uzgodnienia na forum architektury.

---

## 4. Dekompozycja Systemu na Grupy Funkcjonalności (Epiki) (EU1)

> Każdy student odpowiada osobiście za specyfikację wymagań (User Stories + Kryteria Akceptacji) dla przypisanego mu Epiku.

---

### Epik 1: [Nazwa Modułu, np. Moduł Uwierzytelniania, Użytkowników i Uprawnień (RBAC)]
- **Właściciel Epiku (Autor EU1):** [Imię i Nazwisko Studenta 1]
- **Klucz Jira:** `[NEX-EPIC-1]`
- **Zakres:** Zarządzanie kontami użytkowników, role systemowe, sesje, logi audytowe logowania, polityka haseł.
- **Wstępne User Stories:**
  - `US-1.1`: Jako administrator chcę definiować role i przypisywać im uprawnienia, aby ograniczyć dostęp do poufnych modułów finansowych.
    - *Kryteria akceptacji:* Given administrator w panelu uprawnień, When odbierze uprawnienie `FIN_VIEW` roli `Magazynier`, Then użytkownik z tą rolą otrzymuje HTTP 403 przy próbie wejścia w raporty.
  - `US-1.2`: Jako użytkownik chcę bezpiecznie zalogować się do systemu, aby uzyskać dostęp do swoich zadań.
    - *Kryteria akceptacji:* Poprawne dane -> generowanie sesji/tokena; 3 błędne próby -> blokada konta na 5 minut.
  - `US-1.3`: Jako audytor bezpieczeństwa chcę przeglądać logi zdarzeń uwierzytelniania, aby wykrywać próby nieautoryzowanego dostępu.

---

### Epik 2: [Nazwa Modułu, np. Moduł Kartoteki Zasobów i Katalogu Usług]
- **Właściciel Epiku (Autor EU1):** [Imię i Nazwisko Studenta 2]
- **Klucz Jira:** `[NEX-EPIC-2]`
- **Zakres:** Definiowanie pozycji katalogowych, warianty, cenniki, kategorie, wyszukiwanie i filtrowanie.
- **Wstępne User Stories:**
  - `US-2.1`: Jako menedżer chcę dodawać nowe pozycje do katalogu wraz ze zdjęciem, kodem SKU i ceną jednostkową, aby udostępnić je do zamawiania.
    - *Kryteria akceptacji:* Walidacja unikalności SKU; weryfikacja poprawności formatu ceny (dokładność 2 miejsc po przecinku).
  - `US-2.2`: Jako pracownik chcę filtrować katalog po kategoriach i stanach aktywności, aby szybko odnaleźć poszukiwaną pozycję.
  - `US-2.3`: Jako menedżer chcę wycofywać pozycje z oferty (soft-delete), aby zachować spójność historycznych transakcji.

---

### Epik 3: [Nazwa Modułu, np. Moduł Rezerwacji i Cyklu Życia Zamówień]
- **Właściciel Epiku (Autor EU1):** [Imię i Nazwisko Studenta 3]
- **Klucz Jira:** `[NEX-EPIC-3]`
- **Zakres:** Składanie zamówień, walidacja reguł biznesowych, maszyna stanów (`Draft` -> `Confirmed` -> `InPreparation` -> `Completed` -> `Cancelled`).
- **Wstępne User Stories:**
  - `US-3.1`: Jako klient / dyspozytor chcę złożyć nowe zamówienie wielopozycyjne, aby zainicjować proces realizacji.
    - *Kryteria akceptacji:* Zamówienie musi zawierać min. 1 pozycję; automatyczna rezerwacja stanów przez port modułu magazynu.
  - `US-3.2`: Jako kierownik chcę zmieniać stan zamówienia zgodnie ze zdefiniowaną maszyną stanów, aby monitorować postęp.
    - *Kryteria akceptacji:* Przejście do `Cancelled` dozwolone tylko przed stanem `InPreparation`; każde przejście logowane z czasem i ID użytkownika.
  - `US-3.3`: Jako użytkownik chcę podejrzeć historię zmian statusów zamówienia, aby wiedzieć, kto i kiedy dokonał modyfikacji.

---

### Epik 4: [Nazwa Modułu, np. Moduł Gospodarki Magazynowej i Rezerwacji Stanów]
- **Właściciel Epiku (Autor EU1):** [Imię i Nazwisko Studenta 4]
- **Klucz Jira:** `[NEX-EPIC-4]`
- **Zakres:** Bilans magazynowy, dokumenty przyjęcia/wydania (PZ/WZ), ostrzeżenia o brakach, partie towarów.
- **Wstępne User Stories:**
  - `US-4.1`: Jako magazynier chcę zarejestrować przyjęcie dostawy (PZ), aby zwiększyć dostępny stan magazynowy.
    - *Kryteria akceptacji:* Wprowadzenie ilości całkowitej > 0; aktualizacja stanu dostępnego i fizycznego w transakcji atomowej.
  - `US-4.2`: Jako system chcę automatycznie blokować stan magazynowy w momencie potwierdzenia zamówienia, aby uniknąć sprzedaży nadmiarowej (*Overselling*).
  - `US-4.3`: Jako kierownik chcę otrzymywać raport pozycji poniżej stanu minimalnego, aby w porę złożyć zamówienie u dostawcy.

---

### Epik 5: [Nazwa Modułu, np. Moduł Finansów, Rozliczeń i Fakturowania]
- **Właściciel Epiku (Autor EU1):** [Imię i Nazwisko Studenta 5]
- **Klucz Jira:** `[NEX-EPIC-5]`
- **Zakres:** Kalkulacja podatku VAT, generowanie podsumowań finansowych, wystawianie dokumentów rozliczeniowych, obsługa płatności.
- **Wstępne User Stories:**
  - `US-5.1`: Jako księgowy chcę wygenerować dokument podsumowania sprzedaży dla zrealizowanego zamówienia, aby udokumentować transakcję.
    - *Kryteria akceptacji:* Wyliczenie kwot netto, stawek VAT i brutto; generowanie unikalnego numeru dokumentu wg maski `FV/YYYY/MM/NNNN`.
  - `US-5.2`: Jako klient chcę zarejestrować płatność za zamówienie, aby zaktualizować status rozliczenia na `Opłacone`.
  - `US-5.3`: Jako menedżer chcę wygenerować raport obrotów w wybranym przedziale dat z podziałem na metody płatności.

---

### Epik 6: [Nazwa Modułu, np. Moduł Powiadomień, Alertów i Komunikacji]
- **Właściciel Epiku (Autor EU1):** [Imię i Nazwisko Studenta 6]
- **Klucz Jira:** `[NEX-EPIC-6]`
- **Zakres:** Wysyłka powiadomień e-mail, alerty wewnątrz aplikacji (in-app toast/bell), szablony wiadomości, kolejkowanie powiadomień.
- **Wstępne User Stories:**
  - `US-6.1`: Jako klient chcę otrzymać e-mail z potwierdzeniem zamówienia i zestawieniem pozycji, aby mieć trwały dowód zakupu.
    - *Kryteria akceptacji:* Wysłanie wiadomości w tle w czasie < 30 s od zdarzenia `OrderPlacedDomainEvent`; obsługa błędów SMTP z mechanizmem retry.
  - `US-6.2`: Jako pracownik magazynu chcę widzieć alert w systemie, gdy zamówienie oczekuje na skompletowanie dłużej niż 15 minut.
  - `US-6.3`: Jako administrator chcę konfigurować szablony powiadomień e-mail za pomocą zmiennych szablonowych (`{{user_name}}`, `{{order_id}}`).

---

## 5. Harmonogram Semestru 1 i Szacunki Nakładów (EU4)

Semestr 1 obejmuje fazę analizy, przygotowania fundamentów architektonicznych oraz realizację kluczowych ścieżek krytycznych (Core MVP) w podziale na 5 dwutygodniowych sprintów:

| Sprint | Przedział Czasowy | Cel Sprintu (Sprint Goal) | Szacowany Nakład (h) | Kluczowy Deliverable |
|:---:|:---:|---|:---:|---|
| **Sp 0** | Tydzień 1–2 | Przygotowanie DIP, środowiska Jira/Confluence/Bitbucket, szkieletu projektu i CI | 60 h (zespół) | Gotowy DIP, zielony pipeline CI, szkielet Monorepo |
| **Sp 1** | Tydzień 3–4 | Zręby modułów 1 i 2: Autentykacja podstawowa + CRUD Katalogu | 60 h (zespół) | Działające logowanie i dodawanie pozycji katalogowych |
| **Sp 2** | Tydzień 5–6 | Moduły 3 i 4: Logika zamówień + Podstawowy stan magazynowy | 60 h (zespół) | Złożenie zamówienia z rezerwacją stanu magazynowego |
| **Sp 3** | Tydzień 7–8 | Moduły 5 i 6: Pierwsze podsumowanie finansowe + E-mail notyfikacje | 60 h (zespół) | Pełny obieg zamówienia od koszyka do powiadomienia |
| **Sp 4** | Tydzień 9–10 | Pętla z użytkownikiem końcowym: Poprawki UX, optymalizacje, testy regresji | 50 h (zespół) | Zweryfikowany przez użytkownika działający system MVP |
| **Sp 5** | Tydzień 11–12 | Stabilizacja, audyt dokumentacji (EU6), przygotowanie do pokazu końcowego (EU5) | 40 h (zespół) | Raport końcowy semestru, prezentacja, demonstracja |

---

## 6. Organizacja Zespołu i Harmonogram Rotacji Ról (EU2, EU3, EU4)

Zgodnie z wymogami sylabusa każdy student pełni rolę **Właściciela Produktu (Kierownika Zespołu)** w co najmniej jednym sprincie, podlegając rygorystycznej ocenie w zakresie EU3 i EU4.

### 6.1. Harmonogram Rotacji Roli Product Ownera

| Sprint | Imię i Nazwisko PO | Zakres odpowiedzialności ocenianej na bdb |
|:---:|---|---|
| **Sprint 1** | [Student 1] | Przygotowanie Backlogu Sprintu 1, podział zadań $\le 4$h, prowadzenie ceremonii, raporty Daily, wykres Burndown, Retro z delty estymacji. |
| **Sprint 2** | [Student 2] | Przejęcie backlogu, estymacja Sprintu 2, zarządzanie ryzykiem technicznym magazynu, raportowanie Daily, analiza Burndown. |
| **Sprint 3** | [Student 3] | Koordynacja integracji finansowo-notyfikacyjnej, ceremonie, egzekwowanie Definition of Ready, analiza delty szacunków. |
| **Sprint 4** | [Student 4] | Organizacja sesji Review z użytkownikiem końcowym, zbieranie feedbacku, zarządzanie poślizgami, raport Daily. |
| **Sprint 5** | [Student 5] | Stabilizacja, koordynacja dokumentacji Confluence (EU6), przygotowanie demonstracji końcowej (EU5). |
| *(Opcjonalnie Sp 6)* | [Student 6] | Retrospektywa semestralna, archiwizacja metryk, plan na Semestr 2. |

### 6.2. Macierz Odpowiedzialności (RACI)

| Aktywność Projektowa | Product Owner Sprintu | Deweloper (Autor Epiku) | Zespół Deweloperski | Prowadzący (Scrum Master) |
|---|:---:|:---:|:---:|:---:|
| **Tworzenie założeń Epiku (EU1)** | C | **A / R** | C | I |
| **Prowadzenie Planningu & Rozbicie Zadań (EU3)** | **A / R** | C | C | I |
| **Estymacja Zadań w Jira (EU4)** | A | **R** | R | I |
| **Prowadzenie Burndown Charta (EU4)** | **A / R** | I | I | I |
| **Prowadzenie Daily & Raporty (EU3, EU2)** | **A / R** | R | R | I |
| **Implementacja Kodu w Sprincie (EU2)** | I | **A / R** | R | I |
| **Dokumentacja Kodu w Confluence (EU6)** | C | **A / R** | R | I |
| **Prowadzenie Sprint Review (EU5)** | **A / R** | R (Demo modułu) | R | I (Oceniający) |
| **Arbitraż w sporach estymacji** | R | R | I | **A (Arbiter)** |

*Legenda: A - Accountable (Odpowiedzialny jednoosobowo za wynik), R - Responsible (Wykonujący zadanie), C - Consulted (Konsultowany), I - Informed (Informowany).*

---

## 7. Rejestr Ryzyk i Plan Mitygacji (EU4)

| ID | Opis Ryzyka | P-stwo | Wpływ | Plan Mitygacji (Działanie Prewencyjne) | Właściciel |
|:---:|---|:---:|:---:|---|:---:|
| **R-1** | **Przeciążenie dewelopera / Niedoszacowanie zadania:** Zadanie okazuje się zbyt trudne, grożąc karą obniżenia oceny. | Średnie | Wysoki | **Zasada zadania atomowego $\le 4$h.** W przypadku niepewności PO tworzy zadanie badawcze (*Spike*) na 2h przed planowaniem właściwym. | PO danego sprintu |
| **R-2** | **Konflikty w kodzie i łamanie granic modułów:** Deweloperzy edytują te same pliki lub wstrzykują zależności bazy danych. | Wysokie | Wysoki | Architektura Modular Monolith. Wydzielone katalogi per moduł. Testy integracyjne w CI blokujące merge przy naruszeniu reguł zależności. | Tech Lead / PO 1 |
| **R-3** | **Utrata kontaktu z użytkownikiem końcowym:** Użytkownik przestaje odpisywać lub nie ma czasu na Review. | Średnie | Krytyczny | Zabezpieczenie drugiego (zastępczego) użytkownika w fazie inicjacji. Weryfikacja dostępności na 3 dni przed każdym Review. | PO Sprintu |
| **R-4** | **Nierównomierne zaangażowanie w zespole:** Część osób nie loguje czasu ani nie uczestniczy w Daily. | Średnie | Średni | Jawne raporty Daily w Confluence. Zgodnie z regulaminem każdy brak na Daily skutkuje bezpośrednim obniżeniem oceny indywidualnej o 0.5 lub 1. | PO Sprintu / SM |

---

## 8. Umowa Zespołowa (Working Agreement & Definition of Done)

### 8.1. Definition of Ready (DoR) — Warunek wejścia zadania do Sprintu
Zadanie może zostać dodane do Backlogu Sprintu przez PO **wyłącznie wtedy, gdy**:
1. Posiada precyzyjne kryteria akceptacji (Given-When-Then).
2. Posiada oszacowany czas realizacji **$\le 4$ godzin**.
3. Deweloper przypisany do zadania osobiście potwierdził realizm estymacji podczas ceremonii Sprint Planningu.
4. Zależności zewnętrzne (np. endpoint z innego modułu) są zmockowane lub gotowe.

### 8.2. Definition of Done (DoD) — Warunek zaliczenia zadania w Sprincie
Zadanie w Jira może przejść do statusu `DONE` **wyłącznie wtedy, gdy**:
1. Kod znajduje się na gałęzi funkcjonalnej powiązanej z kluczem Jira (`feature/NEX-XX-opis`).
2. Kod kompiluje się bez błędów i ostrzeżeń lintera w pipeline Bitbucket CI.
3. Testy jednostkowe dla logiki biznesowej przechodzą w 100%.
4. Pull Request został przejrzany i zaakceptowany przez co najmniej 1 innego członka zespołu (Code Review).
5. Funkcjonalność została udokumentowana na dedykowanej stronie modułu w Confluence (EU6).
6. Zmiana została zaprezentowana na środowisku deweloperskim i zweryfikowana z kryteriami akceptacji.
