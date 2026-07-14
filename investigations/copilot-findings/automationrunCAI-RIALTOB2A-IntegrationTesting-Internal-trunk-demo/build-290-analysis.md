# Root Cause Analysis — Build 290

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`
**Report:** [build-290.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-290.md)

---

## Summary

Build 290 is `UNSTABLE` with 3 failures out of 14 tests in the CASS TC4 Change Placement flow. The failures split into two categories: MediaHouse discount/financial mismatches and Rialto placement/state mismatches.

---

## Root Cause

1. **MediaHouse discount/financial projection drift**
   - `tc_getMHTC03` and `tc_getMHTC03a` fail because `discountType` and basket financial fields (commission, VAT, total incl. VAT) differ from expected values.
2. **Rialto placement update state not reflected in GET validation**
   - `tc_getIntegrationRialto05b` fails due to mismatches in placement/state and pricing fields (`statusFlags`, `depth`, `commissionAmount`, `priceNet`).

---

## Affected Components

- MediaHouse GET validation (`MediaHouse/getMHB2A.csv`): `tc_getMHTC03`, `tc_getMHTC03a`
- Rialto GET validation (`Rialto/RialtoB2A/getRialtoB2A.csv`): `tc_getIntegrationRialto05b`
- Feature: `rialtoB2A(CASS)TestCase4.feature`

---

## Recommended Fix

- Verify discount propagation and recalculation logic from Rialto to MediaHouse after placement updates.
- Verify placement change persistence/mapping in Rialto before GET validation assertions execute.
- Compare service-side payload values against expected test data for TC4 (`tc_getMHTC03`, `tc_getMHTC03a`, `tc_getIntegrationRialto05b`).

---

## Prevention

- Add a targeted integration assertion checkpoint immediately after placement update to validate `discountType`, `statusFlags`, and key price fields before final GET checks.
- Track this failure cluster as a single recurring issue in CI triage to avoid fragmented analysis across builds.
