# Root Cause Analysis — Build 145

**Source Report:** [build-145.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-145.md)

---

## Summary

Build 145 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, 2026-07-20 21:03 UTC) is UNSTABLE with **88 failures out of 513 tests (82.8% pass rate)**. The failure count is identical to build #144 (88 failures) — no regression fixes have landed. All six root cause groups identified in build #144 persist unchanged.

---

## Root Cause

### 1. `discountType` Not Set to `RIALTO` (31 failures — **highest impact**)
- The B2A/CASS integration service returns `null` instead of `RIALTO` for `orders[*].printDetails.discountType` across newspaper and magazine scenarios, both MH-initiated and Rialto-initiated changes.
- Affects 21 feature files spanning TC1&2 through TC36.
- The null discount type causes basket-level financial fields (`orderDiscount`, `sumDiscount`, `netPrice`) to be miscalculated in the same response, producing secondary assertion failures.
- Present and unresolved since at least build #143.

### 2. Financial Calculation Drift (22 failures)
- `discountAmount`, `commissionAmount`, `priceNet`, `priceGross`, `vat`, and `totalInclVat` diverge from test-fixture expectations across POST and GET steps.
- `statusFlags` returns `[[]]` instead of `[[PRELIMINARY]]` for TC1&2, TC3, TC4, TC5, TC6, suggesting order initialisation is not completing.
- TC6 POST appears as a new failure in build 145 (not present in build 144), indicating the scope of financial drift is widening.
- TC27 and TC28 Rialto assertions additionally fail on array-vs-scalar serialisation: `discountAmount` expected `[[3600.0]]` found `[3600.0]`.
- Possibly downstream of root cause 1: missing `discountType` triggers incorrect price recalculation.

### 3. CSV Parsing Index Out-of-Bounds → TestContext Cascade (10 failures)
- `ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` at `CSVRecord.get()` indicates the CSV test-data fixture for two-product scenarios (TC16–TC20) attempts to access column index 13 in a 13-column record (indices 0–12).
- The GET step fails before `odIds` are written to TestContext; the downstream POST step then errors with `No MH odIds found in TestContext`.
- Unchanged from build #144 — the CSV fixture has not been corrected.

### 4. Array Ordering Non-determinism (7 failures)
- `packageId`, `productId`, `paCode`, `plaCode`, and `prodCode` arrays from CASS POST/GET responses return in non-deterministic order.
- Strict ordered-equality assertions fail across TC15, TC19, TC22, TC24, and TC37.
- The ordering issue for TC22 also causes the revert-state GET step to fail independently.

### 5. Path Parameter Mapping Error — TC24 and TC29 (6 failures)
- For TC24 the `uuid` path parameter is missing while `agencyPrisaId` is passed redundantly.
- For TC29 the parameters are reversed: `uuid` is supplied where `agencyPrisaId` is expected.
- The TC29 Rialto step fails first, causing all four downstream MH/Rialto steps to produce null or missing-odId errors.
- Both defects are in test step-definition wiring; unchanged from build #144.

### 6. Post-Patch State Not Applied and Transaction Rollback (10 failures)
- TC16, TC17, TC18, TC20: after PATCH, `issueDate`, `moduleCode`, and `placementId` retain original values, possibly because the CSV index error (root cause 3) causes the wrong `odId` to be patched.
- TC22 and TC24: a `PATCH` triggers `Transaction rolled back because it has been marked as rollback-only (500)`, indicating a server-side constraint violation.
- TC27: `issueDate` in the MH update step returns `2026-08-26` instead of the expected `2026-08-19`, suggesting a test-data date drift.
- TC35: `placementId` expected `[[SIDAN2]]` found `[[HALVLIGG]]`; basket-ID synchronisation drift `[6590]` vs `[6591]` between MH and Agency Prisa.

---

## Affected Components

- **CASS B2A Synchronisation Service** — `discountType` population, price recalculation, PATCH application, transaction management
- **CSV Test Data Fixture** — column count mismatch causing `ArrayIndexOutOfBoundsException` in TC16–TC20 two-product flows
- **Test Step Definitions** — path parameter wiring for `agencyPrisaId`/`uuid` (TC24, TC29)
- **MH–Agency Prisa Integration** — basket-ID synchronisation drift (TC35)

---

## Recommended Fix

- **discountType null:** Investigate the CASS/B2A order sync service for the condition that sets `discountType`; verify the assignment is triggered for all change-event types (size, placement, date, product, magazine).
- **CSV index out of bounds:** Inspect TC16–TC20 CSV fixture — it must have ≥14 columns (indices 0–13); update to match the current CASS export schema.
- **Path parameter wiring:** Fix the Cucumber step definitions for TC24 and TC29 so `agencyPrisaId` and `uuid` resolve to the correct parameters.
- **Array ordering:** Replace strict-ordered assertions on `packageId`/`productId`/`paCode`/`plaCode` with order-agnostic matchers (e.g. `containsInAnyOrder`).
- **TC27 issueDate drift:** Refresh TC27 test-data fixture date; verify the date used in the update step matches the fixture.

---

## Prevention

- Add a schema-validation pre-check for CSV test fixtures to detect column-count drift before test execution.
- Add an integration-level smoke test asserting `discountType` is non-null for at least one representative B2A order after each deployment.
- Use order-agnostic collection matchers for all multi-element array assertions where API element ordering is not contractually guaranteed.
