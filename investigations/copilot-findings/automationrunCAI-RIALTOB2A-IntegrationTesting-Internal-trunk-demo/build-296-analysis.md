# Root Cause Analysis — Build 296

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-296.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-296.md)

---

## Summary

- Build 296 is `UNSTABLE` with 3 failed tests out of 14.
- All three failures have persisted since build 246, indicating a long-running regression in the TC4 Change Placement flow.
- Failures group into MediaHouse financial-field mismatches and Rialto post-update payload mismatches.

---

## Root Cause

1. **MediaHouse projection mismatch after placement flow**
   - `tc_getMHTC03` fails on `discountType` being `null` instead of `RIALTO`, indicating the discount type is not being set/propagated correctly to the MH order upon initial creation.
   - `tc_getMHTC03a` fails on pricing totals (`commission`, `vat`, `orderbasketSum`, `totalInclVat`) after the placement change, suggesting the commission calculation post-update is incorrect.
2. **Rialto post-update state mismatch**
   - `tc_getIntegrationRialto05b` fails because status, depth, and commission/price fields in the Rialto GET response differ from expected assertions after the placement change.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS)TestCase4.feature`
- MediaHouse GET validation data: `MediaHouse/getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto GET validation data: `Rialto/RialtoB2A/getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)

---

## Recommended Fix

- Investigate why `discountType` is not populated in the MH order during the B2A placement creation flow.
- Re-check commission calculation logic applied after placement change — actual commission (`12500.00`) differs significantly from expected (`7750.00`).
- Re-check post-update Rialto expected values for `statusFlags`, `depth`, and `commissionAmount` against current service outputs.

---

## Prevention

- Add a targeted checkpoint in TC4 flow to verify key transformed fields immediately after placement update.
- This cluster (`tc_getMHTC03`, `tc_getMHTC03a`, `tc_getIntegrationRialto05b`) has failed continuously since build 246 — escalate as a blocking regression if not addressed.
