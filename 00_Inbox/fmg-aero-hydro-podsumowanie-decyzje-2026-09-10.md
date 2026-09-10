---
type: decision
title: "Podsumowanie analizy i decyzje redesignu Aero-Hydro"
created: 2026-09-10
updated: 2026-09-10
tags: [adr, fantasy-map-generator, aero-hydro, redesign, renderer, ux]
aliases: []
up: "[[90_Meta/_index]]"
---

# Decyzja główna

Rekomenduję **ukierunkowany redesign bez pełnego rewrite’u**.

Należy zachować model `grid`/`pack`, format `.map`, kanoniczny pipeline FMG, rejestr
warstw, istniejące edytory i kompatybilne globalne adaptery. Rewrite byłby uzasadniony
wyłącznie przy zmianie produktu na niezależny silnik map z nowym formatem danych.
Obecne wymagania dotyczą poprawności, kontroli i wydajności istniejącego systemu,
więc migracja etapowa ma mniejsze ryzyko i pozwala mierzyć regresje.

# Macierz decyzji

| Moduł | Decyzja | Uzasadnienie |
|---|---|---|
| Atmosfera | Ulepszyć | Struktura jest dobra; trzeba ujednolicić jednostki, geostrofię i testy skalowania. |
| Ocean | Redesign lokalny | Western intensification wymaga krawędzi basenu, nie pozycji globalnej. |
| Temperatura | Ulepszyć | Zachować model, podłączyć parametry FMG i oddzielić dane proceduralne od intencji. |
| Wilgoć/opady | Ulepszyć | Ciągłe `precipMm` jest właściwym fundamentem; potrzebuje pełnego UI i jawnych jednostek. |
| Hydrologia | Zachować niezależnie | Priority-Flood i przepływ są wartościowe, ale nie mogą bezpośrednio zastąpić semantyki FMG. |
| Koordynator | Redesign kontraktu | Dodać jawne wejście/wyjście, pozostawić adapter legacy. |
| Biomy | Ulepszyć | Dodać ochronę ręcznych zmian przed rekalkulacją. |
| Rejestr warstw | Zachować i rozszerzyć | Jest właściwym punktem kontroli kolejności i widoczności. |
| ViewportRenderer | Ulepszyć | Istnieją overscan, guard pixels i rAF; należy dodać pomiary i selektywne culling. |
| Renderer ciężkich warstw | Redesign etapowy | Canvas/WebGL dla terenu i pól; nie migrować etykiet ani interakcji do WebGL. |
| Renderer ciśnienia | Zbudować od nowa | Obecne punkty nie są izobarami; kontury powinny wynikać z pola skalarnego. |
| Animacja cząstek | Ulepszyć | Zachować mechanizm, naprawić czas, DPR i zależność od globalnego viewportu. |
| Panel edytora | Redesign | Obecny wzorzec jest dobry, ale nie pokazuje wszystkich parametrów i skutków zmiany. |
| Cały generator FMG | Nie przebudowywać | Zbyt duży koszt i ryzyko utraty kompatybilności bez proporcjonalnej korzyści. |

# Docelowy kontrakt modułu

Docelowo każdy silnik powinien przyjmować jawny kontekst:

- dane świata,
- opcje modelu,
- geometrię i skalę mapy,
- identyfikator wersji modelu,
- tryb recompute.

Powinien zwracać:

- zmienione pola,
- zakres zależności do odświeżenia,
- ostrzeżenia diagnostyczne,
- metryki czasu wykonania.

W pierwszym etapie nie należy usuwać globalnego API. Należy utworzyć adapter,
który tłumaczy globalny `grid` i `pack` na jawny kontekst. Dzięki temu nowy kod
można testować niezależnie, a `public/main.js` pozostaje kompatybilny.

# Plan wdrożenia

## Etap 1 — kontrakty i obserwowalność

1. Zdefiniować typy jednostek i pól klimatycznych.
2. Dodać raport zależności po recompute.
3. Dodać metryki czasu dla każdego silnika i renderera.
4. Utrzymać wszystkie adaptery legacy.

## Etap 2 — poprawność modelu

1. Ustabilizować atmosferę w jednostkach fizycznych niezależnych od siatki.
2. Wygasić geostrofię przy równiku.
3. Uzależnić western intensification od rozpoznanego basenu.
4. Zależności temperatury i wilgoci oprzeć na wspólnych przelicznikach.
5. Dodać testy różnych rozdzielczości, szerokości geograficznych i układów oceanów.

## Etap 3 — edycja

1. Udostępnić pełną konfigurację `MoistureConfig` i termiki.
2. Pokazywać użytkownikowi wpływ zmiany: warstwa, biomy, hydrologia lub pełna regeneracja.
3. Wprowadzić warstwę intencji dla ręcznie chronionych biomów i obiektów.
4. Rozszerzyć undo/redo o parametry klimatu, nie tylko geometrię.

## Etap 4 — renderowanie

1. Zachować SVG dla etykiet, selekcji i elementów dostępnych z klawiatury.
2. Utrzymywać Canvas/WebGL dla ciężkich pól rastrowych.
3. Zintegrować grupy Aero-Hydro z `LayersRegistry`.
4. Przebudować renderer ciśnienia na kontury izoliniowe.
5. Naprawić animację czasu, DPR i transformację viewportu.

# Kryteria akceptacji

- Ten sam układ ciśnienia nie zmienia prędkości wiatru wyłącznie z powodu
  zwiększenia liczby komórek.
- Prądy zachowują sens przy oceanie na zachodzie, wschodzie i w wielu basenach.
- Zapis i odczyt `.map` zachowują stan kompatybilny z FMG.
- Rekalkulacja klimatu nie usuwa chronionych zmian użytkownika.
- Renderer nie modyfikuje danych świata.
- Panel pokazuje, co zostanie przeliczone przed zatwierdzeniem.
- Testy jednostkowe, build i lint istniejącego projektu pozostają zielone.

# Decyzja wizualna

Docelowy interfejs powinien być spokojnym narzędziem kartograficznym, a nie
demonstracją technologii. W centrum pozostaje mapa. Lewy toolbar służy do wyboru
czynności, prawy dock do warstw i inspekcji, a dolny pasek do statusu, skali,
FPS i postępu regeneracji.

Kolor akcentu oznacza aktywną domenę: niebieski dla wody i wilgoci, bursztynowy
dla temperatury, fioletowy dla atmosfery. Nie należy kodować znaczenia wyłącznie
kolorem; każda warstwa musi mieć nazwę, ikonę i stan tekstowy.

Prototyp znajduje się w:

`00_Inbox/fmg-aero-hydro-prototyp-2026-09-10.html`

Jest zamrożoną wizualizacją kierunku, nie deklaracją gotowej implementacji WebGL.
Po porównaniu z uruchomionym FMG prototyp został skorygowany: używa układu
pełnoekranowej mapy, małego panelu pływającego w lewym górnym rogu, zakładek
`Layers / Style / Options / Tools / About`, siatki istniejących warstw oraz
dolnego paska skali i statusu. Aero-Hydro jest przedstawiony jako dodatkowa
sekcja wewnątrz panelu Layers, a nie jako osobna aplikacja.
