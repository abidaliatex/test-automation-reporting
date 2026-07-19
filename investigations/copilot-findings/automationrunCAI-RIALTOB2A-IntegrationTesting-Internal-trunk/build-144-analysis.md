# Root Cause Analysis — Build 144

**Source Report:** [build-144.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-144.md)

---

## Summary

Build 144 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, 2026-07-19) is UNSTABLE with **88 failures out of 513 tests (82.8% pass rate)**. Failure count increased by 2 from build #143 (86). Six root cause groups are identified below; the discountType-null cluster remains the dominant issue.

---

## Root Cause

### 1. `discountType` Not Set to `RIALTO` (34 failures — **highest impact**)
- The B2A integration layer is returning `null` instead of `RIALTO` for `orders[*].printDetails.discountType` across a wide range of scenarios (newspaper and magazine, MH-initiated and Rialto-initiated changes).
- This indicates a server-side regression in discount-type population logic, likely in the CASS/B2A order synchronisation service.
- The same failure was present in build #143 (39 failures there); the count slightly decreased but the root cause has not been addressed.

### 2. Financial Calculation Drift (16 failures)
- `discountAmount`, `commissionAmount`, `priceNet`, `priceGross`, `vat`, and `totalInclVat` diverge from test-fixture expectations across multiple scenarios.
- Several assertions also fail on `statusFlags` (expected `[PRELIMINARY]`, found `[]`), suggesting order initialisation is not completing before the GET/POST under test.
- Possibly related to root cause 1: a missing/null `discountType` may cause downstream price recalculation to produce wrong values.
- TC27/TC28 Rialto assertions fail on array-vs-scalar type (`[[3600.0]]` vs `[3600.0]`), pointing to a serialisation inconsistency in addition to the value drift.

### 3. CSV Parsing Index Out-of-Bounds → TestContext Cascade (11 failures)
- `ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` in `CSVRecord.get()` indicates the CSV file driving multi-product test data has fewer columns than the framework expects (it attempts to access column index 13 in a 13-column record, i.e. index 0–12).
- Possibly a new column was added to the CASS export and the test CSV fixture was not updated, **or** vice-versa.
- All affected scenarios are in the "2 products" family (TC16–TC20) and TC29.

### 4. Array Ordering Non-determinism (2 failures)
- `packageId`/`productId` arrays from CASS POST responses are returned in inconsistent order.
- Test assertions use strict ordered equality; the API does not guarantee element order.

### 5. Path Parameter Mapping Error (6 failures)
- `agencyPrisaId` and `uuid` are swapped or absent in CASS API calls for TC24 and TC29.
- This is a test-configuration defect in the step definition wiring for those scenarios; it also cascades into `NullPointerException` in downstream TC29 steps.

### 6. Post-Patch/Revert State Not Applied (8 failures)
- After PATCH operations, `issueDate`, `moduleCode`, and `placementId` fields retain their original values in the response.
- One TC24 revert triggers `Transaction rolled back because it has been marked as rollback-only`, pointing to a server-side constraint violation.
- TC35 fails with `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6552] does not match Agency Prisa ID [6553]` — a basket-ID drift between MH and Agency Prisa systems.

---

## Affected Components

- **CASS B2A Synchronisation Service** — discount type population (`discountType` → `RIALTO`), price calculation, PATCH application
- **CSV Test Data Fixture** — column count mismatch causing `ArrayIndexOutOfBoundsException` in multi-product flows (TC16–TC20, TC29)
- **Test Step Definition** — path parameter wiring for `agencyPrisaId`/`uuid` (TC24, TC29)
- **MH–Agency Prisa Integration** — basket ID synchronisation (TC35)

---

## Recommended Fix

- **discountType null:** Investigate the CASS/B2A order sync service for the condition that sets `discountType`; verify the discount-type assignment is triggered for all order-change event types (size, placement, date, product).
- **CSV index out of bounds:** Inspect the test CSV fixture for TC16–TC20 and TC29 to confirm it has ≥14 columns (indices 0–13); update to match the current CASS export schema.
- **Path parameter wiring:** Review the Cucumber step definitions for TC24 and TC29 to ensure `agencyPrisaId` and `uuid` are resolved correctly before the API call.
- **Array ordering:** Replace strict-ordered assertions on `packageId`/`productId` with order-agnostic matchers (e.g., `containsInAnyOrder`).
- **Financial drift:** After fixing discountType, re-run to determine how much price drift resolves; remaining delta may require fixture refresh.

---

## Prevention

- Add a schema-validation step for test CSV fixtures to detect column-count drift before test execution.
- Add an integration-level smoke test asserting `discountType` is non-null for at least one representative B2A order to catch regressions early.
- Use order-agnostic collection matchers for all multi-element array assertions where API ordering is not contractually guaranteed.
