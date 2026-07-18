# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #319  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoints under `/api/870/v1/cass` returned 404

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Attempts to log in a user (`tc_postRialtoB2A01`)
- Create ad for self service (`tc_postRialtoB2A02`)
- Calculate price for self service (`tc_postRialtoB2A03`)
- Queries space availability (`tc_postRialtoB2A04`)
- get order details using order ID (`tc_getRialtoB2A01`)
- Returns package and placement data (`tc_getRialtoB2A02`)
- Returns OrderHeader objects for orders associated with the user. (`tc_getRialtoB2A04`)

**Failure Pattern:**
Expected success status codes (N200/N202) but received `HTTP Status 404 – Not Found`.

**Evidence:**
- `java.lang.AssertionError: ... HTTP Status 404 – Not Found ... expected [N200] but found [N404]`
- `java.lang.AssertionError: ... HTTP Status 404 – Not Found ... expected [N202] but found [N404]`

**Impact:** 7 failures

**Confidence:** High

---

## Missing `uuid` and invalid JSON parsing in dependent flow

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent API calls failed when `uuid` path input was not populated, and one step attempted to parse a non-JSON response.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
