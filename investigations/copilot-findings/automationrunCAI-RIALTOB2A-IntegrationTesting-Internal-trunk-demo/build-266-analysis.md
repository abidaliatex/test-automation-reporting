# Build 266 Root Cause Analysis

Source report: [build-266.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-266.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #266 finished `UNSTABLE` with 3 failed checks out of 14.
- All failures belong to `rialtoB2A (CASS TC4 Change Placement)` and occur in post-change retrieval assertions.
- The same 3 test cases have been failing continuously since build #246, indicating a persistent unresolved regression rather than a new breakage.

## Root Cause

- Failures are consistent with those seen in builds #246–#265, pointing to a regression in the placement-change pricing/discount flow that has not been resolved.
- Two MediaHouse GET assertions (`tc_getMHTC03`, `tc_getMHTC03a`) fail on `discountType`, commission, VAT, and order total values.
- One Rialto GET assertion (`tc_getIntegrationRialto05b`) fails on `statusFlags`, `depth`, commission, and price fields after placement update.
- All mismatches suggest the backend service is returning different pricing semantics than the test data files expect, possibly introduced by an API version bump.

## Affected Components

- MediaHouse retrieval checks driven by `getMHB2A.csv`
- Rialto retrieval checks driven by `getRialtoB2A.csv`
- Shared soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Determine whether the discrepancy is a service-side regression or outdated test fixtures, and act accordingly.
- If the service behaviour changed (e.g. due to an API version bump), update the expected values in the CSV test-data files to match current responses.
- If it is a service-side bug, raise a defect against the placement-change pricing calculation in the backend.

## Prevention

- Add a changelog review gate for placement-change pricing fields when API version is bumped.
- Consider adding contract assertions in a lower-cost smoke suite so regressions are caught before the full integration run accumulates repeated failures across builds.
