# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #293  
Date: 2026-07-10 12:45 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

### CASS v88 endpoints unavailable under `/api/870/v1/cass`

**Affected Features:**
- `rialtoB2A(CASS)` POST API
- `rialtoB2A(CASS)` GET API

**Affected Scenarios:**
- Attempts to log in a user (`tc_postRialtoB2A01`)
- Create ad for self service (`tc_postRialtoB2A02`)
- Calculate price for self service (`tc_postRialtoB2A03`)
- Queries space availability (`tc_postRialtoB2A04`)
- get order details using order ID (`tc_getRialtoB2A01`)
- Returns package and placement data (`tc_getRialtoB2A02`)
- Returns OrderHeader objects for orders associated with the user. (`tc_getRialtoB2A04`)

**Failure Pattern:**
Requests to multiple CASS endpoints under `/api/870/v1/cass/...` returned Tomcat 404 pages instead of the expected 200/202 responses immediately after the API version bump.

**Evidence:**
- Commit message: `updated api version from 87 to 88`.
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login` expected `N200`, found `N404`.
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders` expected `N202`, found `N404`.
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice`, `/api/870/v1/cass/orders/spaceAvailability`, `/api/870/v1/cass/staticData/validPackagesAndPlacements`, and `/api/870/v1/cass/orders/orderHeaders` returned the same 404 pattern.

**Impact:** 7 failures

**Confidence:** High

### Cascading UUID and response-parsing failures after the 404s

**Affected Features:**
- `rialtoB2A(CASS)` follow-up GET validation
- `rialtoB2A(CASS)` update flow

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Later steps relied on IDs and JSON payloads from earlier requests. Once earlier calls returned HTML 404 responses, follow-up steps failed with missing `uuid` path parameters or JSON parsing errors.

**Evidence:**
- `tc_getRialtoB2A05` and `tc_getRialtoB2A06`: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `tc_patchRialtoB2A01`: `JsonPathException: Failed to parse the JSON document` caused by `Lexing failed ... while reading '<'`, indicating an HTML body instead of JSON.

**Impact:** 3 failures

**Confidence:** High

## Failing Tests / Steps

- `tc_postRialtoB2A01` — Attempts to log in a user
- `tc_postRialtoB2A02` — Create ad for self service
- `tc_getRialtoB2A05` — Returns StoreStatus of Order
- `tc_patchRialtoB2A01` — Update ad(Order) for self service
- `tc_getRialtoB2A06` — Returns StoreStatus of Update Order
- `tc_postRialtoB2A03` — Calculate price for self service
- `tc_postRialtoB2A04` — Queries space availability
- `tc_getRialtoB2A01` — get order details using order ID
- `tc_getRialtoB2A02` — Returns package and placement data
- `tc_getRialtoB2A04` — Returns OrderHeader objects for orders associated with the user.

## Error Output

```text
java.lang.AssertionError: ... /api/870/v1/cass/users/login ... expected [N200] but found [N404]
java.lang.AssertionError: ... /api/870/v1/cass/orders/orders ... expected [N202] but found [N404]
java.lang.IllegalArgumentException: Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.
io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document
Caused by: groovy.json.JsonException: Lexing failed on line: 1, column: 1, while reading '<'
java.lang.AssertionError: ... /api/870/v1/cass/orders/calculatePrice ... expected [N200] but found [N404]
java.lang.AssertionError: ... /api/870/v1/cass/orders/spaceAvailability ... expected [N200] but found [N404]
java.lang.AssertionError: ... /api/870/v1/cass/orders/orders/1620 ... expected [N200] but found [N404]
java.lang.AssertionError: ... /api/870/v1/cass/staticData/validPackagesAndPlacements ... expected [N200] but found [N404]
java.lang.AssertionError: ... /api/870/v1/cass/orders/orderHeaders ... expected [N200] but found [N404]
```
