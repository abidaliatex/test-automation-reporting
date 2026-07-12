# Build 307 Root Cause Analysis

Source report: [build-307.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-307.md)

## Summary

- Build `automationrunCAI-RIALTO-B2A-trunk` #307 finished `UNSTABLE` with 10 failed tests out of 17 (pass rate 41.2%).
- All direct failures are CASS API calls returning HTTP 404 instead of the expected success responses.
- Three additional failures are downstream cascades caused by missing `uuid` values and unparseable JSON bodies.
- The failure signature is identical to build #306, indicating a persistent environment issue rather than a transient flake.

## Root Cause

- **Primary:** All seven direct failures are caused by CASS routes returning `HTTP Status 404 – Not Found` (Apache Tomcat/9.0.73). The affected routes span login, order creation, price calculation, space availability, static data, and order-header endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/...`. This consistently suggests the CASS service context or deployment is missing/misconfigured on the target server for this job.
- **Secondary:** Three dependent scenarios (`tc_getRialtoB2A05`, `tc_patchRialtoB2A01`, `tc_getRialtoB2A06`) fail because `uuid` was never stored from the failed upstream POST, resulting in unresolved path parameters and JSON parse failures on HTML error bodies.

## Affected Components

- `rialtoB2A(CASS).feature`
- Test data: `postRialtoB2A.csv`, `getRialtoB2A.csv`, `patchRialtoB2A.csv`
- CASS service routes under `/agency/crossad-integration-ws/api/870/v1/cass/`

## Recommended Fix

- Verify that the CASS service (`crossad-integration-ws`) is deployed and accessible at context path `/api/870/v1/cass/` in the B2A-trunk test environment.
- Confirm endpoint configuration values in the test data CSVs match the actual deployment.
- Add a pipeline pre-check step that validates CASS service availability before running test scenarios.

## Prevention

- Add a lightweight CASS health-check gate in the pipeline to fail fast when the service is unreachable, avoiding cascading downstream failures.
- Track consecutive 404 signatures across builds (#306, #307) and raise an alert to the environment team when the pattern repeats.
