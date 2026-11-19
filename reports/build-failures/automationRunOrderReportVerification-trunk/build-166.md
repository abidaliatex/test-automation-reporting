## Build Summary

Build: 166 — [Jenkins build](https://crossadv.atex.com/jenkins/job/automationRunOrderReportVerification-trunk/166/)  
Date: 2026-11-19 00:11:23 UTC  
Status: UNSTABLE  
Total Tests: 108  
Passed: 102  
Failed: 6  
Pass Rate: 94.44%

---

## Root Cause Groups

Jenkins identifies the failing test steps and feature locations, but does not provide scenario titles or TC identifiers. Affected test cases are listed by their recorded step names.

## Generated Order Data Mismatch

**Affected Features:**
- `createorder.feature`

**Affected Scenarios:**
- `User verify generated report data "Order Data"` (`createorder.feature:2537`) — expected 7,905.60, found 7,115.04
- `User verify generated report data "Order Data"` (`createorder.feature:2537`) — expected 103.00, found 102.00 (2 failures)

**Failure Pattern:** Generated order report values differ from expected values.

**Evidence:**
- `CommonPage.verifyData` failed while verifying the Net value: expected 7,905.60, found 7,115.04.
- The same verification failed twice with expected 103.00, found 102.00.

**Impact:** 3 failures  
**Confidence:** Medium

## Net Column Not Visible

**Affected Features:**
- `stockOfOrdersCorrCode.feature`

**Affected Scenarios:**
- `User verify generated report data "Order Data"` (`stockOfOrdersCorrCode.feature:24`)

**Failure Pattern:** Timed out after 10 seconds waiting for the Net column header.

**Evidence:**
- Selenium could not find a visible header using `//span[contains(text(),'Net')]//parent::div//parent::th`.

**Impact:** 1 failure  
**Confidence:** Medium

## Filtered Order Number Mismatch

**Affected Features:**
- `printstockoforders.feature`

**Affected Scenarios:**
- `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`) — expected empty, found 90000353
- `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`) — expected empty, found 926332

**Failure Pattern:** The filtered-order verification returned an order number when it expected no result.

**Evidence:**
- `verifyOrderNoText` failed with `expected [] but found [90000353]`.
- The same check failed with `expected [] but found [926332]`.

**Impact:** 2 failures  
**Confidence:** Medium
