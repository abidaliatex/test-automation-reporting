# Investigation — automationrunCAI-RIALTO-B2A-trunk #335

Source report: [build-335.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-335.md)

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
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
`Invalid number of path parameters... Undefined path parameters are: uuid` and `Failed to parse the JSON document`

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `Failed to parse the JSON document`
- `Lexing failed on line: 1, column: 1, while reading '<'`

**Impact:** 3 failures

**Confidence:** High

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #335 finished `UNSTABLE` with 10 failed tests out of 17.
- Seven scenarios failed directly because CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat HTTP 404 responses.
- Three additional failures were downstream effects after order creation/update data was unavailable, leaving `uuid` unset or causing an HTML error page to be parsed as JSON.
- This is a recurring pattern also seen in build #334.

## Root Cause

- Primary failure group: CASS login, order, pricing, availability, static-data, and order-header routes were unavailable in the target environment.
- Secondary failure group: dependent GET/PATCH scenarios reused missing upstream data and failed with undefined path parameters or JSON parsing errors.

## Affected Components

- `rialtoB2A(CASS).feature`
- CASS API routes under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- Dependent GET/PATCH steps that require a successful prior response containing `uuid`

## Recommended Fix

- Restore or correct routing for the `/api/870/v1/cass/` endpoints before rerunning the suite.
- Stop dependent `uuid` scenarios early when prerequisite POST/PATCH requests fail.

## Prevention

- Add a lightweight pre-check for a critical CASS route before running the full `rialtoB2A(CASS)` pack.
- Surface prerequisite-data failures as a single blocking error to reduce cascade noise.
