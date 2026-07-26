# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #335

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 335 |
| **Date** | 2026-07-26 21:02:17 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~48 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/335/ |

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #335  
Total Tests: 17  
Passed: 7  
Failed: 10  
Pass Rate: 41.2%

---

## Root Cause Groups

## CASS endpoints unavailable (HTTP 404)

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
Tomcat returned `HTTP Status 404 – Not Found` for `/agency/crossad-integration-ws/api/870/v1/cass/*` routes.

**Evidence:**
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/calculatePrice] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/spaceAvailability] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders/1620] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/staticData/validPackagesAndPlacements] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orderHeaders] is not available`

**Impact:** 7 failures

**Confidence:** High

## Cascade failures from missing `uuid` / non-JSON response

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent scenarios failed with missing `uuid` path parameters or by attempting to parse an HTML 404 page as JSON.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`
- `Lexing failed on line: 1, column: 1, while reading '<'`

**Impact:** 3 failures

**Confidence:** High
