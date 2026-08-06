# kb-merge — scalanie duplikatów notatek i klipów

## Cel
Konsolidacja dwóch lub więcej niepotrzebnie zduplikowanych notatek opisujących tę samą bibliotekę, ten sam wzorzec lub ten sam artykuł w jedną spójną i zwięzłą notatkę.

## Kiedy użyć
- Wykrycie duplikatów przez scouta lub lintera (`kb-lint`).
- Gdy użytkownik prosi: "scal notatki X i Y", "połącz te dwa klipy".

## Kroki
1. **Analiza wejścia:** Pobierz 2 lub więcej notatki wskazane jako duplikaty.
2. **Kompilacja treści:** Stwórz połączony draft, wyciągając unikalne spostrzeżenia, API, przykłady i gotchas z obu dokumentów. Zadbaj o unikanie powtórzeń.
3. **Zapis propozycji merged:** Zapisz scalony draft w `00_Inbox/_proposals/tpl-merge-<slug>.md`.
4. **Prezentacja podglądu (Diff):** Przedstaw użytkownikowi wynik scalenia oraz wskaż plik, który zostanie nadpisany i plik, który zostanie usunięty/zarchiwizowany.
5. **Wykonanie:** Po zatwierdzeniu przez użytkownika:
   - Zastąp główną notatkę wygenerowanym draftem.
   - Przenieś drugi plik (duplikat) do `99_Archive/` lub go usuń, jeśli zawierał wyłącznie bezwartościową kopię.
   - Uruchom `kb-compile`.

## Input
- Co najmniej dwa odnośniki do zduplikowanych plików.

## Output
- Nowy lub scalony plik propozycji w `00_Inbox/_proposals/`.

## Guardrails
- **NIGDY nie usuwaj ani nie nadpisuj plików produkcyjnych bez zaprezentowania diffa i uzyskania zgody.**
- Upewnij się, że żadne unikalne uwagi i przykłady autorskie użytkownika z żadnej z połączonych notatek nie zostały utracone w procesie scalania.

## Warianty
- Brak.
