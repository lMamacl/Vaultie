# Lab 2.2 — Wzorzec Monolitu Modułowego, Ports & Adapters oraz Testy Sprawnościowe Architektury

> **Przeznaczenie:** Referencyjne laboratorium inżynieryjne dla Lekcji 2.2 Masterclass.  
> **Kluczowy cel:** Praktyczna demonstracja izolacji Bounded Contexts, odwrócenia zależności (DIP) oraz automatycznego egzekwowania granic architektonicznych za pomocą testów sprawnościowych (Fitness Functions).

---

## 1. Architektura Laboratorium

```
labs/web-engineering/2.2/
├── package.json
├── README.md
└── src/
    ├── modules/
    │   ├── shared/
    │   │   └── in-memory-event-bus.mjs       <-- Szyna zdarzeń in-process (brak brokera sieciowego)
    │   ├── catalog/                          <-- Bounded Context: Katalog Diet
    │   │   └── catalog.module.mjs            <-- Publiczna Fasada / API modułu
    │   └── orders/                           <-- Bounded Context: Zamówienia (Hexagonal)
    │       ├── orders.module.mjs             <-- Publiczna Fasada
    │       ├── core/                         <-- RDZEŃ BIZNESOWY (Vanilla JS, brak zależności!)
    │       │   ├── entities/
    │       │   │   └── order.entity.mjs      <-- Bogata encja domenowa chroniąca niezmienniki
    │       │   └── use-cases/
    │       │       └── checkout.use-case.mjs <-- Czysty przypadek użycia zależny tylko od portów
    │       └── infrastructure/
    │           └── adapters/                 <-- ADAPTERY WTÓRNE (Wtyczki technologiczne)
    │               ├── in-memory-order.adapter.mjs <-- Pamięciowe repozytorium (testy w 0.1 ms)
    │               └── stripe-mock.adapter.mjs     <-- Symulator bramki płatności
    └── tests/
        ├── checkout.use-case.test.mjs        <-- Hermetyczny test use case'u w RAM
        └── architecture-fitness.test.mjs     <-- Test sprawdzający granice architektoniczne
```

---

## 2. Definition of Done (DoD)

- [x] **Izolacja rdzenia (DIP):** Katalog `modules/orders/core/` nie importuje żadnych plików z `infrastructure/` ani `adapters/`.
- [x] **Szczelność Bounded Context:** Żaden moduł zewnętrzny (`catalog`) nie importuje prywatnych klas z wnętrza modułu `orders`.
- [x] **Komunikacja asynchroniczna in-process:** Reakcja modułu `catalog` na opłacenie zamówienia następuje wyłącznie poprzez zdarzenie `order.paid` na szynie `InMemoryEventBus`.
- [x] **Hermetyczna testowalność:** Testy logiki biznesowej wykonują się w pamięci RAM bez bazy danych i bez sieci w czasie poniżej 100 ms.
- [x] **Automatyczna bramka architektoniczna:** Test `architecture-fitness.test.mjs` weryfikuje importy statyczne i blokuje nieautoryzowane powiązania.

---

## 3. Uruchomienie Testów

```bash
# Wszystkie testy (biznesowe + architektoniczne):
npm test

# Tylko testy reguł architektonicznych:
npm run test:fitness

# Tylko testy logiki biznesowej use case'u:
npm run test:domain
```
