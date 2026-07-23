# Investigation — automationrunCAI-RIALTO-B2A-trunk #329

Source report: [build-329.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-329.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #329  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoints unavailable (HTTP 404)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Attempts to log in a user (tc_postRialtoB2A01)
- Create ad for self service (tc_postRialtoB2A02)
- Calculate price for self service (tc_postRialtoB2A03)
- Queries space availability (tc_postRialtoB2A04)
- get order details using order ID (tc_getRialtoB2A01)
- Returns package and placement data (tc_getRialtoB2A02)
- Returns OrderHeader objects for orders associated with the user. (tc_getRialtoB2A04)

**Failure Pattern:**
HTTP Status 404 – Not Found for `/agency/crossad-integration-ws/api/870/v1/cass/*`

**Evidence:**
- `Request URI: https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/users/login`
- `Request URI: https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/orders/orders`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`

**Impact:** 7 failures

**Confidence:** High

## Cascade failures from missing `uuid`/non-JSON response

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)
- Update ad(Order) for self service (tc_patchRialtoB2A01)

**Failure Pattern:**
`Invalid number of path parameters... Undefined path parameters are: uuid` and `Failed to parse the JSON document`

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High

---

## Summary
- Build failures are dominated by HTTP 404 responses from CASS endpoints.
- Remaining failures are downstream effects when `uuid` is not produced and HTML error bodies are parsed as JSON.

## Root Cause
- CASS service routes under `/api/870/v1/cass/` are unavailable in the target environment for this build.

## Affected Components
- `crossad-integration-ws` CASS API routes
- `rialtoB2A(CASS)` POST/GET test flows

## Recommended Fix
- Restore availability/routing for `/api/870/v1/cass/` endpoints before rerun.
- Ensure create-order response returns the `uuid` required by dependent scenarios.

## Prevention
- Add a pre-check that validates key CASS endpoints before executing full scenario packs.
