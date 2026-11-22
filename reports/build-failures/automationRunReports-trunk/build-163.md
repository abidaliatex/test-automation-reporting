# Build Failure Report

## Build Summary

Build: [163](https://crossadv.atex.com/jenkins/job/automationRunReports-trunk/163/) | Date: 2026-11-22 21:41:19 UTC | Status: UNSTABLE
Total Tests: 53 | Passed: 51 | Failed: 2 | Pass Rate: 96.2%

**Failing Tests / Steps:**
- `report_offer.feature`: `User verify generated data for offer "verify Data"` (TC not exposed in Jenkins results).
- `reports_stockoforders.feature`: `User Save created filter as "Filter Name"` (TC: tc_pfa01).

---

## Root Cause Groups

## Offer report data mismatch

**Affected Features:**
- `report_offer.feature`

**Affected Scenarios:**
- `User verifying offer reports` (TC not exposed)

**Failure Pattern:**
The offer report returned `Anne Jensen (dkanne)` where `Ebba Andersson (swebba)` was expected.

**Evidence:**
- Assertion from `Reports_OffersPage.verifyData` failed in `Reports_OffersPage.java:91`.
- Jenkins logs show the mismatch at `report_offer.feature:70`.

**Impact:** 1 failure

**Confidence:** High

## Stock Orders filter dialog timeout

**Affected Features:**
- `reports_stockoforders.feature`

**Affected Scenarios:**
- `Perform Filter Actions for Stock of Order` (tc_pfa01)

**Failure Pattern:**
Selenium waited 10 seconds for the dialog OK button but it did not become clickable while saving the created filter.

**Evidence:**
- `TimeoutException` from `Reports_Orders_StockOfOrdersPage.setFiltername` (`Reports_Orders_StockOfOrdersPage.java:656`).
- Jenkins logs show the timeout at `reports_stockoforders.feature:23`.

**Impact:** 1 failure

**Confidence:** Medium
