# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #320  
Date: 2026-07-18 21:09 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoints under `/api/870/v1/cass` returned 404

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API — login (`tc_postRialtoB2A01`)
- User perform CASS POST API — create ad for self service (`tc_postRialtoB2A02`)
- User perform CASS POST API — calculate price for self service (`tc_postRialtoB2A03`)
- User perform CASS POST API — space availability (`tc_postRialtoB2A04`)
- User perform CASS GET API — get order details by order ID (`tc_getRialtoB2A01`)
- User perform CASS GET API — returns package and placement data (`tc_getRialtoB2A02`)
- User perform CASS GET API — returns OrderHeader objects (`tc_getRialtoB2A04`)

**Failure Pattern:**
Apache Tomcat returned `HTTP Status 404 – Not Found` for all CASS endpoints; expected HTTP 2xx, received 404.

**Evidence:**
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login` expected `N200`, found `N404`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders` expected `N202`, found `N404`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice` expected `N200`, found `N404`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability` expected `N200`, found `N404`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620` expected `N200`, found `N404`
- `/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements` expected `N200`, found `N404`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders` expected `N200`, found `N404`

**Impact:** 7 failures

**Confidence:** High

---

## Missing `uuid` / JSON parsing failures (cascade from upstream 404s)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API — returns StoreStatus of Order (`tc_getRialtoB2A05`)
- User perform CASS POST API — update ad (Order) for self service (`tc_patchRialtoB2A01`)
- User perform CASS POST API — returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent scenarios failed because `uuid` was never populated after the failed create-order call, or an HTML 404 response body was parsed as JSON.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.` (2 occurrences)
- `Failed to parse the JSON document`
- `Lexing failed on line: 1, column: 1, while reading '<'` — HTML error page returned instead of JSON

**Impact:** 3 failures

**Confidence:** High
