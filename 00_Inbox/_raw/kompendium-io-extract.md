---
type: raw-extract
title: "Ekstrakcja: Kompendium Egzaminacyjne Inżynierii Oprogramowania (Kluczowe 25%)"
created: 2026-08-07
tags: [academic, exam, io, requirements, lifecycle, metrics, srs]
up: "[[90_Meta/_index]]"
---

# Ekstrakcja z Kompendium Egzaminacyjnego IO

Wyselekcjonowane 25% najbardziej wartościowej wiedzy akademickiej i praktycznej przydatnej w budowie Vaulta oraz w Lekcjach Masterclass (Etap 1 i 2).

---

## 1. Dlaczego systemy Legacy powstrzymują rozwój (Kryzys Oprogramowania)

Najważniejszą przyczyną tzw. **kryzysu oprogramowania** jest **trudność przystosowania istniejących systemów dziedziczonych (Legacy)** do nowych wymagań i platform.

* **Uzasadnienie:** Systemy legacy często obsługują krytyczne procesy biznesowe organizacji. Zbudowane w starych technologiach są niezwykle trudne i ryzykowne w modyfikacji. Ich przebudowa bywa tak samo kosztowna jak stworzenie systemu od zera, ale organizacja nie może ich wyłączyć ze względu na paraliż biznesowy.

---

## 2. Cechy Dobrej Specyfikacji Wymagań (SRS Checklist)

Każdy dokument specyfikacji (np. `spec-fr-nfr.md` z Lekcji 1.1) powinieneś audytować pod kątem poniższych 8 cech:

1. **Jednoznaczna (unambiguous):** Tylko jedna interpretacja dla analityka, programisty i promotora.
2. **Kompletna (complete):** Zawiera wszystkie FR, NFR oraz reakcje na sytuacje wyjątkowe (np. błędy 4xx/5xx).
3. **Spójna (consistent):** Wymagania nie wykluczają się wzajemnie.
4. **Weryfikowalna (verifiable):** Istnieje skończony pomiar lub test (np. `p95 <= 300ms`), unika się słów "system będzie szybki".
5. **Możliwa do realizacji (feasible):** Wykonalna w czasie semestru i budżecie zespołu.
6. **Uporządkowana (prioritized):** Metoda MoSCoW z limitem czasowym.
7. **Modyfikowalna (modifiable):** Unikalne ID (`FR-001`, `NFR-PERF-001`) pozwalają na bezbolesne zmiany.
8. **Śledzalna (traceable):** Każde FR łączy się z NFR i przypadkiem testowym.

---

## 3. Próbkowanie Dokumentów jako Metoda Pozyskiwania Wymagań

Analiza rzeczywistych formularzy, raportów i faktur klientów.
* **Analiza Jakościowa:** Badanie pustych i wypełnionych formularzy pod kątem struktur danych i reguł biznesowych.
* **Analiza Ilościowa:** Badanie trendów, częstotliwości, objętości danych oraz częstotliwości błędów w papierowym/starym obiegu.
* **Zagrożenie:** Dokumenty formalne często nie odzwierciedlają **rzeczywistego (nieformalnego) obiegu informacji** w firmie, bo pracownicy stosują własne obejścia!

---

## 4. Karty CRC (Class-Responsibility-Collaborator)

Narzędzie wstępnego projektowania obiektowego bez wchodzenia w formalne diagramy UML. Każda karta papierowa/notatka reprezentuje klasę:
* **Class (Klasa):** Nazwa (rzeczownik).
* **Responsibility (Odpowiedzialność):** Co klasa wie (dane) i co robi (metody).
* **Collaborator (Współpracownicy):** Z jakimi innymi klasami wchodzi w interakcję.

---

## 5. Myślenie Grupowe (Groupthink) w Zespole i Walka z Nim

Zjawisko w zintegrowanych zespołach polegające na braku samokrytyki w imię uniknięcia konfliktów i obrony "swojego" kodu.
* **Remedium:**
  1. *Sesje krytyki:* Przeglądy kodu, na których dopuszczalna jest tylko konstruktywna krytyka, a autorzy mają zakaz usprawiedliwiania się (muszą wysłuchać uwag).
  2. *Adwokat Diabła:* Wyznaczenie osoby kwestionującej przyjęte założenia architektoniczne.
  3. *Egoless Programming:* Kod jest własnością całego zespołu, nie jednostki.

---

## 6. Szacowanie Nakładu — COCOMO I vs COCOMO II

| Cecha | COCOMO 81 | COCOMO II |
| :--- | :--- | :--- |
| **Dane wejściowe** | Wyłącznie linie kodu (KLOC). | KLOC lub Punkty Funkcyjne (FP). |
| **Klasyfikacja** | Sztywne 3 klasy (Organic, Semi-detached, Embedded). | Płynne czynniki skali ($SF_i$) oceniające nowatorskość i spójność. |
| **Wykładnik skali ($E$)** | Stały (1.05, 1.12, 1.20). | Dynamiczny ($E = 0.91 + 0.01 \cdot \sum SF_i$). |
| **Czynniki korekcyjne ($EAF$)** | 15 stałych czynników. | Zależne od fazy: 7 (Early Design) lub 17 (Post-Architecture). |

*Wniosek inżynierski:* Dziś używa się rozszerzeń COCOMO II lub estymacji w Story Pointach na podstawie historycznego velocity zespołu.
