import test from "node:test";
import assert from "node:assert/strict";
import { Order } from "../modules/orders/core/entities/order.entity.mjs";
import { InMemoryOrderAdapter } from "../modules/orders/infrastructure/adapters/in-memory-order.adapter.mjs";
import { StripeMockPaymentAdapter } from "../modules/orders/infrastructure/adapters/stripe-mock.adapter.mjs";
import { CheckoutOrderUseCase } from "../modules/orders/core/use-cases/checkout.use-case.mjs";
import { InMemoryEventBus } from "../modules/shared/in-memory-event-bus.mjs";

test("CheckoutOrderUseCase — hermetyczny test jednostkowy w RAM", async (t) => {
  await t.test("sukces płatności: zmienia status na Paid i publikuje zdarzenie integracyjne", async () => {
    const eventBus = new InMemoryEventBus();
    const publishedEvents = [];
    eventBus.subscribe("order.paid", (evt) => publishedEvents.push(evt));

    const initialOrder = new Order("ord_101", "usr_5", 77.0, "Draft", [{ mealId: "meal_1", quantity: 2 }]);
    const orderRepo = new InMemoryOrderAdapter([initialOrder]);
    const paymentGateway = new StripeMockPaymentAdapter({ shouldFail: false });

    const useCase = new CheckoutOrderUseCase({ orderRepo, paymentGateway, eventBus });

    const result = await useCase.execute({ orderId: "ord_101", paymentToken: "tok_visa_valid" });

    assert.equal(result.success, true);
    assert.match(result.transactionId, /^ch_stripe_/);

    const updatedOrder = await orderRepo.getById("ord_101");
    assert.equal(updatedOrder.status, "Paid");
    assert.equal(updatedOrder.paymentTransactionId, result.transactionId);

    // Sprawdzenie publikacji zdarzenia:
    assert.equal(publishedEvents.length, 1);
    assert.equal(publishedEvents[0].orderId, "ord_101");
    assert.equal(publishedEvents[0].amount, 77.0);
  });

  await t.test("odrzucenie płatności: zachowuje status Draft i nie publikuje zdarzenia", async () => {
    const eventBus = new InMemoryEventBus();
    const publishedEvents = [];
    eventBus.subscribe("order.paid", (evt) => publishedEvents.push(evt));

    const initialOrder = new Order("ord_102", "usr_5", 50.0, "Draft");
    const orderRepo = new InMemoryOrderAdapter([initialOrder]);
    const paymentGateway = new StripeMockPaymentAdapter({ shouldFail: true });

    const useCase = new CheckoutOrderUseCase({ orderRepo, paymentGateway, eventBus });

    const result = await useCase.execute({ orderId: "ord_102", paymentToken: "tok_invalid" });

    assert.equal(result.success, false);
    assert.equal(result.error, "PLATNOSC_ODRZUCONA");

    const unchangedOrder = await orderRepo.getById("ord_102");
    assert.equal(unchangedOrder.status, "Draft");
    assert.equal(publishedEvents.length, 0);
  });

  await t.test("ochrona niezmiennika: nie można opłacić już opłaconego zamówienia", async () => {
    const initialOrder = new Order("ord_103", "usr_5", 50.0, "Paid");
    const orderRepo = new InMemoryOrderAdapter([initialOrder]);
    const paymentGateway = new StripeMockPaymentAdapter();

    const useCase = new CheckoutOrderUseCase({ orderRepo, paymentGateway });
    const result = await useCase.execute({ orderId: "ord_103", paymentToken: "tok_valid" });

    assert.equal(result.success, false);
    assert.equal(result.error, "NIEPRAWIDLOWY_STAN_ZAMOWIENIA");
  });
});
