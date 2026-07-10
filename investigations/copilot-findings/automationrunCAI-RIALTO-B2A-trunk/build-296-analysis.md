# Root Cause Analysis — `automationrunCAI-RIALTO-B2A-trunk` Build #296

**Source report:** [build-296.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-296.md)  
**Date:** 2026-07-10  
**Build URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/296/

---

## Summary

Build #296 is UNSTABLE with 10 failures out of 17 tests (41.2% pass rate). All 10 failures are concentrated in the `rialtoB2A(CASS)` suite. 7 failures are direct HTTP 404 responses from every CASS API endpoint under `/api/870/v1/cass/`; the remaining 3 are cascading failures caused by the upstream login endpoint returning no valid JSON, leaving the `uuid` path parameter unpopulated.

---

## Root Cause

**Primary:** The `crossad-integration-ws` CASS service at context path `/agency/crossad-integration-ws/api/870/v1/cass/` is not deployed or not reachable on the test target server (`crossadv.atex.com`). Apache Tomcat/9.0.73 returns a standard HTML 404 for every CASS route, indicating the WAR/context is missing or has not started correctly.

**Secondary (cascading):** The CASS login step (`/cass/users/login`) is the first step in the scenario chain. When login returns a 404 HTML page instead of JSON, the `uuid` field cannot be extracted. Subsequent steps that reference `{uuid}` as a path parameter fail with `IllegalArgumentException: Invalid number of path parameters. Expected 1, was 0.` One step also attempts to parse the HTML error body as JSON, raising `JsonPathException: Failed to parse the JSON document`.

This is identical to the failure pattern observed in build #295, suggesting the CASS service has been unavailable since at least that build.

---

## Affected Components

- `crossad-integration-ws` — CASS module (deployment on `crossadv.atex.com`)
- Endpoints: `users/login`, `orders/orders`, `orders/calculatePrice`, `orders/spaceAvailability`, `orders/orders/{id}`, `staticData/validPackagesAndPlacements`, `orders/orderHeaders`
- Test suite: `rialtoB2A(CASS)` — scenarios `tc_postRialtoB2A01` through `tc_getRialtoB2A06`

---

## Recommended Fix

- Verify the `crossad-integration-ws` application is deployed and running on the target Tomcat instance at `crossadv.atex.com`.
- Check Tomcat server logs for startup errors or context deployment failures for the `/api/870/v1/cass/` context.
- Confirm the API version (`870`) used by the test suite matches the deployed version.

---

## Prevention

- Add a pre-flight health-check step in the pipeline that asserts `GET /api/870/v1/cass/` returns a non-404 before running the full suite.
- Alert on consecutive builds with identical 404 failure patterns to detect persistent deployment issues sooner.
