# Build 300 Root Cause Analysis

Source report: [build-300.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-300.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #300 finished `UNSTABLE` with 10 failed tests out of 17.
- Seven scenarios failed on status-code assertions because every CASS endpoint under `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat `404 Not Found`.
- Three additional failures were downstream cascades: a `uuid` path parameter was never captured from the failed upstream response, or an HTML error page was parsed as JSON.
- The same failure pattern recurred across builds 295, 298, and now 300, indicating a persistent environment issue rather than a transient outage.

## Root Cause

- **Primary:** CASS service routes (`/api/870/v1/cass/users/login`, `/api/870/v1/cass/orders/...`, `/api/870/v1/cass/staticData/...`) are unavailable in the target environment — Apache Tomcat returns `404 Not Found` for all of them.
- **Downstream:** Steps that depend on a `uuid` captured from a successful order-creation call receive no usable value; subsequent path-parameterised requests and JSON assertions fail as a result.
- Checkout revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (commit message: `updated api version from 87 to 88`) is the same revision used in build 298, suggesting the test code has not changed and the failure originates in the environment, not the automation.

## Affected Components

- CASS API routes under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- `rialtoB2A(CASS).feature` — scenarios: `User perform CASS POST API`, `User perform CASS GET API`
- RestAssured step definitions that extract `uuid` from the order-creation response and reuse it in subsequent requests

## Recommended Fix

- Verify the CASS service is deployed and reachable in the `crossadv.atex.com` environment under `/api/870/v1/cass/...`.
- Confirm the API version (`870`) matches what the environment currently exposes; possibly the deployment rolled back or was not promoted.
- Guard downstream steps so they skip or fail fast when a prerequisite call returns a non-2xx response, reducing cascade noise.

## Prevention

- Add a pre-flight health check for one CASS endpoint before the full feature runs; fail the build immediately if the check returns 404.
- Introduce a version/path compatibility assertion when the `crossad-integration-ws` base URI or API version is changed.
- Alert on repeated 404 patterns across consecutive builds to surface persistent environment regressions earlier.
