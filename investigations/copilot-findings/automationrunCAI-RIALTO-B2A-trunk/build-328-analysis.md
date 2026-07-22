# Investigation — automationrunCAI-RIALTO-B2A-trunk #328

Source report: [build-328.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-328.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #328
Total Tests: 17
Passed: 7
Failed: 10
Pass Rate: 41.2%

---

## Root Cause Groups

## Root Cause 1 — CASS API Endpoints Return HTTP 404

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (login endpoint)
- User perform CASS POST API - #1.1 (create order endpoint)
- User perform CASS POST API - #1.1 (calculatePrice endpoint)
- User perform CASS POST API - #1.2 (spaceAvailability endpoint)
- User perform CASS GET API - #1.1 (get order by ID)
- User perform CASS GET API - #1.1 (validPackagesAndPlacements)
- User perform CASS GET API - #1.1 (orderHeaders)

**Failure Pattern:**
HTTP 404 – Not Found for all `/agency/crossad-integration-ws/api/870/v1/cass/` endpoints; expected N200/N202 but found N404.

**Evidence:**
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders] is not available`
- Apache Tomcat/9.0.73 returned standard 404 responses (not a test or assertion error)

**Impact:** 7 failures

**Confidence:** High

---

## Root Cause 2 — Cascade Failures: Missing `uuid` After Failed POST

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (uuid extraction — 2 occurrences)
- User perform CASS POST API - #1.1 (JSON parse failure — 1 occurrence)

**Failure Pattern:**
`IllegalArgumentException: Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid` and `JsonPathException: Failed to parse the JSON document`

**Evidence:**
- The `orders/orders` POST (create order) returned HTTP 404 HTML instead of JSON with a `uuid` field
- Test framework tried to extract `uuid` from the HTML error body — extraction failed silently
- Subsequent steps that substitute `{uuid}` into URL path raised `IllegalArgumentException`
- One step attempted `JsonPath.get()` on the 404 HTML body, causing `JsonPathException`

**Impact:** 3 failures (cascading from Root Cause 1)

**Confidence:** High

---

## Summary

All 10 failures in build 328 stem from a single underlying issue: **the CASS service under `crossad-integration-ws/api/870/v1/cass/` is not reachable on the target environment** (returns HTTP 404 for every endpoint). This is identical to the failure pattern observed in build 327. Three additional failures are cascading consequences of the unavailable login/create-order endpoints — no `uuid` token can be obtained, so all downstream parameterised steps fail.

## Root Cause

The CASS integration web-service is not deployed or not routed correctly at context path `/agency/crossad-integration-ws/api/870/v1/cass/` on the test environment. Apache Tomcat/9.0.73 confirms the resources are simply not present (not an authentication or authorisation error).

## Affected Components

- `crossad-integration-ws` — CASS module (all endpoints under `/api/870/v1/cass/`)
- Test suite: `rialtoB2A(CASS)` — POST and GET scenario groups

## Recommended Fix

- Verify that `crossad-integration-ws` with CASS support is deployed to the target environment.
- Confirm the context root and API version (`870`) match the deployment configuration.
- Re-run the build after the service is available.

## Prevention

- Add a pre-flight health-check step in the pipeline to verify CASS endpoint availability before executing the full test suite.
- Alert on repeated 404s across consecutive builds (this issue has persisted since at least build 327).
