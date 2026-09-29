---
type: deep-analysis
title: "Pilot — bezpieczne retry dla zewnętrznego API"
created: 2026-09-29
updated: 2026-09-29
tags: [pilot, research, resilience, retry, idempotency]
aliases: []
up: "[[90_Meta/start-here]]"
status: proposed
---

# Pilot: bezpieczne retry dla zewnętrznego API

> **Status:** propozycja do oceny, nie zatwierdzona reguła ani ADR. To próbka nowego formatu analizy problemu.

## Rekomendacja w skrócie

Nie wdrażaj retry jako ogólnego wrappera „powtarzaj każdy wyjątek”. Dla operacji ze skutkiem ubocznym (np. utworzenie zamówienia lub obciążenie płatności) najpierw ustal, czy serwer obsługuje klucz idempotencji albo inny mechanizm deduplikacji. Timeout klienta nie dowodzi, że serwer nie wykonał operacji. Ponowienie jest bezpieczne dopiero, gdy kontrakt operacji gwarantuje semantycznie bezpieczne powtórzenie lub gdy aplikacja potrafi rozpoznać poprzedni wynik.

Dla kwalifikujących się błędów przejściowych stosuj ograniczoną liczbę ponowień, budżet czasu i losowe rozproszenie opóźnień (jitter). Nie ponawiaj bezwarunkowo błędów walidacji ani każdej odpowiedzi 4xx/5xx: decyzja zależy od kontraktu API, klasy błędu, `Retry-After`, stanu zależności i budżetu wywołującego.

## Problem i kontekst

**Scenariusz pilota:** monolit Node.js wykonuje checkout przez zewnętrzne API. Klient otrzymuje timeout po wysłaniu żądania; nie wiadomo, czy serwer przetworzył płatność. Zespół chce poprawić odporność na awarie, nie wprowadzając mikroserwisów.

To scenariusz do analizy, a nie opis potwierdzonego systemu użytkownika. Przed zastosowaniem rekomendacji trzeba ustalić dostawcę API, jego kontrakt idempotencji, typy błędów i limity czasowe.

## Założenia i niewiadome

| Pytanie | Dlaczego zmienia decyzję | Jak zweryfikować |
|---|---|---|
| Czy API płatności przyjmuje klucz idempotencji? | Bez tego powtórzenie po niejednoznacznym timeoutcie może utworzyć drugi skutek uboczny. | Dokumentacja i kontrakt konkretnego endpointu. |
| Czy timeout nastąpił przed wysłaniem, czy po wysłaniu requestu? | Po wysłaniu wynik może być nieznany, niekoniecznie nieudany. | Telemetria klienta, trace ID i logi dostawcy. |
| Które błędy są przejściowe i czy API zwraca `Retry-After`? | Nie wszystkie błędy warto lub wolno ponawiać. | Dokumentacja API, odpowiedzi z sandboxa i testy kontraktowe. |
| Jaki jest całkowity budżet czasu checkoutu? | Retry nie może przekroczyć czasu, po którym klient lub użytkownik rezygnuje. | NFR, timeouty upstream/downstream i pomiary p95/p99. |
| Czy retry jest już w SDK, proxy lub warstwie infrastruktury? | Retry w wielu warstwach mnożą liczbę prób i obciążenie. | Konfiguracja SDK/proxy, logi prób i test kontrolowany. |

## Rozważane rozwiązania

| Opcja | Kiedy pasuje | Korzyści | Koszty i ryzyka |
|---|---|---|---|
| Brak automatycznych retry; zwrócenie wyniku nieznanego i reconciliation | API nie ma idempotencji, a skutek uboczny jest istotny | Nie tworzy duplikatów przez ślepe powtórzenie | Gorsze UX; potrzebny proces sprawdzenia statusu/reconciliation |
| Retry z kluczem idempotencji, limitem prób/czasu i jitterem | API gwarantuje deduplikację dla tego klucza i zakresu czasu | Może odzyskać część awarii przejściowych bez powielania operacji | Zależność od semantyki, retencji i zakresu klucza u dostawcy |
| Retry tylko dla operacji odczytu lub jawnie idempotentnych | Request jest bezpieczny do powtórzenia według kontraktu | Prostsza polityka i mniejsze ryzyko skutków ubocznych | Nadal może zwiększyć obciążenie zależności lub przekroczyć deadline |
| Kolejka i asynchroniczna obsługa/reconciliation | Operacja może zakończyć się po czasie odpowiedzi użytkownikowi | Rozdziela czas życia żądania od pracy i pozwala ponawiać kontrolowanie | Większa złożoność, eventual consistency i potrzeba widocznego statusu |

## Uzasadnienie i dowody

