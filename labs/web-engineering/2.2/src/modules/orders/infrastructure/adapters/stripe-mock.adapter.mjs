/**
 * Adapter Wtórny (Driven Adapter): Symulator bramki Stripe.
 */
export class StripeMockPaymentAdapter {
  constructor({ shouldFail = false } = {}) {
    this.shouldFail = shouldFail;
  }

  async processPayment({ amount, token, currency }) {
    if (this.shouldFail || token === "tok_invalid") {
      return {
        isSuccess: false,
        reason: "Karta_Odrzucona_Brak_Srodkow",
        transactionId: null,
      };
    }

    return {
      isSuccess: true,
      transactionId: `ch_stripe_${Date.now()}_${Math.random().toString(36).substring(7)}`,
      currency,
      amount,
    };
  }
}
