# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #329

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 329 |
| **Date** | 2026-07-23 21:02:18 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~50 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/329/ |

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
| User perform CASS POST API - #1.1 | tc_postRialtoB2A01 | HTTP Status 404 – Not Found |
| User perform CASS POST API - #1.1 | tc_postRialtoB2A02 | HTTP Status 404 – Not Found |
| User perform CASS POST API - #1.1 | tc_postRialtoB2A03 | HTTP Status 404 – Not Found |
| User perform CASS POST API - #1.2 | tc_postRialtoB2A04 | HTTP Status 404 – Not Found |
| User perform CASS GET API - #1.1 | tc_getRialtoB2A01 | HTTP Status 404 – Not Found |
| User perform CASS GET API - #1.1 | tc_getRialtoB2A02 | HTTP Status 404 – Not Found |
| User perform CASS GET API - #1.1 | tc_getRialtoB2A04 | HTTP Status 404 – Not Found |

### Group 2 — Cascading failures after missing order identifier (3 failures)

| Scenario | Test Case | Error |
|---|---|---|
| User perform CASS POST API - #1.1 | tc_getRialtoB2A05 | Undefined path parameters: uuid |
| User perform CASS POST API - #1.1 | tc_getRialtoB2A06 | Undefined path parameters: uuid |
| User perform CASS POST API - #1.1 | tc_patchRialtoB2A01 | Failed to parse the JSON document |

---

## Key Evidence

- Request URI observed: `https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/users/login`
- Request URI observed: `https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/orders/orders`
- Error detail observed: `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available`
- Error detail observed: `The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/orders/orders] is not available`
