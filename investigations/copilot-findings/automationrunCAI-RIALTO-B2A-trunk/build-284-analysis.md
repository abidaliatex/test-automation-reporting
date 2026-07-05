# Build 284 Root Cause Analysis

Source report: [build-284.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-284.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #284 finished `UNSTABLE` with 10 failed checks out of 17.
- Seven scenarios failed immediately with Tomcat 404 responses from `/agency/crossad-integration-ws/api/870/v1/cass/...`.
- The checked-out revision was `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.
- The remaining three failures are downstream symptoms: missing `uuid` path parameters and an HTML response parsed as JSON.

## Root Cause

- The strongest evidence points to an API routing/version drift introduced around the v87 → v88 change.
- Core login, order, pricing, static-data, and order-header endpoints all returned 404s on `/api/870/v1/cass/...`, which suggests the configured route is unavailable rather than a single test-data issue.
- Once those prerequisite calls failed, later steps no longer had a valid created order or JSON payload, which explains the missing `uuid` and JSON parsing failures.

## Affected Components

- CASS endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...`
- `rialtoB2A(CASS)` POST and GET scenario flows
- Downstream RestAssured steps that depend on a created order UUID and JSON response bodies

## Recommended Fix

- Verify the correct CASS base path/version for the v88 rollout and restore/update the unavailable login, order, pricing, and static-data routes.
- After the 404 issue is fixed, re-run `tc_getRialtoB2A05`, `tc_patchRialtoB2A01`, and `tc_getRialtoB2A06` to confirm they recover without further test changes.

## Prevention

- Add a small smoke check for one login endpoint and one order endpoint whenever the API version is bumped.
- Fail fast on non-JSON prerequisite responses so downstream UUID-dependent scenarios are marked as cascading rather than producing secondary errors.
