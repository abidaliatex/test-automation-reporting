# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #307  
Date: 2026-07-12 21:02 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoints returned HTTP 404

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
Status-code assertions failed because all CASS API calls returned `HTTP Status 404 – Not Found` HTML pages instead of expected success codes (`N200`, `N202`).

**Evidence:**
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login` → 404; expected N200
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders` → 404; expected N202
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice` → 404; expected N200
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability` → 404; expected N200
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620` → 404; expected N200
- `/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements` → 404; expected N200
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders` → 404; expected N200

**Impact:** 7 failures

**Confidence:** High

---

## Missing `uuid` and JSON parse errors (downstream cascade)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent scenarios failed because upstream POST calls (which set the `uuid`) returned 404 and never stored a UUID, leaving path parameters unresolved and response bodies unparseable.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
