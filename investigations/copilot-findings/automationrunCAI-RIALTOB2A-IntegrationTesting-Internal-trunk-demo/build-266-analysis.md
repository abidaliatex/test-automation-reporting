# Build 266 Root Cause Analysis

Source report: [build-266.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-266.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #266 finished `UNSTABLE` with 3 failed tests out of 14.
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur in post-change retrieval assertions.
- The same 3 tests have been failing since build #246 (`failedSince: 246`), confirming a persistent unresolved regression.

## Root Cause

- **MH discountType / pricing drift:** After the CASS TC4 placement-change flow, the MediaHouse B2A integration returns `discountType: null` on initial order arrival (expected `RIALTO`) and retains `RIALTO` after the placement change (expected `NONE`). The resulting VAT and total values are also wrong, consistent with the discount not being applied correctly.
- **Rialto order not fully updated after placement patch:** After the MH PATCH request to change the placement, Rialto does not reflect the updated depth (`372` instead of `184`), commission (`620.0` instead of `7750.00`), or status flag (`[]` instead of `[PRELIMINARY]`). This possibly indicates the placement-change event is not being consumed and processed correctly on the Rialto side.
- Both root causes involve the same end-to-end placement-change flow and may share a single upstream cause in the B2A integration event handling.

## Affected Components

- MediaHouse order retrieval — `getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto order retrieval — `getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)
- Soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown` (ApiStepDefinition.java:69)

## Recommended Fix

- Verify whether the B2A integration correctly propagates and clears `discountType` during the placement-change flow.
- Check that Rialto processes the placement-change event and recalculates depth, commission, and status flags accordingly.
- If runtime behaviour is now correct, update the test CSV fixtures with the actual expected values.

## Prevention

- Add a contract check on `discountType`, commission, VAT, and depth whenever a placement-change flow is triggered.
- Treat a `failedSince` count exceeding 10 builds as a priority alert to prevent silent, long-running regressions.
