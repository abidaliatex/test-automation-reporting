# Build 135 Root Cause Analysis

Source report: [build-135.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-135.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #135 finished `UNSTABLE` with 86 failures out of 513 tests (83.2% pass rate).
- The build checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (`updated api version from 87 to 88`) and ran against `api/880/v1` — the same revision and API version as build #134.
- The failure count (86) and pass rate (83.2%) are identical to build #134, indicating no regression or recovery between the two runs; all failures are pre-existing.
- Failures cluster into six repeatable patterns: `discountType=null` pricing drift, missing `PRELIMINARY` status flag, two-product MH index error with TestContext cascade, array ordering mismatches, malformed path parameters, and residual magazine pricing/identity mismatches.

## Root Cause

- **Primary pattern (35 failures):** MH basket responses return `discountType=null` where `RIALTO` is expected, driving downstream incorrect `orderDiscount`, `sumDiscount`, `netPrice`, `vat`, and `totalInclVat` values. Affects both newspaper and magazine scenarios across 20 feature files.
- **PRELIMINARY flag absent (5 failures):** `orderHeader.statusFlags` is returned empty instead of `[PRELIMINARY]` during POST/creation steps. Commission amounts also deviate on the same calls, suggesting a pricing calculation is skipped when the flag is absent.
- **Two-product MH index error + cascade (15 failures):** TC16–TC20 all fail with `Index 13 out of bounds for length 13` in the GET step. This prevents `odIds` from being stored in `TestContext`, causing all subsequent patch steps to fail immediately with `No MH odIds found in TestContext`.
- **Array ordering / state drift (7 failures):** Multi-product scenarios return `paCode`, `plaCode`, `packageId`, `placementId`, and `issueDate` arrays in a different order than fixtures expect. Revert steps in TC23/TC24 also do not restore the original state.
- **Request construction errors (4 failures):** TC24 and TC29 have swapped or missing Rialto path parameters (`uuid` / `agencyPrisaId`). TC23 revert triggers a server-side HTTP 500 rollback-only error.
- **Residual pricing/identity mismatches (15 failures):** A mixed group of post-change validations with commission, priceNet, or totalInclVat drift not caused by `discountType=null`; TC35 shows an MH basket ID vs Agency Prisa ID correlation failure; TC27/TC28 have assertion format errors (nested list `[[v]]` vs scalar `[v]`).

## Affected Components

- MediaHouse basket-order GET validations — newspaper and magazine scenarios
- Rialto follow-up GET validations after date/size/placement changes
- MH patch-step payload construction and path-parameter routing
- Shared `TestContext` hand-off for two-product MH `odIds`

## Recommended Fix

- Investigate why `discountType` is returning `null` for RIALTO-discounted orders and why `PRELIMINARY` is not set; both may relate to the API v87→v88 upgrade.
- Fix the two-product array indexing bug (`Index 13 out of bounds for length 13`) to unblock the 10 downstream patch-step failures.
- Correct the swapped/undefined path parameters in TC24 and TC29 Rialto follow-up steps.
- Review whether array-ordering assertions need order-independent matching for `paCode`, `packageId`, and `issueDate` arrays.
- Fix assertion fixtures in TC27/TC28 that compare nested lists against scalar values.

## Prevention

- Add a post-upgrade smoke check that validates `discountType` and `statusFlags` on a sample MH basket immediately after any API version change.
- Fail fast on missing `odIds` in `TestContext` to block downstream patch steps and surface them as "blocked" rather than independent failures.
- Consider order-independent matchers for array fields where server ordering is not contractually defined.
