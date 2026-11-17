## Build Summary

- **Build:** [160](https://crossadv.atex.com/jenkins/job/automationRunMiscellaneousCases-trunk/160/)
- **Date:** 2026-11-17 02:40 UTC
- **Status:** UNSTABLE
- **Total Tests:** 108
- **Passed:** 106
- **Failed:** 2
- **Pass Rate:** 98.15%

## Root Cause Groups

## Subscription-order EAN result not visible

**Affected Features:**
- `subscriptionorder.feature`

**Affected Scenarios:**
- User creating a subscription order — Jenkins `runScenario` case 33; failing step: `User verify EAN number through DB "query"` (line 342).

**Failure Pattern:**
Timed out after 10 seconds waiting for `//span[contains(text(),'5798007304591')]` to become visible.

**Evidence:**
- Jenkins test report records a `TimeoutException` for the EAN visibility wait.
- Console trace points to `subscriptionorder.feature:342`.

**Impact:** 1 failure

**Confidence:** Low — the logs confirm the expected value was not visible, but do not establish whether the cause was test data or UI state.

## Subscription-order confirmation button unavailable

**Affected Features:**
- `subscriptionorder.feature`

**Affected Scenarios:**
- User creating a subscription order — Jenkins `runScenario` case 41; failing step: `User click on Ok "SubscriptionOrder" page` (line 467).

**Failure Pattern:**
Timed out after 10 seconds waiting for `//button[@class='btn btn-primary ng-binding']` to become clickable.

**Evidence:**
- Jenkins test report records a `TimeoutException` for the confirmation-button wait.
- The console also records `expected [No Discount] but found [No discount]` in the same scenario outline.

**Impact:** 1 failure

**Confidence:** Low — the button was not clickable; the accompanying label-case mismatch may be relevant, but the logs do not establish a causal link.

Jenkins reports generic `runScenario` cases and does not provide `TCxx` identifiers; case numbers above identify the failed entries in the test report.
