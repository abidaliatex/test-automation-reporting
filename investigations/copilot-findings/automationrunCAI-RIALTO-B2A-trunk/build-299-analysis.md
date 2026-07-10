# Root Cause Analysis — Build 299

**Source Report:** [build-299.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-299.md)  
**Job:** `automationrunCAI-RIALTO-B2A-trunk`  
**Build:** #299  
**Date:** 2026-07-10 16:23 UTC  
**Status:** UNSTABLE — 10 failed / 17 total (41.2% pass rate)

---

## Summary

All 10 failures are confined to the `rialtoB2A(CASS).feature` suite. Seven tests failed because every CASS REST endpoint returned HTTP 404, and three further tests failed as a downstream consequence of missing UUIDs or unparseable responses caused by those 404s. The pattern is identical to build #298, indicating the CASS integration layer (`/agency/crossad-integration-ws/api/870/v1/cass/…`) is persistently unavailable on the target server.

---

## Root Cause

**Primary:** CASS service endpoints are returning `HTTP 404 – Not Found` from Tomcat.  
All affected endpoints share the base path `/agency/crossad-integration-ws/api/870/v1/cass/`. A 404 at this level indicates the WAR/context is either not deployed, mis-configured, or was undeployed on the target server between build #298 and #299.

**Secondary:** Three scenarios that depend on a `uuid` value obtained from a prior successful POST received an invalid path parameter error (`Undefined path parameters are: uuid`) or a JSON parse failure because the prior POST returned an HTML 404 page instead of a JSON body.

---

## Affected Components

- CASS integration web service: `/agency/crossad-integration-ws/api/870/v1/cass/`
- Endpoints: `users/login`, `orders/orders`, `orders/calculatePrice`, `orders/spaceAvailability`, `orders/orders/{id}`, `staticData/validPackagesAndPlacements`, `orders/orderHeaders`, `orders/storeStatus/{uuid}`
- Test data files: `Rialto\RialtoB2A\postRialtoB2A.csv`, `Rialto\RialtoB2A\getRialtoB2A.csv`, `Rialto\RialtoB2A\patchRialtoB2A.csv`

---

## Recommended Fix

- Verify the `crossad-integration-ws` WAR is deployed and running on the target Tomcat instance.
- Check Tomcat server logs for deployment errors or context-path mismatches.
- Confirm the API version path (`/api/870/v1/`) matches the deployed version.

---

## Prevention

- Add a pre-flight health-check step in the pipeline that asserts the CASS base URL returns a non-404 before running the full suite.
- Alert on consecutive builds with the same 404 pattern (this is the second consecutive build affected).
