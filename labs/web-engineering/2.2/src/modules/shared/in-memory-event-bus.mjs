/**
 * Prosta szyna zdarzeń w pamięci procesu dla Monolitu Modułowego.
 * Umożliwia asynchroniczną komunikację między Bounded Contexts bez sieci.
 */
export class InMemoryEventBus {
  constructor() {
    this.handlers = new Map();
  }

  subscribe(eventName, handler) {
    if (!this.handlers.has(eventName)) {
      this.handlers.set(eventName, []);
    }
    this.handlers.get(eventName).push(handler);
  }

  async publish(eventName, payload) {
    const list = this.handlers.get(eventName) || [];
    await Promise.all(list.map((fn) => fn(payload)));
  }
}
