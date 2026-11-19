## Build Summary

- Build: [192](https://crossadv.atex.com/jenkins/job/automationrunCAI-trunk/192/)
- Date: 2026-11-19 02:10:18 UTC
- Status: UNSTABLE
- Total Tests: 260
- Passed: 244
- Failed: 16
- Pass Rate: 93.85%

---

## Root Cause Groups

## MC order creation references an unavailable adspace

**Affected Features:**
- `adapters.feature`
- `mc_orders.feature`

**Affected Scenarios:**
- Create new order(for adapter) - ONLINE - MC - POST (`tc_mc_ord_post_05`)
- Create new order - ONLINE - MC - POST (`tc_mc_ord_post_03`)

**Failure Pattern:** Expected N200; received N400 because no adspace was found for variant ID `3`.

**Evidence:**
- Both POST cases returned `error.ws.caivalidation.non.existing.adspace.for.variant`.

**Impact:** 2 failures

**Confidence:** High

## Adapter GET requests return errors

**Affected Features:**
- `adapters.feature`

**Affected Scenarios:**
- get mapped data about an order-line - ADAPTER - GET - success (`tc_getadapters02`)
- get info about mapped adspaces - ADAPTER - GET - success (`tc_getadapters05`)

**Failure Pattern:** Expected N200; received N400 and N500, respectively.

**Evidence:**
- `tc_getadapters05` returned a `NullPointerException` in `WSAdaptersServiceImpl.getInfoAboutMappedAdspaces` at line 255. Jenkins recorded no further cause for the N400 in `tc_getadapters02`.

**Impact:** 2 failures

**Confidence:** Medium

## Print order POST fails while loading service-fee charges

**Affected Features:**
- `print_orders.feature`

**Affected Scenarios:**
- create new order - print - success (`tc_print_ord_post_01`)
- create new order with orTypeofsplit - print - success (`tc_print_ord_post_07`)
- create new order without orTypeofsplit - print - success (`tc_print_ord_post_08`)

**Failure Pattern:** Expected N200; received N500 while lazily initializing `FServicefee.FChargeses` without an active session.

**Evidence:**
- The same lazy-initialization error was returned for all three POST scenarios.

**Impact:** 3 failures

**Confidence:** High

## BASE, CUSTOMER, and DWL responses differ from expected test data

**Affected Features:**
- `base.feature`
- `customerapi.feature`
- `getcustomeractivitiesapi.feature`
- `dwl.feature`

**Affected Scenarios:**
- get all non-expired production-flows for print - BASE - GET - success (`tc_getbase10`)
- get information about database-version - BASE - GET - success (`tc_getbase22`)
- Get customer information objects - salesman and legal person combination - success (`tc_cust29`)
- Get customer activities - success (`tc_cust24`)
- Get salesman activities - success (`tc_cust25`)
- get Netsale rows - DWL - GET - success (`tc_getdwl01`)
- get Online rows - DWL - GET - success (`tc_getdwl02`)

**Failure Pattern:** Returned records, counts, or values differ from the expected fixtures.

**Evidence:**
- `tc_getbase10` returned an additional `PROD2` flow; `tc_getbase22` returned version `8.9` instead of `8.8`.
- CUSTOMER cases returned unexpected record counts/IDs; DWL cases differed in row content or returned one fewer expected row.

**Impact:** 7 failures

**Confidence:** Medium

## MC order PATCH rejects a zero order number

**Affected Features:**
- `mc_orders.feature`

**Affected Scenarios:**
- Update order - ONLINE - MC - PATCH (`tc_mc_ord_patch_09`)

**Failure Pattern:** Expected N200; received N400 because field `ono` was `0`.

**Evidence:**
- Jenkins reported that `ono` must not be null or zero.

**Impact:** 1 failure

**Confidence:** High

## Suggested-services response order differs from expectation

**Affected Features:**
- `print_orders.feature`

**Affected Scenarios:**
- Get suggested services - PRINT - POST - success (`tc_print_ord_post_05`)

**Failure Pattern:** Expected `[ESP, MIL]`; received `[MIL, ESP]`.

**Evidence:**
- The status check passed; the response-field assertion failed on the service ordering.

**Impact:** 1 failure

**Confidence:** High
