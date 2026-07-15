# Weekly Test Failure Summary

**Period:** 2026-07-08 → 2026-07-15  
**Generated:** 2026-07-15  
**Observed builds:** 30 | **Failed/Unstable builds:** 30 | **Jobs affected:** 3

---

## Root Cause Groups

### 1. CASS 404 after v88 upgrade

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 160 (10 per build × 16 builds) |
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
| Total Failures | ~188 (internal-trunk: ~34 × 5 builds; demo: 2 × 9 builds) |
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
| Total Failures | ~34 (demo: 1 × 9 builds; internal-trunk: ~5 × 5 builds) |
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
| Total Failures | ~65 (13 per build × 5 builds) |
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
| Total Failures | ~15 (3 per build × 5 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15, 22-24.feature`
  - `TC15` CASS POST — `packageId`, `issueDate` array ordering mismatch
  - `TC22` CASS GET — `paCode`, `plaCode`, `prodCode` ordering wrong
  - `TC23`/`TC24` — reverted state does not match original fixture values

### 6. Request construction / path parameter errors

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~25 (5 per build × 5 builds) |
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
| Total Failures | ~105 (21 per build × 5 builds) |
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

- **CASS 404 streak reaches 22 consecutive builds with no remediation.** The v88 API route issue first seen on 2026-07-05 (#284) continued uninterrupted through builds #311–#312 this period. The failure pattern is identical across all 16 builds in scope: 7 direct 404 failures + 3 cascade failures = 10 per build. No fix has been deployed to environment `870`.
- **Internal-trunk ran 5 builds this period; all UNSTABLE.** Build #139 (07-14) shows 88 failures (+2 vs #138), with newly emerging TC1/TC2 `discountAmount` mismatches (`expected 0.0, found 63660.63`) — a regression not present in builds #134–#138. All other failure groups remain unchanged.
- **Demo job failures stable at 3/14 per build across 9 consecutive runs.** All nine demo builds (#271, #283–#290) failed with the same 3 tests: `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b`. Failure values (`depth=372`, `commissionAmount=620.0`, `statusFlags=[]`) are consistent across every run.
- **Zero passing builds across all three jobs this week.** All 30 observed builds were UNSTABLE.
- **No improvement in any failure group compared to last week.** All patterns are unchanged; no fixes have been deployed. The TC1/TC2 discountAmount regression in build #139 represents a new deterioration.

## Recommended Actions

1. **Immediately investigate the CASS `/api/870/v1/cass/` routing gap** — 16 consecutive build failures with an identical 404 pattern on environment `870` strongly indicates an undeployed route configuration or a missing base-path mapping in the v88 release. Escalate if not already tracked; this issue has persisted for over a week.
2. **Reconcile test fixtures against live API v88 responses** — update `getMHB2A.csv` and `getRialtoB2A.csv` to reflect post-v88 values for `discountType`, commission, VAT, depth, and `statusFlags`. Internal-trunk and demo failures will continue indefinitely without fixture updates.
3. **Fix the TC16–TC20 off-by-one index error** — the `Index 13 out of bounds for length 13` defect in multi-product GET steps blocks `odIds` from being stored, cascading into 15 failures per internal-trunk run. This is a test-framework defect (not a service issue) and should be straightforward to fix.
4. **Investigate the TC24/TC29 path parameter swap** — `uuid` and `agencyPrisaId` appear to be used in the wrong positions in follow-up Rialto GET requests. Fix the request construction in these test steps.
5. **Address the internal-trunk 86-failure backlog as a sprint item** — with the CASS 404 and fixture issues resolved, the remaining failures (array ordering, residual pricing, TC37 magazine basket) will be more isolated and easier to debug.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #312](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-312.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-312-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #311](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-311.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-311-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #139](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-139.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-139-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #290](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-290.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-290-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #310](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-310.md) | 2026-07-13 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-310-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #309](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-309.md) | 2026-07-13 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-309-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #138](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-138.md) | 2026-07-13 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-138-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #289](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-289.md) | 2026-07-13 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-289-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #308](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-308.md) | 2026-07-12 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-308-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #307](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-307.md) | 2026-07-12 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-307-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #137](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-137.md) | 2026-07-12 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-137-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #288](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-288.md) | 2026-07-12 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-288-analysis.md) |
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

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
