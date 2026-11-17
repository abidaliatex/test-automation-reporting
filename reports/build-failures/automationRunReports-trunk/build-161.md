# Build Failure Report

## Build Summary

Build: [161](https://crossadv.atex.com/jenkins/job/automationRunReports-trunk/161/) | Date: 2026-11-16 19:24:19 UTC | Status: UNSTABLE  
Total Tests: 53 | Passed: 51 | Failed: 2 | Pass Rate: 96.2%

---

## Root Cause Groups

## Stock Orders filter save timeout

**Affected Features:**
- `reports_stockoforders.feature`

**Affected Scenarios:**
- Save created filter as "Filter Name" (test case ID not exposed in Jenkins results)

**Failure Pattern:** Selenium timed out waiting for the dialog's OK button to become clickable while saving the filter as CSV.

**Evidence:**
- Waited 10 seconds for `//span[contains(text(),'OK')]//parent::msg//parent::button`.
- Stack trace points to `Reports_Orders_StockOfOrdersPage.setFiltername`.

**Impact:** 1 failure

**Confidence:** Medium

## Offer report data mismatch

**Affected Features:**
- `report_offer.feature`

**Affected Scenarios:**
- User verifying offer reports (`tc_offer01`)

**Failure Pattern:** Generated report data did not match the expected user value.

**Evidence:**
- `Reports_OffersPage.verifyData` failed: expected user value differed from the returned user value. Names are omitted.

**Impact:** 1 failure

**Confidence:** High
