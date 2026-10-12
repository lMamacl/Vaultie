# Katalog Przykładowych Tematów Projektów Zespołowych

Niniejszy dokument zawiera ustrukturyzowany zbiór przykładowych tematów projektowych dla przedmiotu *Projekt zespołowy*. Każdy temat przedstawia kontekst biznesowy lub domenowy problemu, zidentyfikowane wyzwania inżynierskie, wymagania funkcjonalne oraz zestaw materiałów referencyjnych.

---

## Temat 1: Platforma do organizacji konferencji i spotkań biznesowych z modułem business matchingu

### Tło problemu
Konferencje, meetupy, śniadania biznesowe oraz spotkania firmowe to dla uczestników kluczowa okazja do nawiązywania relacji z potencjalnymi klientami, partnerami handlowymi i współpracownikami. Uczestnicy zgodnie podkreślają, że największą wartością takich wydarzeń są bezpośrednie rozmowy. 

W praktyce networking bywa dziełem przypadku: uczestnicy nie wiedzą z wyprzedzeniem, kto bierze udział w wydarzeniu, czym się zajmuje ani jakich tematów poszukuje. Krótkie przerwy kawowe rzadko wystarczają na odnalezienie odpowiednich rozmówców. Z kolei organizatorzy korzystają z wielu rozproszonych narzędzi (rejestracja w jednym serwisie, agenda w pliku PDF, korespondencja e-mailowa, a spotkania 1:1 ustalane manualnie na kartkach lub w arkuszu kalkulacyjnym).

### Zidentyfikowane problemy
- **Przypadkowy networking:** Uczestnicy nie mają narzędzi umożliwiających wcześniejsze zidentyfikowanie osób o zbliżonych profilach zawodowych lub komplementarnych potrzebach.
- **Szczątkowe profile uczestników:** Listy uczestników ograniczają się zazwyczaj do imienia, nazwiska i nazwy firmy, bez informacji o obszarach kompetencji, celach biznesowych czy poszukiwanych kontaktach.
- **Trudności w koordynacji spotkań 1:1:** Manualne uzgadnianie terminów i lokalizacji rodzi kolizje z agendą prelekcji oraz innymi spotkaniami.
- **Fragmentacja narzędzi organizatora:** Dane dotyczące rejestracji, harmonogramu, komunikacji oraz list obecności znajdują się w odrębnych, niespójnych systemach.
- **Utrata relacji po wydarzeniu:** Brak ujednoliconego kanału do kontynuowania rozpoczętych dyskusji i planowania kolejnych kroków biznesowych.
- **Brak analityki powydarzeniowej:** Organizator nie dysponuje danymi o liczbie zrealizowanych spotkań, wskaźnikach zaangażowania ani najbardziej poszukiwanych tematach.

### Cel i wyzwanie projektowe
Zaprojektowanie i wdrożenie responsywnej aplikacji webowej (w pełni zoptymalizowanej pod kątem urządzeń mobilnych), która wesprze kompleksową organizację wydarzeń (od małych spotkań biznesowych po wielościeżkowe konferencje). Kluczowym modułem systemu ma być mechanizm inteligentnego doboru kontaktów (*business matching*), umawianie dedykowanych sesji 1:1 oraz obsługa rotacyjnych sesji networkingowych typu *speed networking*.

System powinien obsługiwać co najmniej cztery role użytkowników:
1. **Organizator:** Tworzenie i konfiguracja wydarzeń, zarządzanie agendą, koordynacja sesji networkingowych, podgląd statystyk;
2. **Uczestnik:** Zarządzanie profilem biznesowym, personalizacja agendy, wyszukiwanie kontaktów, umawianie spotkań;
3. **Prelegent:** Zarządzanie biogramem, informacjami o wystąpieniach oraz materiałami prezentacyjnymi;
4. **Administrator:** Centralne zarządzanie kontami, uprawnieniami i parametrami technicznymi systemu.

### Wymagania funkcjonalne

#### 1. Zarządzanie wydarzeniami
- Obsługa różnych formatów: konferencje wielotorowe, meetupy, śniadania biznesowe, spotkania kontraktacyjne B2B, dedykowane sesje *speed networkingu*.
- Obsługa formuły wydarzeń: stacjonarne, zdalne (online) oraz hybrydowe.
- Moduł rejestracji: limity miejsc, obsługa list rezerwowych/oczekujących, rejestracja otwarta lub na zaproszenie.
- Weryfikacja obecności uczestników na miejscu z wykorzystaniem dynamicznych kodów QR.

#### 2. Agenda i harmonogram
- Definiowanie sesji, ścieżek tematycznych, sal i prelegentów wraz z tagowaniem tematycznym.
- Spersonalizowana agenda uczestnika (wybór interesujących prelekcji, eksport do zewnętrznych kalendarzy iCal/Google).
- System powiadomień w czasie rzeczywistym o zmianach w agendzie i opóźnieniach.

#### 3. Profile biznesowe uczestników
- Wizytówka zawodowa: stanowisko, organizacja, branża, biogram, fotografia profilowa.
- Matryca zainteresowań wybierana z puli tagów zdefiniowanej przez organizatora.
- Dedykowane sekcje kompetencyjne: „Chcę porozmawiać o…”, „Oferuję” oraz „Szukam”.
- Globalny profil użytkownika z możliwością dostosowywania widoczności i treści pod konkretne wydarzenie.
- Elastyczne ustawienia prywatności: kontrola widoczności profilu oraz możliwość wstrzymania przyjmowania zaproszeń.

#### 4. Wyszukiwanie kontaktów i silnik rekomendacji
- Zaawansowane filtry wyszukiwania: branża, organizacja, tagi zainteresowań, relacje „oferuję / szukam”.
- Algorytm rekomendacji uczestników w oparciu o zbieżność profili i komplementarność potrzeb.
- Uzasadnienie rekomendacji (np. „Użytkownik polecany ze względu na wspólny obszar: *Cloud Architecture*”).
- Oznaczanie kontaktów jako interesujących oraz ukrywanie nietrafionych podpowiedzi.

#### 5. Moduł Business Matchingu (Spotkania 1:1)
- Wysyłanie zaproszeń na precyzyjnie zdefiniowane spotkania z określeniem agendy rozmowy; workflow: akceptacja, odrzucenie, propozycja alternatywnego terminu.
- Definiowanie przez organizatora okienek czasowych (np. sloty 15-, 20- lub 30-minutowe) oraz dedykowanych stref spotkań (stoliki, boksy, sale).
- Automatyczne wykrywanie i blokowanie kolizji z wybranymi prelekcjami w agendzie i innymi spotkaniami; konfigurowalny limit spotkań na uczestnika.
- Obsługa spotkań przed, w trakcie oraz po wydarzeniu (w tym integracja wideorozmów online).
- Automatyczne przypomnienia przed spotkaniem oraz potwierdzenie jego realizacji.
- Możliwość sporządzenia prywatnej notatki i oceny wartości spotkania po jego zakończeniu.

