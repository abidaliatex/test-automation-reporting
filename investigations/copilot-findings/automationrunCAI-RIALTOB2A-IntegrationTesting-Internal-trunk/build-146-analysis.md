# Root Cause Analysis — Build 146

**Source Report:** [build-146.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-146.md)

---

## Summary

Build 146 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, 2026-07-21 21:03 UTC) is UNSTABLE with **87 failures out of 513 tests (83.0% pass rate)**. Failure count decreased by 1 from build #145 (88 failures) — no root cause has been resolved. All six root cause groups identified in build #145 persist unchanged.

---

## Root Cause

### 1. `discountType` Not Set to `RIALTO` (39 failures — **highest impact**)
- The B2A/CASS integration service returns `null` instead of `RIALTO` for `orders[*].printDetails.discountType` across all change-event types (size, placement, date, product, uppslag, magazine).
- Affects 21 feature files spanning TC1&2 through TC36.
- The null discount type causes basket-level financial fields (`orderDiscount`, `sumDiscount`, `netPrice`) to be miscalculated in the same response, generating secondary assertion failures.
- Present and unresolved since at least build #143.
- Impact increased by 8 compared to build #145 (31 → 39), suggesting wider propagation.

### 2. Financial Calculation Drift and Status Flag Missing (29 failures)
- `discountAmount`, `commissionAmount`, `priceNet`, `priceGross`, `vat`, and `totalInclVat` diverge from test-fixture expectations across POST and GET steps.
- `orderHeader.statusFlags` returns `[[]]` instead of `[[PRELIMINARY]]` for TC1&2, TC3, TC4, TC5, TC6, indicating order initialisation is not completing.
- TC27 and TC28 Rialto assertions fail on array-vs-scalar serialisation: `discountAmount` expected `[[3600.0]]` found `[3600.0]`.
- Possibly downstream of root cause 1: missing `discountType` triggers incorrect price recalculation.

### 3. CSV Parsing Index Out-of-Bounds → TestContext Cascade (11 failures)
- `ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` at `CSVRecord.get()` indicates the CSV test-data fixture for two-product scenarios (TC16–TC20) accesses column index 13 in a 13-column record (indices 0–12).
- The GET step fails before `odIds` are written to TestContext; the downstream POST step errors with `No MH odIds found in TestContext`.
- TC29 now also hits the null-odId error (new in build 146), increasing impact from 10 → 11 failures.
- Unchanged from build #145 — CSV fixture has not been corrected.

### 4. Array Ordering Non-determinism (3 failures)
- `packageId`, `productId`, `paCode`, and `placementId` arrays from CASS POST responses return in non-deterministic order.
- Strict ordered-equality assertions fail for TC15, TC19, TC22.
- Impact reduced slightly compared to build #145 (7 → 3); TC24 and TC37 ordering failures may have been absorbed into other groups.

### 5. Path Parameter Mapping Error — TC24 and TC29 (3 failures)
- For TC24: `uuid` path parameter is missing while `agencyPrisaId` is passed redundantly.
- For TC29: parameters reversed — `uuid` supplied where `agencyPrisaId` is expected.
- Both defects are in Cucumber step-definition wiring; unchanged from build #145.

### 6. Post-Patch State Mismatch / Basket ID Drift (1 failure)
- TC35 MH verify step hits `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6590] does not match Agency Prisa ID [6591]`.
- Basket-ID synchronisation drift between MH and Agency Prisa after a Rialto-initiated change.

---

## Affected Components

- **CASS B2A Synchronisation Service** — `discountType` population, price recalculation, PATCH application, transaction management
- **CSV Test Data Fixture** — column count mismatch causing `ArrayIndexOutOfBoundsException` in TC16–TC20 two-product flows
- **Test Step Definitions** — path parameter wiring for `agencyPrisaId`/`uuid` (TC24, TC29)
- **MH–Agency Prisa Integration** — basket-ID synchronisation drift (TC35)

---

## Recommended Fix

- **discountType null:** Investigate the CASS/B2A order sync service for the condition that sets `discountType`; verify the assignment is triggered for all change-event types (size, placement, date, product, magazine).
- **CSV index out of bounds:** Inspect TC16–TC20 CSV fixture — must have ≥14 columns (indices 0–13); update to match the current CASS export schema. Also check TC29 for the same issue.
- **Path parameter wiring:** Fix the Cucumber step definitions for TC24 and TC29 so `agencyPrisaId` and `uuid` resolve to the correct parameters.
- **Array ordering:** Replace strict-ordered assertions on `packageId`/`productId`/`paCode`/`placementId` with order-agnostic matchers (e.g. `containsInAnyOrder`).

---

## Prevention

- Add a schema-validation pre-check for CSV test fixtures to detect column-count drift before test execution.
- Add an integration-level smoke test asserting `discountType` is non-null for at least one representative B2A order after each deployment.
- Use order-agnostic collection matchers for all multi-element array assertions where API element ordering is not contractually guaranteed.
