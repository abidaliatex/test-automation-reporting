# Build 193 Failure Report

## Build Summary

Build: https://crossadv.atex.com/jenkins/job/automationrunCAI-trunk/193/
Date: 2026-11-23
Status: UNSTABLE
Total Tests: 260
Passed: 244
Failed: 16
Pass Rate: 93.85%

## Root Cause Groups

### Missing adapter/adspace or invalid order fixture data

**Affected Features:**
- adapters.feature
- mc_orders.feature

**Affected Scenarios:**
- get mapped data about an order-line - ADAPTER - GET - success (tc_getadapters02)
- get info about mapped adspaces - ADAPTER - GET - success (tc_getadapters05)
- Create new order - ONLINE - MC - POST (tc_mc_ord_post_03)
- Create new order(for adapter) - ONLINE - MC - POST (tc_mc_ord_post_05)
- Update order - ONLINE - MC - PATCH (tc_mc_ord_patch_09)

**Failure Pattern:**
- Missing adspace for variant id `3`
- Adapter lookup returns N400 or a server NullPointerException
- PATCH validation rejects `ono` as `0`

**Evidence:**
- Adapter POST: N200 expected, N400 found; `No adspace found for variant with id '3'`
- Adapter GET: N200 expected, N400 found
- Adapter GET: N200 expected, N500 found; `NullPointerException` in `WSAdaptersServiceImpl.getInfoAboutMappedAdspaces`
- MC PATCH: N200 expected, N400 found; `ono` is null or zero

**Impact:** 5 failures

**Confidence:** High

### Hibernate session/lazy-loading failure

**Affected Features:**
- print_orders.feature

**Affected Scenarios:**
- create new order - print - success (tc_print_ord_post_01)
- create new order with orTypeofsplit - print - success (tc_print_ord_post_07)
- create new order without orTypeofsplit - print - success (tc_print_ord_post_08)

**Failure Pattern:**
- Print POST requests return N500
- Same lazy-initialization error occurs across multiple print-order scenarios

**Evidence:**
- `failed to lazily initialize a collection of role: com.atex.crossad.core.db.entities.FServicefee.FChargeses`
- Error text includes `could not initialize proxy - no Session`

**Impact:** 3 failures

**Confidence:** High

### Stale or changed API response fixtures

**Affected Features:**
- base.feature
- customerapi.feature
- dwl.feature
- print_orders.feature

**Affected Scenarios:**
- get all non-expired production-flows for print - BASE - GET - success (tc_getbase10)
- get information about database-version - BASE - GET - success (tc_getbase22)
- Get customer activities - success (tc_cust24)
- Get salesman activities - success (tc_cust25)
- Get customer information objects - salesman and legal person combination - success (tc_cust29)
- get Netsale rows - DWL - GET - success (tc_getdwl01)
- get Online rows - DWL - GET - success (tc_getdwl02)
- Get suggested services - PRINT - POST - success (tc_print_ord_post_05)

**Failure Pattern:**
- Returned lists contain extra or different records
- DWL timestamp differs from the fixture
- Suggested-service result order differs

**Evidence:**
- BASE: expected `[[100, FM, PROD]]`, found `[[100, FM, PROD, PROD2]]`
- BASE: database version expected `8.8`, found `8.9`
- CUSTOMER: expected 21 or 5 returned IDs, found additional/new IDs
- DWL: timestamp expected `2023-08-29T12:30:19`, found `2026-06-23T14:06:28`
- DWL: expected five order IDs ending `906588`, found only four rows
- PRINT: expected `[ESP, MIL]`, found `[MIL, ESP]`

**Impact:** 8 failures

**Confidence:** High
