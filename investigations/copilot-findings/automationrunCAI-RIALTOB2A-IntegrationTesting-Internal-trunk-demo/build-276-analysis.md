# Root Cause Analysis — Build #276

**Source report:** [build-276.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-276.md)
**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`
**Build:** #276 | **Date:** 2026-07-10 | **Status:** UNSTABLE

---

## Summary

Build #276 produced 3 failures in the `CASS TC4 Change Placement` scenario, all within the same end-to-end flow: create a placement in Rialto → verify it arrives in MediaHouse (MH) → apply a placement change via MH PATCH → re-verify updated state in both systems. All 3 failures have been recurring since build #246, indicating a persistent regression that has not been resolved.

---

## Root Cause

### RC-1: discountType not set on initial placement arrival in MH (tc_getMHTC03)

The MH basket order returned `orders[0].printDetails.discountType = null` instead of `RIALTO`. This suggests the discount type is not being populated when the placement is forwarded from Rialto to MediaHouse during the initial order creation flow.

### RC-2: discountType not cleared after placement change in MH (tc_getMHTC03a)

After the MH PATCH changes the placement, `discountType` remains `RIALTO` instead of resetting to `NONE`. This is the inverse symptom of RC-1 and points to the same discount type propagation logic failing in both directions. The resulting pricing cascade (commission, orderbasketSum, totalInclVat) diverges because the discount rate is incorrectly applied.

### RC-3: Rialto order not updated after placement change (tc_getIntegrationRialto05b)

After the placement change, the Rialto order shows `statusFlags = []` (expected `[PRELIMINARY]`), `depth = 372` (expected `184`), and reduced commission/pricing values. This points to either the PATCH not being fully processed on the Rialto side before the verification GET, or the placement-change handler not updating order metadata correctly.

---

## Affected Components

- **discountType propagation logic** — Rialto → MediaHouse order mapping
- **Placement change handler** — MH PATCH endpoint and subsequent Rialto order update
- **Pricing/commission recalculation** — triggered on placement change in both systems

---

## Recommended Fix

- Investigate the Rialto-to-MH order mapping to ensure `printDetails.discountType` is correctly set on initial placement creation and reset when placement type changes to one with no discount.
- Verify that the MH PATCH handler triggers a Rialto order update and sets `statusFlags = PRELIMINARY` and the correct `depth` for the new placement.
- Review commission calculation for the changed placement; the found value (`620.0`) is significantly lower than expected (`7750.00`), suggesting the commission rate is applied against the wrong base price.

---

## Prevention

- Add an assertion for `discountType` in the earliest MH verification step so failures surface before cascading into pricing assertions.
- Consider adding a dedicated smoke test that verifies `statusFlags = PRELIMINARY` immediately after a placement change, before running full price validations.
