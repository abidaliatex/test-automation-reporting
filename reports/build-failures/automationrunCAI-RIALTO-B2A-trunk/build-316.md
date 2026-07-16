# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #316  
Date: 2026-07-16 21:09 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoint calls returned HTTP 404

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Attempts to log in a user (`tc_postRialtoB2A01`)
- Create ad for self service (`tc_postRialtoB2A02`)
- Calculate price for self service (`tc_postRialtoB2A03`)
- Queries space availability (`tc_postRialtoB2A04`)
- Get order details using order ID (`tc_getRialtoB2A01`)
- Returns package and placement data (`tc_getRialtoB2A02`)
- Returns OrderHeader objects for orders associated with the user (`tc_getRialtoB2A04`)

**Failure Pattern:**
Status-code assertions failed because API responses returned `HTTP Status 404 – Not Found` HTML pages instead of expected success codes.

**Evidence:**
- `/cass/users/login` → expected N200, got N404
- `/cass/orders/orders` → expected N202, got N404
- `/cass/orders/calculatePrice` → expected N200, got N404
- `/cass/orders/spaceAvailability` → expected N200, got N404
- `/cass/orders/orders/{id}` → expected N200, got N404
- `/cass/staticData/validPackagesAndPlacements` → expected N200, got N404
- `/cass/orders/orderHeaders` → expected N200, got N404

**Impact:** 7 failures

**Confidence:** High

---

## Missing `uuid` and JSON parse errors (downstream cascade)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad (Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent requests failed because the `uuid` extracted from a previous CASS POST response was never set (due to the 404 above), and subsequent steps that require it could not proceed.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
