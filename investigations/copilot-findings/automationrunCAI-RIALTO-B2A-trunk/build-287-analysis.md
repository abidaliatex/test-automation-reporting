# Root Cause Analysis — Build 287

**Source Report:** [build-287.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-287.md)

---

## Summary

Build 287 of `automationrunCAI-RIALTO-B2A-trunk` is UNSTABLE with 10 of 17 tests failing (41.2% pass rate). Every failure is confined to the `rialtoB2A(CASS).feature` suite. The pattern is identical to builds 284–286: all CASS API endpoints under `/api/870/v1/cass/` return HTTP 404, and the three remaining failures cascade from missing `uuid` values and unparseable HTML error responses.

---

## Root Cause

**Primary — CASS service unavailable at API version 870**

The test run targets `https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1` (set via `-Dpom-baseuri-cai`). The last commit (`4a04ddba`, message: `"updated api version from 87 to 88"`) bumped the base URI from `api/87` to `api/870`. Apache Tomcat returns `404 Not Found` for every CASS endpoint under this path, indicating the CASS module is either not deployed at version `870` or the path mapping is incorrect.

**Secondary — Cascading uuid / JSON parse failures**

Three tests depend on a `uuid` extracted from the response of a prior order-creation call. Because that call returns an HTML 404 page, the `uuid` is never populated, causing:
- `IllegalArgumentException: Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `JsonPathException: Failed to parse the JSON document`

---

## Affected Components

- CASS integration service at `/agency/crossad-integration-ws/api/870/v1/cass/`
- Affected endpoints:
  - `POST cass/users/login`
  - `POST cass/orders/orders`
  - `POST cass/orders/calculatePrice`
  - `POST cass/orders/spaceAvailability`
  - `GET  cass/orders/orders/{id}`
  - `GET  cass/staticData/validPackagesAndPlacements`
  - `GET  cass/orders/orderHeaders`
  - `GET  cass/orders/storeStatus/{uuid}` (cascading)

---

## Recommended Fix

- Verify the correct API version path for the CASS service on the target environment; the commit changed `87` → `88` but the base URI was set to `870`, which may be a typo.
- If `api/88` is the intended version, update `-Dpom-baseuri-cai` to `…/api/88/v1` and redeploy or rerun the build.
- If `api/870` is intentional, ensure the CASS service is deployed and mapped at that path on `crossadv.atex.com`.

---

## Prevention

- Add a pre-flight health-check step that validates the base URI returns a non-404 before executing the full suite.
- Gate the API version bump commit with a smoke test against the target environment before merging.
