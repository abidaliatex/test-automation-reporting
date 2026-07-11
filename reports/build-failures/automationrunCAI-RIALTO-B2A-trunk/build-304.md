# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #304  
Date: 2026-07-11 15:09 UTC  
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
- Attempts to log in a user (`tc_postRialtoB2A01`)
- Create ad for self service (`tc_postRialtoB2A02`)
- Calculate price for self service (`tc_postRialtoB2A03`)
- Queries space availability (`tc_postRialtoB2A04`)
- get order details using order ID (`tc_getRialtoB2A01`)
- Returns package and placement data (`tc_getRialtoB2A02`)
- Returns OrderHeader objects for orders associated with the user (`tc_getRialtoB2A04`)

**Failure Pattern:**
Expected HTTP success codes (`200`/`202`) but received `404` from Tomcat for CASS endpoints.

**Evidence:**
- `expected [N200] but found [N404]`
- `expected [N202] but found [N404]`
- `/agency/crossad-integration-ws/api/870/v1/cass/users/login`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/orders`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice`
- `/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability`

**Impact:** 7 failures

**Confidence:** High

### Dependent flow failures from missing UUID / invalid response parsing

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)

**Failure Pattern:**
Downstream steps depend on a `uuid` extracted from earlier failed requests; missing path parameter and response-processing errors cascade.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
