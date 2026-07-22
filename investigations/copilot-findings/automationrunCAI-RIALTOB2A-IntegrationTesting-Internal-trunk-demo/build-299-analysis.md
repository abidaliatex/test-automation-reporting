# Root Cause Analysis — Build 299

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-299.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-299.md)

---

## Summary

- Build 299 is `UNSTABLE` with 5 failed tests out of 15.
- All failures are confined to `rialtoB2A(CASS)TestCase29.feature`.
- The failure pattern matches build 298: the initial Rialto GET cannot resolve `agencyPrisaId`, and three MediaHouse checks then fail because shared context was never populated.

---

## Root Cause

1. **Rialto GET step uses the wrong or missing path parameter**
   - The first failing step calls the GET endpoint with key `uuid`, but the request URI expects `agencyPrisaId`.
   - The later revert-state verification also fails because no `agencyPrisaId` value is available when the GET step runs.
2. **MediaHouse assertions are downstream failures**
   - Because the earlier Rialto GET never captures shared identifiers, MediaHouse verification steps hit `NullPointerException` or fail the explicit `MH odIds` guard.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS)TestCase29.feature`
- Rialto GET step using `User perfrom "get" request with keys ...`
- `ApiStepDefinition.user_verify_the_prisa_id_matches_with_the_prisa_id_from_agency` (`ApiStepDefinition.java:1488`)
- Shared TestContext values: `agencyPrisaId`, `MH odIds`

---

## Recommended Fix

- Check the TC29 Rialto verification step so the GET request binds `agencyPrisaId` instead of `uuid`.
- Verify the step that should store `agencyPrisaId` runs before any dependent MediaHouse assertions.
- Keep the `MH odIds` guard and add a similar fast-fail message for missing `agencyPrisaId` to avoid opaque `NullPointerException`s.

---

## Prevention

- Add a lightweight validation checkpoint after the first Rialto GET to confirm `agencyPrisaId` and `MH odIds` were stored before continuing.
- Since Jenkins reports this failure as continuing from build 298, treat TC29 as an active regression until the path-parameter binding is fixed.
