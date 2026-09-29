import { CheckoutOrderUseCase } from "./core/use-cases/checkout.use-case.mjs";
import { InMemoryOrderAdapter } from "./infrastructure/adapters/in-memory-order.adapter.mjs";
import { StripeMockPaymentAdapter } from "./infrastructure/adapters/stripe-mock.adapter.mjs";

/**
 * Publiczne API Modułu Zamówień (Orders Module Facade).
 * Jedyny punkt kontaktu dla świata zewnętrznego i innych Bounded Contexts.
 */
export class OrdersModule {
  constructor(eventBus, initialOrders = [], paymentAdapter = null) {
    this.orderRepo = new InMemoryOrderAdapter(initialOrders);
    this.paymentGateway = paymentAdapter || new StripeMockPaymentAdapter();
    this.checkoutUseCase = new CheckoutOrderUseCase({
      orderRepo: this.orderRepo,
      paymentGateway: this.paymentGateway,
      eventBus,
    });
  }

  // Publiczna metoda fasady:
  async checkout(orderId, paymentToken) {
    return await this.checkoutUseCase.execute({ orderId, paymentToken });
  }

  async getOrderSummary(orderId) {
    const order = await this.orderRepo.getById(orderId);
    if (!order) return null;
    return {
      id: order.id,
      customerId: order.customerId,
      totalAmount: order.totalAmount,
      status: order.status,
    };
  }
}
