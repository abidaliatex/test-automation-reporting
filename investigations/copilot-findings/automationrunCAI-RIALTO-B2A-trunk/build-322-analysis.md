# Root Cause Analysis — Build 322

**Source report:** [build-322.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-322.md)

---

## Summary

Build 322 of `automationrunCAI-RIALTO-B2A-trunk` is UNSTABLE with 10 failures out of 17 tests (41.2% pass rate). All failures originate from a single root cause: every CASS API endpoint under `/agency/crossad-integration-ws/api/870/v1/cass/` returned HTTP 404. Three additional cascade failures occurred because the `uuid` value was never populated after the failed create-order call.

This is a persistent failure pattern observed in multiple prior builds (e.g. #320, #319, #318), indicating a continuing infrastructure or deployment issue rather than a new code regression.

---

## Root Cause

**Primary:** The `crossad-integration-ws` service at API version `870` appears unresponsive or not deployed on the test environment (`crossadv.atex.com`). Apache Tomcat/9.0.73 returns a standard 404 "Not Found" response for every CASS endpoint — login, order creation, price calculation, space availability, static data, and order headers.

**Secondary (cascade):** Because the `POST /cass/orders/orders` call never returned a valid JSON body, the `uuid` path parameter used by subsequent GET/PATCH steps was never extracted. This caused `IllegalArgumentException: Undefined path parameters: uuid` and `JsonPathException: Failed to parse the JSON document` in dependent steps.

---

## Affected Components

- Feature file: `rialtoB2A(CASS).feature`
- Service: `crossad-integration-ws` (API version `870`, CASS module)
- Endpoints: `/cass/users/login`, `/cass/orders/orders`, `/cass/orders/calculatePrice`, `/cass/orders/spaceAvailability`, `/cass/orders/storeStatus/{uuid}`, `/cass/staticData/validPackagesAndPlacements`, `/cass/orders/orderHeaders`

---

## Recommended Fix

- Verify the `crossad-integration-ws` deployment on `crossadv.atex.com` — confirm the WAR/service is running and that API version `870` routes are accessible.
- Check whether a redeployment or context reload is required (server returned 404, not 503/502, suggesting the context may be missing rather than the service being down).
- Once the service is restored, re-run the pipeline to confirm cascading failures resolve automatically.

---

## Prevention

- Add a pre-flight health-check step in the pipeline that validates CASS endpoint availability before running the full suite, to distinguish infrastructure outages from test code failures.
- Implement test dependency handling so that scenarios depending on `uuid` are skipped (not failed) when the upstream create-order step has already failed.
