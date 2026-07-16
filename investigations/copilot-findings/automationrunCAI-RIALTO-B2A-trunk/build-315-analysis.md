# Build 315 – Root Cause Analysis

**Source report:** [build-315.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-315.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-07-16 21:02:21 UTC

---

## Build Summary

Build: 315
Total Tests: 17
Passed: 7
Failed: 10
Pass Rate: 41%

---

## Root Cause Groups

---

## RC-1: CASS API Endpoints Unavailable (HTTP 404)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API – Login step (line 23)
- User perform CASS POST API – Create Order step (line 45)
- User perform CASS POST API – Calculate Price step (line 163)
- User perform CASS POST API – Space Availability step (line 164)
- User perform CASS GET API – Get Order by ID (line 178)
- User perform CASS GET API – Get Valid Packages and Placements (line 191)
- User perform CASS GET API – Get Order Headers (line 205)

**Failure Pattern:**
`expected [N200] but found [N404]` / `expected [N202] but found [N404]`

**Evidence:**
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders] is not available`
- All responses served by Apache Tomcat/9.0.73 with HTTP 404 Status Report

**Impact:** 7 failures

**Confidence:** High

---

## RC-2: UUID Path Parameter Not Populated (Cascade from RC-1)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API – Store Status GET (line 57)
- User perform CASS POST API – Store Status GET (line 109)

**Failure Pattern:**
`Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

**Evidence:**
- Request URI: `https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/orders/storeStatus/%7Buuid%7D`
- The `{uuid}` placeholder was never resolved — UUID is stored from a prior order creation step
- Prior order creation (`/cass/orders/orders`) failed with 404 (RC-1), so no UUID was captured in context

**Impact:** 2 failures

**Confidence:** High

---

## RC-3: JSON Parse Failure (Cascade from RC-1)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API – Alter IDs from recent created ad (line 85)

**Failure Pattern:**
`io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Evidence:**
- Step: `User perfrom "post" request with request body "Request Body" and alterd IDs from recent created ad`
- The step attempts to parse a JSON response body using JsonPath, but the response is an HTML 404 error page (cascade from RC-1 login failure)
- `stepDefinition.ApiStepDefinition.user_perfrom_request_with_request_body_and_alterd_IDs_from_recent_created_ad`

**Impact:** 1 failure

**Confidence:** High

---

## Summary

| Root Cause | Failures | Confidence |
|---|---|---|
| RC-1: CASS API endpoints returning 404 | 7 | High |
| RC-2: UUID not populated (cascade) | 2 | High |
| RC-3: JSON parse error (cascade) | 1 | High |

**Primary cause:** All 10 failures trace back to the CASS integration endpoints being unavailable at `api/870/v1/cass/*`. The server returns HTTP 404 for every CASS endpoint, indicating the CASS module may not be deployed, the context path has changed, or the service is down on the test environment.

---

## Recommended Fix

- Verify the CASS integration service (`crossad-integration-ws`) is deployed and running on the test server
- Confirm the API context path `/agency/crossad-integration-ws/api/870/v1/cass/` is correct for the current deployment
- Re-run build after service restoration; RC-2 and RC-3 are expected to auto-resolve

## Prevention

- Add a pre-flight health-check step in the feature or pipeline that validates CASS service availability before running dependent scenarios
