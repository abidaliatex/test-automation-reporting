# Build 295 Root Cause Analysis

Source report: [build-295.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-295.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #295 finished `UNSTABLE` with 10 failed tests out of 17.
- Seven scenarios failed on status-code checks because CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat HTTP 404 pages.
- Three additional failures are downstream effects where `uuid` was missing or an HTML error response was parsed as JSON.

## Root Cause

- Primary failure: CASS routes used by this suite were unavailable (`404 Not Found`) for login, order creation, pricing, space availability, order details, static data, and order headers.
- Downstream failure: later GET/PATCH steps depend on data from the failed upstream calls, leading to undefined `uuid` parameters and JSON parsing exceptions.
- Jenkins build metadata shows revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`, consistent with this recurring route/version mismatch pattern.

## Affected Components

- CASS API routes under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- `rialtoB2A(CASS).feature` POST/GET/PATCH scenarios in `postRialtoB2A.csv`, `getRialtoB2A.csv`, and `patchRialtoB2A.csv`
- RestAssured path-parameter and JSON parsing steps that rely on successful prior order responses

## Recommended Fix

- Verify the API gateway/service deployment exposes the `/api/870/v1/cass/...` routes expected by this job.
- Confirm environment configuration aligns with the API version update and rerun after endpoint routing is restored.
- Gate dependent `uuid` scenarios when prerequisite creation/update responses fail to reduce cascade noise.

## Prevention

- Add a pre-flight check for one critical CASS endpoint before running the full feature set.
- Track API version bumps with a compatibility check in pipeline validation to catch route/path drift early.