- AWS Builders’ Library opisuje retry jako obciążenie dodatkową pracą zależności i wskazuje, że timeout nie dowodzi braku skutku ubocznego. Omawia backoff, jitter, limity i ostrożne kwalifikowanie błędów. To praktyka opisana przez AWS, nie uniwersalny eksperyment porównujący wszystkie polityki w każdym systemie.
- Osobny artykuł AWS wyjaśnia, jak klucze idempotencji pozwalają rozpoznać semantycznie to samo żądanie i bezpieczniej obsłużyć ponowienie. Mechanizm musi być potwierdzony w kontrakcie używanego API; sama obecność nagłówka o podobnej nazwie nie wystarcza.
- W tym Vaultie istnieje ćwiczenie retry w `labs/benchmark-suite/task-03-retry-backoff/`. To materiał dydaktyczny do inspekcji, nie dowód, że jego przykładowa implementacja jest bezpieczną polityką produkcyjną.

## Proponowana polityka dla scenariusza

1. Rozróżnij błędy przed wysłaniem requestu od niejednoznacznego wyniku po wysłaniu.
2. Użyj stabilnego klucza idempotencji dla jednej logicznej operacji checkoutu, jeśli dostawca gwarantuje jego semantykę.
3. Ustal listę ponawialnych błędów na podstawie kontraktu API; respektuj `Retry-After`, jeśli ma zastosowanie.
4. Ogranicz liczbę prób i łączny czas, uwzględniając deadline całego checkoutu. Unikaj niezależnych, nakładających się retry w SDK, kliencie i proxy.
5. Zastosuj backoff z jitterem dla retry, które są dozwolone; monitoruj liczbę prób, opóźnienia, błędy końcowe i duplikaty.
6. Przy wyniku nieznanym pokaż stan „weryfikujemy” lub wykonaj reconciliation/status lookup, zamiast bezwarunkowo ponowić płatność.
7. Przetestuj: timeout przed wysłaniem, timeout po stronie klienta po przetworzeniu przez serwer, 429 z `Retry-After`, błędy trwałe, wyczerpanie budżetu i ponowne dostarczenie tego samego klucza.

To jest kierunek do walidacji z konkretnym dostawcą, nie gotowy kod ani uniwersalne wartości timeoutu/backoffu.

## Ryzyka i warunki zmiany rekomendacji

- Jeżeli dostawca nie gwarantuje idempotencji dla endpointu i klucza, nie wolno zakładać bezpieczeństwa retry operacji płatniczej.
- Jeżeli SDK już ponawia wywołania, własna warstwa retry może pomnożyć liczbę prób.
- Jitter ogranicza synchronizację ponowień w określonych warunkach, ale nie naprawia przeciążenia ani nie czyni operacji bezpieczną semantycznie.
- Circuit breaker nie jest automatycznym dodatkiem: dobór zależy od zachowania zależności, mechanizmów limitowania i wymagań UX.
- Konkretne progi i kody odpowiedzi muszą wynikać z dokumentacji dostawcy oraz pomiarów systemu.

## Następny krok

Dla wybranego API zebrać dokumentację jego idempotency key, polityki retry/429 i timeoutów SDK; następnie przygotować test kontraktowy symulujący timeout po przetworzeniu operacji. Dopiero na tej podstawie podjąć decyzję i ewentualnie zapisać ADR.

## Źródła

1. Marc Brooker, **Timeouts, retries, and backoff with jitter**, AWS Builders’ Library. https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ — dostęp: 2026-09-29. Źródło opisuje praktyki AWS dotyczące timeoutów, retry, backoffu, jitteru, ograniczania prób i ryzyka skutków ubocznych.
2. Malcolm Featonby, **Making retries safe with idempotent APIs**, AWS Builders’ Library. https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/ — dostęp: 2026-09-29. Źródło omawia kontrakt idempotencji i semantycznie równoważne odpowiedzi przy powtórzeniu.
3. Lokalny przykład do przeglądu: `labs/benchmark-suite/task-03-retry-backoff/` — przykład laboratoryjny, nie referencyjna implementacja produkcyjna.

## Ocena pilota

- **Czy rekomendacja odpowiada na konkretny kontekst?** Do oceny przez użytkownika.
- **Czy źródła są weryfikowalne i powiązane z twierdzeniami?** Tak dla dwóch źródeł pierwotnych AWS; nie rozstrzygają kontraktu nieznanego dostawcy płatności.
- **Czy niepewność została ujawniona?** Tak — brak API/dostawcy i jego gwarancji blokuje gotową implementację.
- **Czy wynik powinien zostać promowany do wiedzy produkcyjnej?** Nie bez oceny użytkownika i uzupełnienia szczegółów dostawcy.
