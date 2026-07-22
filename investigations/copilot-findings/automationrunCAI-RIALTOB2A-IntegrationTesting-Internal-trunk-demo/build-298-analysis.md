# Root Cause Analysis — Build 298

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-298.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-298.md)

---

## Summary

- Build 298 is `UNSTABLE` with 5 failed tests out of 15 (66.7% pass rate).
- All failures are confined to `rialtoB2A(CASS)TestCase29.feature` (Magazine — change to Uppslag/Spread/Panorama).
- The primary failure is a misconfigured Rialto GET request using `uuid` instead of `agencyPrisaId` as a path parameter; three MediaHouse steps cascade-fail due to missing TestContext state.

---

## Root Cause

1. **`agencyPrisaId` path parameter not resolved in Rialto GET calls**
   - Two Rialto verification steps fail with `IllegalArgumentException`: the API call is constructed with `uuid` as the path parameter when `agencyPrisaId` is expected.
   - First failure: `uuid=1829d8f3-7e33-4bdd-9964-b45c03af5f88` is passed as a redundant parameter while `agencyPrisaId` is undefined.
   - Second failure (revert state check): `agencyPrisaId` is entirely absent — `Expected 1, was 0` path parameters.
   - This suggests the step definition resolves the identifier variable incorrectly — possibly using a `uuid` variable binding where `agencyPrisaId` should be used.

2. **Cascading NullPointerException in MediaHouse steps**
   - Because the Rialto GET step that captures shared identifiers failed, the Prisa ID is never written to `TestContext`.
   - `MEDIAHOUSE - Verify original full-page order state` and `MEDIAHOUSE - Verify updated MediaHouse basket state` throw `NullPointerException` at `ApiStepDefinition:1488` when attempting to read the Prisa ID from `TestContext`.
   - `MEDIAHOUSE - Update two MediaHouse order lines to uppslag` fails with an explicit guard: `No MH odIds found in TestContext`.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS)TestCase29.feature`
- Step definition: `ApiStepDefinition.java` — `user_verify_the_prisa_id_matches_with_the_prisa_id_from_agency` (line 1488) and the Rialto GET path-parameter binding step
- TestContext shared state keys: `agencyPrisaId`, `MH odIds`

---

## Recommended Fix

- Check the Rialto GET step that constructs the URL for `tc29` — the path parameter binding should use `agencyPrisaId`, not `uuid`.
- Add a null-guard in `ApiStepDefinition:1488` to produce a meaningful assertion failure instead of a `NullPointerException` when `agencyPrisaId` is missing from `TestContext`.

---

## Prevention

- Validate required `TestContext` keys at the start of each dependent step and fail fast with a descriptive message rather than propagating `NullPointerException`.
- Add a dedicated unit/integration check for the `agencyPrisaId` path-parameter binding in TC29 Rialto GET steps to catch misconfigured URL templates early.
