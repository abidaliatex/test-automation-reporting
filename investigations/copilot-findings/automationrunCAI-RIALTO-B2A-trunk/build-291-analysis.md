# Build 291 Root Cause Analysis

Source report: [build-291.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-291.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #291 finished `UNSTABLE` with 10 failed tests out of 17 (41.2% pass rate).
- Seven scenarios failed immediately because CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...` returned Tomcat HTTP 404 pages.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`, matching the same failure pattern already seen in recent builds for this job.
- The remaining three failures are downstream symptoms caused by missing `uuid` values and an HTML error page being parsed as JSON.

## Root Cause

- The primary issue is an unavailable or misrouted CASS API path for `/api/870/v1/cass/...`.
- Login, order creation, pricing, space availability, static-data, and order-header requests all failed with `404 Not Found`, which points to a shared deployment or routing problem rather than isolated test-data errors.
- After the create/update flow failed, dependent steps could not substitute `uuid` into `storeStatus/{uuid}` and update flows could not parse the HTML error body as JSON.

## Affected Components

- CASS routes under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- `rialtoB2A(CASS).feature`
- Downstream RestAssured steps that depend on a created order UUID and JSON response payloads

## Recommended Fix

- Verify that the deployed CASS service exposes the routes expected by this suite under `/api/870/v1/cass/...`.
- If the v87 → v88 change altered the effective base path, update the Jenkins job configuration before rerunning the suite.

## Prevention

- Add a lightweight pre-flight smoke call for one CASS login endpoint after API version changes so route issues fail fast.
- Mark UUID-dependent steps as blocked when the prerequisite order call fails to reduce secondary noise.
