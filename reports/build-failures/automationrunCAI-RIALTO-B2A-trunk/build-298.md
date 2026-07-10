# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #298  
Date: 2026-07-10 15:57 UTC  
Status: UNSTABLE  
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
Tomcat returned `HTTP Status 404 – Not Found` for CASS login, order, pricing, space-availability, order-detail, package/placement, and order-header endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...`.

**Evidence:**
- `cass/users/login` expected `N200`, found `N404`
- `cass/orders/orders` expected `N202`, found `N404`
- `cass/orders/calculatePrice` expected `N200`, found `N404`
- `cass/orders/spaceAvailability` expected `N200`, found `N404`
- `cass/orders/orders/1620` expected `N200`, found `N404`
- `cass/staticData/validPackagesAndPlacements` expected `N200`, found `N404`
- `cass/orders/orderHeaders?...` expected `N200`, found `N404`

**Impact:** 7 failures

**Confidence:** High

## Missing `uuid` / JSON parsing failures after upstream 404s

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Dependent scenarios failed after earlier create/update requests returned HTML 404 pages, leaving `uuid` unset or causing the HTML body to be parsed as JSON.

**Evidence:**
- `cass/orders/storeStatus/{uuid}` failed with `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `Failed to parse the JSON document` occurred while updating an order after consuming a non-JSON error response

**Impact:** 3 failures

**Confidence:** High
