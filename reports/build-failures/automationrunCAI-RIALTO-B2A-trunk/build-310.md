# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #310  
Date: 2026-07-13 22:35 UTC  
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
- User perform CASS POST API — attempts to log in a user (tc_postRialtoB2A01)
- User perform CASS POST API — create ad for self service (tc_postRialtoB2A02)
- User perform CASS POST API — calculate price for self service (tc_postRialtoB2A03)
- User perform CASS POST API — queries space availability (tc_postRialtoB2A04)
- User perform CASS GET API — get order details using order ID (tc_getRialtoB2A01)
- User perform CASS GET API — returns package and placement data (tc_getRialtoB2A02)
- User perform CASS GET API — returns OrderHeader objects for orders associated with the user (tc_getRialtoB2A04)

**Failure Pattern:**
Status-code assertions failed because API responses returned `HTTP Status 404 – Not Found` HTML pages instead of expected success codes.

**Evidence:**
- `/cass/users/login` → expected N200, got N404
- `/cass/orders/orders` → expected N202, got N404
- `/cass/orders/calculatePrice` → expected N200, got N404
- `/cass/orders/spaceAvailability` → expected N200, got N404
- `/cass/orders/orders/1620` → expected N200, got N404
- `/cass/staticData/validPackagesAndPlacements` → expected N200, got N404
- `/cass/orders/orderHeaders` → expected N200, got N404

**Impact:** 7 failures

**Confidence:** High

---

## Missing `uuid` and JSON parse errors (downstream cascade)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS GET API — returns StoreStatus of Order (tc_getRialtoB2A05)
- User perform CASS POST API — update ad (Order) for self service (tc_patchRialtoB2A01)
- User perform CASS GET API — returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
Dependent requests failed after upstream call failures left `uuid` unset or returned non-JSON bodies.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
