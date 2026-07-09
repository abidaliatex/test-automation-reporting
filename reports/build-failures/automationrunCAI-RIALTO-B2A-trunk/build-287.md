# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #287  
Date: 2026-07-09 20:48 UTC  
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
- User perform CASS POST API - Attempts to log in a user (tc_postRialtoB2A01)
- User perform CASS POST API - Create ad for self service (tc_postRialtoB2A02)
- User perform CASS POST API - Calculate price for self service (tc_postRialtoB2A03)
- User perform CASS POST API - Queries space availability (tc_postRialtoB2A04)
- User perform CASS GET API - get order details using order ID (tc_getRialtoB2A01)
- User perform CASS GET API - Returns package and placement data (tc_getRialtoB2A02)
- User perform CASS GET API - Returns OrderHeader objects for orders associated with the user (tc_getRialtoB2A04)

**Failure Pattern:**
All CASS requests to `/agency/crossad-integration-ws/api/870/v1/cass/...` return Tomcat `HTTP 404 Not Found` instead of the expected `N200`/`N202` API responses.

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

---

## Cascading UUID and JSON parsing failures after prerequisite 404s

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API - Returns StoreStatus of Order (tc_getRialtoB2A05)
- User perform CASS POST API - Update ad(Order) for self service (tc_patchRialtoB2A01)
- User perform CASS POST API - Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
Follow-up steps depend on a valid `uuid` extracted from a prior order response; once the preceding calls return HTML 404 pages, subsequent requests fail with missing path parameters or JSON parse errors.

**Evidence:**
- `cass/orders/storeStatus/{uuid}` — `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `JsonPathException: Failed to parse the JSON document` (HTML 404 response body not parseable as JSON)
- Checkout revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd`, commit message: `"updated api version from 87 to 88"`

**Impact:** 3 failures

**Confidence:** High
