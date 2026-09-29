/**
 * Adapter Wtórny (Driven Adapter): Pamięciowe repozytorium zamówień.
 * Implementuje port oczekiwany przez Use Case, operując w 100% w RAM.
 */
export class InMemoryOrderAdapter {
  constructor(initialOrders = []) {
    this.storage = new Map(initialOrders.map((o) => [o.id, o]));
  }

  async getById(id) {
    return this.storage.get(id) || null;
  }

  async save(order) {
    this.storage.set(order.id, order);
  }
}
