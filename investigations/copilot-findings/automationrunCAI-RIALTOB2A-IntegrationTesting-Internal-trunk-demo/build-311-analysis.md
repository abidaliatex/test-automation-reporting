# Root Cause Analysis — Build 311

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-311.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-311.md)

---

## Summary

- Build 311 is `UNSTABLE` with 1 failed test out of 14 (92.9% pass rate).
- The failure is a new REGRESSION first introduced in this build (failedSince: 311).
- The TC7 "Change Date, Size & Placement" flow fails at the MediaHouse order verification step due to a missing `discountType` value.

---

## Root Cause

1. **`discountType` field is `null` in MediaHouse order response for TC7**
   - After Rialto creates and the agency processes the "Change Date, Size & Placement" order, the GET call to MediaHouse (`tc_getMHTC06`) expects `orders[0].printDetails.discountType=RIALTO` but the field is not populated (`null`).
   - This is a new regression — all prior builds passed this assertion. Possibly caused by a recent change in the Rialto-to-MediaHouse B2A integration that stopped propagating the `discountType` field.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS TC7 Change Date, Size & Placement)`
- MediaHouse GET validation: `tc_getMHTC06` — "verify that order arrived in MH from rilato - Change Date, Size & Placement"
- Assertion point: `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

---

## Recommended Fix

- Investigate recent changes to the Rialto B2A integration that may have stopped setting `discountType` on print details when forwarding "Change Date, Size & Placement" orders to MediaHouse.
- Verify whether `discountType=RIALTO` should be set during order creation or order update propagation.

---

## Prevention

- Add a dedicated assertion checkpoint immediately after order propagation to MediaHouse to confirm `discountType` is populated before downstream TC7 assertions run.
- Include `discountType` in the rebaseline checklist whenever B2A order-mapping logic is modified.
