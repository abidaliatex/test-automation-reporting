# Root Cause Analysis — Build 323

**Source report:** [build-323.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-323.md)

---

## Summary

Build 323 of `automationrunCAI-RIALTO-B2A-trunk` is UNSTABLE with 10 failures out of 17 tests (41.2% pass rate). All failures stem from a single infrastructure root cause: every CASS API endpoint under `/agency/crossad-integration-ws/api/870/v1/cass/` returned HTTP 404. Two additional cascade failures occurred because the `uuid` value was never populated after the failed create-order call. This is a persistent pattern seen across multiple prior builds (#320, #321, #322), indicating a continuing deployment/environment issue.

---

## Root Cause Groups

## CASS Service Unavailable (HTTP 404)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Attempts to log in a user (tc_postRialtoB2A01)
- Create ad for self service (tc_postRialtoB2A02)
- Calculate price for self service (tc_postRialtoB2A03)
- Queries space availability (tc_postRialtoB2A04)
- get order details using order ID (tc_getRialtoB2A01)
- Returns package and placement data (tc_getRialtoB2A02)
- Returns OrderHeader objects for orders associated with the user (tc_getRialtoB2A04)

**Failure Pattern:**
HTTP 404 – The requested resource is not available (expected 200/202, found 404)

**Evidence:**
- `GET /cass/users/login` → 404 – "The requested resource [/agency/crossad-integration-ws/api/870/v1/cass/users/login] is not available"
- `POST /cass/orders/orders` → 404 – resource not available
- `POST /cass/orders/calculatePrice` → 404 – resource not available
- `POST /cass/orders/spaceAvailability` → 404 – resource not available
- `GET /cass/orders/orders/1620` → 404 – resource not available
- `GET /cass/staticData/validPackagesAndPlacements` → 404 – resource not available
- Server: Apache Tomcat/9.0.73 (standard 404, not 503 — suggests context/deployment missing)

**Impact:** 7 direct failures

**Confidence:** High

---

## UUID Cascade Failures (Downstream of CASS 404)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Update ad(Order) for self service (tc_patchRialtoB2A01)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
`IllegalArgumentException: Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

**Evidence:**
- `tc_postRialtoB2A02` (Create ad) failed with 404 → `uuid` never extracted from response
- `GET /cass/orders/storeStatus/{uuid}` called with empty `uuid` → `IllegalArgumentException` at feature line 57
- `GET /cass/orders/storeStatus/{uuid}` called with empty `uuid` → `IllegalArgumentException` at feature line 109
- `patchRialtoB2A01` failed to obtain a new `uuid` from PATCH step → downstream GET also failed

**Impact:** 3 cascade failures

**Confidence:** High

---

## Root Cause

The `crossad-integration-ws` service at API version `870` is not deployed or not accessible on `crossadv.atex.com`. Tomcat returns HTTP 404 (not 503/502), which indicates the WAR context is missing or undeployed — the server is reachable but has no handler for the CASS routes.

## Affected Components

- Feature: `rialtoB2A(CASS).feature`
- Service: `crossad-integration-ws` (API version `870`, CASS module)
- Endpoints: `/cass/users/login`, `/cass/orders/orders`, `/cass/orders/calculatePrice`, `/cass/orders/spaceAvailability`, `/cass/orders/storeStatus/{uuid}`, `/cass/staticData/validPackagesAndPlacements`, `/cass/orders/orderHeaders`

## Recommended Fix

- Verify and redeploy `crossad-integration-ws` WAR on `crossadv.atex.com` — confirm API version `870` context is active.
- Re-run the pipeline after service restoration to confirm all cascade failures resolve automatically.

## Prevention

- Add a pre-flight health-check step that validates CASS endpoint availability before the full suite runs.
- Implement test dependency handling so `uuid`-dependent scenarios are skipped rather than failed when the upstream create-order step has already failed.
