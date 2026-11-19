# Build Failure Report

## Build Summary

Build: [162](https://crossadv.atex.com/jenkins/job/automationRunOrderCreation-trunk/162/) | Date: 2026-11-18 18:33:40 UTC | Status: UNSTABLE  
Total Tests: 282 | Passed: 241 | Failed: 41 | Pass Rate: 85.5%

## Root Cause Groups

## Missing online job notes fixture
**Affected Features:** `onlineJobNotes.feature`  
**Affected Scenarios:** User Testing Online Job Notes (`tc_jobNotes01`–`tc_jobNotes06`)  
**Failure Pattern:** `NoSuchFileException` for `testdata/onlinejobNotes.csv`.  
**Evidence:** All six cases fail while selecting the same missing fixture.  
**Impact:** 6 failures | **Confidence:** High

## Top-order save click intercepted
**Affected Features:** `toporder.feature`  
**Affected Scenarios:** User Creates new order (case IDs not exposed).  
**Failure Pattern:** `ElementClickInterceptedException` on the save button during “Click on OK”.  
**Evidence:** `LoginPageSteps.click_on_OK`; failures reference feature lines 25 and 52.  
**Impact:** 5 failures | **Confidence:** Medium

## Material ad text control unavailable
**Affected Features:** `createorder.feature`  
**Affected Scenarios:** User Creates new print order (case IDs not exposed).  
**Failure Pattern:** 10-second wait timed out for the material accordion button while editing ad text.  
**Evidence:** `LoginPageSteps.user_edit_the_material_Ad_text`; same wait in all cases.  
**Impact:** 12 failures | **Confidence:** Medium

## Job-note edit control unavailable
**Affected Features:** `jobNotes.feature`  
**Affected Scenarios:** User Testing Job Notes (case IDs not exposed): edit print order.  
**Failure Pattern:** 10-second wait timed out for the print-order edit button.  
**Evidence:** `LoginPageSteps.user_edit_print_order`.  
**Impact:** 5 failures | **Confidence:** Medium

## Job-note values missing from order search
**Affected Features:** `jobNotes.feature`  
**Affected Scenarios:** User Testing Job Notes (case IDs not exposed): verify notes and manuscript values.  
**Failure Pattern:** Assertions expected `[Automation]` but found `[]`.  
**Evidence:** Failures occur in order-search and header verification steps.  
**Impact:** 4 failures | **Confidence:** High

## Revised-order action unavailable
**Affected Features:** `revisedOrder.feature`  
**Affected Scenarios:** User Creates new online order (case IDs not exposed): add/remove another payer.  
**Failure Pattern:** 10-second wait timed out for the “Revise” control.  
**Evidence:** `user_add_other_payer_for_revised_order` and `user_remove_other_payer_for_revised_order`.  
**Impact:** 2 failures | **Confidence:** Medium

## Sales Forecast order not found
**Affected Features:** `salesForecast.feature`  
**Affected Scenarios:** Create order for -Order with amount less than Sales Forecast; Verify order within forecast amount links and saves normally (case IDs not exposed).  
**Failure Pattern:** Recent Orders did not contain invoice text `[SF_LessAmount]`.  
**Evidence:** Both cases report the existing order was not found when adding it to Sales Forecast.  
**Impact:** 2 failures | **Confidence:** Medium

## Online job type control unavailable
**Affected Features:** `onlineJob.feature`  
**Affected Scenarios:** User verify online jobs (case ID not exposed): edit job type.  
**Failure Pattern:** 10-second wait timed out for the job-type change control.  
**Evidence:** `LoginPageSteps.user_edit_job_type`; feature line 152.  
**Impact:** 1 failure | **Confidence:** Medium

## Undefined placement-column database step
**Affected Features:** `minmaxplacementcol.feature`  
**Affected Scenarios:** Scenario name and case ID not exposed; failed step sets column max value `"UpdateMaxQuery"` through the database.  
**Failure Pattern:** Cucumber reports the step as undefined.  
**Evidence:** `UndefinedStepException` identifies the missing step binding.  
**Impact:** 1 failure | **Confidence:** High

## Customer selection database error
**Affected Features:** `commissionorders.feature`  
**Affected Scenarios:** User creates new online order for verifying commision (case ID not exposed): search and select customer.  
**Failure Pattern:** `SQLException: Result set after last row`.  
**Evidence:** Raised in `LoginPageSteps.user_search_and_select_Customer`.  
**Impact:** 1 failure | **Confidence:** Medium

## Undefined Sales Forecast step
**Affected Features:** `salesForecast.feature`  
**Affected Scenarios:** Verify cumulative order amounts trigger info message on Sales Forecast (case ID not exposed): open Sales Forecast.  
**Failure Pattern:** Cucumber reports `User opens Sales Forecast "SF Name"` as undefined.  
**Evidence:** `UndefinedStepException` references feature line 189.  
**Impact:** 1 failure | **Confidence:** High

## Duplicate-order module save timed out
**Affected Features:** `duplicateOrders.feature`  
**Affected Scenarios:** User Creates Module (case ID not exposed): save the module.  
**Failure Pattern:** 10-second wait timed out for `//button[@id='save']` to become clickable.  
**Evidence:** `LoginPageSteps.user_save_the_module`; feature line 26.  
**Impact:** 1 failure | **Confidence:** Medium
