# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #300  
Date: 2026-07-10 21:03 UTC  
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
- User perform CASS POST API - #1.1 (login: `cass/users/login`)
- User perform CASS POST API - #1.1 (create order: `cass/orders/orders`)
- User perform CASS POST API - #1.1 (calculate price: `cass/orders/calculatePrice`)
- User perform CASS POST API - #1.2 (space availability: `cass/orders/spaceAvailability`)
- User perform CASS GET API - #1.1 (order detail: `cass/orders/orders/1620`)
- User perform CASS GET API - #1.1 (packages & placements: `cass/staticData/validPackagesAndPlacements`)
- User perform CASS GET API - #1.1 (order headers: `cass/orders/orderHeaders`)

**Failure Pattern:**
Tomcat returned `HTTP Status 404 – Not Found` for every CASS endpoint under `/agency/crossad-integration-ws/api/870/v1/cass/...`.

**Evidence:**
- `cass/users/login` expected `N200`, found `N404`
- `cass/orders/orders` expected `N202`, found `N404`
- `cass/orders/calculatePrice` expected `N200`, found `N404`
- `cass/orders/spaceAvailability` expected `N200`, found `N404`
- `cass/orders/orders/1620` expected `N200`, found `N404`
- `cass/staticData/validPackagesAndPlacements` expected `N200`, found `N404`
- `cass/orders/orderHeaders` expected `N200`, found `N404`

**Impact:** 7 failures

**Confidence:** High

---

## Cascading failures — missing `uuid` / JSON parse error

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (store-status probe: `cass/orders/storeStatus/{uuid}`)
- User perform CASS POST API - #1.1 (update order: JSON parse after upstream 404)
- User perform CASS POST API - #1.1 (store-status probe after update: `cass/orders/storeStatus/{uuid}`)

**Failure Pattern:**
Dependent steps failed because upstream create/update calls returned HTML 404 pages, leaving `uuid` undefined or causing RestAssured to attempt JSON parsing on an HTML body.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`

**Impact:** 3 failures

**Confidence:** High
