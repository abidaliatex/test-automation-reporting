# Build 265 Root Cause Analysis

Source report: [build-265.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-265.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #265 completed `UNSTABLE` with 3 failed checks out of 14.
- All failed checks are in `rialtoB2A (CASS TC4 Change Placement)` and occur in post-placement-update retrieval assertions.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.

## Root Cause

- The failures likely share one contract-alignment issue after the API version update.
- MediaHouse and Rialto retrieval assertions both show consistent mismatches in financial and status-related fields after placement change.
- Repeated drift in `discountType`, commission, VAT/totals, `statusFlags`, and `depth` indicates expected fixtures may not match current response calculations.

## Affected Components

- MediaHouse retrieval validation from `MediaHouse\\getMHB2A.csv`
- Rialto retrieval validation from `Rialto\\RialtoB2A\\getRialtoB2A.csv`
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Compare expected values for `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b` against build #265 payloads.
- Confirm API v88 behavior for placement-change pricing/status fields and align fixtures or service logic accordingly.

## Prevention

- Add a focused regression check for placement-change financial/status fields during API version bumps.
- Add a fixture-review gate for high-sensitivity fields (`discountType`, commission, totals, status flags, depth) before merge.
