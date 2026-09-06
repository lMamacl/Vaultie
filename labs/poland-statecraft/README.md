# Poland Statecraft: Architekt Państwa (Polska 2026+)

> **Interaktywny symulator systemowy i drzewo reform polityczno-gospodarczych Rzeczypospolitej Polskiej.**  
> Wcielasz się w rolę **Architekta Państwa** — bezpartyjnego stratega państwowego, który musi przeprowadzić kraj przez wielowymiarowe kryzysy lat 2026–2040, balansując pomiędzy ograniczonym budżetem, kapitałem politycznym a groźbą wybuchu buntu społecznego (próg 3.0%).

---

## 1. Główne Założenia Symulacji

| Parametr | Wartość bazowa | Opis |
|---|---|---|
| **Rok startowy** | **2026** | Punkt wyjścia: zastałe spory instytucjonalne, presja demograficzna, wojna za granicą, presja ETS. |
| **Krok czasowy** | **1 rok (1 Tura)** | Każdy rok to nowa pula zasobów, aktualizacja wskaźników i potencjalne wydarzenia losowe. |
| **Pula Zasobów (Zasada 30%)** | **30% łącznej wartości wyzwań** | Budżet reform pokrywa zaledwie ~30% zapotrzebowania. Musisz brutalnie selekcjonować priorytety. |
| **Próg Buntu Społecznego** | **3.0% populacji (~1.15 mln osób)** | Wg reguły Chenoweth, 3-3.5% aktywnie protestujących obywateli paraliżuje państwo i cofa reformy. |
| **Aparat Rządzący** | **Aktor Pośredni (Zmienny)** | Rządy zmieniają się w wyborach (lub upadają). Każdy archetyp ma inne preferencje i weta. |

---

## 2. Trójkąt Zasobów Architekta

W każdym roku (turze) operujesz trzema zasobami krytycznymi:

1. **Budżet Rozwojowy (PLN mld / % PKB):**
   * Całkowity budżet państwa to głównie wydatki sztywne (ZUS, NFZ, obsługa długu, pensje sfery budżetowej).
   * Na reformy strukturalne i inwestycje rozwojowe pozostaje elastyczna pula rzędu **40–60 mld PLN rocznie** (zależnie od procedury nadmiernego deficytu UE i ratingów).
2. **Kapitał Polityczny (KP):**
   * Pula od 0 do 100 punktów. Generowana przez stabilność koalicji rządzącej i zaufanie publiczne.
   * Każda niepopularna reforma (np. wiek emerytalny, podatek emisyjny, konsolidacja szpitali) spala KP.
3. **Przepustowość Administracyjna (Administrative Throughput):**
   * Maksymalnie **3–5 dużych projektów legislacyjno-wdrożeniowych rocznie**.
   * Państwo nie jest w stanie w jednym czasie sprawnie napisać, skonsultować i wdrożyć 15 wielkich reform bez chaosu prawnego.

---

## 3. Topologia 6 Filarów

Drzewo rozkłada się na 6 filarów powiązanych relacjami sąsiedztwa i zależnościami międzysektorowymi:

```
                      [ FILAR IV: GEOPOLITYKA & DYPLOMACJA ]
                                      ▲
                                      │
 [ FILAR III: OBRONNOŚĆ ] ◄───┐       │       ┌───► [ FILAR I: ENERGETYKA & KLIMAT ]
 (zbrojeniówka, armia,        │       │       │     (miks, atom, sieci, węgiel)
  odporność cywilna)          │       │       │
          ▲                   ▼       ▼       ▼                   ▲
          │              [ FILAR VI: INSTYTUCJE & PRAWO ]         │
          │              (aparat państwa, sądy, cyfryzacja,        │
          │               przewidywalność, samorządy)             │
          │                           ▲                           │
          ▼                           │                           ▼
 [ FILAR II: GOSPODARKA & PRZEMYSŁ ] ─┴─────► [ FILAR V: KAPITAŁ LUDZKI & DEMOGRAFIA ]
 (reindustrializacja, CPK, R&D,               (dzietność, NFZ, ZUS, migracja,
  podatki, innowacje)                          edukacja i rynek pracy)
```

1. **Filar I: Energetyka, Surowce i Klimat** – transformacja miksu węglowego, program jądrowy, OZE, modernizacja sieci przesyłowych PSE/OSD.
2. **Filar II: Gospodarka, Przemysł i Innowacje** – reindustrializacja, megaprojekty logistyczne (CPK/KDP, porty), ucieczka z pułapki średniego dochodu.
3. **Filar III: Obronność, Przemysł Zbrojeniowy i Bezpieczeństwo** – modernizacja SZ RP, krajowa amunicja 155mm, obrona cywilna i odporność infrastruktury.
4. **Filar IV: Geopolityka, Dyplomacja i Pozycja Międzynarodowa** – relacje z UE, sojusz z USA/NATO, polityka wschodnia, strategia migracyjno-graniczna.
5. **Filar V: Kapitał Ludzki, Demografia i Ochrona Socjalna** – demografia i dzietność, wydolność ZUS i wiek emerytalny, kadry i finansowanie NFZ.
6. **Filar VI: Instytucje, Prawo i Sprawność Państwa** – przezwyciężenie dualizmu w sądownictwie, walka z resortowością, cyfryzacja i automatyzacja administracji.

---

## 4. Frakcje Społeczno-Polityczne i Próg Buntu (3.0%)

Niezadowolenie społeczne wyrażone jest jako odsetek populacji skłonnej do aktywnego buntu (strajki generalne, blokady dróg, paraliż miast). **Przekroczenie 3.0% wywołuje kryzys gabinetowy i cofnięcie reform.**

Frakcje monitorowane w modelu:
* **Górnicy i Związki Przemysłowe (ZPRZ):** Wysoka zdolność paraliżu miast i infrastruktury.
* **Rolnicy i Środowiska Wiejskie (WIES):** Zdolność blokowania dróg i przejść granicznych.
* **Emeryci i Osoby 60+ (EMER):** Najliczniejsza i najzdyscyplinowana baza wyborcza w Polsce.
* **Klasa Średnia i Przedsiębiorcy (PRZED):** Źródło wpływów podatkowych, wrażliwi na inflację i koszty pracy.
* **Pracownicy Ochrony Zdrowia i Budżetówki (MED):** Zdolność do strajków głodowych i paraliżu szpitali.
* **Bruksela / Komisja Europejska (UE):** Wpływ na wypłatę funduszy spójności i KPO, kary TSUE.
* **Waszyngton / Dowództwo NATO (USA):** Gwarancje wojskowe, transfery technologii zbrojeniowych i nuklearnych.
* **Rynki Finansowe (RYNKI):** Rentowności obligacji skarbowych (10Y), kurs złotego (PLN).

---

## 5. Struktura Katalogów

* `config/` – pliki konfiguracyjne aktorów, parametrów startowych i reguł gry.
* `dossiers/` – szczegółowe karty poszczególnych reform w podziale na 6 filarów.
* `canvases/` – pliki wizualne w formacie Obsidian Canvas (`.canvas`) do interaktywnego przeglądania powiązań w Obsidianie.
* `web-panel/` – interaktywny symulator graficzny (HTML/TS) pozwalający klikać decyzje, testować różne rządy i symulować wskaźnik buntu.
