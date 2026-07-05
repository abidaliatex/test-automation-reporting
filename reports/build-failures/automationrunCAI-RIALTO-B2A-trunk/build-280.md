# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #280  
Date: 2026-07-05 20:24 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

### HTTP 404 — API base path not available (`/api/870/v1/cass/…`)

**Affected Features:**
- `rialtoB2A (CASS)`

**Affected Scenarios:**
- Attempts to log in a user (`tc_postRialtoB2A01`)
- Create ad for self service (`tc_postRialtoB2A02`)
- Calculate price for self service (`tc_postRialtoB2A03`)
- Queries space availability (`tc_postRialtoB2A04`)
- get order details using order ID (`tc_getRialtoB2A01`)
- Returns package and placement data (`tc_getRialtoB2A02`)
- Returns OrderHeader objects for orders associated with the user (`tc_getRialtoB2A04`)

**Failure Pattern:**
All requests to `/agency/crossad-integration-ws/api/870/v1/cass/…` return `HTTP 404`. The API version segment `870` is not deployed or the base path has changed. Expected status codes `200`/`202` were not received.

**Evidence:**
- `tc_postRialtoB2A01`: `/api/870/v1/cass/users/login` → 404 (expected 200)
- `tc_postRialtoB2A02`: `/api/870/v1/cass/orders/orders` → 404 (expected 202)
- `tc_postRialtoB2A03`: `/api/870/v1/cass/orders/calculatePrice` → 404 (expected 200)
- `tc_postRialtoB2A04`: `/api/870/v1/cass/orders/spaceAvailability` → 404 (expected 200)
- `tc_getRialtoB2A01`: `/api/870/v1/cass/orders/orders/1620` → 404 (expected 200)
- `tc_getRialtoB2A02`: `/api/870/v1/cass/staticData/validPackagesAndPlacements` → 404 (expected 200)
- `tc_getRialtoB2A04`: `/api/870/v1/cass/orders/orderHeaders` → 404 (expected 200)

**Impact:** 7 failures

**Confidence:** High

---

### Missing `uuid` path parameter (cascading failure from login/create step)

**Affected Features:**
- `rialtoB2A (CASS)`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Steps that rely on a `uuid` populated by an earlier step fail because the login/create flow upstream returned 404. The `uuid` path parameter is never set, so the GET request cannot be constructed.

**Evidence:**
- `tc_getRialtoB2A05`: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `tc_getRialtoB2A06`: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

**Impact:** 2 failures

**Confidence:** High

---

### Failed to parse JSON document (cascading failure from login/create step)

**Affected Features:**
- `rialtoB2A (CASS)`

**Affected Scenarios:**
- Update ad (Order) for self service (`tc_patchRialtoB2A01`)

**Failure Pattern:**
The PATCH step could not construct a valid request body because the preceding login/order-creation step failed, leaving the context without the required order data.

**Evidence:**
- `tc_patchRialtoB2A01`: `Failed to parse the JSON document`

**Impact:** 1 failure

**Confidence:** High

---

## Failing Tests / Steps

| Test Case | Scenario | Error |
|---|---|---|
| `tc_postRialtoB2A01` | Attempts to log in a user | HTTP 404 `/api/870/v1/cass/users/login` |
| `tc_postRialtoB2A02` | Create ad for self service | HTTP 404 `/api/870/v1/cass/orders/orders` |
| `tc_getRialtoB2A05` | Returns StoreStatus of Order | Missing path param `uuid` |
| `tc_patchRialtoB2A01` | Update ad (Order) for self service | Failed to parse JSON document |
| `tc_getRialtoB2A06` | Returns StoreStatus of Update Order | Missing path param `uuid` |
| `tc_postRialtoB2A03` | Calculate price for self service | HTTP 404 `/api/870/v1/cass/orders/calculatePrice` |
| `tc_postRialtoB2A04` | Queries space availability | HTTP 404 `/api/870/v1/cass/orders/spaceAvailability` |
| `tc_getRialtoB2A01` | get order details using order ID | HTTP 404 `/api/870/v1/cass/orders/orders/1620` |
| `tc_getRialtoB2A02` | Returns package and placement data | HTTP 404 `/api/870/v1/cass/staticData/validPackagesAndPlacements` |
| `tc_getRialtoB2A04` | Returns OrderHeader objects for orders | HTTP 404 `/api/870/v1/cass/orders/orderHeaders` |

## Error Output

```text
HTTP Status 404 – Not Found
  The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available
  Apache Tomcat/9.0.73

HTTP Status 404 – Not Found
  The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available

Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.

Failed to parse the JSON document

HTTP Status 404 – Not Found
  The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice] is not available

HTTP Status 404 – Not Found
  The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability] is not available
```

## Suggested Next Steps

- Verify whether API version `870` is deployed to the target environment; check if the correct version number is configured in the test suite.
- The `uuid`/JSON-parse failures are cascading from the 404 on login — fixing the 404 root cause will likely resolve those too.
