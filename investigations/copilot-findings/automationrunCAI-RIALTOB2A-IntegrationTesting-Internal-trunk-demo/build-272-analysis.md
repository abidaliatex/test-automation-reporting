# Build 272 Root Cause Analysis

Source report: [build-272.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-272.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #272 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- All 3 scenarios have been failing since build #246 (`failedSince: 246`), indicating a persistent fixture drift rather than a newly introduced regression.
- Compared to build #271, the MH failures (`tc_getMHTC03`, `tc_getMHTC03a`) are identical in pattern. The Rialto failure (`tc_getIntegrationRialto05b`) has partially changed: the `placementId` mismatch seen in #271 is no longer present, but new failures on `statusFlags` (empty instead of `[PRELIMINARY]`) and a dramatically lower `commissionAmount` (620.0 vs 7750.00) have appeared, along with minor decimal format mismatches.

## Root Cause

- **MediaHouse failures (`tc_getMHTC03`, `tc_getMHTC03a`):** `discountType` is returned in the wrong state at each check — `null` before placement change (expected `RIALTO`) and `RIALTO` after change (expected `NONE`). This inversion suggests the discount is being applied at the wrong point in the placement lifecycle. All pricing fields (VAT, commission, basket totals) diverge from fixture expectations as a result.
- **Rialto failure (`tc_getIntegrationRialto05b`):** The order retrieved from Rialto after the placement change shows `statusFlags: []` instead of `[PRELIMINARY]`, indicating the order has not returned to the expected preliminary state after the MH placement change. `commissionAmount` is 620.0 instead of 7750.00 — a 92% reduction — which causes `priceNet` to drop by exactly 620 (250000 − 620 = 249380). The `depth` mismatch (372 vs 184) persists from prior builds. The decimal formatting discrepancies (`250000.0` vs `250000.00`) are a minor fixture serialisation issue.

## Affected Components

- MediaHouse basket order retrieval validation (`MediaHouse\getMHB2A.csv`) — test cases `tc_getMHTC03`, `tc_getMHTC03a`.
- Rialto order retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) — test case `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Investigate why `statusFlags` is empty after the MH placement change — the placement-change write path may not be re-setting the Rialto order to `PRELIMINARY` state.
- Confirm whether the commission rate applied to the changed order is intentionally 620.0 or whether the commission calculation is picking up a stale/wrong rate after placement update.
- If the service behaviour is intentionally different, update `getRialtoB2A.csv` and `getMHB2A.csv` fixture values to match the current API output, and align the `discountType` expectations with the actual discount application ordering.
- Fix decimal serialisation in fixtures to use consistent two-decimal format (`250000.00`) to avoid false positives.

## Prevention

- Add a contract assertion on `statusFlags` and `commissionAmount` to the placement-change smoke suite so regressions surface at deploy time.
- Gate fixture CSV updates behind a PR review that includes the relevant service team, to ensure expected values reflect intentional API contract rather than accidental drift.
