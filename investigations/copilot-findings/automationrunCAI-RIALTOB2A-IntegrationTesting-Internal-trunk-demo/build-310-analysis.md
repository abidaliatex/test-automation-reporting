# Root Cause Analysis — Build 310

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-310.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-310.md)

---

## Summary

- Build 310 is `UNSTABLE` with 1 failed test out of 14 (92.9% pass rate).
- The failure is a new occurrence (`failedSince: 310`) in the TC7 Change Date, Size & Placement flow.
- The `discountType` field is missing (`null`) in the MediaHouse response after the order is forwarded from Rialto.

---

## Root Cause

- **`discountType` not propagated from Rialto to MediaHouse**
  - The MediaHouse GET endpoint (`tc_getMHTC06`) returns `orders[0].printDetails.discountType=null` instead of the expected value `RIALTO`.
  - This suggests either the field is not set during the order creation/forwarding step in Rialto, or MediaHouse is not mapping it into its response for the "Change Date, Size & Placement" scenario.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS TC7 Change Date, Size & Placement)`
- MediaHouse validation: `tc_getMHTC06` — "verify that order arrived in MH from rilato - Change Date, Size & Placement"
- Assertion point: `ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

---

## Recommended Fix

- Verify that the Rialto POST step (`tc_postIntegrationRialtoE2E07`) correctly sets `discountType` on the order before forwarding to MediaHouse.
- Check the MediaHouse basket order API mapping to ensure `printDetails.discountType` is included in the TC7 response.

---

## Prevention

- Add an intermediate assertion after the Rialto creation step to confirm `discountType` is present in the Agency/Rialto response before the MediaHouse verification step.
- Rebaseline TC7 expected datasets if the `discountType` contract has changed.