#### 6. Speed Networking (Sesje rotacyjne)
- Parametryzacja sesji: liczba rund, czas trwania rozmowy, liczba dostępnych stanowisk/stolików.
- Automatyczny algorytm rotacyjny: kojarzenie par lub małych grup z uwzględnieniem preferencji tematycznych, wykluczaniem powtórzeń oraz blokowaniem par z tej samej organizacji.
- Panel sterowania sesją na żywo: odliczanie czasu, prezentacja kolejnych par na ekranie głównym sali konferencyjnej.
- Mechanizm obustronnej zgody (*mutual match*): wymiana danych kontaktowych następuje wyłącznie w sytuacji, gdy obie strony wyrażą taką chęć po zakończonej sesji.

#### 7. Relacje powydarzeniowe
- Cyfrowa wizytówka (kod QR) umożliwiająca natychmiastową wymianę namiarów.
- Indeks poznanych osób z prywatnymi notatkami oraz opcją eksportu danych.
- Możliwość inicjowania kolejnych spotkań po formalnym zakończeniu wydarzenia.
- Wielokanałowe powiadomienia (e-mail, komunikaty w aplikacji) oraz ogłoszenia organizatora.

#### 8. Panel analityczny organizatora
- Bieżący monitoring frekwencji: statystyki zapisów, obecności na miejscu, obłożenie sal.
- Analityka spotkań 1:1: liczba zaproszeń, współczynnik akceptacji, odsetek spotkań zrealizowanych.
- Macierz zapotrzebowania tematycznego (analiza dysproporcji pomiędzy tematami poszukiwanymi a oferowanymi).
- Moduł ankiet powydarzeniowych z automatycznym podsumowaniem wyników.

---

## Temat 2: Aplikacja carpooling / ridesharing („podwózka” miejska)

### Tło problemu
Współdzielenie samochodu w modelu *peer-to-peer* (*carpooling* / *ridesharing*) polega na udostępnianiu wolnych miejsc w pojeździe przez kierowcę, który realizuje zaplanowaną trasę, osobom podróżującym w tym samym kierunku. Model ten stanowi kluczowy element ekonomii współdzielenia (*sharing economy*) i znajduje zastosowanie zarówno w podróżach dalekobieżnych, jak i w codziennych dojazdach aglomeracyjnych.

Wyróżnia się kilka modeli biznesowych współdzielenia pojazdów: *carsharing* stacjonarny, *free-floating*, *peer-to-peer* oraz klasyczny *carpooling/ridesharing*. Niniejsze zadanie koncentruje się na modelu miejskiego *ridesharingu*, w którym kierowca zabiera pasażerów w trakcie swoich regularnych przejazdów po mieście lub aglomeracji (dojazdy do pracy, na uczelnię).

Kluczowe wyróżniki modelu:
- **Partycypacja w kosztach:** Przejazdy nie mają charakteru zarobkowego (w przeciwieństwie do taksówek czy platform typu ride-hailing na zlecenie); celem jest zrównoważenie kosztów paliwa i eksploatacji.
- **Rozliczenia przez platformę:** Płatności i rozliczenia realizowane są za pośrednictwem systemu (w tym z wykorzystaniem punktów lub wewnętrznej waluty wirtualnej), co zapewnia bezpieczeństwo i eliminuje konieczność rozliczeń gotówkowych.
- **Lokalna specyfika aglomeracyjna:** Koncepcja zbliżona mechaniką do serwisu BlaBlaCar, lecz zoptymalizowana pod kątem powtarzalnych tras miejskich i podmiejskich.

### Cel i wyzwanie projektowe
Opracowanie aplikacji mobilnej i webowej łączącej kierowców dysponujących wolnymi miejscami z pasażerami poszukującymi przejazdu na terenie aglomeracji miejskiej. 

Kluczowe zagadnienia do analizy i implementacji:
1. **Publikacja i wyszukiwanie tras:** Kierowcy publikują regularne trasy i liczbę dostępnych miejsc; pasażerowie przeszukują i filtrują oferty według lokalizacji początkowej, punktów pośrednich i docelowych oraz rezerwują miejsca online.
2. **Integracja z samorządem miejskim:** Przeprowadzenie analizy dobrych praktyk na rynku europejskim i zaprojektowanie mechanizmów zachęt we współpracy z urzędem miasta dla kierowców udostępniających przejazdy (np. punkty wymienialne na zniżki na bilety komunikacji miejskiej, dostęp do stref płatnego parkowania, uprawnienia do korzystania z buspasów).
3. **Budowa zaufania i bezpieczeństwa:** Obustronny system ocen, recenzji i weryfikacji tożsamości użytkowników po zakończonym przejeździe.

