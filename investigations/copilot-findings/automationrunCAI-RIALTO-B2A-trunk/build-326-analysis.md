# Root Cause Analysis — Build 326

**Source report:** [build-326.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-326.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #326
Total Tests: 17
Passed: 7
Failed: 10
Pass Rate: 41.2%

---

## Root Cause Groups

---

## Root Cause 1 — CASS Service Unavailable (HTTP 404)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Attempts to log in a user (tc_postRialtoB2A01)
- Create ad for self service (tc_postRialtoB2A02)
- Calculate price for self service (tc_postRialtoB2A03)
- Queries space availability (tc_postRialtoB2A04)
- Get order details using order ID (tc_getRialtoB2A01)
- Returns package and placement data (tc_getRialtoB2A02)
- Returns OrderHeader objects for orders associated with the user (tc_getRialtoB2A04)

**Failure Pattern:**
Apache Tomcat/9.0.73 returns `HTTP Status 404 – Not Found` for every CASS endpoint under `/agency/crossad-integration-ws/api/870/v1/cass/`.

**Evidence:**
- `tc_postRialtoB2A01` — POST `/cass/users/login` → 404
- `tc_postRialtoB2A02` — POST `/cass/orders/orders` → 404
- `tc_postRialtoB2A03` — POST `/cass/orders/calculatePrice` → 404
- `tc_postRialtoB2A04` — POST `/cass/orders/spaceAvailability` → 404
- `tc_getRialtoB2A01` — GET `/cass/orders/orders/{uuid}` → 404
- `tc_getRialtoB2A02` — GET `/cass/staticData/validPackagesAndPlacements` → 404
- `tc_getRialtoB2A04` — GET `/cass/orders/orderHeaders` → 404

**Impact:** 7 direct failures

**Confidence:** High

---

## Root Cause 2 — Cascade: Missing `uuid` Path Parameter

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)
- Update ad(Order) for self service (tc_patchRialtoB2A01)

**Failure Pattern:**
`Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid` / `Failed to parse the JSON document`

**Evidence:**
- `tc_postRialtoB2A02` (Create ad) returned 404 → `uuid` was never stored
- `tc_getRialtoB2A05` — GET `/cass/orders/storeStatus/{uuid}` raised `IllegalArgumentException: Undefined path parameters: uuid`
- `tc_getRialtoB2A06` — same `uuid` lookup failure on update-order status
- `tc_patchRialtoB2A01` — PATCH used altered IDs from the missing ad → `uuid` unresolved; additionally `JsonPathException: Failed to parse the JSON document` on the 404 HTML body

**Impact:** 3 cascade failures (all downstream of Root Cause 1)

**Confidence:** High

---

## Summary

- **Primary root cause:** `crossad-integration-ws` at API version `870` is not responding on `crossadv.atex.com`. All 7 direct 404 failures share the same Tomcat 404 HTML response, indicating the WAR context is missing or not deployed.
- **Secondary root cause:** 3 additional failures cascade from the missing `uuid` that would have been returned by the failed create-order call.
- This pattern is consistent with prior builds #320–#324, indicating a persistent environment/deployment issue.
