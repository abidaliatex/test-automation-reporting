# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #296  
Date: 2026-07-10 15:12 UTC  
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
- User perform CASS POST API - #1.1 (login: `tc_postRialtoB2A01`)
- User perform CASS POST API - #1.1 (create order: `tc_postRialtoB2A02`)
- User perform CASS POST API - #1.1 (calculatePrice: `tc_postRialtoB2A03`)
- User perform CASS POST API - #1.2 (spaceAvailability: `tc_postRialtoB2A04`)
- User perform CASS GET API - #1.1 (order by ID: `tc_getRialtoB2A01`)
- User perform CASS GET API - #1.1 (validPackagesAndPlacements: `tc_getRialtoB2A02`)
- User perform CASS GET API - #1.1 (orderHeaders: `tc_getRialtoB2A04`)

**Failure Pattern:**
Tomcat HTML `404 Not Found` page returned for all CASS routes where the suite expected API codes (`N200`/`N202`), e.g. `expected [N200] but found [N404]`.

**Evidence:**
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders` → expected `[N202]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements` → expected `[N200]`, found `[N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders` → expected `[N200]`, found `[N404]`

**Impact:** 7 failures

**Confidence:** High

---

## Cascading UUID and JSON parsing failures after upstream 404s

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (uuid path param missing — `tc_getRialtoB2A05`)
- User perform CASS POST API - #1.1 (uuid path param missing — `tc_patchRialtoB2A01`)
- User perform CASS POST API - #1.1 (JSON parse failure — `tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent steps fail because login returned no valid JSON; `uuid` token is never captured, causing subsequent requests to fail with path parameter and JSON parsing errors.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.` (×2)
- `JsonPathException: Failed to parse the JSON document` (×1)

**Impact:** 3 failures

**Confidence:** High
