# Root Cause Analysis — Build #148

**Source report:** [build-148.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-148.md)

---

## Summary

Build #148 of `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` completed on 2026-07-23 21:03 UTC with status **UNSTABLE**: 88 failures out of 513 tests (82.8% pass rate). This is two more failures than build #147 (86 failures). Jenkins checked out revision `d120278b4bba91939ae718e0f45b6de5827461ac` with commit message `updated testcase29 data`; however, the failures remain broad across TC1/3/4/5/6/7/9/11/14/15/16/22/23/24/26-37, so the dominant defects are still systemic rather than isolated to TC29.

---

## Root Cause

### 1. `discountType` is still not populated for Rialto-originated order flows
- The clearest recurring defect is `orders[*].printDetails.discountType expected [[RIALTO]] but found [[null]]`.
- It affects both classic CASS API flows (TC1, TC3, TC4, TC5, TC6, TC7, TC9, TC11) and magazine verification flows (TC26-TC36).
- Basket discounts drift in the same responses (`orderDiscount` expected `0.00` but found values such as `3600.00` or `4800.00`), so the missing field is likely feeding directly into the wrong financial state.

### 2. Financial, date, and status values drift after create/update operations
- Many failures are not transport errors; the operations succeed but return the wrong values.
- Repeated examples include `discountAmount expected [0.0] but found [63660.63]`, `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`, and issue-date mismatches such as `2026-08-19` vs `2026-08-26`.
- TC27-TC31 and TC35 show that magazine updates are especially sensitive to this drift, with wrong `priceNet`, `commissionAmount`, `placementId`, and `issueDate` coming back after the update.

### 3. The two-product MH flows still break on column parsing before downstream validation
- TC16-TC20 all hit `Index 13 out of bounds for length 13` in the GET step.
- Because the GET step never stores `odIds`, the paired POST step fails with `No MH odIds found in TestContext`.
- The remaining POST assertions (`moduleCode`, `placementId`, `issueDate`) indicate that even when execution continues, the wrong line-item data is being validated.

### 4. Multi-line MH full-page/uppslag updates are unstable and partially non-transactional
- TC22-TC24 show reordering of package/product/placement arrays during MH basket updates and reverts.
- The patch/revert steps in TC22-TC24 also hit `Transaction rolled back because it has been marked as rollback-only`, which points to server-side update handling rather than an assertion-only problem.
- TC24 has an additional step-definition/input binding problem: `agencyPrisaId` is supplied but `uuid` is left undefined in the final Rialto verification step.

### 5. Basket identity is still drifting after Rialto-driven magazine updates
- TC35 ends with `MH basket ID (orBoxid) [6712] does not match Agency Prisa ID [6713]`.
- This looks like post-update identifier desynchronisation between MH and the Agency-side record, not just a fixture formatting issue.

---

## Affected Components

- **Rialto/CASS discount propagation** — `discountType`, `orderDiscount`, and related totals are inconsistent across many successful responses.
- **Price/status recalculation logic** — `discountAmount`, `commissionAmount`, `priceNet`, `priceGross`, `statusFlags`, and `issueDate` drift after updates.
- **MH two-product parser / context storage** — GET-step column parsing fails before `odIds` are persisted for TC16-TC20.
- **MH multi-line update handling** — full-page/uppslag basket updates reorder arrays and trigger rollback-only transactions in TC22-TC24.
- **Step-definition parameter wiring** — TC24 still binds `agencyPrisaId` without a `uuid`.
- **Cross-system basket identity sync** — TC35 still ends with `orBoxid` / Agency Prisa ID mismatch.

---

## Recommended Fix

- Verify where the integration sets `printDetails.discountType` for Rialto-managed orders and why it is returning `null` on both newspaper and magazine flows.
- Recheck the post-update calculation pipeline for totals/status flags; build #148 shows successful API calls that return stale or wrong business values.
- Fix the TC16-TC20 GET-step parser/schema expectation so `odIds` are stored before the POST step runs.
- Investigate the TC22-TC24 MH update transaction path for rollback-only handling and unstable line ordering; TC24 also needs the `uuid` binding corrected.
- For TC35, capture or reconcile the post-update basket identifier used by MH versus Agency Prisa.

---

## Prevention

- Add a focused contract check that rejects successful responses where `discountType` is `null` for Rialto scenarios.
- Add a parser/schema guard for the TC16-TC20 two-product GET payload before attempting to read column index 13.
- Add a dedicated regression around TC22-TC24 multi-line full-page/uppslag updates that checks both transaction success and stable identifier binding.
