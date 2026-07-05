# Build 280 Root Cause Analysis

Source report: [build-280.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-280.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #280 finished `UNSTABLE` with 10 failures out of 17 tests (41.2% pass rate).
- All 7 direct `HTTP 404` failures target the path `/agency/crossad-integration-ws/api/870/v1/cass/…`; the remaining 3 failures are cascading consequences of those 404s.
- The `failedSince` values (`231` and `265`) indicate two separate waves of failures, both persistent and unresolved across many builds.

## Root Cause

- **Primary:** The API version segment `870` in the base URL is not reachable in the test environment. Every CASS endpoint under this path returns `HTTP 404 – Not Found` from Apache Tomcat. This may mean: (a) API version `870` was never deployed to the target server, (b) the version number in the test configuration is incorrect, or (c) the context root was changed.
- **Cascading:** Steps that depend on a `uuid` or order data populated by earlier failed steps inherit those failures — the `uuid` path parameter is never set and the JSON document cannot be constructed.

## Affected Components

- All CASS API endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/`
- Test configuration — base URL / API version number
- Context-sharing between sequential test steps (uuid propagation)

## Recommended Fix

- Confirm the deployed API version number in the target environment and align the test base URL configuration to match.
- If API version `870` is intentionally the target, confirm the deployment reached the server being tested.
- Once the 404 root cause is resolved, the cascading `uuid`/JSON-parse failures should self-correct.

## Prevention

- Add a pre-flight smoke check that verifies the CASS login endpoint returns `200` before running the full suite.
- Treat recurring `failedSince` counts beyond 10 builds as a blocking issue requiring a dedicated fix ticket.
