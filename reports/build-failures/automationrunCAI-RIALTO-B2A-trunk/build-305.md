# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #305  
Date: 2026-07-11 21:02 UTC  
Status: UNSTABLE  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

### CASS API endpoint 404 errors

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API — Login (`tc_postRialtoB2A01`)
- User perform CASS POST API — Create order (`tc_postRialtoB2A02`)
- User perform CASS POST API — Calculate price (`tc_postRialtoB2A03`)
- User perform CASS POST API — Space availability (`tc_postRialtoB2A04`)
- User perform CASS GET API — Get order by ID (`tc_getRialtoB2A01`)
- User perform CASS GET API — Valid packages and placements (`tc_getRialtoB2A02`)
- User perform CASS GET API — Order headers (`tc_getRialtoB2A04`)

**Failure Pattern:**
Expected HTTP success codes (`200`/`202`) but received `404` from Tomcat for CASS endpoints.

**Evidence:**
- `expected [N200] but found [N404]`
- `expected [N202] but found [N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620`
- `/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders`

**Impact:** 7 failures

**Confidence:** High

### Cascade failures from missing UUID / unparseable response

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API — Update ad (uuid extraction fails) (`tc_patchRialtoB2A01`)
- User perform CASS POST API — Store status of order (`tc_getRialtoB2A05`)
- User perform CASS POST API — Store status of update order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Downstream steps depend on a `uuid` extracted from a prior create-order response; since that response was a 404 HTML page the JSON parse fails and the path parameter is missing.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
