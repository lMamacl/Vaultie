# Lab 1.3 — Repozytorium, Monorepo i Git Workflow

---

## Cel ćwiczenia

Skonfigurujesz wzorcowe **Monorepo** (`pnpm workspaces`), deterministyczny build (`pnpm-lock.yaml` + `--frozen-lockfile`), hooki Husky (Conventional Commits) oraz przeanalizujesz potok CI w GitHub Actions.

---

## Struktura katalogu

```text
labs/web-engineering/1.3/
├── pnpm-workspace.yaml
├── package.json
├── pnpm-lock.yaml              # commit do repo — NIE .gitignore
├── .editorconfig
├── .gitignore
├── .husky/
│   ├── pre-commit              # frozen install + lint + test + build
│   └── commit-msg              # Conventional Commits
├── .github/workflows/ci.yml
├── scripts/lint.mjs
├── apps/web/
│   ├── package.json
│   └── index.mjs
└── packages/shared/
    ├── package.json
    └── index.js
```

---

## Szybki start

```bash
cd labs/web-engineering/1.3
pnpm install
pnpm run lint
pnpm run test
pnpm run build
```

W CI używamy:

```bash
pnpm install --frozen-lockfile
```

---

## Definition of Done

1. **Monorepo:** zmiana w `packages/shared/index.js` jest widoczna w `apps/web` przez `workspace:*` bez `npm publish`.
2. **Lockfile:** `pnpm-lock.yaml` jest w repo; `pnpm install --frozen-lockfile` kończy się PASS.
3. **Husky:** commit `quick fix` → odrzucony; `feat: add verification step` → akceptowany.
4. **CI:** przeanalizuj `.github/workflows/ci.yml` — kolejność: checkout → node → pnpm → frozen install → lint → test → build.
5. **Atomowy commit:** jedna zmiana DTO + konsument w jednym PR (symulacja monorepo advantage).

---

## Wymagania

- Node.js ≥ 20
- pnpm 9 (`corepack enable` lub `npx pnpm@9.15.0`)

Powiązana lekcja: [[1.3/1.3-repo-monorepo-git-workflow]]
