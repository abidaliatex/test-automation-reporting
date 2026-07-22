# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #327

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 327 |
| **Date** | 2026-07-22 21:02:18 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~49 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/327/ |

---

## Build Summary

| Metric | Count |
|---|---|
| Total Tests | 17 |
| Passed | 7 |
| Failed | 10 |
| Skipped | 0 |
| Pass Rate | 41.2% |

---

## Failing Tests / Steps

### rialtoB2A(CASS) — CASS POST API

| Test Case | Scenario | Failure Step | Error |
|---|---|---|---|
| tc_postRialtoB2A01 | Attempts to log in a user | `Then User verify the status code` | HTTP 404 – Not Found |
| tc_postRialtoB2A02 | Create ad for self service | `Then User verify the status code` | HTTP 404 – Not Found |
| tc_postRialtoB2A03 | Calculate price for self service | `Then User verify the status code` | HTTP 404 – Not Found |
| tc_postRialtoB2A04 | Queries space availability | `Then User verify the status code` | HTTP 404 – Not Found |
| tc_patchRialtoB2A01 | Update ad(Order) for self service | `When User perfrom "post" request … alterd IDs` | `Undefined path parameters: uuid` |
| tc_getRialtoB2A05 | Returns StoreStatus of Order | `When User perfrom "get" request with keys "uuid"` | `Undefined path parameters: uuid` / JSON parse failure |
| tc_getRialtoB2A06 | Returns StoreStatus of Update Order | `When User perfrom "get" request with keys "uuid"` | `Undefined path parameters: uuid` |

### rialtoB2A(CASS) — CASS GET API

| Test Case | Scenario | Failure Step | Error |
|---|---|---|---|
| tc_getRialtoB2A01 | Get order details using order ID | `Then User verify the status code` | HTTP 404 – Not Found |
| tc_getRialtoB2A02 | Returns package and placement data | `Then User verify the status code` | HTTP 404 – Not Found |
| tc_getRialtoB2A04 | Returns OrderHeader objects for orders associated with the user | `Then User verify the status code` | HTTP 404 – Not Found |

---

## Error Details

- **HTTP 404 – Not Found**: Apache Tomcat/9.0.73 returned a standard 404 for all CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/`. Affects login, order creation, price calculation, space availability, static data, and order headers.
- **`Undefined path parameters: uuid`**: After the failed create-order POST, no `uuid` was extracted from the response body. Subsequent steps that depend on `uuid` raised `IllegalArgumentException: Undefined path parameters: uuid`.
- **`Failed to parse the JSON document`**: A GET step attempted to parse a non-JSON 404 HTML response, producing a `JsonPathException`.
