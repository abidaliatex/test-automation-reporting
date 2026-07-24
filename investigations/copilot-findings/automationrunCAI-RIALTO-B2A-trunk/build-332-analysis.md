# Investigation — automationrunCAI-RIALTO-B2A-trunk #332

Source report: [build-332.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-332.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #332  
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
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability] is not available`

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
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.` (tc_getRialtoB2A05, tc_getRialtoB2A06)
- `Failed to parse the JSON document` — patch step received HTML 404 body from prior failed POST instead of valid JSON (tc_patchRialtoB2A01)

**Impact:** 3 failures

**Confidence:** High

---

## Summary
- All 10 failures stem from the same root cause seen in preceding builds: the CASS API routes under `/api/870/v1/cass/` are returning HTTP 404, causing both direct assertion failures and cascading downstream failures when order UUIDs cannot be extracted.

## Root Cause
- The `/api/870/v1/cass/` routes were unavailable on the test environment at the time of this run. Downstream scenarios that depend on a `uuid` from a prior POST step (tc_postRialtoB2A02) then fail with missing path parameters or JSON parse errors.

## Affected Components
- `crossad-integration-ws` CASS API routes
- `rialtoB2A(CASS)` POST / GET / PATCH flows

## Recommended Fix
- Restore availability/routing for the CASS endpoints before rerunning this feature pack.
- Guard dependent scenarios so they stop early when order creation does not return a `uuid`.

## Prevention
- Add a lightweight pre-check for critical `/api/870/v1/cass/` routes before executing the full `@rialtoB2AAPIs` suite.
