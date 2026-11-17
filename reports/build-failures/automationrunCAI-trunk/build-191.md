# Build Failure Report

## Build Summary

Build: [191](https://crossadv.atex.com/jenkins/job/automationrunCAI-trunk/191/)  
Date: 2026-11-17 03:39:51 UTC  
Status: UNSTABLE  
Total Tests: 199  
Passed: 184  
Failed: 15  
Pass Rate: 92.5%

---

## Root Cause Groups

Jenkins provides API suite labels, not `.feature` filenames; the suite labels are shown below.

## Missing adspace for variant 3

**Affected Features:**
- ADAPTERS APIs
- MC ORDER APIs

**Affected Scenarios:**
- Create new order(for adapter) - ONLINE - MC - POST (tc_mc_ord_post_05)
- Create new order - ONLINE - MC - POST (tc_mc_ord_post_03)

**Failure Pattern:** Order POST requests expect success but return HTTP 400 because no adspace exists for variant 3.

**Evidence:**
- `error.ws.caivalidation.non.existing.adspace.for.variant`: “No adspace found for variant with id '3'.”
- Both scenarios expected HTTP 200 and received HTTP 400.

**Impact:** 2 failures  
**Confidence:** High

## Adapter GET failures

**Affected Features:**
- ADAPTERS APIs

**Affected Scenarios:**
- get mapped data about an order-line - ADAPTER - GET - success (tc_getadapters02)
- get info about mapped adspaces - ADAPTER - GET - success (tc_getadapters05)

**Failure Pattern:** Adapter GET requests return HTTP 400 or HTTP 500 instead of HTTP 200.

**Evidence:**
- `tc_getadapters02`: expected HTTP 200, received HTTP 400.
- `tc_getadapters05`: HTTP 500 with `NullPointerException` at `WSAdaptersServiceImpl.getInfoAboutMappedAdspaces:255`.

**Impact:** 2 failures  
**Confidence:** Medium

## BASE response mismatches

**Affected Features:**
- BASE APIs

**Affected Scenarios:**
- get all non-expired production-flows for print - BASE - GET - success (tc_getbase10)
- get information about database-version - BASE - GET - success (tc_getbase22)

**Failure Pattern:** Returned production-flow and database-version values differ from expected values.

**Evidence:**
- Expected production flows `[100, FM, PROD]`; actual response also contains `PROD2`.
- Expected database version `8.8`; actual response is `8.9`.

**Impact:** 2 failures  
**Confidence:** Medium

## Unexpected customer results

**Affected Features:**
- CUSTOMER APIs

**Affected Scenarios:**
- Get customer information objects - salesman and legal person combination - success (tc_cust29)
- Get customer activities - success (tc_cust24)
- Get salesman activities - success (tc_cust25)

**Failure Pattern:** Responses contain more customer or activity results than expected.

**Evidence:**
- `tc_cust29`: expected 2 results, received 4.
- `tc_cust24` and `tc_cust25`: returned activity ID lists include IDs absent from expected lists.

**Impact:** 3 failures  
**Confidence:** Medium

## DWL response mismatches

**Affected Features:**
- DWL APIs

**Affected Scenarios:**
- get Netsale rows - DWL - GET - success (tc_getdwl01)
- get Online rows - DWL - GET - success (tc_getdwl02)

**Failure Pattern:** Returned DWL rows differ from expected response data.

**Evidence:**
- `tc_getdwl01`: row for order `906191` has timestamp `2026-06-23T14:06:28`; expected `2023-08-29T12:30:19`.
- `tc_getdwl02`: expected order ID `906588`, which is absent from the returned list.

**Impact:** 2 failures  
**Confidence:** Medium

## MC order PATCH rejects zero order number

**Affected Features:**
- MC ORDER APIs

**Affected Scenarios:**
- Update order - ONLINE - MC - PATCH (tc_mc_ord_patch_09)

**Failure Pattern:** The PATCH request is rejected because `ono` is zero.

**Evidence:** `error.valuevalidation.named.value.must.not.be.null.or.zero`; expected HTTP 200, received HTTP 400.

**Impact:** 1 failure  
**Confidence:** High

## Print order POST lazy initialization error

**Affected Features:**
- PRINT ORDER APIs

**Affected Scenarios:**
- create new order - print - success (tc_print_ord_post_01)
- create new order with orTypeofsplit - print - success (tc_print_ord_post_07)
- create new order without orTypeofsplit - print - success (tc_print_ord_post_08)

**Failure Pattern:** Print order creation returns HTTP 500 when service-fee prices are accessed after the persistence session closes.

**Evidence:** `FServicefee.FServprices, could not initialize proxy - no Session` appears in all three failures.

**Impact:** 3 failures  
**Confidence:** High
