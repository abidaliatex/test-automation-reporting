# Build Failure Report

## Build Summary

Build: [190](https://crossadv.atex.com/jenkins/job/automationrunCAI-trunk/190/)  
Date: 2026-11-13 14:17:59 UTC | Status: UNSTABLE  
Total Tests: 199 | Passed: 184 | Failed: 15 | Pass Rate: 92.5%

---

## Root Cause Groups

Jenkins provides suite labels, not feature filenames; labels are shown below.

## Missing adspace for variant 3
**Affected Features:** ADAPTERS APIs; MC ORDER APIs
**Affected Scenarios:**
- Create new order(for adapter) - ONLINE - MC - POST (tc_mc_ord_post_05)
- Create new order - ONLINE - MC - POST (tc_mc_ord_post_03)
**Failure Pattern:** Order POST validation cannot find an adspace for variant 3.
**Evidence:** `error.ws.caivalidation.non.existing.adspace.for.variant`: no adspace found for variant `3`.
**Impact:** 2 failures  
**Confidence:** High

## Adapter GET failures
**Affected Features:** ADAPTERS APIs
**Affected Scenarios:**
- get mapped data about an order-line - ADAPTER - GET - success (tc_getadapters02)
- get info about mapped adspaces - ADAPTER - GET - success (tc_getadapters05)
**Failure Pattern:** HTTP 400 instead of 200; separate mapped-adspaces `NullPointerException`.
**Evidence:** `expected [N200] but found [N400]`; NPE at `WSAdaptersServiceImpl.getInfoAboutMappedAdspaces:255`.
**Impact:** 2 failures  
**Confidence:** High

## BASE reference and version mismatches
**Affected Features:** BASE APIs
**Affected Scenarios:**
- get all non-expired production-flows for print - BASE - GET - success (tc_getbase10)
- get information about database-version - BASE - GET - success (tc_getbase22)
**Failure Pattern:** Returned production-flow data and database version differ from expectations.
**Evidence:** Expected `[100, FM, PROD]`, found `[100, FM, PROD, PROD2]`; expected `8.8`, found `8.9`.
**Impact:** 2 failures  
**Confidence:** Medium

## Unexpected customer activity results
**Affected Features:** CUSTOMER APIs
**Affected Scenarios:**
- Get customer information objects - salesman and legal person combination - success (tc_cust29)
- Get customer activities - success (tc_cust24)
- Get salesman activities - success (tc_cust25)
**Failure Pattern:** Responses contain more results or IDs than expected.
**Evidence:** Expected 2 results, found 4; expected activity ID lists omit IDs present in actual responses.
**Impact:** 3 failures  
**Confidence:** Medium

## DWL response content mismatches
**Affected Features:** DWL APIs
**Affected Scenarios:**
- get Netsale rows - DWL - GET - success (tc_getdwl01)
- get Online rows - DWL - GET - success (tc_getdwl02)
**Failure Pattern:** Returned rows differ from expectations, including a missing expected row.
**Evidence:** First expected response row differs; expected order IDs include `906588`, which is absent from the returned list.
**Impact:** 2 failures  
**Confidence:** Medium

## MC order PATCH rejects zero order number
**Affected Features:** MC ORDER APIs
**Affected Scenarios:**
- Update order - ONLINE - MC - PATCH (tc_mc_ord_patch_09)
**Failure Pattern:** PATCH request is rejected because `ono` is zero.
**Evidence:** `error.valuevalidation.named.value.must.not.be.null.or.zero`; found `ono=0`.
**Impact:** 1 failure  
**Confidence:** High

## Print order POST lazy initialization error
**Affected Features:** PRINT ORDER APIs
**Affected Scenarios:**
- create new order - print - success (tc_print_ord_post_01)
- create new order with orTypeofsplit - print - success (tc_print_ord_post_07)
- create new order without orTypeofsplit - print - success (tc_print_ord_post_08)
**Failure Pattern:** Order creation cannot access service-fee prices after the persistence session closes.
**Evidence:** `FServicefee.FServprices, could not initialize proxy - no Session`.
**Impact:** 3 failures  
**Confidence:** High
