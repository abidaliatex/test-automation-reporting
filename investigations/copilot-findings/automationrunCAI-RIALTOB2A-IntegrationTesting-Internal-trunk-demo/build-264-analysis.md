# Build 264 Root Cause Analysis

Source report: [build-264.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-264.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #264 completed `UNSTABLE` with 3 failed checks out of 14.
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-update retrieval assertions.
- Build checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd`.

## Root Cause

- Two failures are on MediaHouse GET checks and one on Rialto GET checks, all in the same placement-change flow.
- The shared mismatch pattern is discount/commission/VAT/total recalculation differences plus status/depth differences after the update.
- This indicates likely contract drift between expected test fixtures and runtime API responses for placement-change scenarios.

## Affected Components

- MediaHouse retrieval checks backed by `getMHB2A.csv`
- Rialto retrieval checks backed by `getRialtoB2A.csv`
- Soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Compare expected values in `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b` against build #264 payloads.
- Confirm whether API v88 changed placement-change pricing/discount behavior and update either service logic or expected fixtures accordingly.

## Prevention

- Add a focused post-placement-update contract check covering `discountType`, commission, VAT, totals, and depth.
- Include a fixture review for placement-change retrieval assertions when API version changes.
