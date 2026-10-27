---
name: kb-lint
description: "Checks Vaultie knowledge-note frontmatter, dates, note types, and local wikilinks. Use when auditing repository integrity."
---

# kb-lint — walidacja integralności notatek

## Cel
Wykrywanie błędów strukturalnych i martwych wikilinków w notatkach przed przeglądem lub publikacją zmian.

## Uruchomienie

```bash
python3 .agent/scripts/vaultie-lint.py
python3 .agent/scripts/vaultie-lint.py --json
python3 .agent/scripts/vaultie-lint.py /ścieżka/do/vaulta
```

Skrypt jest read-only. Kod wyjścia `0` oznacza brak błędów blokujących; kod `1` oznacza co najmniej jeden błąd. Raport trafia na stdout i nie zapisuje pliku.

## Zakres i reguły
Skrypt skanuje `10_Libraries/`, `20_Patterns/`, `30_Decisions/`, `40_Snippets/`, `50_Concepts/` oraz notatki w `00_Inbox/_clips/` i bezpośrednie propozycje w `00_Inbox/_proposals/`. Surowe ekstrakty `00_Inbox/_raw/` są celowo wyłączone, bo nie są jeszcze znormalizowanymi notatkami.

Automatyczne kontrole:
- poprawne delimitery frontmatteru i podstawowa struktura pól; w CI PyYAML dodatkowo waliduje składnię YAML;
- wymagane pola `type`, `title`, `created`, `updated`, `tags`, `up`;
- dozwolone typy i daty ISO (`YYYY-MM-DD`);
- lokalne wikilinki, z pominięciem bloków kodu i komentarzy HTML;
- heurystyczne ostrzeżenia dla braku `aliases` (migracja starszych notatek) i pustych sekcji.

Błędy blokują CI; ostrzeżenia nie. Linter nie ocenia prawdziwości treści, jakości źródeł ani merytorycznej aktualności.

## Uzupełniający przegląd
Ręczny lub agentowy audyt może dodatkowo ocenić sieroty, aktualność bibliotek, alternatywy, zgodność verdict/confidence, weryfikację snippetów i wiek surowców. Nie należy przedstawiać tych heurystyk jako wykonanych przez skrypt, dopóki nie mają implementacji i testów.

## Guardrails
Nie naprawiaj ani nie usuwaj plików automatycznie. Przed zmianami w treści produkcyjnej pokaż diff i uzyskaj akceptację zgodnie z `.agent/AGENTS.md`.
