# Build Failure Report

**Build ID:** 315
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-07-16 21:02:21 UTC
**Status:** UNSTABLE
**Build URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/315/

---

## Build Summary

| Metric        | Count |
|---------------|-------|
| Total Tests   | 17    |
| Passed        | 7     |
| Failed        | 10    |
| Skipped       | 0     |
| Pass Rate     | 41%   |

---

## Failing Tests / Steps

All failures are in feature: `rialtoB2A(CASS).feature`

### HTTP 404 – CASS API Endpoints Not Found

| Scenario | Endpoint | Expected | Got |
|---|---|---|---|
| User perform CASS POST API (line 23) | `/cass/users/login` | 200 | 404 |
| User perform CASS POST API (line 45) | `/cass/orders/orders` | 202 | 404 |
| User perform CASS POST API (line 163) | `/cass/orders/calculatePrice` | 200 | 404 |
| User perform CASS POST API (line 164) | `/cass/orders/spaceAvailability` | 200 | 404 |
| User perform CASS GET API (line 178) | `/cass/orders/orders/1620` | 200 | 404 |
| User perform CASS GET API (line 191) | `/cass/staticData/validPackagesAndPlacements` | 200 | 404 |
| User perform CASS GET API (line 205) | `/cass/orders/orderHeaders` | 200 | 404 |

All 404 responses contain: *"The requested resource is not available"* (Apache Tomcat/9.0.73)

### Missing UUID Path Parameter (Cascade)

| Scenario | Request URI | Error |
|---|---|---|
| User perform CASS POST API (line 57) | `/cass/orders/storeStatus/{uuid}` | `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.` |
| User perform CASS POST API (line 109) | `/cass/orders/storeStatus/{uuid}` | Same as above |

### JSON Parse Failure (Cascade)

| Scenario | Error |
|---|---|
| User perform CASS POST API (line 85) | `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document` |

---

## Environment

- Base URI: `https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1`
- Tag filter: `@rialtoB2AAPIs`
- Feature file: `src/test/resources/features/rialtoB2A(CASS).feature`
- Build: Trunk / Linux / Jenkins
