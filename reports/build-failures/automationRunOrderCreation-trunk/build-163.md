# Build Failure Report

## Build Summary

Build: [163](https://crossadv.atex.com/jenkins/job/automationRunOrderCreation-trunk/163/)  
Date: 2026-11-22 21:53:58 UTC  
Status: UNSTABLE  
Total Tests: 282  
Passed: 241  
Failed: 41  
Pass Rate: 85.5%

---

## Root Cause Groups

## Material editor control not visible
**Affected Features:** `createorder.feature`  
**Affected Scenarios:** User Creates new print order (`tc_cno50`, `tc_cno52`, `tc_cno53`, `tc_cno54`, `tc_cno56`, `tc_cno58`, `tc_cno60`, `tc_cno66`, `tc_cno69`, `tc_cno70`, `tc_cno72`, `tc_cno74`)  
**Failure Pattern:** Material accordion button visibility wait timed out in all 12 cases.  
**Evidence:** Selenium waited for the same material accordion button in each case.  
**Impact:** 12 failures | **Confidence:** High

## Job Notes edit button not visible
**Affected Features:** `jobNotes.feature`  
**Affected Scenarios:** User Testing Job Notes (`tc_jobNotes01`, `tc_jobNotes03`, `tc_jobNotes04`, `tc_jobNotes05`, `tc_jobNotes06`)  
**Failure Pattern:** Timed out waiting for the `js-sc-editOrder` button.  
**Evidence:** Jenkins reports the same visibility wait failure in all five cases.  
**Impact:** 5 failures | **Confidence:** High

## Job Notes value missing from search results
**Affected Features:** `jobNotes.feature`  
**Affected Scenarios:** User Testing Job Notes (`tc_jobNotes02`, `tc_jobNotes07`, `tc_jobNotes08`, `tc_jobNotes09`)  
**Failure Pattern:** Expected `Automation` but received an empty value.  
**Evidence:** Four assertions returned `expected [Automation] but found []`.  
**Impact:** 4 failures | **Confidence:** High

## Online Job Notes input file unavailable
**Affected Features:** `onlineJobNotes.feature`  
**Affected Scenarios:** User Testing Online Job Notes (`tc_jobNotes01`–`tc_jobNotes06`)  
**Failure Pattern:** `onlinejobNotes.csv` was not found.  
**Evidence:** The same missing-file path was reported in all six cases.  
**Impact:** 6 failures | **Confidence:** High

## Order save click intercepted
**Affected Features:** `toporder.feature`  
**Affected Scenarios:** User Creates new order (`tc_topord02`, `tc_topord03`, `tc_topord04`, `tc_topord05`, `tc_topord06`)  
**Failure Pattern:** Another element intercepted the save-button click.  
**Evidence:** Selenium reports another element would receive the click in each case.  
**Impact:** 5 failures | **Confidence:** High

## Revised-order action not visible
**Affected Features:** `revisedOrder.feature`  
**Affected Scenarios:** User Creates new online order (`tc_revonline02`, `tc_revonline03`)  
**Failure Pattern:** The “Revise” control visibility wait timed out in both cases.  
**Evidence:** Both failures use the same selector wait.  
**Impact:** 2 failures | **Confidence:** High

## Sales Forecast order not found
**Affected Features:** `salesForecast.feature`  
**Affected Scenarios:** Create order for -Order with amount less than Sales Forecast (`tc_sf_order01`); Verify order within forecast amount links and saves normally (`tc_sf03`)  
**Failure Pattern:** The order with invoice text `SF_LessAmount` was not found in Recent Orders.  
**Evidence:** The missing-order assertion failed in both cases.  
**Impact:** 2 failures | **Confidence:** High

## Undefined test steps
**Affected Features:** `minmaxplacementcol.feature`, `salesForecast.feature`  
**Affected Scenarios:** User updated placement codes for automation execution (`tc_minplacol01`); Verify cumulative order amounts trigger info message on Sales Forecast (`tc_sf04`)  
**Failure Pattern:** The database max-value update and opening a Sales Forecast steps are undefined.  
**Evidence:** Cucumber generated implementation stubs for both steps.  
**Impact:** 2 failures | **Confidence:** High

## Duplicate-module save button not clickable
**Affected Features:** `duplicateOrders.feature`  
**Affected Scenarios:** User Creates Module (`tc_cno01`)  
**Failure Pattern:** The save-button clickable wait timed out after 10 seconds.  
**Evidence:** Jenkins reports a timeout waiting for `//button[@id='save']`.  
**Impact:** 1 failure | **Confidence:** High

## Commission order query returned no rows
**Affected Features:** `commissionorders.feature`  
**Affected Scenarios:** User creates new online order for verifying commision (`tc_commord01`)  
**Failure Pattern:** The query returned “Result set after last row.”  
**Evidence:** Jenkins reports an empty result set.  
**Impact:** 1 failure | **Confidence:** High

## Online job type control not visible
**Affected Features:** `onlineJob.feature`  
**Affected Scenarios:** User verify online jobs (`tc_onlinejobtype01`)  
**Failure Pattern:** The `changeJobType` control visibility wait timed out.  
**Evidence:** Jenkins reports a visibility wait failure for the selector.  
**Impact:** 1 failure | **Confidence:** High
