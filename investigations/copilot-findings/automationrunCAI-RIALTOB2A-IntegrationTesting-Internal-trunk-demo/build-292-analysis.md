# Root Cause Analysis — Build 292

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`
**Report:** [build-292.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-292.md)

---

## Summary

Build 292 is `UNSTABLE` with 3 failures out of 14 tests. All 3 failures have been recurring since build 246. Failures cluster into two groups: MediaHouse discount/financial mismatches and Rialto placement/pricing mismatches after the TC4 placement-change flow.

---

## Root Cause

1. **MediaHouse financial projection mismatch**
   - `tc_getMHTC03`: `discountType` is `null` instead of `RIALTO`, and basket totals (VAT, totalInclVat) are higher than expected — possibly discount not applied before MH receives the order.
   - `tc_getMHTC03a`: `discountType` persists as `RIALTO` after placement change instead of resetting to `NONE`; commission and basket sum differ from expected values after update.

2. **Rialto post-update payload mismatch**
   - `tc_getIntegrationRialto05b`: After the MH placement change, the Rialto GET response shows `statusFlags` as empty (expected `PRELIMINARY`), `commissionAmount` as `620.0` (expected `7750.00`), and `depth` as `372` (expected `184`). May indicate the placement-change callback or commission recalculation has not completed before the GET assertion runs.

---

## Affected Components

- MediaHouse GET assertions (`MediaHouse/getMHB2A.csv`): `tc_getMHTC03`, `tc_getMHTC03a`
- Rialto GET assertions (`Rialto/RialtoB2A/getRialtoB2A.csv`): `tc_getIntegrationRialto05b`
- Feature flow: `rialtoB2A(CASS)TestCase4.feature`

---

## Recommended Fix

- Verify discount type mapping from Rialto to MediaHouse is applied correctly on initial order and reset after placement change.
- Confirm placement-update processing and commission recalculation complete before final Rialto GET assertions execute.
- Reconcile expected TC4 values for `commissionAmount`, `depth`, `statusFlags`, and `totalInclVat` against current service behaviour.

---

## Prevention

- Add an intermediate validation checkpoint after placement update and before final GET checks for key fields (`discountType`, `statusFlags`, `commissionAmount`, `totalInclVat`).
- Track this as a recurring TC4 placement-update failure cluster (failing since build 246) until root cause is resolved.
