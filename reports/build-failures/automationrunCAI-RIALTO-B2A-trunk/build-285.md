# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #285  
Date: 2026-07-06 10:01 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

### CASS endpoints unavailable under `/api/870/v1/cass`

**Affected Features:**
- `rialtoB2A(CASS)` POST API
- `rialtoB2A(CASS)` GET API

**Affected Scenarios:**
- `User perform CASS POST API - #1.1` — Attempts to log in a user (`cass/users/login`)
- `User perform CASS POST API - #1.1` — Create ad for self service (`cass/orders/orders`)
- `User perform CASS POST API - #1.1` — Calculate price for self service (`cass/orders/calculatePrice`)
- `User perform CASS POST API - #1.1` — Queries space availability (`cass/orders/spaceAvailability`)
- `User perform CASS POST API - #1.2` — Get order details using order ID (`cass/orders/orders/1620`)
- `User perform CASS GET API - #1.1` — Returns package and placement data (`cass/staticData/validPackagesAndPlacements`)
- `User perform CASS GET API - #1.1` — Returns OrderHeader objects for orders associated with the user (`cass/orders/orderHeaders`)

**Failure Pattern:**
Requests to CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat 404 pages instead of the expected 200/202 responses. The same revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (commit: `updated api version from 87 to 88`) is being checked out, and the same routing issue from build 284 persists.

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

### Cascading UUID and response-parsing failures after the 404s

**Affected Features:**
- `rialtoB2A(CASS)` follow-up storeStatus and update flows

**Affected Scenarios:**
- `User perform CASS POST API - #1.1` — Returns StoreStatus of Order (`cass/orders/storeStatus/{uuid}`)
- `User perform CASS POST API - #1.1` — Update ad (Order) for self service (JSON parse failure)
- `User perform CASS GET API - #1.1` — Returns StoreStatus of Update Order (`cass/orders/storeStatus/{uuid}`)

**Failure Pattern:**
Later steps relied on a `uuid` extracted from the JSON body of a preceding POST call. Once those prerequisite calls returned HTML 404 responses, follow-up steps failed because no `uuid` was captured and the HTML body could not be parsed as JSON.

**Evidence:**
- `cass/orders/storeStatus/{uuid}` (×2): `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `JsonPathException: Failed to parse the JSON document` — caused by HTML body returned instead of JSON from a preceding 404 response.

**Impact:** 3 failures

**Confidence:** High

---

## Error Output

```text
Request URI: .../api/870/v1/cass/users/login
java.lang.AssertionError: ... expected [N200] but found [N404]

Request URI: .../api/870/v1/cass/orders/orders
java.lang.AssertionError: ... expected [N202] but found [N404]

Request URI: .../api/870/v1/cass/orders/storeStatus/%7Buuid%7D
java.lang.IllegalArgumentException: Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.

io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document

Request URI: .../api/870/v1/cass/orders/calculatePrice
java.lang.AssertionError: ... expected [N200] but found [N404]

Request URI: .../api/870/v1/cass/orders/spaceAvailability
java.lang.AssertionError: ... expected [N200] but found [N404]

Request URI: .../api/870/v1/cass/orders/orders/1620
java.lang.AssertionError: ... expected [N200] but found [N404]

Request URI: .../api/870/v1/cass/staticData/validPackagesAndPlacements
java.lang.AssertionError: ... expected [N200] but found [N404]

Request URI: .../api/870/v1/cass/orders/orderHeaders?polySearch=1620&bookedFromDate=2024-10-10&pageNo=1&pageSize=10
java.lang.AssertionError: ... expected [N200] but found [N404]
```

## Suggested Next Steps

- The same 404 issue from build 284 is unresolved. Verify whether the CASS service under `/api/870/v1/cass/...` has been deployed with the correct routes for v88.
- Re-run after the routing issue is fixed to confirm the UUID-dependent and JSON-parse failures are purely cascading.
