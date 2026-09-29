import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { OrdersModule } from "../modules/orders/orders.module.mjs";
import { CatalogModule } from "../modules/catalog/catalog.module.mjs";
import { InMemoryEventBus } from "../modules/shared/in-memory-event-bus.mjs";
import { Order } from "../modules/orders/core/entities/order.entity.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const srcDir = path.resolve(__dirname, "..");

test("Testy Sprawnościowe Architektury (Architectural Fitness Functions)", async (t) => {
  await t.test("Reguła DIP: Rdzeń Orders Core nie może importować żadnych adapterów ani infrastruktury", () => {
    const coreDir = path.join(srcDir, "modules", "orders", "core");
    const coreFiles = [];

    function scan(dir) {
      for (const item of fs.readdirSync(dir)) {
        const full = path.join(dir, item);
        if (fs.statSync(full).isDirectory()) scan(full);
        else if (full.endsWith(".mjs")) coreFiles.push(full);
      }
    }
    scan(coreDir);

    const violations = [];
    for (const file of coreFiles) {
      const content = fs.readFileSync(file, "utf-8");
      if (content.includes("infrastructure") || content.includes("adapters")) {
        violations.push(path.relative(srcDir, file));
      }
    }

    assert.deepEqual(violations, [], `Naruszenie DIP w plikach: ${violations.join(", ")}`);
  });

  await t.test("Reguła Bounded Context: Moduł Catalog nie może importować prywatnych klas Orders", () => {
    const catalogDir = path.join(srcDir, "modules", "catalog");
    const catalogFiles = fs.readdirSync(catalogDir).map((f) => path.join(catalogDir, f));

    const violations = [];
    for (const file of catalogFiles) {
      if (!fs.statSync(file).isFile()) continue;
      const content = fs.readFileSync(file, "utf-8");
      if (content.includes("orders/core") || content.includes("orders/infrastructure")) {
        violations.push(path.relative(srcDir, file));
      }
    }

    assert.deepEqual(violations, [], `Moduł Catalog narusza granice modułu Orders w: ${violations.join(", ")}`);
  });

  await t.test("Przepływ Międzymodułowy: Orders i Catalog współpracują wyłącznie przez In-Memory Event Bus", async () => {
    const eventBus = new InMemoryEventBus();
    const catalog = new CatalogModule(eventBus);

    // Początkowa sprzedaż posiłku meal_1 = 0
    assert.equal(catalog.getMeal("meal_1").totalSold, 0);

    const initialOrder = new Order("ord_201", "usr_9", 38.5, "Draft", [{ mealId: "meal_1", quantity: 3 }]);
    const orders = new OrdersModule(eventBus, [initialOrder]);

    // Opłacenie zamówienia przez publiczną fasadę
    const checkoutResult = await orders.checkout("ord_201", "tok_valid");
    assert.equal(checkoutResult.success, true);

    // Moduł Catalog odebrał zdarzenie 'order.paid' bez bezpośredniego importu z bazy Orders!
    assert.equal(catalog.getMeal("meal_1").totalSold, 3);
  });
});
