/**
 * Przypadek użycia (Use Case) w architekturze Hexagonalnej.
 * Zależy WYŁĄCZNIE od portów (interfejsów) wstrzykiwanych w konstruktorze.
 */
export class CheckoutOrderUseCase {
  constructor({ orderRepo, paymentGateway, eventBus }) {
    this.orderRepo = orderRepo;
    this.paymentGateway = paymentGateway;
    this.eventBus = eventBus;
  }

  async execute({ orderId, paymentToken }) {
    const order = await this.orderRepo.getById(orderId);
    if (!order) {
      return { success: false, error: "ZAMOWIENIE_NIE_ISTNIEJE" };
    }

    if (!order.canBePaid()) {
      return { success: false, error: "NIEPRAWIDLOWY_STAN_ZAMOWIENIA" };
    }

    // Wywołanie portu wtórnego płatności (Use Case nie wie czy to Stripe, PayU czy Fake!)
    const payment = await this.paymentGateway.processPayment({
      amount: order.totalAmount,
      token: paymentToken,
      currency: "PLN",
    });

    if (!payment.isSuccess) {
      return { success: false, error: "PLATNOSC_ODRZUCONA", details: payment.reason };
    }

    // Modyfikacja stanu encji przez jej własną metodę biznesową
    order.markAsPaid(payment.transactionId);
    await this.orderRepo.save(order);

    // Publikacja zdarzenia integracyjnego dla innych Bounded Contexts (np. Magazyn / WMS)
    if (this.eventBus) {
      await this.eventBus.publish("order.paid", {
        orderId: order.id,
        customerId: order.customerId,
        amount: order.totalAmount,
        items: order.items,
        timestamp: new Date().toISOString(),
      });
    }

    return {
      success: true,
      orderId: order.id,
      transactionId: payment.transactionId,
    };
  }
}
