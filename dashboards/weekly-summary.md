# Weekly Test Failure Summary

**Period:** 2026-07-04 → 2026-07-11  
**Generated:** 2026-07-11  
**Observed builds:** 14 | **Failed/Unstable builds:** 14 | **Jobs affected:** 3

---

## Failure Counts by Test Pattern

| Test Pattern | Failing tests this week | Failing tests last week | Trend |
|---|---|---|---|
| CASS B2A API (`tc_postRialtoB2A*`, `tc_getRialtoB2A*`, `tc_patchRialtoB2A*`) | 10 | 0 | ↑ |
| MH discountType / pricing assertions | 40 | 2 | ↑ |
| Rialto placement / integration assertions | 23 | 1 | ↑ |
| MH multi-product indexing (`TC23`/`TC24`) | 11 | 0 | ↑ |
| Request construction / malformed parameters | 6 | 0 | ↑ |
| Residual pricing / identity mismatches | 8 | 0 | ↑ |

> **Note:** Counts reflect unique failing test steps. The CASS API group (10 tests) recurred across 7 consecutive builds. MH and Rialto counts include failures from both the demo job (3 tests × 6 builds) and the internal-trunk job (86 failures in build #134).

---

## Failed Builds

### `automationrunCAI-RIALTO-B2A-trunk`

| Build | Date | Tests (fail/total) | Root Cause Summary | Investigation |
|---|---|---|---|---|
| [#284](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-284.md) | 2026-07-05 | 10 / 17 | CASS `/api/870/v1/cass` endpoints return 404 after v87 → v88 API version update | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-284-analysis.md) |
| [#285](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-285.md) | 2026-07-06 | 10 / 17 | Same as #284 — issue unresolved, second consecutive failure | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-285-analysis.md) |
| [#286](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-286.md) | 2026-07-09 | 10 / 17 | Same CASS 404 pattern — third consecutive failure | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-286-analysis.md) |
| [#295](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-295.md) | 2026-07-10 | 10 / 17 | Persistent CASS route unavailability; no change in failure pattern | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-295-analysis.md) |
| [#298](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-298.md) | 2026-07-10 | 10 / 17 | Persistent CASS route unavailability | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-298-analysis.md) |
| [#300](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-300.md) | 2026-07-10 | 10 / 17 | Persistent CASS route unavailability | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-300-analysis.md) |
| [#301](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-301.md) | 2026-07-10 | 10 / 17 | Persistent CASS route unavailability — 7th consecutive UNSTABLE build | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-301-analysis.md) |

### `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`

| Build | Date | Tests (fail/total) | Root Cause Summary | Investigation |
|---|---|---|---|---|
| [#134](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134.md) | 2026-07-10 | 86 / 513 | MH discountType/pricing drift, Rialto state-update drift, multi-product indexing, malformed follow-up requests | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134-analysis.md) |

### `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`

| Build | Date | Tests (fail/total) | Root Cause Summary | Investigation |
|---|---|---|---|---|
| [#262](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262.md) | 2026-07-05 | 3 / 14 | Placement-change fixture drift — `discountType`, commission, and depth mismatches after v88 update | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262-analysis.md) |
| [#269](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269.md) | 2026-07-05 | 3 / 14 | Same as #262 — recurring fixture vs service-response mismatch | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269-analysis.md) |
| [#270](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270.md) | 2026-07-06 | 3 / 14 | Same fixture drift — additional Rialto sum/VAT fields also mismatched | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270-analysis.md) |
| [#271](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271.md) | 2026-07-09 | 3 / 14 | Same + Rialto `placementId` now returning `TEXT` instead of `SIDAN3`; service response continuing to diverge | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271-analysis.md) |
| [#283](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283.md) | 2026-07-10 | 3 / 14 | MH `discountType` not propagated; Rialto order state (statusFlags, commission, depth) not updated after placement change | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283-analysis.md) |
| [#284](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284.md) | 2026-07-10 | 3 / 14 | Same — `depth` (372 vs 184), `statusFlags` empty, `commissionAmount` drifted to 620.0 | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284-analysis.md) |

---

## Key Observations

- **Single root cause, maximum impact:** All 7 `automationrunCAI-RIALTO-B2A-trunk` failures share one cause — the CASS service routes under `/api/870/v1/cass/...` are unavailable following the v87 → v88 API version update (commit `4a04ddba1e4`). This is an environment/deployment issue, not a test code issue. The failure has persisted for 7 consecutive builds with no remediation.
- **Persistent fixture drift in demo and internal-trunk jobs:** The `rialtoB2A (CASS TC4 Change Placement)` scenario has been failing since build #246 (demo) and since build #99 in many cases (internal-trunk). The v88 update widened the divergence — `discountType`, commission, VAT, depth, and `statusFlags` all differ from pinned fixture values. This points to a service contract change that has never been reflected in the test data.
- **Internal-trunk build #134 surfaced 86 failures** spanning 5 distinct failure patterns — the majority (75 of 86) are long-standing failures that pre-date this week, confirming the fixture drift is a chronic issue.
- **No passing builds observed this week** across any of the three affected jobs — all 14 reported builds were UNSTABLE.

## Recommended Actions

1. **Immediately investigate the CASS `/api/870/v1/cass/` routing gap** — confirm whether the v88 deployment is missing a route configuration or whether the base path should be different for environment `870`. 7 consecutive build failures with an identical pattern strongly suggests an environment misconfiguration rather than a test data issue.
2. **Reconcile test fixtures against live API v88 responses** — update `getMHB2A.csv` and `getRialtoB2A.csv` to reflect the post-v88 values for `discountType`, commission, VAT, depth, and `statusFlags`. Consider generating fixture snapshots automatically on each API version bump.
3. **Address the multi-product MH indexing failure in build #134** — the `Index 13 out of bounds for length 13` error in two-product scenarios causes cascading failures in downstream patch steps. This is a test-framework defect (off-by-one in `odIds` collection) that should be isolated and fixed before it masks further regressions.
4. **Treat build #134's 86 failures as a backlog item** — 75 of them pre-date this week. Schedule a dedicated sprint to address the long-standing fixture and state-update failures so the internal-trunk job can serve as a reliable quality gate.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #301](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-301.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-301-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #300](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-300.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-300-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #298](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-298.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-298-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #295](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-295.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-295-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #134](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #284](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #283](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283.md) | 2026-07-10 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #286](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-286.md) | 2026-07-09 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-286-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #271](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271.md) | 2026-07-09 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #270](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270.md) | 2026-07-06 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #285](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-285.md) | 2026-07-06 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-285-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #284](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-284.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-284-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #269](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #262](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262.md) | 2026-07-05 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262-analysis.md) |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
