# Build 277 Root Cause Analysis

Source report: [build-277.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-277.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #277 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failures remain in `rialtoB2A (CASS TC4 Change Placement)` during the post-placement retrieval checks.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.
- Each failing scenario still reports `failedSince: 246`, so this is a continuing drift/regression rather than a new failure signature.

## Root Cause

- **MediaHouse retrieval drift:** `tc_getMHTC03` and `tc_getMHTC03a` still return discount and pricing values that do not match `MediaHouse\getMHB2A.csv`. The response shows `discountType=null` before the change and `discountType=RIALTO` after the change instead of the expected `RIALTO`/`NONE`, with commission, VAT, and total values moving with that drift.
- **Rialto post-update drift:** `tc_getIntegrationRialto05b` still returns the same altered post-update state seen in recent builds: empty `orderHeader.statusFlags`, `depth=372` instead of `184`, and `commissionAmount=620.0` instead of `7750.00`. That points to either stale fixture expectations for API v88 or a placement-change persistence/output regression in the service response.

## Affected Components

- MediaHouse retrieval validation in `MediaHouse\getMHB2A.csv` for `tc_getMHTC03` and `tc_getMHTC03a`.
- Rialto retrieval validation in `Rialto\RialtoB2A\getRialtoB2A.csv` for `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Confirm whether API v88 intentionally changed post-placement discount, commission, and status behavior; if yes, update the affected MediaHouse and Rialto fixture rows to the new contract values.
- If the API version bump was not meant to change this flow, compare the placement-change response against the last passing API version and restore the expected `statusFlags`, `depth`, `commission`, VAT, and total outputs.

## Prevention

- Run a focused regression check for `rialtoB2A(CASS)TestCase4.feature` whenever the base URI version changes.
- Review fixture updates together with API-version bumps so long-running `failedSince` failures are resolved before they persist across builds.
