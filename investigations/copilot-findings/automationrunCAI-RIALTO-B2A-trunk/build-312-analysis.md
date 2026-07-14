# Root Cause Analysis — Build 312

**Source Report:** [build-312.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-312.md)

---

## Summary

Build 312 of `automationrunCAI-RIALTO-B2A-trunk` is UNSTABLE with 10 failures out of 17 tests (41.2% pass rate). All failures are confined to the `rialtoB2A(CASS)` suite. The failure pattern is identical to builds 306–310, indicating a persistent environment issue rather than a regression introduced in this run.

---

## Root Cause

All 10 failures trace to two cascading causes:

1. **CASS API endpoints returning HTTP 404** — Apache Tomcat/9.0.73 responds with a "Not Found" status page for every CASS resource under `/agency/crossad-integration-ws/api/870/v1/cass/`. This strongly indicates the `crossad-integration-ws` web application is not deployed or is mis-routed on the target server for context path `870`.
2. **Downstream cascade failures** — Once the login step fails (no `uuid` extracted), subsequent steps that reference `{uuid}` as a path parameter throw `IllegalArgumentException`, and steps trying to parse the previous non-JSON 404 response throw `JsonPathException`.

---

## Affected Components

- CASS integration API module under context `/agency/crossad-integration-ws/api/870/v1/cass/`
- Endpoints: `users/login`, `orders/orders`, `orders/calculatePrice`, `orders/spaceAvailability`, `orders/orders/{uuid}`, `staticData/validPackagesAndPlacements`, `orders/orderHeaders`

---

## Recommended Fix

- Verify that `crossad-integration-ws` is correctly deployed on the test server for API version context `870`.
- Confirm the Tomcat application context path and URL mapping match the test configuration.
- Re-deploy or restart the application if necessary before re-running the suite.

---

## Prevention

- Add a pre-flight health-check step in the pipeline that verifies CASS endpoint reachability before executing the full suite; fail fast with a clear environment error instead of cascading test failures.
