# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #288  
Date: 2026-07-09 21:02 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoints under `/api/870/v1/cass` return HTTP 404

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Attempts to log in a user (`tc_postRialtoB2A01`)
- Create ad for self service (`tc_postRialtoB2A02`)
- Calculate price for self service (`tc_postRialtoB2A03`)
- Queries space availability (`tc_postRialtoB2A04`)
- get order details using order ID (`tc_getRialtoB2A01`)
- Returns package and placement data (`tc_getRialtoB2A02`)
- Returns OrderHeader objects for orders associated with the user. (`tc_getRialtoB2A04`)

**Failure Pattern:**
Core CASS requests to `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat `404 Not Found` pages instead of the expected `N200`/`N202` API responses.

**Evidence:**
- `cass/users/login` — expected `N200`, found `N404`
- `cass/orders/orders` — expected `N202`, found `N404`
- `cass/orders/calculatePrice` — expected `N200`, found `N404`
- `cass/orders/spaceAvailability` — expected `N200`, found `N404`
- `cass/orders/orders/1620` — expected `N200`, found `N404`
- `cass/staticData/validPackagesAndPlacements` — expected `N200`, found `N404`
- `cass/orders/orderHeaders` — expected `N200`, found `N404`

**Impact:** 7 failures

**Confidence:** High

## Cascading UUID and JSON parsing failures after prerequisite 404s

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Follow-up steps depended on a valid order response and extracted `uuid`; once the create/update calls returned HTML 404 pages, later requests failed with missing path parameters or JSON parsing errors.

**Evidence:**
- `cass/orders/storeStatus/{uuid}` — `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `JsonPathException: Failed to parse the JSON document`
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd`

**Impact:** 3 failures

**Confidence:** High
