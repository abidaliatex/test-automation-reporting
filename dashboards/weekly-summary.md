# Weekly Test Failure Summary

**Period:** 2026-07-14 → 2026-07-16  
**Generated:** 2026-07-16  
**Observed builds:** 6 | **Failed/Unstable builds:** 6 | **Jobs affected:** 3

---

## Root Cause Groups

### 1. CASS 404 after v88 upgrade

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 30 (10 per build × 3 builds) |
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
| Total Failures | 38 (internal-trunk: 34 × 1 build; demo: 2 × 2 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature` (demo)
  - `tc_getMHTC03` — Verify MH `discountType` on initial placement
  - `tc_getMHTC03a` — Verify MH `discountType` after placement change
- `rialtoB2A(CASS)TestCase3-9, 11, 14-15, 22-24, 26-28, 30-37.feature` (internal-trunk)
  - Multiple MH GET steps asserting `discountType`, `totalInclVat`, `vat`, and `netPrice`

### 3. Financial calculation errors (discount / commission / pricing)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | 24 (internal-trunk: 22 × 1 build; demo: 1 × 2 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature` (demo)
  - `tc_getIntegrationRialto05b` — Verify Rialto reflects placement change (`statusFlags`, `depth`, `commissionAmount`, `priceNet`)
- `rialtoB2A(CASS)TestCase1and2, 3-6, 9, 11, 15, 27-28, 30-31, 35, 37.feature` (internal-trunk)
  - CASS POST steps — `discountAmount`, `commissionAmount`, `statusFlags = [PRELIMINARY]` mismatches
  - CASS GET steps — `totalInclVat`, `priceNetExComm` drift post-change
  - Rialto steps — nested assertion format `[[v]]` vs `[v]`; basket ID (`orBoxid` vs `agencyPrisaId`) mismatch on TC35

### 4. Two-product MH indexing out-of-bounds (TC16–TC20)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 13 (13 per build × 1 build) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase16-20.feature`
  - TC16–TC20 CASS GET step — `Index 13 out of bounds for length 13`
  - TC16–TC20 subsequent CASS POST steps — `No MH odIds found in TestContext` (cascade)
  - TC16/TC17/TC18/TC20 final POST — attribute mismatch (`issueDate`, `moduleCode`, `placementId`) indicating change was not applied

### 5. Array ordering non-determinism

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 3 (3 per build × 1 build) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15, 19, 22.feature`
  - `TC15` CASS POST — `packageId`/`productId` array order `[AB, SVD]` found `[SVD, AB]`
  - `TC19` CASS POST — same `packageId`/`productId` ordering mismatch
  - `TC22` CASS POST — `packageId` array elements returned in mixed order

### 6. Request construction / path parameter errors

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 5 (5 per build × 1 build) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase24, 29.feature`
  - `TC24` revert — `placementId` expected `[TEXT×6]` found `[UPPSLAG×6]`; Rialto GET — `uuid` undefined, `agencyPrisaId` redundant
  - `TC29` Rialto GET (create) — `uuid` and `agencyPrisaId` path parameters swapped; subsequent MH steps — `No MH odIds found in TestContext` (cascade); Rialto revert — missing `agencyPrisaId`

---

## Key Observations

- **CASS 404 streak now at 24+ consecutive builds with no remediation.** The v88 API route issue first seen on 2026-07-05 (#284) continued uninterrupted through builds #311–#313 this period. The failure pattern remains identical: 7 direct 404 failures + 3 cascade failures = 10 per build. No fix has been deployed to environment `870`.
- **Internal-trunk build #139 (07-14) shows a slight increase to 88 failures** (up from 86 in builds #134–#135 and #138). The `discountType=null` group widened to 34 failing scenarios across TC3–TC37 magazine tests, and financial calculation errors account for a further 22. No other failure groups improved.
- **Demo job failures stable at 3/14 per build across 2 consecutive runs.** Both demo builds (#290 on 07-14, #291 on 07-15) failed with the same 3 tests: `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b`. Failure values (`depth=372`, `commissionAmount=620.0`, `statusFlags=[]`) are consistent across every run.
- **Zero passing builds across all three jobs this period.** All 6 observed builds were UNSTABLE.
- **No improvement in any failure group compared to last week.** All patterns are unchanged; no fixes have been deployed.

## Recommended Actions

1. **Immediately escalate the CASS `/api/870/v1/cass/` routing gap** — 24+ consecutive build failures with an identical 404 pattern on environment `870` strongly indicates an undeployed route configuration or missing base-path mapping in the v88 release. This issue has persisted for over two weeks with zero progress.
2. **Reconcile test fixtures against live API v88 responses** — update `getMHB2A.csv` and `getRialtoB2A.csv` to reflect post-v88 values for `discountType`, commission, VAT, depth, and `statusFlags`. Both internal-trunk and demo failures will continue indefinitely without fixture updates.
3. **Fix the TC16–TC20 off-by-one index error** — the `Index 13 out of bounds for length 13` defect in multi-product GET steps blocks `odIds` from being stored, cascading into 13 failures per internal-trunk run. This is a test-framework defect (not a service issue) and should be straightforward to fix.
4. **Investigate the TC24/TC29 path parameter swap** — `uuid` and `agencyPrisaId` appear to be used in the wrong positions in follow-up Rialto GET requests. Fix the request construction in these test steps.
5. **Address the internal-trunk 88-failure backlog as a sprint priority** — with the CASS 404 and fixture issues resolved, the remaining failures (array ordering, financial calculation drift, TC35 basket mismatch) will be more isolated and easier to debug.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #313](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-313.md) | 2026-07-15 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-313-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #291](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-291.md) | 2026-07-15 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-291-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #312](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-312.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-312-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #311](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-311.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-311-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #139](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-139.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-139-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #290](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-290.md) | 2026-07-14 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-290-analysis.md) |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
