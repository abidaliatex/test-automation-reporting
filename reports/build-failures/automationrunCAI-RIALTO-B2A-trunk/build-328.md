# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #328

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 328 |
| **Date** | 2026-07-22 22:35:06 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~51 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/328/ |

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

| Test Case | Failure Step | Error |
|---|---|---|
| User perform CASS POST API - #1.1 | `Then User verify the status code` | HTTP 404 – `/cass/users/login` not found |
| User perform CASS POST API - #1.1 | `Then User verify the status code` | HTTP 404 – `/cass/orders/orders` not found |
| User perform CASS POST API - #1.1 | `When User perfrom request … alterd IDs` | `Undefined path parameters: uuid` |
| User perform CASS POST API - #1.1 | `When User perfrom request … alterd IDs` | `Failed to parse the JSON document` |
| User perform CASS POST API - #1.1 | `When User perfrom request … alterd IDs` | `Undefined path parameters: uuid` |
| User perform CASS POST API - #1.1 | `Then User verify the status code` | HTTP 404 – `/cass/orders/calculatePrice` not found |
| User perform CASS POST API - #1.2 | `Then User verify the status code` | HTTP 404 – `/cass/orders/spaceAvailability` not found |

### rialtoB2A(CASS) — CASS GET API

| Test Case | Failure Step | Error |
|---|---|---|
| User perform CASS GET API - #1.1 | `Then User verify the status code` | HTTP 404 – `/cass/orders/orders/1620` not found |
| User perform CASS GET API - #1.1 | `Then User verify the status code` | HTTP 404 – `/cass/staticData/validPackagesAndPlacements` not found |
| User perform CASS GET API - #1.1 | `Then User verify the status code` | HTTP 404 – `/cass/orders/orderHeaders` not found |

---

## Error Details

- **HTTP 404 – Not Found**: Apache Tomcat/9.0.73 returned 404 for all CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/`. Affected paths: `users/login`, `orders/orders`, `orders/calculatePrice`, `orders/spaceAvailability`, `orders/orders/{id}`, `staticData/validPackagesAndPlacements`, `orders/orderHeaders`.
- **`Undefined path parameters: uuid`**: After the failed create-order POST, no `uuid` was extractable from the (HTML) error response. Subsequent steps depending on `uuid` raised `IllegalArgumentException: Undefined path parameters: uuid`.
- **`Failed to parse the JSON document`**: A GET step attempted JSON parsing on a non-JSON HTML 404 response, producing a `JsonPathException`.
