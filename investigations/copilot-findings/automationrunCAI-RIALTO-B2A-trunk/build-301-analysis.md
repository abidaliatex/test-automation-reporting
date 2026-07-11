# Build 301 Root Cause Analysis

Source report: [build-301.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-301.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #301 finished `UNSTABLE` with 10 failed tests out of 17 (pass rate 41.2%).
- Seven scenarios failed on status-code assertions because CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat `404 Not Found`.
- Three additional failures were downstream cascade effects: `uuid` was never captured from a failed upstream create call, or HTML error pages were parsed as JSON.
- The failure pattern is identical to builds 284, 285, 286, 295, and 298 — the CASS route under `/api/870/v1/cass` has been consistently unavailable across multiple runs.

## Root Cause

- **Primary:** CASS routes under `/agency/crossad-integration-ws/api/870/v1/cass/...` are not reachable on the test target (environment `870`). All login, order, pricing, space-availability, order-detail, static-data, and order-header calls returned HTTP 404 from Apache Tomcat/9.0.73.
- **Downstream:** Later GET/PATCH steps depend on data (`uuid`) from the failed upstream calls, leaving the path parameter undefined and causing JSON-parsing exceptions when HTML error bodies are processed.
- The failure is recurring; it may indicate the CASS service is not deployed or the API version path (`/api/870/`) is incorrect for the current environment.

## Affected Components

- CASS API routes under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- `rialtoB2A(CASS).feature` scenarios backed by `postRialtoB2A.csv`, `getRialtoB2A.csv`, and `patchRialtoB2A.csv`
- RestAssured step definitions that resolve `{uuid}` path parameters from prior response data

## Recommended Fix

- Verify that the CASS service is deployed and the `/api/870/v1/cass/...` context path is registered in the target environment.
- Confirm the environment configuration (base URI, API version segment) matches the running deployment.
- Add a guard in dependent steps to skip or fail fast when the upstream `uuid` is missing, to reduce cascade noise.

## Prevention

- Add a pre-flight smoke test for one critical CASS endpoint before executing the full suite.
- Alert when the same CASS route fails for more than two consecutive builds to surface environment issues earlier.
