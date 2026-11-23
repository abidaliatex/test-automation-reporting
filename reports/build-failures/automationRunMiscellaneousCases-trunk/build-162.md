# Build Failure Report

## Build Summary

- Build: [162](https://crossadv.atex.com/jenkins/job/automationRunMiscellaneousCases-trunk/162/)
- Date: 2026-11-23 04:42:40 UTC
- Status: UNSTABLE
- Total Tests: 108
- Passed: 106
- Failed: 2
- Pass Rate: 98.1%

---

## Root Cause Groups

## Subscription order OK button unavailable

**Affected Features:**
- `subscriptionorder.feature`

**Affected Scenarios:**
- User creating a subscription order (TC unavailable)

**Failure Pattern:** Timed out waiting for the Subscription Order OK button to become clickable.

**Evidence:**
- Expected clickable element: `//button[@class='btn btn-primary ng-binding']`
- Failing step: `User click on Ok "SubscriptionOrder" page`
- Stack trace: `SubscriptionOrderPage.clickOk` at feature line 467

**Impact:** 1 failure

**Confidence:** Medium

## Subscription order EAN not visible

**Affected Features:**
- `subscriptionorder.feature`

**Affected Scenarios:**
- User creating a subscription order (TC unavailable)

**Failure Pattern:** Timed out waiting for EAN `5798007304591` to become visible.

**Evidence:**
- Selenium waited 10 seconds for `//span[contains(text(),'5798007304591')]`
- Failing step: `User verify EAN number through DB "query"`
- Stack trace: `SubscriptionOrderPage.verifyEANNumber` at feature line 342

**Impact:** 1 failure

**Confidence:** Medium
