# Build 311 — Root Cause Analysis

**Source report:** [build-311.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-311.md)

---

## Summary

Build 311 of `automationrunCAI-RIALTO-B2A-trunk` is UNSTABLE: 10 of 17 tests failed (41.2% pass rate). All failures are confined to the `rialtoB2A(CASS)` suite. The failure pattern is identical to builds 308–310, indicating a persistent environment issue rather than a new code regression.

---

## Root Cause

**Primary — CASS API context unreachable (HTTP 404)**

All seven direct-call failures received an Apache Tomcat 404 HTML response from the CAI base URI (`/agency/crossad-integration-ws/api/870/v1/cass/...`). This indicates the CASS module is not deployed or is not routed correctly on the test server at the time of the run.

**Secondary — Cascade failures due to missing `uuid`**

Three further tests that depend on a `uuid` extracted from the response of an earlier (failing) POST call fail with:
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `JsonPathException: Failed to parse the JSON document` (HTML 404 body cannot be parsed as JSON)

These are cascade failures; fixing the primary issue will resolve them automatically.

---

## Affected Components

- CASS login endpoint: `/cass/users/login`
- CASS order endpoints: `/cass/orders/orders`, `/cass/orders/calculatePrice`, `/cass/orders/spaceAvailability`, `/cass/orders/orders/{uuid}`, `/cass/orders/orderHeaders`
- CASS static-data endpoint: `/cass/staticData/validPackagesAndPlacements`

---

## Recommended Fix

- Verify that the CASS module is deployed and running on `crossadv.atex.com` for the `api/870/v1` context path.
- Check Apache Tomcat deployment logs for the CASS web application context.
- Confirm the base URI configured in the pipeline (`-Dpom-baseuri-cai`) matches the active deployment path.

---

## Prevention

- Add a pre-flight health-check step in the pipeline that validates CASS endpoint availability before running the full suite.
- Alert on repeated 404s across consecutive builds to distinguish environment outages from code regressions sooner.
