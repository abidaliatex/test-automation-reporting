# Build 264 Root Cause Analysis

Source report: [build-264.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-264.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #264 finished `UNSTABLE` with 3 failed checks out of 14.
- All failures are from `rialtoB2A (CASS TC4 Change Placement)` and occur in post-placement-change retrieval validations.
- Jenkins console shows revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with message `updated api version from 87 to 88`.

## Root Cause

- The failures cluster around pricing/discount contract mismatches after the placement-change flow.
- Two failures are MediaHouse GET checks (`tc_getMHTC03`, `tc_getMHTC03a`) and one is a Rialto GET check (`tc_getIntegrationRialto05b`), all showing mismatched computed fields.
- This pattern may indicate response-contract drift after the API version bump or stale expected fixtures.

## Affected Components

- MediaHouse retrieval expectations driven by `getMHB2A.csv`
- Rialto retrieval expectations driven by `getRialtoB2A.csv`
- Assertion aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Compare expected fixture values vs. real #264 payloads for `discountType`, commission, VAT, totals, status flags, and depth in the three failing scenarios.
- Align expectations if API v88 behavior is intentional; otherwise raise a regression for service-side recalculation.

## Prevention

- Add a focused contract check for placement-change pricing fields whenever API version changes.
- Include fixture review for post-change GET validations in version-upgrade PR checks.
