/**
 * Publiczne API Modułu Katalogu Diet (Catalog Module Facade).
 * Bounded Context odizolowany od modułu Orders.
 */
export class CatalogModule {
  constructor(eventBus) {
    this.meals = new Map([
      ["meal_1", { id: "meal_1", name: "Łosoś na parze z batatami", price: 38.5, calories: 550 }],
      ["meal_2", { id: "meal_2", name: "Bowlu z tofu i komosą", price: 29.0, calories: 480 }],
    ]);

    this.soldCount = new Map([
      ["meal_1", 0],
      ["meal_2", 0],
    ]);

    // Subskrypcja zdarzenia integracyjnego w pamięci procesu:
    if (eventBus) {
      eventBus.subscribe("order.paid", (event) => {
        for (const item of event.items || []) {
          const current = this.soldCount.get(item.mealId) || 0;
          this.soldCount.set(item.mealId, current + (item.quantity || 1));
        }
      });
    }
  }

  getMeal(mealId) {
    const meal = this.meals.get(mealId);
    if (!meal) return null;
    return { ...meal, totalSold: this.soldCount.get(mealId) || 0 };
  }

  listActiveMeals() {
    return Array.from(this.meals.values());
  }
}
