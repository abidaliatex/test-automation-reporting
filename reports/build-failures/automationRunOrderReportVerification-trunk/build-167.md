## Build Summary

Build: [167](https://crossadv.atex.com/jenkins/job/automationRunOrderReportVerification-trunk/167/)<br>
Date: 2026-11-23 03:35:56 UTC<br>
Status: UNSTABLE<br>
Total Tests: 108<br>
Passed: 101<br>
Failed: 7<br>
Pass Rate: 93.52%

---

## Root Cause Groups

Jenkins exposes the failing scenario-step names and feature locations, but not the associated test-case IDs. The names below are the exact failing steps reported by Jenkins.

## Generated Order Net-Value Mismatches

**Affected Features:**
- `createorder.feature`

**Affected Scenarios:**
- `User verify generated report data "Order Data"` (`createorder.feature:2537`; test-case ID not exposed)

**Failure Pattern:** The generated report's Net value differed from the expected value.

**Evidence:**
- Expected 7,905.60, found 7,115.04.
- Expected 103.00, found 102.00 (2 failures).
- Expected 73.00, found 71.00.

**Impact:** 4 failures

**Confidence:** Medium

## Filtered Order Number Mismatch

**Affected Features:**
- `printstockoforders.feature`

**Affected Scenarios:**
- `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`; test-case ID not exposed)

**Failure Pattern:** The filtered-order check expected no order number but found one.

**Evidence:**
- Expected empty, found 90000353.
- Expected empty, found 926332.

**Impact:** 2 failures

**Confidence:** Medium

## Net Column Visibility Timeout

**Affected Features:**
- `stockOfOrdersCorrCode.feature`

**Affected Scenarios:**
- `User verify generated report data "Order Data"` (`stockOfOrdersCorrCode.feature:24`; test-case ID not exposed)

**Failure Pattern:** Selenium timed out waiting for the Net column header to become visible.

**Evidence:**
- The wait for `//span[contains(text(),'Net')]//parent::div//parent::th` timed out after 10 seconds.

**Impact:** 1 failure

**Confidence:** Medium
