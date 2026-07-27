# Root Cause Analysis — `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` Build 319

Source report: [build-319.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-319.md)

---

## Summary

Build 319 finished UNSTABLE with 4 failures out of 16 tests (75.0% pass rate). All failures are in `rialtoB2A(CASS)TestCase29.feature` and cluster into two groups: cross-system ID drift between MH and Agency identifiers, plus one reverted-state validation mismatch in Rialto.

---

## Root Cause

- **Primary:** MediaHouse returned basket identifier `6863` while Agency context expected Prisa ID `6868`, causing ID-consistency assertions to fail in both MH verification scenarios.
- **Cascade:** Because the earlier MH verification flow did not produce stable order-line IDs in context, the follow-up patch scenario failed with `No MH odIds found in TestContext`.
- **Secondary:** The final Rialto verification step returned non-reverted field values (placement/dimensions/pricing/status), indicating order-state data did not match the expected post-flow state.

---

## Affected Components

- `rialtoB2A(CASS)TestCase29.feature`
- MH basket/Prisa ID consistency check (`User verify the Prisa ID matches with the Prisa ID from Agency`)
- Test context storage/consumption for MH `odIds`
- Rialto order response fields under `orderAdDetails` and `orderHeader`

---

## Recommended Fix

- Validate ID mapping between MH `orBoxid` and Agency Prisa ID for the TC29 flow before verification assertions.
- Ensure MH GET step reliably stores `odIds` before executing `tc_patchIntegrationMH_MZN03`.
- Re-check expected reverted-state fixtures for `tc_getIntegrationRialtoMZN04b` against current service output (placement, size, pricing, status flags).

---

## Prevention

- Add an early guard in TC29 to fail fast when MH `orBoxid` and Agency Prisa ID diverge.
- Add a prerequisite assertion that `odIds` are present before patch-step execution.
- Keep a focused regression check for TC29 reverted-state fields to detect drift immediately.
