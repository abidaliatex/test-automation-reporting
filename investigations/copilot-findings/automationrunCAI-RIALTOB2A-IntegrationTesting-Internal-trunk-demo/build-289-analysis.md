# Root Cause Analysis — Build 289

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`
**Report:** [build-289.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-289.md)

---

## Summary

Build 289 is UNSTABLE with 3 failures out of 14 tests (78.6% pass rate). All three failures have been recurring since build 246 (`failedSince: 246`) and are identical to those seen in build 288. The failures cover the CASS TC4 Change Placement end-to-end flow across MediaHouse (MH) and Rialto Agency validations.

---

## Root Cause

**Two distinct but related root causes, both persistent since build 246:**

1. **MediaHouse discountType and basket pricing drift** — After the placement change flow, the MH order basket returns `discountType=null` (pre-change) and `discountType=RIALTO` (post-change) where the expected values are `RIALTO` and `NONE` respectively. Associated financial totals (`totalInclVat`, `vat`, `commission`, `orderbasketSum`) are consistently wrong, indicating the discount propagation from Rialto to MH is broken or delayed.

2. **Rialto placement state and pricing mismatch** — After the placement change, the Rialto order returned by GET shows `statusFlags=[]` instead of `[PRELIMINARY]`, `depth=372` instead of `184`, and incorrect commission/price values, suggesting the placement update in Rialto is not being applied correctly.

---

## Affected Components

- MediaHouse GET API (`getMHB2A.csv` — `tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto Agency GET API (`getRialtoB2A.csv` — `tc_getIntegrationRialto05b`)
- CASS TC4 Change Placement feature (`rialtoB2A(CASS)TestCase4.feature`)

---

## Recommended Fix

- Investigate the discount type propagation logic in the Rialto→MH integration layer; `discountType` is not being set or is being reset after the placement change event.
- Check the placement update handler in Rialto: `statusFlags`, `depth`, and commission calculation appear to revert or not apply on the changed placement.
- Review any changes introduced at or around build 246 that may have altered the placement-change processing path.

---

## Prevention

- Add contract assertions on `discountType` in the placement-change integration test to catch regressions earlier.
- Monitor `failedSince` counts — this failure has persisted for 43 consecutive builds; escalate if unresolved.
