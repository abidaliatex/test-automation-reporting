# Root Cause Analysis — `automationrunCAI-RIALTO-B2A-trunk` Build #310

**Source Report:** [build-310.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-310.md)

---

## Summary

Build #310 (2026-07-13 22:35 UTC) is the **16th consecutive UNSTABLE build** of `automationrunCAI-RIALTO-B2A-trunk`. The failure pattern is identical to builds #284–#309: all 7 direct CASS API calls return HTTP 404, and 3 dependent scenarios cascade-fail due to an unresolved `uuid`. No new failure modes or improvements were observed.

---

## Root Cause

The CASS API base path `/agency/crossad-integration-ws/api/870/v1/cass/` is not reachable on the test environment. All POST and GET calls targeting environment `870` respond with an HTML 404 page instead of JSON. This has been the consistent root cause since build #284 (2026-07-05) and correlates with the v87 → v88 API version upgrade, which appears to have broken or removed the `870` route mapping.

---

## Affected Components

- `rialtoB2A(CASS).feature` — all CASS-dependent scenarios
- Environment `870` CASS API route (`/api/870/v1/cass/`)
- Tests: `tc_postRialtoB2A01`–`tc_postRialtoB2A04`, `tc_getRialtoB2A01`, `tc_getRialtoB2A02`, `tc_getRialtoB2A04` (direct); `tc_getRialtoB2A05`, `tc_getRialtoB2A06`, `tc_patchRialtoB2A01` (cascade)

---

## Recommended Fix

- Investigate the route/gateway configuration for the v88 release on environment `870` — the `/api/870/v1/cass/` path mapping is absent or misconfigured.
- Confirm whether a new base path was introduced in v88 and update the test configuration to match, or restore the `870` route in the environment deployment.
- This issue has persisted across 16 builds without remediation; escalation is strongly recommended if not already tracked.

---

## Prevention

- Add a smoke-test health check for CASS endpoint availability before running the full regression suite, to surface routing gaps immediately after deployments.
- Gate deployments to test environments on a basic route-reachability check for all versioned API paths.
