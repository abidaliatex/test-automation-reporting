# Build 137 Root Cause Analysis

Source report: [build-137.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-137.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #137 finished `UNSTABLE` with 89 failures out of 513 tests (82.7% pass rate).
- The build checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (`updated api version from 87 to 88`) and ran against `api/880/v1` — the same revision and API version as builds #134 and #135.
- Compared to build #135 (86 failures), this build added 3 regressions (TC6, TC7, TC22 POST) while retaining all pre-existing failures, indicating a slight deterioration.
- Failures cluster into six repeatable patterns: `discountType=null` pricing drift, missing `PRELIMINARY` status flag, two-product MH index error with TestContext cascade, array ordering mismatches, path parameter / basket setup errors, and residual magazine pricing/identity mismatches.

## Root Cause

- **Primary pattern (31 failures):** MH basket responses return `discountType=null` where `RIALTO` is expected, driving downstream incorrect `orderDiscount`, `sumDiscount`, `netPrice`, `vat`, and `totalInclVat` values. Affects both newspaper and magazine scenarios across 22 feature files.
- **PRELIMINARY flag absent (4 failures):** `orderHeader.statusFlags` is returned empty instead of `[PRELIMINARY]` during POST/creation steps in TC3, TC4, TC5, TC6. Commission amounts also deviate on the same calls, suggesting a pricing calculation is skipped when the flag is absent.
- **Two-product MH index error + cascade (15 failures):** TC16–TC20 all fail with `Index 13 out of bounds for length 13` in the GET step. This prevents `odIds` from being stored in `TestContext`, causing all subsequent patch steps to fail immediately with `No MH odIds found in TestContext`.
- **Array ordering / state drift (6 failures):** Multi-product scenarios return `packageId`, `placementId`, `paCode`, `plaCode`, and `issueDate` arrays in a different order than fixtures expect. TC24 revert step also does not restore the original placementId state.
- **Path parameter and basket setup errors (12 failures):** TC1 fails with `Basket not found for campaign: TestCase01 expected [false] but found [true]`, cascading to `mhBasketOrderId` path parameter errors. TC24 and TC29 have swapped/missing Rialto path parameters (`agencyPrisaId`/`uuid`). TC23 revert triggers a server-side HTTP 500 rollback-only error.
- **Residual pricing/identity mismatches (21 failures):** Post-change validations showing commission, priceNet, and totalInclVat deviations not caused by `discountType=null`; TC27/TC28 assertion format errors (nested list `[[v]]` vs scalar `[v]`); TC27 issueDate mismatch (`2026-08-19` vs `2026-08-26`); TC35 MH basket ID vs Agency Prisa ID correlation failure.

## Affected Components

- MediaHouse basket-order GET validations — newspaper and magazine scenarios
- Rialto follow-up GET validations after date/size/placement changes
- MH patch-step payload construction and path-parameter routing
- Shared `TestContext` hand-off for two-product MH `odIds`
- TC1 test data / basket lifecycle state (basket exists when expected absent)

## Recommended Fix

- Investigate why `discountType` is returning `null` for RIALTO-discounted orders and why `PRELIMINARY` is not set; both may relate to the API v87→v88 upgrade (same revision since build #134 — confirm whether API-side behaviour changed between runs).
- Fix the two-product array indexing bug (`Index 13 out of bounds for length 13`) to unblock the 10 downstream patch-step failures in TC16–TC20.
- Correct the swapped/undefined path parameters in TC24 and TC29 Rialto follow-up steps (`agencyPrisaId` vs `uuid`).
- Resolve TC1 basket state issue — basket persists between runs; verify test teardown or data-setup step cleans up `TestCase01` basket before the scenario.
- Fix assertion fixtures in TC27/TC28 that compare nested lists against scalar values (`[[v]]` vs `[v]`).

## Prevention

- Add a post-upgrade smoke check that validates `discountType` and `statusFlags` on a sample MH basket immediately after any API version change.
- Fail fast on missing `odIds` in `TestContext` to surface array index failures as the root cause rather than generating multiple downstream failures.
- Consider order-independent matchers for array fields where server ordering is not contractually defined.
- Enforce basket teardown in TC1 to avoid state bleed between test runs.
