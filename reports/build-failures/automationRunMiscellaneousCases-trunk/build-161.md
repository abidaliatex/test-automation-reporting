# Build Failure Report

## Build Summary

- Build: [161](https://crossadv.atex.com/jenkins/job/automationRunMiscellaneousCases-trunk/161/)
- Date: 2026-11-19 01:11:35 UTC
- Status: UNSTABLE
- Total Tests: 108
- Passed: 106
- Failed: 2
Pass Rate: 98.1%

---

## Root Cause Groups

## Subscription order EAN not visible

**Affected Features:**
- `subscriptionorder.feature`

**Affected Scenarios:**
- User creating a subscription order (test case ID unavailable; feature line 349)

**Failure Pattern:** Timed out waiting for the EAN element to become visible.

**Evidence:**
- Selenium waited 10 seconds for the EAN text in `SubscriptionOrderPage.verifyEANNumber`.
- The failing step is `User verify EAN number through DB "query"` at feature line 342.

**Impact:** 1 failure

**Confidence:** Medium

## Subscription order OK button not clickable

**Affected Features:**
- `subscriptionorder.feature`

**Affected Scenarios:**
- User creating a subscription order (test case ID unavailable; feature line 475)

**Failure Pattern:** Timed out waiting for the OK button to become clickable.

**Evidence:**
- Selenium waited 10 seconds for `//button[@class='btn btn-primary ng-binding']` in `SubscriptionOrderPage.clickOk`.
- The failing step is `User click on Ok "SubscriptionOrder" page` at feature line 467.

**Impact:** 1 failure

**Confidence:** Medium
