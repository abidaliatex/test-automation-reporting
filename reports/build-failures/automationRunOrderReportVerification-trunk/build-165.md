# Build Failure Report

## Build Summary

Build: [165](https://crossadv.atex.com/jenkins/job/automationRunOrderReportVerification-trunk/165/)  
Date: 2026-11-17 01:36:46 UTC  
Status: UNSTABLE  
Total Tests: 108  
Passed: 100  
Failed: 8  
Pass Rate: 92.6%

---

## Root Cause Groups

## Order report data differs from expected

**Affected Features:**
- `createorder.feature`

**Affected Scenarios:**
- The Jenkins results expose the failing step, `User verify generated report data "Order Data"` (`createorder.feature:2537`), but not scenario titles or TC identifiers. Five failures occurred at this step.

**Failure Pattern:** Generated order report values do not match expected values.

**Evidence:**
- Expected net `7,905.60`, found `7,115.04`.
- Expected net `103.00`, found `102.00` (twice); expected net `73.00`, found `71.00`.
- Expected customer `Autotest Customer2`, found `Atex`.

**Impact:** 5 failures  
**Confidence:** High

## Order-number filter returns unexpected rows

**Affected Features:**
- `printstockoforders.feature`

**Affected Scenarios:**
- The Jenkins results expose the failing step, `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`), but not scenario titles or TC identifiers. Two failures occurred at this step.

**Failure Pattern:** The test expected no matching order numbers, but received rows.

**Evidence:**
- Expected `[]`, found `[926332]`.
- Expected `[]`, found `[90000353]`.

**Impact:** 2 failures  
**Confidence:** High

## Net column is not visible for sorting

**Affected Features:**
- `stockOfOrdersCorrCode.feature`

**Affected Scenarios:**
- The Jenkins result identifies the failing step as `User verify generated report data "Order Data"` (`stockOfOrdersCorrCode.feature:24`); it does not expose the scenario title or TC identifier.

**Failure Pattern:** The test timed out waiting for the `Net` column header.

**Evidence:**
- Selenium timed out after 10 seconds waiting for the `Net` header element.

**Impact:** 1 failure  
**Confidence:** High
