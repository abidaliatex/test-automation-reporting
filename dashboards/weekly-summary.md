# Weekly Test Failure Summary

**Period:** 2026-06-29 → 2026-07-05  
**Generated:** 2026-07-05  
**Total builds:** 2 | **Unstable builds:** 2 | **Pass rate (per test):** 78.6 %

---

## Failure Counts by Test Suite

| Test Suite | Failures this week | Failures last week | Trend |
|---|---|---|---|
| `CASS TC4 Change Placement` (MH readback — tc_getMHTC03) | 2 | 2 | → |
| `CASS TC4 Change Placement` (MH readback — tc_getMHTC03a) | 2 | 2 | → |
| `CASS TC4 Change Placement` (Rialto readback — tc_getIntegrationRialto05b) | 2 | 2 | → |

---

## Unstable Builds This Week

| Build | Date | Root Cause Summary | Investigation |
|---|---|---|---|
| [#261](../reports/build-failures/build-261.md) | 2026-07-05 | Cross-system discount/commission mismatch in Rialto↔MH placement-change flow | [analysis](../investigations/copilot-findings/build-261-analysis.md) |
| [#262](../reports/build-failures/build-262.md) | 2026-07-05 | Same 3 failures persist; commit "updated api version from 87 to 88" did not resolve | [analysis](../investigations/copilot-findings/build-262-analysis.md) |

---

## Key Observations

- The same 3 test cases (`tc_getMHTC03`, `tc_getMHTC03a`, `tc_getIntegrationRialto05b`) have been failing since build #246 — regression is persistent across API version bumps.
- Root cause is a cross-system field mapping issue: `discountType` is not propagated correctly, and `statusFlags`/`commissionAmount` are stale after MH applies placement changes.
- Build #262 upgraded the API version (87→88) but did not fix the underlying data sync problem.

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [#262](../reports/build-failures/build-262.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/build-262-analysis.md) |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
