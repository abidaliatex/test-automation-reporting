# Root Cause Analysis — Build 303

**Source report:** [build-303.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-303.md)

---

## Summary

Build 303 of `automationrunCAI-RIALTO-B2A-trunk` is UNSTABLE with 10 failures out of 17 tests (41.2% pass rate). All failures are confined to the `rialtoB2A(CASS)` feature. The pattern is identical to build 302 — every CASS API endpoint returns HTTP 404, and downstream steps that depend on a `uuid` from a prior response then fail with cascade errors.

---

## Root Cause

**Primary:** CASS integration service endpoints under `/agency/crossad-integration-ws/api/870/v1/cass/` are returning HTTP 404. Apache Tomcat/9.0.73 reports "the requested resource is not available", indicating the CASS module is either not deployed, not started, or the context path has changed on the target environment.

**Secondary (cascade):** Steps that extract a `uuid` from a prior create-order response cannot proceed because that response was a 404 HTML page rather than JSON. This causes:
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- `Failed to parse the JSON document`

---

## Affected Components

- CASS integration endpoints: `users/login`, `orders/orders`, `orders/calculatePrice`, `orders/spaceAvailability`, `orders/orders/{id}`, `staticData/validPackagesAndPlacements`, `orders/orderHeaders`
- Test class: `rialtoB2A(CASS)`
- API context root: `/agency/crossad-integration-ws/api/870/v1/cass/`

---

## Recommended Fix

- Verify the CASS module is deployed and running on the target server (`api/870`).
- Confirm the context path `/agency/crossad-integration-ws/api/870/v1/cass/` has not changed.
- Re-run the build once the service is confirmed available; cascade failures will resolve automatically.

---

## Prevention

- Add a pre-flight health-check step to the pipeline that validates CASS endpoint availability before executing the full scenario suite.
- Monitor for recurring 404s across consecutive builds (builds 302 and 303 show the same failure pattern) to detect persistent environment outages early.
