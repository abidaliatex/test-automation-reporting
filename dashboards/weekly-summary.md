# Weekly Test Failure Summary

**Period:** 2026-07-05 → 2026-07-12  
**Generated:** 2026-07-12  
**Observed builds:** 23 | **Failed/Unstable builds:** 23 | **Jobs affected:** 3

---

## Failure Counts by Test Pattern

| Test Pattern | Failing tests this week | Failing tests last week | Trend |
|---|---|---|---|
| CASS B2A API (`tc_postRialtoB2A*`, `tc_getRialtoB2A*`, `tc_patchRialtoB2A*`) | 10 | 10 | → |
| MH discountType / pricing assertions | 40 | 40 | → |
| Rialto placement / integration assertions | 23 | 23 | → |
| MH multi-product indexing (TC16–TC20) | 15 | 11 | ↑ |
| Request construction / malformed parameters | 6 | 6 | → |
| Residual pricing / identity mismatches | 8 | 8 | → |

> **Note:** Counts reflect unique failing test steps. The CASS API group (10 tests) recurred across all 12 `automationrunCAI-RIALTO-B2A-trunk` builds this period — 5 additional builds on 2026-07-11 (#302–#306) confirmed the CASS 404 pattern is still unresolved. The multi-product indexing count increased from 11 to 15; the TC16–TC20 index-out-of-bounds defect was confirmed in both internal-trunk builds (#134 and #135) this period. MH and Rialto counts include failures from the demo job (3 tests × 9 builds) and the internal-trunk job (86 failures each in builds #134 and #135).

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
| [#302](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-302.md) | 2026-07-11 | 10 / 17 | Same CASS 404 — 8th consecutive UNSTABLE build | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-302-analysis.md) |
| [#303](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-303.md) | 2026-07-11 | 10 / 17 | Same CASS 404 — 9th consecutive UNSTABLE build | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-303-analysis.md) |
| [#304](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-304.md) | 2026-07-11 | 10 / 17 | Same CASS 404 — 10th consecutive UNSTABLE build | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-304-analysis.md) |
| [#305](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-305.md) | 2026-07-11 | 10 / 17 | Same CASS 404 — 11th consecutive UNSTABLE build | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-305-analysis.md) |
| [#306](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-306.md) | 2026-07-11 | 10 / 17 | Same CASS 404 — 12th consecutive UNSTABLE build | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-306-analysis.md) |

### `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`

| Build | Date | Tests (fail/total) | Root Cause Summary | Investigation |
|---|---|---|---|---|
| [#134](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134.md) | 2026-07-10 | 86 / 513 | MH discountType/pricing drift, Rialto state-update drift, multi-product indexing, malformed follow-up requests | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134-analysis.md) |
| [#135](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-135.md) | 2026-07-11 | 86 / 513 | Same root causes as #134 — all 6 failure groups persist; no regressions resolved | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-135-analysis.md) |

### `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`

| Build | Date | Tests (fail/total) | Root Cause Summary | Investigation |
|---|---|---|---|---|
| [#262](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262.md) | 2026-07-05 | 3 / 14 | Placement-change fixture drift — `discountType`, commission, and depth mismatches after v88 update | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262-analysis.md) |
| [#269](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269.md) | 2026-07-05 | 3 / 14 | Same as #262 — recurring fixture vs service-response mismatch | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269-analysis.md) |
| [#270](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270.md) | 2026-07-06 | 3 / 14 | Same fixture drift — additional Rialto sum/VAT fields also mismatched | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270-analysis.md) |
| [#271](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271.md) | 2026-07-09 | 3 / 14 | Same + Rialto `placementId` now returning `TEXT` instead of `SIDAN3`; service response continuing to diverge | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271-analysis.md) |
| [#283](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283.md) | 2026-07-10 | 3 / 14 | MH `discountType` not propagated; Rialto order state (statusFlags, commission, depth) not updated after placement change | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283-analysis.md) |
| [#284](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284.md) | 2026-07-10 | 3 / 14 | Same — `depth` (372 vs 184), `statusFlags` empty, `commissionAmount` drifted to 620.0 | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284-analysis.md) |
| [#285](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-285.md) | 2026-07-11 | 3 / 14 | MH `discountType` null, pricing drift; Rialto depth 372 vs 184, `statusFlags` empty | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-285-analysis.md) |
| [#286](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-286.md) | 2026-07-11 | 3 / 14 | Same fixture drift; depth/commission/`statusFlags` mismatch continues | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-286-analysis.md) |
| [#287](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-287.md) | 2026-07-11 | 3 / 14 | Same — MH `discountType` null, VAT/sum drift; Rialto depth 372 vs 184 | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-287-analysis.md) |

---

## Root Cause Groups

### 1. CASS 404 after v88 upgrade

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 120 (10 per build × 12 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A01` — Login via `/api/870/v1/cass/users/login`
  - `tc_postRialtoB2A02` — Create order
  - `tc_postRialtoB2A03` — Calculate price
  - `tc_postRialtoB2A04` — Space availability
  - `tc_getRialtoB2A01` — Get order by ID
  - `tc_getRialtoB2A02` — Valid packages and placements
  - `tc_getRialtoB2A04` — Order headers
  - `tc_getRialtoB2A05` — Store status of order (cascade from missing `uuid`)
  - `tc_getRialtoB2A06` — Store status after update (cascade)
  - `tc_patchRialtoB2A01` — Update order (cascade)

### 2. MH discountType not propagated / basket pricing drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | 88 (internal-trunk: 35 × 2 builds; demo: 2 × 9 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature` (demo)
  - `tc_getMHTC03` — Verify MH `discountType` on initial placement
  - `tc_getMHTC03a` — Verify MH `discountType` after placement change
- `rialtoB2A(CASS)TestCase3-9, 11, 14-15, 22-24, 26-28, 30-36.feature` (internal-trunk)
  - Multiple MH GET steps checking `discountType`, `totalInclVat`, `vat`, and `netPrice`

### 3. Rialto placement update state and pricing mismatch

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 19 (demo: 1 × 9 builds; internal-trunk: ~5 × 2 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature`
  - `tc_getIntegrationRialto05b` — Verify Rialto reflects placement change (`statusFlags`, `depth`, `commissionAmount`)
- `rialtoB2A(CASS)TestCase1, 3, 4, 6.feature` (internal-trunk)
  - CASS POST / PATCH steps asserting `statusFlags = [PRELIMINARY]` and commission amounts

### 4. Two-product MH indexing out-of-bounds (TC16–TC20)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 30 (15 per build × 2 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase16-20.feature`
  - TC16–TC20 CASS GET step — `Index 13 out of bounds for length 13`
  - TC16–TC20 subsequent CASS POST steps — `No MH odIds found in TestContext` (cascade)

### 5. Array ordering and state drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 14 (7 per build × 2 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15, 22-24.feature`
  - `TC15` CASS POST — `packageId`, `issueDate` array ordering mismatch
  - `TC22` CASS GET — `paCode`, `plaCode`, `prodCode` ordering wrong
  - `TC23`/`TC24` — reverted state does not match original fixture values

### 6. Request construction / path parameter errors

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 8 (4 per build × 2 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase24, 29.feature`
  - `TC24` Rialto follow-up GET — `uuid` undefined, `agencyPrisaId` redundant
  - `TC29` Rialto GET — `uuid` and `agencyPrisaId` path parameters swapped
  - `TC23` revert — HTTP 500 `Transaction rolled back because it has been marked as rollback-only`

### 7. Residual pricing and identity mismatches

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 30 (15 per build × 2 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase11, 27-28, 30-31, 35, 37.feature`
  - `TC11`, `TC27`, `TC28`, `TC30`, `TC31` — commission, `priceNet`, `totalInclVat` post-change drift
  - `TC35` — MH basket ID (`orBoxid`) does not match Agency Prisa ID
  - `TC27`/`TC28` Rialto steps — nested list `[[v]]` vs scalar `[v]` assertion format mismatch

---

## Key Observations

- **CASS 404 now spans 12 consecutive builds with no remediation.** The v88 API route issue first seen on 2026-07-05 (#284) continued uninterrupted through five additional builds on 2026-07-11 (#302–#306). The failure pattern is identical across all 12 builds: 7 direct 404 failures + 3 cascade failures = 10 per build.
- **Internal-trunk #135 confirms all root causes from #134 persist.** Build #135 (2026-07-11) produced the same 86 failures across the same 6 failure groups as #134 (2026-07-10). No regressions were introduced, but none were resolved either.
- **Demo job failures stable at 3/14 per build across 9 consecutive runs.** All nine demo builds (07-05 to 07-11) failed with the same 3 tests: `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b`. The failure values (`depth=372`, `commissionAmount=620.0`, `statusFlags=[]`) are consistent across every run.
- **Zero passing builds across all three jobs this week.** All 23 observed builds were UNSTABLE.

## Recommended Actions

1. **Immediately investigate the CASS `/api/870/v1/cass/` routing gap** — 12 consecutive build failures with an identical 404 pattern on environment `870` strongly indicates an undeployed route configuration or a missing base-path mapping in the v88 release. Escalate if not already tracked.
2. **Reconcile test fixtures against live API v88 responses** — update `getMHB2A.csv` and `getRialtoB2A.csv` to reflect post-v88 values for `discountType`, commission, VAT, depth, and `statusFlags`. Internal-trunk and demo failures will continue indefinitely without fixture updates.
3. **Fix the TC16–TC20 off-by-one index error** — the `Index 13 out of bounds for length 13` defect in multi-product GET steps blocks `odIds` from being stored, cascading into 15 failures per internal-trunk run. This is a test-framework defect (not a service issue) and should be straightforward to fix.
4. **Investigate the TC24/TC29 path parameter swap** — `uuid` and `agencyPrisaId` appear to be used in the wrong positions in follow-up Rialto GET requests. Fix the request construction in these test steps.
5. **Address the internal-trunk 86-failure backlog as a sprint item** — with the CASS 404 and fixture issues resolved, the remaining failures (array ordering, residual pricing, TC37 magazine basket) will be more isolated and easier to debug.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #306](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-306.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-306-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #305](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-305.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-305-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #304](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-304.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-304-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #303](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-303.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-303-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #302](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-302.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-302-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #135](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-135.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-135-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #287](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-287.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-287-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #286](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-286.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-286-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #285](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-285.md) | 2026-07-11 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-285-analysis.md) |
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
