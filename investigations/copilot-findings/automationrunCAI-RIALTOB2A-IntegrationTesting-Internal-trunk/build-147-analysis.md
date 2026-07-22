# Root Cause Analysis — Build #147

**Source report:** [build-147.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-147.md)

---

## Summary

Build #147 of `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` completed on 2026-07-22 with status **UNSTABLE**: 86 failures out of 513 tests (83.2% pass rate). This is one fewer failure than build #146 (87 failures) — no material improvement. All six root cause clusters identified in previous builds remain unresolved.

---

## Root Cause

### 1. `discountType` not populated — `null` returned instead of `RIALTO` (40 failures)

The dominant failure across 23 test cases. The field `orders[*].printDetails.discountType` is expected to hold the value `RIALTO` but the API returns `null`. This is a backend data propagation issue: the discount type is not being set on order lines when orders are created or updated via the B2A integration. As a direct consequence, basket-level price totals (`orderBasketPriceSummary.orderDiscount`, `totalInclVat`) also diverge because no discount is applied.

This issue affects both newspaper (TC1–TC22) and magazine (TC26–TC36) order flows, indicating a cross-cutting defect in the discount-type assignment logic shared by both product types.

### 2. Financial amount and status flag drift (27 failures)

`discountAmount`, `commissionAmount`, `priceNet`, `priceGross`, `totalInclVat`, and `statusFlags` deviate from fixture values. Two sub-patterns:

- **Discount/commission recalculation drift** — likely a downstream consequence of root cause #1: if `discountType=null`, amounts are recalculated without the RIALTO discount applied, producing wrong totals. Affects TC1–TC11, TC27–TC31, TC37.
- **Array/scalar serialisation mismatch** — TC27 and TC28 assert `[[3600.0]]` (array-wrapped) but receive `[3600.0]` (scalar), indicating a response schema change or a test fixture misalignment.
- **Issue date mismatch** — TC27 expects `2026-08-19` but receives `2026-08-26`; test data may be stale or the date-change operation is targeting the wrong issue slot.

### 3. `ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` → cascade (10 failures)

Affects TC16–TC20 (all two-product MH change scenarios). The GET step attempts to read column index 13 from a 13-element array (0-indexed: 0–12), meaning one column was removed or the parser expects one more column than the response contains. Because `odIds` are not stored in TestContext, every downstream POST step in the same scenario fails with `No MH odIds found in TestContext`. TC17 and TC18 additionally show `moduleCode` mismatch (`[54, 58]` vs `[58, 58]`), suggesting the second product line carries a wrong module after the size change.

### 4. Array ordering non-determinism (2 failures)

TC15 and TC19 POST assertions fail because `packageId`/`productId` arrays are returned in a different order than the fixture expects (e.g. `[SVD, AB]` vs `[AB, SVD]`). The API does not guarantee element ordering in multi-product arrays; test assertions use strict ordered equality.

### 5. Path parameter mapping error — TC24 (1 failure)

The step `Verify Rialto reflects the reverted full-page state` supplies `agencyPrisaId=6655` but leaves `uuid` undefined. The request URL template contains `{uuid}`, which is not substituted. Possibly a step definition binds the wrong context variable.

### 6. Basket ID synchronisation drift — TC35 (1 failure)

After a Rialto-initiated change, the MH basket `orBoxid` (`6665`) does not match the Agency Prisa ID (`6666`) stored in the test context. This may indicate that the basket is re-created with a new ID on update rather than updated in place, or that the Prisa ID captured during setup is off by one.

---

## Affected Components

| Component | Evidence |
|---|---|
| B2A discount-type assignment | `discountType` is `null` across all order types |
| CASS GET API response parser | `ArrayIndexOutOfBoundsException` at column index 13 |
| B2A price calculation engine | `discountAmount`, `commissionAmount`, `totalInclVat` drift |
| Test fixtures (TC27 date, TC27/28 scalar vs array) | Issue date stale; response schema mismatch |
| Rialto GET step definition (TC24) | `uuid` path parameter unbound |
| Basket ID persistence logic (TC35) | `orBoxid` vs Prisa ID desync post-patch |

---

## Recommended Fix

- **`discountType=null`** — Investigate B2A order-creation and order-update handlers; ensure `discountType` is set to `RIALTO` when orders originate from or are managed by Rialto.
- **Index OOB** — Inspect the CSV/response parser for the two-product MH GET step; the column at index 13 is missing from the current response. Add a bounds check or update the column mapping to match the current API response shape.
- **Array ordering** — Replace strict ordered-equality assertions with order-insensitive matchers (e.g. `containsInAnyOrder`) for multi-product array fields.
- **TC27 date / scalar mismatch** — Refresh test fixtures for TC27 issue date; align assertion format (array vs scalar) with the current API response schema.
- **TC24 path param** — Correct the step definition to bind `uuid` from TestContext instead of (or in addition to) `agencyPrisaId`.
- **TC35 basket drift** — Capture `orBoxid` from the MH response after the patch step rather than relying on the pre-patch Prisa ID.

---

## Prevention

- Add a contract test that asserts `discountType` is non-null for RIALTO orders at the API boundary.
- Add a column-count assertion in the MH GET parser to fail fast with a descriptive error instead of an `ArrayIndexOutOfBoundsException`.
- Enforce order-insensitive comparison for all multi-element array fields in fixture matchers.
