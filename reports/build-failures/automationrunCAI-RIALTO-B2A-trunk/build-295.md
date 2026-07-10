# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #295  
Date: 2026-07-10 14:42 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS `/api/870/v1/cass` endpoints returning HTTP 404

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
Tomcat HTML `404 Not Found` page returned for CASS routes where the suite expected API codes (`N200`/`N202`), e.g. `expected [N200] but found [N404]`.

**Evidence:**
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders` → expected `[N202]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice` and `/orders/spaceAvailability` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620`, `/staticData/validPackagesAndPlacements`, `/orders/orderHeaders` → expected `[N200]`, found `[N404]`

**Impact:** 7 failures

**Confidence:** High

## Cascading UUID and JSON parsing failures after upstream 404s

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent steps failed because prerequisite order responses did not provide valid data (`uuid`) and one update flow attempted to parse non-JSON error content.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
