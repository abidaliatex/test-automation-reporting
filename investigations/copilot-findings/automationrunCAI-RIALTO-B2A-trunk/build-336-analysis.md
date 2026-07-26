# Investigation — automationrunCAI-RIALTO-B2A-trunk #336

Source report: [build-336.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-336.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #336
Total Tests: 17
Passed: 7
Failed: 10
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS API Endpoints Unavailable (HTTP 404)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Attempts to log in a user (tc_postRialtoB2A01)
- Create ad for self service (tc_postRialtoB2A02)
- Calculate price for self service (tc_postRialtoB2A03)
- Queries space availability (tc_postRialtoB2A04)
- get order details using order ID (tc_getRialtoB2A01)
- Returns package and placement data (tc_getRialtoB2A02)
- Returns OrderHeader objects for orders associated with the user (tc_getRialtoB2A04)

**Failure Pattern:**
HTTP Status 404 – Not Found for `/agency/crossad-integration-ws/api/870/v1/cass/*` — expected [N200/N202] but found [N404]

**Evidence:**
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders] is not available`
- Apache Tomcat/9.0.73 returning HTML 404 error pages instead of JSON

**Impact:** 7 failures

**Confidence:** High

---

## Cascade Failures — Missing `uuid` from Failed Upstream POST

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Update ad(Order) for self service (tc_patchRialtoB2A01)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
`Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid` and `Failed to parse the JSON document`

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `Failed to parse the JSON document` / `Lexing failed on line: 1, column: 1, while reading '<'` (HTML page received instead of JSON)
- These scenarios depend on `uuid` extracted from `tc_postRialtoB2A02` (Create ad), which itself returned 404

**Impact:** 3 failures

**Confidence:** High

---

## Summary

Build `automationrunCAI-RIALTO-B2A-trunk` #336 finished **UNSTABLE** — 10 of 17 tests failed.

## Root Cause

- All CASS routes under `/agency/crossad-integration-ws/api/870/v1/cass/` are returning HTTP 404 from Apache Tomcat/9.0.73, indicating the CASS integration web service is not deployed or not reachable in the target environment.
- Three dependent scenarios cascade-fail because the `uuid` from a prior order-creation POST was never populated (the POST itself returned 404).
- The triggering commit (`updated testcase29 data tc_getMHTC_MZN04a`) is unrelated to the CASS B2A feature — environment-level unavailability is the likely cause, consistent with failures in builds #334 and #333.

## Affected Components

- `rialtoB2A(CASS).feature`
- CASS API routes under `/agency/crossad-integration-ws/api/870/v1/cass/`
- Dependent GET/PATCH steps that require `uuid` from a preceding successful POST

## Recommended Fix

- Restore or redeploy the CASS integration web service (`crossad-integration-ws`) at API version `870` in the target environment.
- Verify `/api/870/v1/cass/users/login` responds before running the full suite.

## Prevention

- Add a smoke-check step that validates at least one CASS endpoint before running the full `rialtoB2A(CASS)` pack.
- Fail fast when prerequisite POST steps return non-2xx to avoid cascade noise on dependent `uuid` scenarios.
