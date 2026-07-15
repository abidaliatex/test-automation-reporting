# Root Cause Analysis — Build 291

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`
**Report:** [build-291.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-291.md)

---

## Summary

Build 291 is `UNSTABLE` with 3 failures out of 14 tests. Failures cluster into two groups: MediaHouse discount/financial mismatches and Rialto placement/pricing mismatches after placement update flow.

---

## Root Cause

1. **MediaHouse financial projection mismatch**
   - `tc_getMHTC03` and `tc_getMHTC03a` fail with `discountType` and basket total/commission/VAT differences from expected values.
2. **Rialto post-update payload mismatch**
   - `tc_getIntegrationRialto05b` fails because placement and pricing fields in the GET response differ from expected test data.

---

## Affected Components

- MediaHouse GET assertions (`MediaHouse/getMHB2A.csv`): `tc_getMHTC03`, `tc_getMHTC03a`
- Rialto GET assertions (`Rialto/RialtoB2A/getRialtoB2A.csv`): `tc_getIntegrationRialto05b`
- Feature flow: `rialtoB2A(CASS)TestCase4.feature`

---

## Recommended Fix

- Verify discount type and financial recalculation mapping from Rialto to MediaHouse after placement change.
- Verify placement-update persistence before running final Rialto GET assertions.
- Reconcile expected TC4 values for pricing and placement fields against current service output.

---

## Prevention

- Add an intermediate validation checkpoint after placement update and before final GET checks for key fields (`discountType`, `placementId`, `commissionAmount`, `totalInclVat`).
- Track this as a recurring TC4 placement-update failure cluster in triage until outputs stabilize.
