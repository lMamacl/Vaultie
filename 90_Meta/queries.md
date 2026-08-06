---
type: moc
title: Queries
created: 2026-08-06
updated: 2026-08-06
tags: []
aliases: []
up: "[[90_Meta/_index]]"
---

# Queries

Nazwane kwerendy i punkty dostępu do przekrojowych danych w vaultcie. Agent i użytkownik mogą się do nich odwołać.

## 1. adopt-stack
Wszystkie biblioteki z `verdict: adopt` — mój produkcyjny stack technologiczny.

```dataview
TABLE lib, ecosystem, version, confidence, used_in
FROM "10_Libraries"
WHERE verdict = "adopt"
SORT lib ASC
```

## 2. do-oceny (Triage / Assessment)
Biblioteki ze stanem `verdict: assess` lub `verdict: trial`, które wymagają decyzji.

```dataview
TABLE lib, ecosystem, verdict, confidence, created
FROM "10_Libraries"
WHERE verdict = "assess" OR verdict = "trial"
SORT created DESC
```

## 3. decyzje-30-dni
Decyzje architektoniczne (ADR) zdefiniowane lub zaktualizowane w ostatnich 30 dniach.

```dataview
TABLE status, affects, updated
FROM "30_Decisions"
WHERE updated >= date(today) - dur(30 days)
SORT updated DESC
```

## 4. snippety-niesprawdzone
Snippety kodu z flagą `verified: false` — wymagają uruchomienia i testu.

```dataview
TABLE lib, language, version, created
FROM "40_Snippets"
WHERE verified = false
SORT created DESC
```

## 5. klipy-do-promocji
Klipy ze źródła zewnętrznego o wysokiej przydatności (`relevance >= 4`).

```dataview
TABLE relevance, topic, source, retrieved
FROM "00_Inbox/_clips"
WHERE relevance >= 4
SORT relevance DESC, retrieved DESC
```

## 6. sieroty i stale versions (Zgłaszane przez `kb-lint`)
Wykrywane automatycznie przez skille audytujące:
- Notatki bez odnośników wchodzących (sieroty)
- Biblioteki z wersjami odcinającymi się od wydanych wydań (stale versions)
