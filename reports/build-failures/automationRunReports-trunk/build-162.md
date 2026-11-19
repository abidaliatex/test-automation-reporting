# Build Failure Report

## Build Summary

Build: [162](https://crossadv.atex.com/jenkins/job/automationRunReports-trunk/162/) | Date: 2026-11-18 18:21:47 UTC | Status: UNSTABLE  
Total Tests: 53 | Passed: 51 | Failed: 2 | Pass Rate: 96.2%

**Failing Tests / Steps:**
- `report_offer.feature`: `User verify generated data for offer "verify Data"` (test case ID not exposed in Jenkins results).
- `reports_stockoforders.feature`: `User Save created filter as "Filter Name"` (test case ID not exposed in Jenkins results).

---

## Root Cause Groups

## Offer report data mismatch

**Affected Features:**
- `report_offer.feature`

**Affected Scenarios:**
- Scenario name and test case ID are not exposed; failing step: `User verify generated data for offer "verify Data"`.

**Failure Pattern:** The generated report's user value did not match the expected value.

**Evidence:**
- Assertion failed in `Reports_OffersPage.verifyData` (`Reports_OffersPage.java:91`); personal values omitted.

**Impact:** 1 failure

**Confidence:** High

## Stock Orders filter save timeout

**Affected Features:**
- `reports_stockoforders.feature`

**Affected Scenarios:**
- Scenario name and test case ID are not exposed; failing step: `User Save created filter as "Filter Name"`.

**Failure Pattern:** Selenium timed out after 10 seconds waiting for the dialog's OK button to become clickable while saving the filter as CSV.

**Evidence:**
- The wait failed on the OK-button locator in `Reports_Orders_StockOfOrdersPage.setFiltername` (`Reports_Orders_StockOfOrdersPage.java:656`).

**Impact:** 1 failure

**Confidence:** Medium
