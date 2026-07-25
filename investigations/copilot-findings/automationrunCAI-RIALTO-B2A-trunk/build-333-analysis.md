# Investigation — automationrunCAI-RIALTO-B2A-trunk #333

Source report: [build-333.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-333.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #333  
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
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders] is not available`

**Impact:** 7 failures

**Confidence:** High

## Cascade failures from missing `uuid` / non-JSON response

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)
- Update ad(Order) for self service (tc_patchRialtoB2A01)

**Failure Pattern:**
`Invalid number of path parameters... Undefined path parameters are: uuid` and `Failed to parse the JSON document`

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.` in both store-status GET scenarios.
- `Failed to parse the JSON document` after the update flow reused a prior response that was not valid JSON.

**Impact:** 3 failures

**Confidence:** High

---

## Summary
- The 10 failures group into one primary service outage and one downstream cascade: the CASS API routes returned HTTP 404, then later steps failed because no usable order UUID was produced.

## Root Cause
- The `/api/870/v1/cass/` routes were unavailable in the target environment during build 333. Downstream scenarios that depend on a created order then failed when `uuid` was absent.

## Affected Components
- `crossad-integration-ws` CASS API routes
- `rialtoB2A(CASS)` POST / GET / PATCH API scenarios

## Recommended Fix
- Restore routing or deployment for the `/api/870/v1/cass/` endpoints before rerunning the suite.
- Stop dependent scenarios early when the create-order flow does not return a `uuid`.

## Prevention
- Add a lightweight health check for critical `/api/870/v1/cass/` endpoints before running the `@rialtoB2AAPIs` pack.
