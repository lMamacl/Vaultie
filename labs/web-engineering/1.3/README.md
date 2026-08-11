# Lab 1.3 — Repozytorium, Monorepo i Git Workflow

---

## 🎯 Cel Ćwiczenia
W tym laboratorium skonfigurujesz wzorcową strukturę **Monorepo** dla projektu inżynieryjnego z wykorzystaniem `pnpm workspaces`, wyznaczysz deterministyczny build przy pomocy `frozen-lockfile`, dodasz automatyczną weryfikację jakości kodu (Husky + lint-staged + Conventional Commits) oraz zaprojektujesz potok CI dla GitHub Actions.

---

## 📂 Struktura Katalogu `labs/web-engineering/1.3/`

```
labs/web-engineering/1.3/
├── pnpm-workspace.yaml          # Konfiguracja obszarów roboczych pnpm
├── package.json                 # Główny manifest monorepo
├── .editorconfig                # Spójność formatowania w IDE
├── .gitignore                   # Ignorowane pliki i build artifacts
├── .github/
│   └── workflows/
│       └── ci.yml               # Potok CI weryfikujący PR-y
├── apps/
│   └── web/                     # Aplikacja kliencka
│       └── package.json
└── packages/
    └── shared/                  # Wspólne typy i DTO
        └── package.json
```

---

## 📋 Lista Kroków (Definition of Done)

1. **Weryfikacja Monorepo:** Upewnij się, że modyfikacja typów w `packages/shared` jest natychmiast widoczna i dostępna w `apps/web` bez konieczności publikacji do npm.
2. **Reprodukowalność Builda:** Przetestuj komendę `pnpm install --frozen-lockfile` (lub `npm ci`), aby sprawdzić determinizm instalacji pakietów.
3. **Automatyczne Git Hooks:** Zweryfikuj działanie `commit-msg` dla **Conventional Commits** (np. `feat: dodanie konta`, `fix: poprawka błędu`, `chore: zmiana w ci`).
4. **Bramka CI:** Przeanalizuj plik `.github/workflows/ci.yml` i odpowiedz, które kroki wykonują się równolegle, a które stanowią twardy warunek scalenia PR do brancha `main`.