### Materiały referencyjne
- [Deloitte: Car Sharing in Europe](https://www2.deloitte.com/content/dam/Deloitte/de/Documents/consumer-industrial-products/CIP-Automotive-Car-Sharing-in-Europe.pdf)
- [The Conversation: 12 best ways to get cars out of cities – ranked by new research](https://theconversation.com/12-best-ways-to-get-cars-out-of-cities-ranked-by-new-research-180642)
- [Włącz Oszczędzanie: Carpooling – jak działa współdzielenie przejazdów](https://wlaczoszczedzanie.pl/carpooling/)

---

## Temat 3: Platforma oceny i zarządzania jakością danych dla systemów AI/analitycznych

### Tło problemu
W dobie dynamicznego rozwoju sztucznej inteligencji i analityki zaawansowanej przedsiębiorstwa stoją przed wyzwaniem zapewnienia jakości, bezpieczeństwa i zgodności regulacyjnej danych wykorzystywanych do trenowania modeli oraz wnioskowania. Europejski akt o sztucznej inteligencji (*EU AI Act – Rozporządzenie 2024/1689*) oraz przepisy RODO nakładają na organizacje rygorystyczne obowiązki w zakresie nadzoru nad danymi (*Data Governance*).

### Zidentyfikowane problemy
- **Brak przejrzystości zasobów danych:** Pracownicy i inżynierowie ML nie mają pewności, które zbiory danych mogą być legalnie i bezpiecznie wykorzystywane w projektach AI, a które podlegają ograniczeniom prawnym.
- **Ryzyko naruszenia regulacji:** *AI Act* wprowadza kategoryzację systemów AI według stopnia ryzyka i wymaga drobiazgowej dokumentacji danych treningowych. Brak sformalizowanej oceny grozi surowymi karami finansowymi.
- **Niska jakość danych wejściowych:** Zbiory bywają niekompletne, zdezaktualizowane lub obarczone błędami, co prowadzi do halucynacji modeli, zjawiska *biasu* oraz nietrafnych decyzji biznesowych.
- **Brak metadanych i identyfikowalności (*Data Lineage*):** Niedostateczna dokumentacja pochodzenia danych i przekształceń utrudnia audytowalność systemów.
- **Rozmyta odpowiedzialność:** Brak klarownego podziału ról pomiędzy właścicielami danych (*Data Owners*), opiekunami danych (*Data Stewards*), oficerami compliance a zespołami Data Science.

### Cel i wyzwanie projektowe
Stworzenie platformy webowej umożliwiającej ustrukturyzowaną inwentaryzację, audyt jakości oraz zarządzanie cyklem akceptacji danych przeznaczonych do systemów AI i analityki biznesowej, zgodnie ze standardami *Data Governance* oraz wytycznymi *AI Act*.

### Zakres modułów funkcjonalnych

#### 1. Katalog i inwentaryzacja danych
- Centralny rejestr zbiorów danych dostępnych w organizacji.
- Automatyczne wykrywanie i tagowanie danych wrażliwych (dane osobowe, dane szczególnych kategorii wg RODO, tajemnica przedsiębiorstwa).
- Rejestracja pochodzenia danych (*Data Lineage*) – pełna ścieżka źródeł, transformacji i potoków ETL.
- Przypisywanie ról zarządczych (*Data Owner*, *Data Steward*) do poszczególnych zasobów.

#### 2. Ocena jakości danych (Data Quality Assessment)
- Automatyczna ewaluacja zbiorów w oparciu o 5 klasycznych wymiarów jakości:
  1. Kompletność (*completeness*)
  2. Dokładność (*accuracy*)
  3. Spójność (*consistency*)
  4. Aktualność (*timeliness*)
  5. Unikalność (*uniqueness*)
- Panel wskaźników (*Dashboard*) prezentujący syntetyczną ocenę jakości dla każdego zbioru.
- Konfigurowalny system powiadomień o degradacji jakości poniżej zadanych progów tolerancji.
- Automatyczne generowanie rekomendacji działań naprawczych.

#### 3. Weryfikacja zgodności z AI Act i RODO
- Kwestionariusz klasyfikacji ryzyka systemu AI (kwalifikacja do kategorii minimalnego, wysokiego lub niedozwolonego ryzyka wg *AI Act*).
- Walidacja wymagań dla systemów wysokiego ryzyka: reprezentatywność próbki, audyt pod kątem niepożądanego obciążenia (*bias audit*), kompletność metadanych technicznych.
- Weryfikacja przesłanek legalności przetwarzania wg RODO (podstawa prawna, zasada minimalizacji danych, retencja).

#### 4. Workflow zatwierdzania wykorzystania danych w projektach AI
- Ścieżka wnioskowania o dostęp do wybranego zbioru danych na potrzeby projektu analitycznego/AI.
- Wielopoziomowy proces weryfikacji:
  - *Data Owner* – autoryzacja biznesowa;
  - *Data Steward* – walidacja jakościowa i profilowanie;
  - *Compliance Officer* – audyt zgodności regulacyjnej;
  - *Inspektor Ochrony Danych (IOD/DPO)* – weryfikacja przetwarzania danych osobowych.
- Niezmienna historia decyzji, zgód i uzasadnień odmów na potrzeby audytu zewnętrznego.

### Materiały referencyjne
- [Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2024/1689 (AI Act)](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32024R1689)
- [Urząd Ochrony Danych Osobowych: RODO a sztuczna inteligencja](https://uodo.gov.pl/pl/138/2458)
- [Dataversity: What is Data Governance?](https://www.dataversity.net/what-is-data-governance/)
- [ISO/IEC 38505: Governance of Data](https://www.iso.org/standard/56639.html)
- [MIT Information Quality Program (MITIQ): Data Quality Dimensions Framework](https://mitiq.mit.edu/)
- [Serwis Rzeczypospolitej Polskiej: AI Act – przewodnik dla przedsiębiorstw](https://www.gov.pl/web/ai/ai-act)

---

## Temat 4: System certyfikacji produktów żywnościowych w łańcuchu dostaw

> [!NOTE]
> **Adnotacja redakcyjna:** W pierwotnym zestawieniu uczelnianym temat ten figurował podwójnie (jako dwie odrębne pozycje na liście). W niniejszej redakcji połączono je w jedną, spójną kartę wymagań, zachowując kompletny zakres merytoryczny.

### Tło problemu
Współczesny rynek rolno-spożywczy boryka się z narastającym problemem fałszowania produktów i bezprawnego przypisywania oznaczeń jakościowych (np. BIO, EKO, ChNP, ChOG). Szacuje się, że straty wynikające z fałszowania żywności w Unii Europejskiej sięgają ok. 50 miliardów euro rocznie. Konsumenci coraz silniej domagają się przejrzystości pochodzenia kupowanych produktów, szczególnie w segmencie żywności ekologicznej i tradycyjnej.

Tradycyjne mechanizmy certyfikacji bazują na dokumentacji papierowej i silosowych bazach danych, podatnych na błędy, opóźnienia i manipulacje. Uczestnicy łańcucha dostaw (producenci, przetwórcy, dystrybutorzy, sieci handlowe) napotykają bariery w natychmiastowej weryfikacji ważności certyfikatów i odtworzeniu pełnej ścieżki partii towaru „od pola do stołu”.

### Zidentyfikowane problemy w łańcuchu dostaw
- **Brak transparentności:** Trudność w prześledzeniu pełnej drogi produktu przez poszczególne ogniwa logistyczne.
- **Ryzyko fałszowania atestów:** Możliwość podrabiania papierowych certyfikatów jakości i rolnictwa ekologicznego.
- **Fragmentacja danych:** Rozproszenie informacji pomiędzy odrębnymi systemami kontrahentów.
- **Czasochłonne kontrole:** Długi czas oczekiwania na potwierdzenie autentyczności certyfikatów przez jednostki inspekcyjne.
- **Erozja zaufania konsumentów:** Spadek zaufania wywołany nagłaśnianymi aferami w branży spożywczej.
- **Wysokie koszty audytów:** Złożone i kosztowne procedury kontrolne w tradycyjnych łańcuchach.

Rozwiązania oparte na technologii rozproszonego rejestru (*Blockchain*) w połączeniu z systemami FoodTech i AgriTech umożliwiają stworzenie niezmiennego, audytowalnego rejestru wszystkich zdarzeń gospodarczych w łańcuchu dostaw.

### Cel i wyzwanie projektowe
Zaprojektowanie i implementacja systemu weryfikacji i certyfikacji produktów żywnościowych, opartego o technologię blockchain, eliminującego ryzyko nadużyć i zapewniającego przejrzystość na każdym etapie dystrybucji.

### Zakres modułów funkcjonalnych

#### 1. Rejestracja i weryfikacja certyfikatów
- Mechanizm cyfrowej rejestracji certyfikatów BIO/EKO przez akredytowane jednostki certyfikujące w sieci blockchain.
- Natychmiastowa weryfikacja ważności atestu poprzez skanowanie kodu QR lub wprowadzenie unikalnego identyfikatora.
- Zabezpieczenie integralności certyfikatów za pomocą podpisów cyfrowych jednostek wystawiających.
- Automatyczne alerty o zbliżającym się terminie wygaśnięcia uprawnień certyfikacyjnych.

#### 2. Śledzenie łańcucha dostaw (Track & Trace)
- Rejestracja przepływu partii towaru w węzłach: producent pierwotny $\to$ przetwórca $\to$ centrum dystrybucyjne $\to$ punkt sprzedaży.
- Powiązanie partii surowców (*batch tracking*) z konkretnymi certyfikatami gospodarstw.
- Implementacja osi czasu „od pola do stołu” dostępnej dla użytkowników.
- Zapis kluczowych parametrów telemetrycznych: data zbioru/uboju, warunki magazynowania, temperatura w łańcuchu chłodniczym.

#### 3. Wykrywanie anomalii i inteligentne kontrakty (Smart Contracts)
- Automatyczne blokowanie prób wprowadzenia do obrotu partii nieposiadających ważnego certyfikatu.
- System ostrzegania o naruszeniach integralności łańcucha (np. próba przetworzenia surowca ekologicznego w zakładzie bez certyfikacji przetwórczej).
- Inteligentne kontrakty egzekwujące reguły jakościowe przed zatwierdzeniem kolejnego transferu własności.
- Pulpit analityczny dla organów kontroli i inspekcji handlowej z mapą wykrytych nieprawidłowości.

#### 4. Portal konsumencki
- Publiczny moduł weryfikacji produktu poprzez skanowanie kodu QR na opakowaniu w sklepie.
- Interaktywna wizualizacja drogi produktu i pochodzenia jego składników.
- Podgląd zweryfikowanych cyfrowo odpisów certyfikatów jakościowych.
- Moduł zgłaszania podejrzeń naruszeń przez konsumentów.

### Materiały referencyjne
- **Regulacje prawne:**
  - [Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2018/848 w sprawie produkcji ekologicznej i znakowania produktów ekologicznych](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32018R0848)
  - [Ustawa o rolnictwie ekologicznym (Dz.U. 2020 poz. 1856)](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20200001856)
- **Standardy certyfikacji:**
  - [GIJHARS: System certyfikacji rolnictwa ekologicznego w Polsce](https://www.gov.pl/web/ijhars)
  - [Komisja Europejska: EU Organic Logo and labelling](https://agriculture.ec.europa.eu/farming/organic-farming/organic-logo_en)
- **Wdrożenia branżowe i FoodTech:**
  - [IBM Food Trust: Blockchain in Food Supply Chain](https://www.ibm.com/products/food-trust)
  - [Deloitte Insights: AgriTech – Revolutionizing Agriculture with Technology](https://www.deloitte.com/insights)
  - [Carrefour: Act for Food Blockchain Initiative](https://www.carrefour.com)
  - [Walmart: Food Traceability Initiative](https://corporate.walmart.com)
  - [TE-FOOD: Supply Chain Management on Blockchain](https://www.te-food.com)

---

## Temat 5: System ocen pracowniczych Politechniki Białostockiej

### Tło problemu
Zgodnie z art. 115 ustawy *Prawo o szkolnictwie wyższym i nauce*, nauczyciele akademiccy (z wyjątkiem rektora) podlegają obowiązkowej ocenie okresowej, w szczególności w zakresie wykonywania obowiązków dydaktycznych, naukowych i organizacyjnych, a także przestrzegania przepisów o prawie autorskim i własności przemysłowej.

System ocen pracowniczych służy kompleksowej ewaluacji osiągnięć kadry akademickiej. W praktyce uczelnianej proces ten często opiera się na ręcznym wypełnianiu formularzy arkuszy kalkulacyjnych, co rodzi problemy z poprawnością wyliczeń, spójnością weryfikacji i terminowością.

### Główne założenia i wymagania ogólne
- **Automatyzacja formularzy:** Generowanie spersonalizowanych arkuszy samooceny z automatycznym wstępnym uzupełnianiem danych na podstawie profilu pracownika w systemie uczelnianym.
- **Dwuetapowa ścieżka weryfikacji:**
  - *Etap I:* bezpośredni przełożony (kierownik katedry / zakładu) – weryfikacja merytoryczna i ewentualna korekta wpisów,
  - *Etap II:* wydziałowa/uczelniana komisja oceniająca – formalne zatwierdzenie wyniku oceny.
- **Elastyczność reguł oceny:** Możliwość równoległego definiowania i funkcjonowania odmiennych kryteriów oceny (np. dla grup pracowników badawczo-dydaktycznych, dydaktycznych oraz badawczych) w tym samym okresie ewaluacyjnym.
- **Obsługa progów i minimów regulaminowych:** Automatyczna kontrola spełnienia progów punktowych wymaganych przez uczelniany regulamin oceny.
- **Hierarchiczna struktura wniosku:** Trzystopniowy układ danych: *Obszar* $\to$ *Kategoria* $\to$ *Osiągnięcie*. Kryteria punktowe podzielone są na trzy główne filary:
  1. Działalność naukowa,
  2. Działalność dydaktyczna,
  3. Działalność organizacyjna.
- **Archiwizacja i ciągłość:** Wgląd w historię ocen z poprzednich okresów oraz treść archiwalnych wniosków.
- **Zapewnienie kompletności:** Formalne zatwierdzanie kompletności zgłoszenia przez pracownika przed przekazaniem do oceny przełożonemu.

### Cel i wyzwanie projektowe
Opracowanie zintegrowanego systemu informatycznego usprawniającego ewidencję osiągnięć, generowanie wniosków, audyt punktowy przełożonych oraz przeprowadzanie posiedzeń komisji oceniających.

### Role użytkowników i zakres odpowiedzialności
1. **Pracownik:**
   - bieżąca ewidencja osiągnięć naukowych, dydaktycznych i organizacyjnych,
   - monitoring bieżącego stanu punktowego w odniesieniu do wymagań regulaminowych w danym okresie oceny,
   - weryfikacja i formalne potwierdzenie kompletności składanego arkusza,
   - wgląd w cząstkowe i ostateczne wyniki oceny wraz z uzasadnieniem.
2. **Przełożony (Kierownik Katedry):**
   - ewidencja własnego dorobku pracowniczego,
   - weryfikacja wniosków podległych pracowników z prawem do korekty liczby punktów i dodawania uwag merytorycznych,
   - zatwierdzanie wniosków i przekazywanie ich do komisji oceniającej.
3. **Administrator / Dział Kadr:**
   - konfiguracja okresów ocen, kryteriów, wag oraz minimów punktowych,
   - wprowadzanie osiągnięć ogólnouczelnianych z zewnętrznych rejestrów,
   - automatyczna wysyłka przypomnień o terminach składania dokumentów,
   - generowanie indywidualnych protokołów ocen oraz zbiorczych zestawień analitycznych dla władz uczelni.

---

## Temat 6: Platforma dla organizacji NGO do zarządzania wolontariatem

### Tło problemu
Koordynacja pracy wolontariuszy w organizacjach pozarządowych (NGO) wiąże się ze znacznymi wyzwaniami operacyjnymi: dynamicznym zarządzaniem harmonogramami, pracą w warunkach nieoczekiwanych zmian podczas wydarzeń oraz koniecznością budowania zaangażowania zespołu. Koordynator pełni rolę kluczowego łącznika pomiędzy zarządem fundacji, liderami akcji, wolontariuszami a darczyńcami. Brak dedykowanych narzędzi prowadzi do chaosu komunikacyjnego, dublowania zapisów lub braków kadrowych w kluczowych godzinach akcji.

### Cel i wyzwanie projektowe
Zaprojektowanie i budowa aplikacji mobilnej zintegrowanej z panelem administracyjnym webowym, dedykowanej organizacjom pozarządowym. System ma usprawnić rejestrację wolontariuszy, planowanie akcji, podział zadań na sloty czasowe, komunikację bieżącą oraz relacje z darczyńcami.

### Wymagania funkcjonalne

#### 1. Zarządzanie użytkownikami i uprawnieniami
- Obsługa trzech podstawowych ról: użytkownik niezarejestrowany (gość), wolontariusz, administrator (koordynator).
- Rejestracja kandydatów na wolontariuszy poprzez profilowany formularz w aplikacji mobilnej.
- Procedura weryfikacji i zatwierdzania kont wolontariuszy przez koordynatora.

#### 2. Planowanie i zarządzanie akcjami wolontariackimi
- Tworzenie i parametryzacja akcji (wydarzenia jednodniowe i cykliczne).
- Podział wydarzenia na precyzyjne sloty czasowe i stanowiska zadaniowe.
- Zapisy wolontariuszy na wybrane sloty czasowe z uwzględnieniem limitów miejsc.
- Automatyczne zarządzanie listą główną oraz listą rezerwową na wypadek rezygnacji uczestnika.
- Zautomatyzowane powiadomienia przypominające o zbliżających się dyżurach.

#### 3. Moduł komunikacji
- System powiadomień *push* dla użytkowników aplikacji mobilnej.
- Segmentacja wysyłki komunikatów (do wszystkich użytkowników, do zweryfikowanych wolontariuszy, do osób zapisanych na konkretną akcję lub slot).
- Tablica aktualności organizacji NGO prezentowana na ekranie głównym aplikacji.

#### 4. Panel administracyjny koordynatora
- Centralne zarządzanie bazą wolontariuszy, historią ich aktywności i statystykami godzin.
- Ręczna moderacja list uczestników (możliwość ręcznego przesuwania pomiędzy listą podstawową a rezerwową dla poszczególnych slotów).
- Generowanie raportów zaangażowania wolontariuszy na potrzeby sprawozdawczości projektowej.

#### 5. Kalendarz wydarzeń
- Wizualizacja nadchodzących inicjatyw w przejrzystym widoku kalendarza.
- Bezpośrednia synchronizacja zarezerwowanych slotów z kalendarzem systemowym w smartfonie wolontariusza.

### Materiały referencyjne
- [Strony dla Organizacji: Moduł kalendarium do zarządzania wydarzeniami](https://stronydlaorganizacji.org/moduly/kalendarium)
- [Portal NGO.pl: Jak zaangażować wolontariusza do działań swojej organizacji?](https://poradnik.ngo.pl/jak-zaangazowac-wolontariusza-do-dzialan-swojej-organizacji)

---

## Temat 7: Platforma ESG do raportowania dla branży budowlanej (AI / LLM)

### Tło problemu
Przedsiębiorstwa sektora budowlanego mierzą się z rosnącymi wymaganiami dotyczącymi raportowania niefinansowego w obszarze ESG (*Environmental, Social, Governance*). Zbieranie danych o emisjach, łańcuchu podwykonawców, BHP na budowach i strukturze ładu korporacyjnego jest procesem pracochłonnym, wymagającym agregacji rozproszonych, nieustrukturyzowanych informacji (pliki PDF, skany faktur, arkusze kalkulacyjne, dokumentacja przetargowa). Ręczne tworzenie raportów grozi błędami, pominięciem istotnych wskaźników oraz trudnościami w interpretacji dynamicznie zmieniających się standardów.

### Cel i wyzwanie projektowe
Stworzenie platformy wykorzystującej duże modele językowe (*Large Language Models – LLM*) do automatyzacji przetwarzania nieustrukturyzowanych dokumentów budowlanych, interpretacji wymogów formalnych oraz generowania spójnych raportów ESG.

### Wymagania funkcjonalne

#### 1. Integracja modeli językowych (LLM)
- Bezpieczna integracja z API modeli LLM (np. rodzina GPT-4 / Claude / modele otwarte).
- Wykorzystanie modeli do semantycznej analizy, ekstrakcji i interpretacji danych z dokumentów technicznych.
- Generowanie podsumowań analitycznych i opisów w języku naturalnym zgodnie z konwencją raportowania niefinansowego.

#### 2. Wszechstronne przetwarzanie danych
- Ingestia i parsowanie plików w formatach Excel, CSV, PDF oraz dokumentów tekstowych.
- Automatyczne wyodrębnianie kluczowych metryk ESG (np. zużycie surowców, emisje Scope 1–3, wskaźniki wypadkowości).
- Kategoryzacja, tagowanie i mapowanie pozyskanych danych na filary E, S i G.

#### 3. Dziedzinowa baza wiedzy ESG
- Utrzymanie dedykowanej bazy wiedzy normatywnej dla budownictwa (taksonomia UE, dyrektywa CSRD, normy budownictwa zrównoważonego).
- Kontekstualizacja danych wejściowych z wykorzystaniem technik RAG (*Retrieval-Augmented Generation*).
- Zapewnienie aktualności bazy wiedzy w odniesieniu do pojawiających się nowelizacji standardów.

#### 4. Generator raportów
- Automatyczne komponowanie gotowych raportów ESG zgodnych z międzynarodowymi standardami (GRI, SASB, TCFD, ESRS).
- Personalizacja szablonów z uwzględnieniem specyfiki poszczególnych budów, projektów kubaturowych czy infrastrukturalnych.
- Interaktywny edytor raportu umożliwiający korektę i rozbudowę treści przy asyście AI.

---

## Temat 8: Obsługa delegacji krajowych

> [!NOTE]
> **Adnotacja redakcyjna:** Podobnie jak w przypadku tematu certyfikacji żywności, w pierwotnym wykazie uczelnianym pozycja ta występowała dwukrotnie. W niniejszej wersji zachowano pełny zakres merytoryczny w ramach jednego ujednoliconego opisu.

### Tło problemu
Delegacje krajowe stanowią powszechną formę podróży służbowych pracowników realizujących zadania poza stałym miejscem wykonywania pracy. Prawidłowa obsługa delegacji wymaga przejścia przez sformalizowane etapy: złożenie wniosku przez pracownika, akceptację przełożonego i dysponenta środków, ewentualne zaliczkowanie oraz końcowe rozliczenie poniesionych kosztów po powrocie.

Kluczowe uwarunkowania prawne i operacyjne:
- Ścisłe podporządkowanie przepisom prawa pracy i ordynacji podatkowej (limity diet, ryczałty za noclegi, zwrot kosztów dojazdu).
- Wymóg precyzyjnej ewidencji dokumentów księgowych na potrzeby kontroli skarbowej.
- Konieczność sprawnego zarządzania wnioskowaniem i rozliczaniem pobranych zaliczek gotówkowych lub przelewowych.

### Cel i wyzwanie projektowe
Zaprojektowanie i wdrożenie systemu informatycznego digitalizującego pełen obieg wniosków delegacyjnych, przyspieszającego zatwierdzanie wyjazdów, automatyzującego naliczanie diet i kosztów oraz ułatwiającego integrację z systemem finansowo-księgowym.

### Zagadnienia do analizy i implementacji
1. **Wnioskowanie i role użytkowników:** Obsługa ról: pracownik delegowany, przełożony zatwierdzający, pracownik kwestury/działu finansowego, administrator.
2. **Workflow akceptacji wniosków:** Elastyczny przepływ pracy (*workflow*) obejmujący możliwość akceptacji, odrzucenia wniosku z uzasadnieniem oraz skierowania do korekty przez pracownika.
3. **Moduł zaliczkowy:** Rejestracja zapotrzebowania na zaliczkę, potwierdzenie wypłaty oraz automatyczne rozliczenie pobranych środków przy składaniu końcowego rozliczenia.
4. **Kalkulator rozliczenia delegacji:** Automatyczne wyliczanie należnych diet (z uwzględnieniem czasu trwania podróży oraz ewentualnych posiłków zapewnionych przez organizatora), limitów i ryczałtów za noclegi oraz pozostałych wydatków udokumentowanych fakturami.
5. **Ewidencja przebiegu pojazdu (kilometrówka):** Obsługa rozliczeń wyjazdów prywatnym samochodem pracownika zgodnie z obowiązującymi stawkami za kilometr.
6. **Integracja systemowa:** Analiza i zaprojektowanie interfejsów wymiany danych z uczelnianym/firmowym systemem kadrowo-płacowym oraz finansowo-księgowym.
7. **Baza wiedzy i ocena infrastruktury:** Możliwość oceniania przez pracowników jakości bazy hotelowej i przewoźników po powrocie z delegacji, tworząca bazę rekomendacji dla kolejnych wyjazdów.

### Materiały referencyjne i akty prawne
- Rozporządzenie Ministra Pracy i Polityki Społecznej w sprawie należności przysługujących pracownikowi zatrudnionemu w państwowej lub samorządowej jednostce sfery budżetowej z tytułu podróży służbowej.
- Ustawa o podatku dochodowym od osób fizycznych (przepisy normujące podróże służbowe).
- [Poradnik Przedsiębiorcy: Delegacje krajowe i zagraniczne pracowników](https://poradnikprzedsiebiorcy.pl/-delegacje-krajowe-i-zagraniczne)
- [Biznes.gov.pl: Wydatki związane z podróżami służbowymi przedsiębiorcy i pracownika](https://www.biznes.gov.pl/pl/portal/00268)
- [BIP Politechniki Białostockiej: Zarządzenie nr 61/2024 Rektora PB w sprawie podróży służbowych](https://bip.pb.edu.pl/index.php?event=informacja&id=21474)

---

## Temat 9: Rozliczanie delegacji zagranicznych

### Tło problemu
Delegacje zagraniczne charakteryzują się znacznie wyższym poziomem złożoności niż podróże krajowe. Wymagają uwzględnienia zróżnicowanych stawek diet i limitów hotelowych przypisanych do poszczególnych państw docelowych, obsługi operacji wielowalutowych (przewalutowania wg kursów NBP z odpowiednich dni), ubezpieczeń podróżnych oraz specyficznych regulacji celno-wizowych.

Kluczowe wyzwania:
- Złożona logistyka podróży multimodalnych (loty, pociągi, transfery lokalne).
- Konieczność precyzyjnego stosowania tabel kursów średnich NBP do przeliczania wydatków poniesionych w walutach obcych.
- Zróżnicowane limity kosztów noclegu w zależności od kraju i miasta docelowego.

### Cel i wyzwanie projektowe
Zaprojektowanie nowoczesnego systemu webowo-mobilnego automatyzującego planowanie, akceptację i rozliczanie zagranicznych podróży służbowych z zachowaniem pełnej zgodności z przepisami fiskalnymi.

### Zagadnienia do analizy i implementacji
1. **Wniosek o delegację zagraniczną:** Formularz kalkulacji kosztów podróży, harmonogramu etapów, celu wizyty oraz zapotrzebowania na zaliczki w obcych walutach.
2. **Rozszerzony workflow formalny:** Ścieżka akceptacji uwzględniająca specyfikę prawną i dysponowanie środkami projektowymi/grantowymi.
3. **Wielowalutowy moduł rozliczeniowy:**
   - automatyczne pobieranie tabel kursowych NBP i przeliczanie wydatków na PLN wg daty poniesienia kosztu lub dnia poprzedzającego,
   - kalkulator diet zagranicznych z uwzględnieniem stawek specyficznych dla poszczególnych krajów tranzytowych i docelowych,
   - weryfikacja limitów hotelowych i diet ryczałtowych zgodnie z rozporządzeniem,
   - ewidencja i rozliczanie zaliczek pobranych w różnych walutach (EUR, USD, GBP itp.).
4. **Integracje zewnętrzne:**
   - automatyczne księgowanie operacji wielowalutowych w systemie FK,
   - pobieranie danych rezerwacyjnych z platform biletowych i hotelowych.

### Materiały referencyjne
- Rozporządzenie MPiPS w sprawie podróży służbowych poza granicami kraju.
- Ustawa o podatku dochodowym od osób fizycznych (koszty podróży zagranicznych).
- [Poradnik Przedsiębiorcy: Zasady rozliczania delegacji zagranicznych](https://poradnikprzedsiebiorcy.pl/-delegacje-krajowe-i-zagraniczne)
- [Biznes.gov.pl: Podróże służbowe poza granicami kraju](https://www.biznes.gov.pl/pl/portal/00268)
- [BIP PB: Zarządzenia Rektora PB regulujące zagraniczne podróże służbowe](https://bip.pb.edu.pl/index.php?event=informacja&id=21474)

---

## Temat 10: „Nowy w firmie” – Platforma onboardingowa

### Tło problemu
Proces adaptacji nowego pracownika w organizacji (*onboarding*) jest kluczowy dla jego przyszłej retencji i satysfakcji. Nowo zatrudniona osoba nierzadko czuje się zagubiona w strukturze firmy, nie zna procedur ani narzędzi, a jej efektywność w początkowych tygodniach pozostaje niska. Im większa organizacja, tym większego znaczenia nabiera standaryzacja i skrócenie czasu wdrożenia.

### Zidentyfikowane bariery w procesie wdrożenia
- **Brak ustrukturyzowanego procesu:** Przypadkowy przebieg pierwszych dni pracy prowadzi do niepewności i stresu u pracownika.
- **Niedostateczne wsparcie szkoleniowe:** Brak dedykowanych materiałów instruktażowych obniża produktywność.
- **Bariery integracji kulturowej:** Trudności w odnalezieniu się w nieformalnych relacjach i kulturze organizacyjnej.
- **Ograniczony dostęp do zasobów:** Opóźnienia w przydzielaniu sprzętu, uprawnień i kont od pierwszego dnia pracy.
- **Niedobór wsparcia menedżerskiego:** Przeciążenie kierowników i brak czasu na mentoring dla nowo przyjętych.

### Cel i wyzwanie projektowe
Stworzenie platformy optymalizującej proces wdrażania pracowników poprzez digitalizację ścieżek adaptacji, zarządzanie zadaniami oraz zaangażowanie mentorów z wykorzystaniem mechanizmów grywalizacji.

### Kluczowe funkcjonalności systemu
1. **Zarządzanie listą zadań onboardingowych:** Przejrzysty panel kroków formalnych, technicznych i szkoleniowych dla nowo zatrudnionego.
2. **Kreator ścieżek wdrożeniowych:** Przydzielanie spersonalizowanych pakietów zadań przez dział HR lub kierowników działów w zależności od stanowiska.
3. **Instytucja mentora (*Buddy*):** Przypisywanie opiekunów do poszczególnych zadań i etapów wdrożenia.
4. **System grywalizacji i wyróżnień:** Motywowanie opiekunów i nowo zatrudnionych poprzez system odznak, punktów i rekomendacji honorujących zaangażowanie w proces wdrożenia.
5. **Ścieżki rozwoju kompetencji:** Moduł budowania prostych sekwencji edukacyjnych prowadzących do samodzielności stanowiskowej.

### Materiały referencyjne
- [HCM Deck: Dobry onboarding pracownika w firmie – 7 kroków](https://hcmdeck.com/blog/dobry-onboarding-w-firmie/)
- [EY Polska: Na czym polega onboarding pracownika i jak go przeprowadzić?](https://www.ey.com/pl_pl/workforce/onboarding-pracownika-na-czym-polega-i-jak-go-przeprowadzic)
- [Traffit: Idealny onboarding pracownika w 5 prostych krokach](https://traffit.com/pl/blog/proces-rekrutacyjny/idealny-onboarding-pracownika-w-5-prostych-krokach/)

---

## Temat 11: Zero Waste – Świat z mniejszą ilością odpadów

### Tło problemu
Współczesny model konsumpcji generuje olbrzymie ilości odpadów wynikające z nadprodukcji oraz nieefektywnej dystrybucji dóbr i żywności. Odpowiedzią na te wyzwania jest ruch *Zero Waste* – filozofia dążąca do minimalizacji wytwarzanych odpadów poprzez odpowiedzialną produkcję, konsumpcję, wielokrotne wykorzystanie oraz recykling.

Wdrożenie zasad *zero waste* w życiu codziennym i działalności przedsiębiorstw wymaga przełamania utartych nawyków, edukacji oraz infrastruktury technologicznej ułatwiającej przekazywanie nadwyżek.

Przykładowe wektory rozwiązań:
- aplikacja społecznościowa łącząca osoby oddające zbędne przedmioty z osobami mogącymi dać im drugie życie;
- platforma B2B umożliwiająca firmom wymianę i odsprzedaż nadwyżek surowców produkcyjnych i materiałów odpadowych.

### Cel i wyzwanie projektowe
Zaprojektowanie i budowa rozwiązania cyfrowego (webowego lub mobilnego), które realnie wspiera konsumentów, społeczności lokalne lub instytucje w ograniczaniu powstawania odpadów poprzez obieg zamknięty (np. redystrybucja mebli, odzieży, sprzętu AGD, książek, materiałów budowlanych).

### Materiały referencyjne
- [Polskie Stowarzyszenie Zero Waste: Tworzymy świat bez odpadów](https://zero-waste.pl/)

---

## Temat 12: Zarządzanie hospitacjami nauczycieli akademickich

### Tło problemu
Hospitacje zajęć dydaktycznych stanowią fundamentalny element Uczelnianego Systemu Zapewniania Jakości Kształcenia w szkołach wyższych. Proces polega na bezpośredniej obserwacji zajęć prowadzonych przez nauczyciela akademickiego w celu ewaluacji metodyki, poprawności merytorycznej oraz relacji ze studentami. 

W wielu uczelniach hospitacje cierpią na brak scentralizowanego wsparcia informatycznego: harmonogramy ustalane są w arkuszach, koordynacja terminów rodzi kolizje, protokoły papierowe giną w archiwach, a wnioski pooceniające rzadko przekładają się na realny rozwój kompetencji dydaktycznych kadry.

### Cel i wyzwanie projektowe
Opracowanie kompleksowego systemu zarządzania cyklem hospitacji, obejmującego automatyzację planowania wizyt, standaryzację formularzy hospitacyjnych, agregację statystyk oraz wsparcie rozwoju dydaktycznego pracowników.

### Wymagania funkcjonalne
1. **Zarządzanie użytkownikami i uprawnieniami:**
   - obsługa ról: administrator, dziekan, kierownik katedry, hospitujący, hospitowany;
   - integracja z uczelnianym systemem uwierzytelniania (SSO / LDAP).
2. **Planowanie hospitacji:**
   - automatyczne generowanie propozycji harmonogramu na podstawie aktualnego planu zajęć;
   - moduł ręcznej modyfikacji terminów i wyznaczania hospitujących;
   - zautomatyzowane powiadomienia i alerty kalendarzowe dla obu stron.
3. **Przeprowadzanie hospitacji i zbieranie uwag:**
   - responsywne formularze oceny dostępne na urządzeniach mobilnych podczas zajęć;
   - możliwość dołączania notatek i załączników (za zgodą hospitowanego);
   - ujednolicone listy kontrolne (*checklists*) zgodne z wytycznymi uczelnianej komisji ds. jakości.
4. **Dokumentacja i raportowanie:**
   - automatyczne generowanie sformalizowanych protokołów hospitacji;
   - centralne archiwum z możliwością wielokryterialnego wyszukiwania;
   - zestawienia zbiorcze na poziomie katedr, wydziałów oraz władz uczelni.
5. **Analityka i wsparcie rozwoju:**
   - identyfikacja luk kompetencyjnych i zapotrzebowania na warsztaty pedagogiczne;
   - moduł rekomendacji szkoleń dydaktycznych;
   - baza dobrych praktyk i przestrzeń do wymiany doświadczeń dydaktycznych.

---

## Temat 13: System układania obciążeń nauczycieli akademickich (Pensum)

### Tło problemu
Przydział zajęć i ewidencja pensum dydaktycznego to jedno z najbardziej złożonych zadań organizacyjnych na uczelni. Wymaga zharmonizowania planów studiów, limitów pensum wynikających z umów i stanowisk, specjalizacji naukowych kadry oraz podziału modułów pomiędzy kilku współprowadzących. Brak zintegrowanego narzędzia prowadzi do dysproporcji w przydziale zajęć, niekontrolowanego narastania kosztownych nadgodzin oraz opóźnień w sprawozdawczości do systemów centralnych (takich jak USOS i POL-on).

### Cel i wyzwanie projektowe
Opracowanie systemu informatycznego do zaawansowanego planowania, bilansowania i bieżącej ewidencji obciążeń dydaktycznych nauczycieli akademickich w ujęciu semestralnym i rocznym.

### Wymagania funkcjonalne
1. **Zarządzanie strukturą jednostek:**
   - modelowanie struktury uczelni: wydziały, katedry, zakłady;
   - ewidencja kadry wraz z przypisaniem do jednostek oraz profilem kompetencji.
2. **Definiowanie i kalkulacja pensum:**
   - konfiguracja pensum bazowego dla różnych stanowisk i form zatrudnienia;
   - przydział przedmiotów i grup laboratoryjnych/ćwiczeniowych do prowadzących;
   - obsługa wieloosobowego prowadzenia zajęć z procentowym lub godzinowym podziałem udziałów.
3. **Bieżący monitoring obciążeń:**
   - śledzenie bilansu godzin w czasie rzeczywistym;
   - alerty o niedociążeniu lub przekroczeniu dopuszczalnych limitów nadgodzin;
   - wagi i przeliczniki dla różnych form zajęć (wykłady, ćwiczenia, seminaria).
4. **Baza przedmiotów i integracja z USOS:**
   - centralny katalog przedmiotów z liczbą godzin, punktami ECTS i formami zajęć;
   - dwukierunkowa integracja z systemem USOS;
   - definiowanie wymogów formalnych wobec prowadzącego (stopień/tytuł naukowy).
5. **Optymalizacja i wyrównywanie obciążeń:**
   - algorytmy wspomagające równoważenie obciążeń pomiędzy pracownikami katedry;
   - uwzględnianie zniżek pensum z tytułu pełnionych funkcji kierowniczych lub grantów badawczych.
6. **Zarządzanie zmianami i zastępstwami:**
   - sformalizowany rejestr wniosków o zmiany w przydziale zajęć w trakcie semestru;
   - moduł zastępstw z automatycznym przeliczaniem godzin dydaktycznych obu pracowników.

---

## Temat 14: System wyboru i zarządzania tematami prac dyplomowych

### Tło problemu
Obsługa tematów prac inżynierskich i magisterskich angażuje studentów, promotorów, kierowników katedr, komisje programowe oraz dziekanat. Tradycyjny obieg tematów (oparty o maile, dokumenty Word i papierowe podania) rodzi chaos: utrudnia śledzenie statusu zgłoszeń, sprzyja dublowaniu tematyki, wydłuża formalną akceptację oraz komplikuje eksport zatwierdzonych tematów do systemu USOS.

### Cel i wyzwanie projektowe
Zbudowanie zintegrowanego portalu do zgłaszania, weryfikacji, selekcji oraz formalnego zatwierdzania tematów prac dyplomowych, z uwzględnieniem elastycznych ścieżek akceptacji oraz limitów promotorów.

### Wymagania funkcjonalne
1. **Zarządzanie użytkownikami:** Dedykowane panele dla ról: administrator, dziekan, kierownik katedry, promotor, student (uwierzytelnianie zintegrowane z uczelnianym systemem kont).
2. **Definiowanie tematów:** Tworzenie tematów indywidualnych i zespołowych; wersje robocze; metadane formalne (tytuł PL/EN, cel, zakres, technologie, kierunek studiów).
3. **Ścieżka akceptacji (*Workflow*):** Kaskadowa ścieżka: promotor $\to$ kierownik katedry $\to$ dziekan/komisja; możliwość zwrócenia tematu do poprawy z komentarzem.
4. **Katalog tematów dla studentów:** Przejrzysty interfejs wyszukiwania z filtrowaniem po katedrach, promotorach, technologiach i słowach kluczowych.
5. **Rezerwacja i wybór tematu:** Moduł składania deklaracji przez studenta lub zespół dyplomowy z automatycznym powiadomieniem promotora.
6. **Decyzja promotora:** Akceptacja lub odrzucenie kandydatury studenta z uzasadnieniem.
7. **Kontrola limitów:** Konfigurowalne limity liczby dyplomantów na promotora i katedrę; bieżący monitoring obłożenia.
8. **Eksport do USOS i raporty:** Generowanie zestawień w formatach CSV, Excel oraz eksport gotowych rekordów do systemu USOS.
9. **Audyt i historia:** Śledzenie historii zmian treści i statusu każdego tematu.
10. **Terminarz i powiadomienia:** Definiowanie uczelnianych deadlinów na zgłaszanie i wybór tematów z automatycznymi przypomnieniami e-mail i in-app.
