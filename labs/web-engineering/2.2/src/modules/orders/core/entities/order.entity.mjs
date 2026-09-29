/**
 * Bogaty model domenowy (Rich Domain Model).
 * Encja Order chroni swoje niezmienniki biznesowe i nie zależy od żadnego ORM-a.
 */
export class Order {
  constructor(id, customerId, totalAmount, status = "Draft", items = []) {
    this.id = id;
    this.customerId = customerId;
    this.totalAmount = totalAmount;
    this.status = status;
    this.items = items;
    this.paymentTransactionId = null;
  }

  canBePaid() {
    return this.status === "Draft" && this.totalAmount > 0;
  }

  markAsPaid(transactionId) {
    if (!this.canBePaid()) {
      throw new Error(`Nie można opłacić zamówienia w stanie '${this.status}' z kwotą ${this.totalAmount}.`);
    }
    if (!transactionId) {
      throw new Error("Wymagany poprawny identyfikator transakcji płatniczej.");
    }
    this.status = "Paid";
    this.paymentTransactionId = transactionId;
  }

  cancel(reason) {
    if (this.status === "Paid") {
      throw new Error("Nie można anulować opłaconego zamówienia bez procedury zwrotu.");
    }
    this.status = "Cancelled";
    this.cancellationReason = reason;
  }
}
