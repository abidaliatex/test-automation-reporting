# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #330

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 330 |
| **Date** | 2026-07-23 22:35:20 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~53 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/330/ |

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

### Group 1 — CASS endpoint responses returned HTTP 404 (7 failures)

| Scenario | Test Case | Error |
|---|---|---|
| Attempts to log in a user | tc_postRialtoB2A01 | HTTP Status 404 – Not Found |
| Create ad for self service | tc_postRialtoB2A02 | HTTP Status 404 – Not Found |
| Calculate price for self service | tc_postRialtoB2A03 | HTTP Status 404 – Not Found |
| Queries space availability | tc_postRialtoB2A04 | HTTP Status 404 – Not Found |
| get order details using order ID | tc_getRialtoB2A01 | HTTP Status 404 – Not Found |
| Returns package and placement data | tc_getRialtoB2A02 | HTTP Status 404 – Not Found |
| Returns OrderHeader objects for orders associated with the user. | tc_getRialtoB2A04 | HTTP Status 404 – Not Found |

### Group 2 — Cascading failures after missing order identifier (3 failures)

| Scenario | Test Case | Error |
|---|---|---|
| Returns StoreStatus of Order | tc_getRialtoB2A05 | Undefined path parameters: uuid |
| Returns StoreStatus of Update Order | tc_getRialtoB2A06 | Undefined path parameters: uuid |
| Update ad(Order) for self service | tc_patchRialtoB2A01 | Failed to parse the JSON document |

---

## Key Evidence

- `Request URI: https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/users/login`
- `Request URI: https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/orders/orders`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/storeStatus/%7Buuid%7D]` failed after `uuid` was not populated
