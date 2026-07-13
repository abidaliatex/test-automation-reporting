# Build 310 Root Cause Analysis

Source report: [build-310.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-310.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #310 finished `UNSTABLE` with 10 failed tests out of 17 (pass rate 41.2%).
- The dominant pattern is CASS API calls returning HTTP 404 instead of success responses.
- Remaining failures are downstream effects where `uuid` was missing or HTML error output was parsed as JSON.
- This failure signature is identical to builds 305–309, indicating a persistent environment issue with CASS route availability.

## Root Cause

- **Primary:** Multiple CASS API routes under `/agency/crossad-integration-ws/api/870/v1/cass/` returned `HTTP 404 – Not Found`, indicating the CASS service is unavailable or its routes are not registered on the test environment.
- **Secondary:** Dependent GET/PATCH scenarios (`tc_getRialtoB2A05`, `tc_patchRialtoB2A01`, `tc_getRialtoB2A06`) reused data from failed upstream calls and failed with a missing `uuid` path parameter or non-JSON response bodies.

## Affected Components

- `rialtoB2A(CASS).feature`
- Test data sets: `postRialtoB2A.csv`, `getRialtoB2A.csv`, `patchRialtoB2A.csv`
- API base URI: `https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1`
- CASS routes: `/cass/users/login`, `/cass/orders/*`, `/cass/staticData/*`

## Recommended Fix

- Verify that the CASS service is deployed and reachable at the expected base URI on the test environment.
- Confirm route registration for `/cass/` endpoints in Apache Tomcat/9.0.73.
- Add an early guard to stop dependent steps when `uuid` is not populated from upstream responses.

## Prevention

- Add a lightweight CASS endpoint health check in pipeline setup to fail fast when routes return 404.
- Track repeated identical failure signatures across consecutive builds (305–310 are identical) and alert on recurrence.
