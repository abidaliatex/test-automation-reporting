# Root Cause Analysis — Build 295

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-295.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-295.md)

---

## Summary

- Build 295 is `UNSTABLE` with 3 failed tests out of 14.
- Failures group into MediaHouse financial-field mismatches and Rialto post-update payload mismatches.

---

## Root Cause

1. **MediaHouse projection mismatch after placement flow**
   - `tc_getMHTC03` and `tc_getMHTC03a` fail on `discountType` and pricing totals (`commission`, `vat`, `totalInclVat`).
2. **Rialto post-update state mismatch**
   - `tc_getIntegrationRialto05b` fails because returned status/placement/pricing fields differ from expected test assertions.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS)TestCase4.feature`
- MediaHouse GET validation data: `MediaHouse/getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto GET validation data: `Rialto/RialtoB2A/getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)

---

## Recommended Fix

- Revalidate expected discount/financial mappings applied after placement change before MH GET assertions run.
- Re-check post-update Rialto expected values for `statusFlags`, `depth`, `commissionAmount`, and `priceNet` against current service outputs.

---

## Prevention

- Add a targeted checkpoint in TC4 flow to verify key transformed fields immediately after placement update.
- Track this as a recurring TC4 mismatch cluster if the same three tests continue to fail in consecutive builds.
