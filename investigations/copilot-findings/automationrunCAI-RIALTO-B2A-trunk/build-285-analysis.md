# Build 285 Root Cause Analysis

Source report: [build-285.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-285.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #285 finished `UNSTABLE` with 10 failed tests out of 17 (41.2% pass rate).
- This is a recurrence of the same failure pattern seen in build 284 — all CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...` return Tomcat HTTP 404 responses.
- The same revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (commit: `updated api version from 87 to 88`) is still checked out; the root cause from build 284 has not been resolved.
- Three additional failures are downstream symptoms: missing `uuid` path parameters and an HTML body parsed as JSON.

## Root Cause

- All primary failures share a single root cause: the CASS service routes under `/api/870/v1/cass/...` are not registered/deployed on the target server for the v88 API version.
- Apache Tomcat/9.0.73 returns `404 – The requested resource is not available` for every CASS endpoint (`/users/login`, `/orders/orders`, `/orders/calculatePrice`, `/orders/spaceAvailability`, `/staticData/validPackagesAndPlacements`, `/orders/orderHeaders`).
- The issue persists across at least two consecutive builds (284 and 285), confirming this is not a transient failure.

## Affected Components

- CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- `rialtoB2A(CASS)` POST and GET scenario flows
- Downstream RestAssured steps that depend on a UUID extracted from `cass/orders/orders` response and JSON response bodies

## Recommended Fix

- Verify the CASS service deployment for v88: confirm that the routes under `/api/870/v1/cass/...` are exposed and that the service is running with the correct version mapping.
- If v88 uses a different base path, update the test configuration property `pom-baseuri-cai` accordingly.
- After resolving the 404s, re-run to confirm the `uuid`-dependent and JSON-parsing failures recover without further test changes.

## Prevention

- Add a pre-flight smoke check for one CASS login endpoint after any API version bump; fail fast before running the full suite.
- Mark downstream steps as "pending prerequisite" rather than letting them emit secondary `IllegalArgumentException`/`JsonPathException` errors when a required path variable was never populated.
