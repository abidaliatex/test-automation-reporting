# Root Cause Analysis — Build #150

**Source report:** [build-150.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-150.md)

---

## Summary

Build #150 of `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` completed on 2026-07-25 21:03 UTC with status **UNSTABLE**: 86 failures out of 513 tests (83.2% pass rate). Failure count is identical to build #149 (86 failures); no regressions or recoveries were observed. The same five systemic defect groups persist across TC1/TC3/TC4/TC5/TC6/TC9/TC11/TC14/TC15/TC16/TC17/TC18/TC19/TC20/TC22/TC23/TC24/TC26/TC27/TC28/TC29/TC30/TC31/TC32/TC33/TC34/TC35/TC36/TC37.

---

## Root Cause

### 1. `discountType` is not populated for Rialto-originated order flows (40 failures)
- `orders[*].printDetails.discountType expected [[RIALTO]] but found [[null]]` affects the widest set of TCs (TC1, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC22, TC23, TC24, TC26, TC27–TC36).
- The same responses show drifting basket discount totals, so the missing field likely feeds directly into downstream financial calculations.
- This defect has persisted unchanged across at least builds #148, #149, and #150, indicating a systemic gap in the Rialto-to-CASS discount-type propagation logic.

### 2. Financial values drift after create/update operations (23 failures)
- Order totals (`netAmount`, `discountAmount`, `commissionAmount`, `totalInclVat`) and `statusFlags` return wrong or stale values after successful API calls.
- Some mismatches are floating-point precision (`38140.399999999994` vs `38140.4`), but others are large discrepancies (`netAmount expected 192192.0 but found 128531.37`), pointing to two distinct sub-issues: rounding and wrong calculation logic.
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` suggests the order creation step does not always reach PRELIMINARY state before the GET assertion fires.

### 3. Two-product MH parser / TestContext cascade (10 failures)
- TC16–TC20 all fail at the GET step with `Index 13 out of bounds for length 13`, meaning the parser reads one column beyond the available response schema.
- Because `odIds` are never stored, the paired POST step fails with `No MH odIds found in TestContext`, cascading further assertion failures for `moduleCode`, `placementId`, and `issueDate` in the same TCs.
- This defect has persisted since at least build #148.

### 4. issueDate not propagated after date-change operations (7 failures)
- After date-change updates via MH (TC15, TC16, TC22, TC24) or Rialto (TC27, TC35), the returned `issueDate` still shows the original value.
- TC16 example: `issueDate expected [[2026-07-01, 2026-07-21]] but found [[2026-07-01, 2026-07-01]]` — the second order line date was not updated.
- Possibly a server-side propagation delay or a missing update trigger in the integration layer.

### 5. Path parameter binding error and basket ID drift (2 failures)
- TC24: `agencyPrisaId=6780` is passed but `uuid` is left undefined in the Rialto verification step — the step definition is wired incorrectly (unchanged from build #149, where `agencyPrisaId=6740`).
- TC35: `MH basket ID (orBoxid) [6790] does not match Agency Prisa ID [6791]` — post-update basket identifiers are out of sync between MH and the Agency side (same pattern as build #149, different ID values).

---

## Affected Components

- **Rialto/CASS discount propagation** — `discountType` and basket-level discount totals are inconsistently set for Rialto-managed orders.
- **Price/status recalculation logic** — `discountAmount`, `commissionAmount`, `netAmount`, `statusFlags` drift after updates; floating-point rounding also contributes.
- **MH two-product parser / context storage** — GET-step column index is off-by-one for two-product responses; `odIds` are never stored for TC16–TC20.
- **Date propagation in update flows** — `issueDate` is not updated on the expected order lines after MH or Rialto date-change operations.
- **Step-definition parameter wiring** — TC24 supplies `agencyPrisaId` but not `uuid` in the Rialto verification step.
- **Cross-system basket identity sync** — TC35 post-update `orBoxid` differs from the captured Agency Prisa ID by 1.

---

## Recommended Fix

- Investigate where `printDetails.discountType` is set for Rialto-managed orders in the CASS API response and why the field returns `null` across both newspaper and magazine flows.
- Separate floating-point rounding fixes (use a tolerance matcher) from genuine calculation errors (`netAmount` 192192 vs 128531); the latter needs logic investigation in the discount/commission pipeline.
- Fix the TC16–TC20 GET-step response parser to not read column index 13 when the payload has only 13 columns (0-indexed); ensure `odIds` are stored before the POST step executes.
- Trace the `issueDate` update path for both MH-initiated (TC15, TC16, TC22, TC24) and Rialto-initiated (TC27, TC35) date changes to identify where the propagation is dropped.
- Correct the TC24 step definition to bind `uuid` instead of (or in addition to) `agencyPrisaId`.
- Investigate why the MH `orBoxid` increments by 1 relative to Agency Prisa ID in TC35 after a Rialto-driven update.

---

## Prevention

- Add a contract assertion that rejects successful CASS GET responses where `discountType` is `null` for any Rialto-originated order.
- Introduce a tolerance-based numeric comparator for price fields to isolate floating-point false positives from genuine calculation bugs.
- Add a bounds check or schema guard before reading the two-product MH GET payload column at index 13.
- Add a targeted regression for `issueDate` propagation covering both MH-side and Rialto-side date-change flows.
