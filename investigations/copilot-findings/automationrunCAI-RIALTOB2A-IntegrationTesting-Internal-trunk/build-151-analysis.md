# Root Cause Analysis — Build #151

**Source report:** [build-151.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-151.md)

---

## Summary

Build #151 of `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` completed on 2026-07-26 21:03 UTC with status **UNSTABLE**: 88 failures out of 513 tests (82.8% pass rate). Failure count increased by 2 compared to build #150 (86 failures). A new failure type — a server-side transaction rollback in TC24 — appeared in this run. The same five systemic defect groups persist across TC1/TC3-TC6/TC9/TC11/TC14/TC15/TC16-TC20/TC22-TC24/TC26-TC37.

---

## Root Cause

### 1. `discountType` is not populated for Rialto-originated order flows (~40 failures)
- `orders[*].printDetails.discountType expected [[RIALTO]] but found [[null]]` affects the widest set of TCs (TC1, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC22, TC23, TC24, TC26, TC27–TC36).
- Basket-level discount totals (`orderDiscount`, `sumDiscount`, `netPrice`) also drift in the same responses, indicating the missing field directly feeds into downstream financial aggregations.
- This defect has persisted unchanged across at least builds #148–#151, indicating a systemic gap in the Rialto-to-CASS discount-type propagation logic.

### 2. Financial values drift after create/update operations (~23 failures)
- Order totals (`netAmount`, `discountAmount`, `commissionAmount`, `totalInclVat`) and `statusFlags` return wrong or stale values after successful API calls.
- Some mismatches are floating-point precision (`33159.79999999999` vs `33159.8`), but others are large discrepancies (`netAmount expected 192192.0 but found 128531.37`), indicating two distinct sub-issues: rounding and wrong calculation logic.
- New in build #151: TC27 and TC28 Rialto steps show a scalar-vs-array type mismatch (`discountAmount expected [[3600.0]] but found [3600.0]`), suggesting the response structure may have changed.
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` suggests the order creation step does not always reach PRELIMINARY state before the GET assertion fires.

### 3. Two-product MH parser / TestContext cascade (10 failures)
- TC16–TC20 all fail at the GET step with `Index 13 out of bounds for length 13`, meaning the parser reads one column beyond the available response schema.
- Because `odIds` are never stored, the paired POST step fails with `No MH odIds found in TestContext`, cascading further assertion failures for `moduleCode`, `placementId`, and `issueDate` in the same TCs.
- This defect has persisted since at least build #148.

### 4. issueDate not propagated after date-change operations (7 failures)
- After date-change updates via MH (TC15, TC16, TC19, TC20) or Rialto (TC27, TC35), the returned `issueDate` still shows the original value.
- TC27 example: `orders.printDetails.issueDate expected [[2026-08-19]] but found [[2026-08-26]]` — the issue date was not updated after the MH change.
- Possibly a server-side propagation delay or a missing update trigger in the integration layer.

### 5. Path parameter error, transaction rollback, and basket ID drift (8 failures)
- TC1: `mhBasketOrderId` is undefined in the CASS GET step — the path parameter is not being injected (2 failures).
- TC24: A server-side HTTP 500 `Transaction rolled back because it has been marked as rollback-only` prevents the revert step from completing — **new in build #151**. A follow-up step also supplies `agencyPrisaId=6817` but leaves `uuid` undefined.
- TC35: `MH basket ID (orBoxid) [6827] does not match Agency Prisa ID [6828]` — post-update basket identifiers are out of sync between MH and the Agency side.

---

## Affected Components

- **Rialto/CASS discount propagation** — `discountType` and basket-level discount totals are inconsistently set for Rialto-managed orders.
- **Price/status recalculation logic** — `discountAmount`, `commissionAmount`, `netAmount`, `statusFlags` drift after updates; floating-point rounding also contributes.
- **Response serialisation** — TC27/TC28 Rialto steps return scalar values where arrays are expected (`[[3600.0]]` vs `[3600.0]`).
- **MH two-product parser / context storage** — GET-step column index is off-by-one for two-product responses; `odIds` are never stored for TC16–TC20.
- **Date propagation in update flows** — `issueDate` is not updated on the expected order lines after MH or Rialto date-change operations.
- **Step-definition parameter wiring** — TC24 supplies `agencyPrisaId` but not `uuid` in the Rialto verification step; TC1 does not inject `mhBasketOrderId`.
- **Transaction management (TC24)** — The server marks the transaction as rollback-only before the revert step, causing a 500 that was not seen in previous builds.
- **Cross-system basket identity sync** — TC35 post-update `orBoxid` differs from the captured Agency Prisa ID by 1.

---

## Recommended Fix

- Investigate where `printDetails.discountType` is set for Rialto-managed orders in the CASS API response and why the field returns `null` across both newspaper and magazine flows.
- Separate floating-point rounding fixes (use a tolerance matcher) from genuine calculation errors (`netAmount` 192192 vs 128531); the latter needs logic investigation in the discount/commission pipeline.
- Investigate the scalar-vs-array response structure change for `discountAmount`/`priceGross` in TC27/TC28 Rialto steps — possibly a recent serialisation change in the Rialto API.
- Fix the TC16–TC20 GET-step response parser to not read column index 13 when the payload has only 13 columns (0-indexed); ensure `odIds` are stored before the POST step executes.
- Trace the `issueDate` update path for both MH-initiated (TC15, TC16, TC19, TC20) and Rialto-initiated (TC27, TC35) date changes to identify where the propagation is dropped.
- Investigate the TC24 transaction rollback root cause on the server side (possibly a concurrent modification or constraint violation).
- Correct the TC24 step definition to bind `uuid` instead of `agencyPrisaId`; ensure TC1 correctly injects `mhBasketOrderId` as a path parameter.

---

## Prevention

- Add a contract assertion that rejects successful CASS GET responses where `discountType` is `null` for any Rialto-originated order.
- Introduce a tolerance-based numeric comparator for price fields to isolate floating-point false positives from genuine calculation bugs.
- Add a schema validator that enforces array vs scalar response types for financial fields.
- Add a bounds check or schema guard before reading the two-product MH GET payload column at index 13.
- Add a targeted regression for `issueDate` propagation covering both MH-side and Rialto-side date-change flows.
- Add a health-check step after revert operations in TC24 to detect transaction rollback conditions before asserting state.
