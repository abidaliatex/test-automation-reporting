# Weekly Test Failure Summary

**Period:** 2026-07-17 → 2026-07-26  
**Generated:** 2026-07-27  
**Observed builds:** 53 | **Failed/Unstable builds:** 53 | **Jobs affected:** 3

---

## Root Cause Groups

### 1. CASS 404 after v88 upgrade

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 200 (10 per build × 20 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A01` — Login via `/api/870/v1/cass/users/login` (HTTP 404)
  - `tc_postRialtoB2A02` — Create order via `/cass/orders/orders` (HTTP 404)
  - `tc_postRialtoB2A03` — Calculate price via `/cass/orders/calculatePrice` (HTTP 404)
  - `tc_postRialtoB2A04` — Space availability via `/cass/orders/spaceAvailability` (HTTP 404)
  - `tc_getRialtoB2A01` — Get order by ID via `/cass/orders/orders/1620` (HTTP 404)
  - `tc_getRialtoB2A02` — Valid packages/placements via `/cass/staticData/validPackagesAndPlacements` (HTTP 404)
  - `tc_getRialtoB2A04` — Order headers via `/cass/orders/orderHeaders` (HTTP 404)
  - `tc_getRialtoB2A05` — Store status of order (cascade — `uuid` undefined due to failed login)
  - `tc_getRialtoB2A06` — Store status after update (cascade — `uuid` undefined)
  - `tc_patchRialtoB2A01` — Update order (cascade — `Failed to parse the JSON document` on HTML 404 response)

### 2. discountType not propagated (null instead of RIALTO)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~369 (internal-trunk: ~345 across 10 builds; demo: ~24 across 20 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase1-2, 3-9, 11, 14-15, 22-24, 26-28, 30-37.feature` (internal-trunk)
  - CASS GET steps — `orders[*].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`; impacts 22–40 scenarios per build
  - Downstream basket totals (`totalInclVat`, `vat`, `netPrice`, `orderDiscount`) drift as a direct consequence
- `rialtoB2A(CASS)TestCase4.feature` (demo)
  - `tc_getMHTC03` — `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`
- `rialtoB2A(CASS)TestCase29.feature` (demo)
  - `tc_getMHTC_MZN04a` — `orders.printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`
  - `tc_getMHTC06` — `orders[0].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`

### 3. Financial calculation and amount mismatch

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~260 (internal-trunk: ~250 across 10 builds; demo: ~10 across 5 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase1-2, 3-6, 9, 11, 15, 27-28, 30-31, 35, 37.feature` (internal-trunk)
  - CASS POST/PATCH steps — `discountAmount`, `commissionAmount`, `statusFlags` mismatches (16–33 failures per build)
  - CASS GET steps — `totalInclVat`, `priceNet`, `grossAmount`, `orderDiscount` diverge from fixtures
  - Rialto GET steps — nested `[[v]]` vs `[v]` assertion format; basket ID (`orBoxid` vs `agencyPrisaId`) mismatch on TC35
- `rialtoB2A(CASS)TestCase4.feature` (demo)
  - `tc_getMHTC03a` — `commission`, `totalInclVat`, `orderbasketSum` incorrect after placement change
  - `tc_getIntegrationRialto05b` — `commissionAmount`, `priceNet`, `statusFlags`, `depth` mismatch on Rialto GET after update

### 4. Placement state not reverted to HALVLIGG (UPPSLAG stuck)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~60 (demo: ~20 across 10 builds; internal-trunk: ~40 across 10 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase29.feature` (demo)
  - `tc_getMHTC_MZN04b` — `orders.printDetails.plaCode` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `totalInclVat` expected `6056.25` found `13062.50`
  - `tc_getIntegrationRialtoMZN04b` — `orderAdDetails.placementId` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `priceGross` expected `5000.0` found `11000.0`
- `rialtoB2A(CASS)TestCase24, 27, 30-31, 35.feature` (internal-trunk)
  - TC24 revert — `placementId` expected `[TEXT×6]` found `[UPPSLAG×6]`; Rialto GET — `uuid` undefined, `agencyPrisaId` redundant
  - TC27 magazine — `issueDate` expected `[[2026-08-19]]` found `[[2026-08-26]]`; `statusFlags` expected `[[PRELIMINARY]]` found `[[]]`
  - TC30/TC31 — MEDIAHOUSE original full-page state verify fails; Rialto reverted state returns wrong `priceNet`
  - TC35 — `placementId` expected `[[SIDAN2]]` found `[[HALVLIGG]]`; basket ID synchronisation drift (`orBoxid` vs `agencyPrisaId`)

### 5. Two-product MH index out-of-bounds / TestContext cascade (TC16–TC20)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~111 (10–15 per build × 10 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase16-20.feature`
  - TC16–TC20 CASS GET step — `Index 13 out of bounds for length 13` (list index error in two-product scenario)
  - TC16–TC20 subsequent CASS POST steps — `No MH odIds found in TestContext` (cascade from missing stored data)
  - TC16/TC17/TC18/TC20 final POST — attribute mismatch (`issueDate`, `moduleCode`, `placementId`) indicating change was not applied

### 6. issueDate not propagated after date-change operations

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~73 (5–15 per build × 10 builds) |
| First Seen | 2026-07-05 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase16, 19, 27, 30-31, 35.feature`
  - TC16 CASS POST — `issueDate` expected `[[2026-07-01, 2026-07-21]]` found `[[2026-07-01, 2026-07-01]]` (second order line date not updated)
  - TC19 CASS POST — same `issueDate` propagation failure on second order line
  - TC27 MEDIAHOUSE/Rialto — `issueDate` expected `[[2026-08-19]]` found `[[2026-08-26]]`; `statusFlags` expected `[[PRELIMINARY]]` found `[[]]`
  - TC30/TC31 Rialto — reverted state returns wrong `priceNet` and `issueDate`
  - TC35 Rialto — `placementId` expected `[[SIDAN2]]` found `[[HALVLIGG]]`; `issueDate` mismatch

### 7. Array ordering non-determinism (packageId / productId / paCode)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~30 (2–7 per build × 10 builds) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15, 19, 22.feature`
  - TC15 CASS POST — `packageId`/`productId` array order `[AB, SVD]` found `[SVD, AB]`
  - TC19 CASS POST — same `packageId`/`productId` ordering mismatch
  - TC22 CASS POST/GET — `packageId`, `paCode`, `plaCode`, `prodCode` returned in non-deterministic order; post-revert state not fully restored

### 8. Path parameter and basket ID drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~38 (3–8 per build across internal-trunk; ~8 across demo builds 298–301) |
| First Seen | 2026-07-10 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase24, 29.feature` (internal-trunk)
  - TC24 Rialto GET — `uuid` undefined, `agencyPrisaId` redundant path parameter
  - TC29 Rialto GET (create) — `uuid` and `agencyPrisaId` swapped; MH steps cascade `No MH odIds found in TestContext`
- `rialtoB2A(CASS)TestCase29.feature` (demo, builds 298–301 on 2026-07-22)
  - `RIALTO - Verify created Rialto order` — `agencyPrisaId` undefined; subsequent MH steps cascade NullPointerException
  - Builds 298–299: 5 failures each; builds 300–301: 3–4 failures as test suite stabilised

---

## Key Observations

- **CASS 404 streak now at 52+ consecutive builds with no remediation.** The v88 API route issue first seen on 2026-07-05 (#284) continued uninterrupted through builds #317–#336 this period. The failure pattern remains identical: 7 direct 404 failures + 3 cascade failures = 10 per build. No fix has been deployed to environment `870`.
- **Internal-trunk failure count stable at 86–88 per build across 10 consecutive runs.** All 10 builds (#142–#151, 07-17 to 07-26) were UNSTABLE with 86–88 failures each. The `discountType=null` group dominates at 22–40 failures per build; financial calculation and state drift add a further 16–33; the two-product index error contributes 10–15.
- **Demo job expanded from 14 to 15 tests on 2026-07-22** (TestCase29 / MZN04 scenarios added). Builds 298–301 (07-22) recorded 3–5 failures during stabilisation. From build 303 onwards the suite settled at 3 failures per run (`tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b`, `tc_getIntegrationRialtoMZN04b`), except builds 310–313 which recorded only 1 failure each (`tc_getMHTC06` discountType).
- **Zero passing builds across all three jobs.** All 53 observed builds were UNSTABLE; pass rate was 0% at the job level.
- **No improvement in any failure group compared to last week.** The `discountType=null`, financial mismatch, CASS 404, and index out-of-bounds patterns are all unchanged; no fixes have been deployed across the 10-day window.

## Recommended Actions

1. **Immediately escalate the CASS `/api/870/v1/cass/` routing gap** — 52+ consecutive build failures with an identical 404 pattern on environment `870` indicates a persistent undeployed route configuration or missing base-path mapping in the v88 release. This issue has now persisted for over three weeks with zero progress.
2. **Fix the `discountType` propagation defect** — this is the single largest source of failures in internal-trunk (22–40 per build) and is also present in both demo jobs. The field `orders[*].printDetails.discountType` is consistently returned as `null` for Rialto-originated flows. Without this fix, downstream basket totals (`totalInclVat`, `vat`, `netPrice`) will also remain incorrect.
3. **Investigate the HALVLIGG/UPPSLAG placement revert failure** — both demo (TC29 MZN04b, Rialto revert) and internal-trunk (TC24, TC30–TC31, TC35) show placement returning `UPPSLAG` after a revert to `HALVLIGG`. This may share a root cause with the `discountType` propagation defect (server-side state not being persisted correctly).
4. **Fix the TC16–TC20 off-by-one index error** — `Index 13 out of bounds for length 13` in two-product GET steps blocks `odIds` from being stored, cascading into 10–15 failures per internal-trunk run. This is a test-framework defect and should be straightforward to fix.
5. **Reconcile test fixtures against live API v88 responses** — update `getMHB2A.csv` and `getRialtoB2A.csv` to reflect post-v88 values for `discountType`, commission, VAT, depth, and `statusFlags`. Both internal-trunk and demo failures will continue indefinitely without fixture updates.
6. **Fix TC24/TC29 path parameter construction** — `uuid` and `agencyPrisaId` are used in the wrong positions in follow-up Rialto GET requests; the issue persists in internal-trunk and was also observed in the demo during TC29 introduction.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #336](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-336.md) | 2026-07-26 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-336-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #335](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-335.md) | 2026-07-26 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-335-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #151](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-151.md) | 2026-07-26 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-151-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #316](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-316.md) | 2026-07-26 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-316-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #315](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-315.md) | 2026-07-26 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-315-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #314](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-314.md) | 2026-07-26 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-314-analysis.md) |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #150](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-150.md) | 2026-07-25 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-150-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #334](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-334.md) | 2026-07-25 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-334-analysis.md) |
| [automationrunCAI-RIALTO-B2A-trunk #333](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-333.md) | 2026-07-25 | UNSTABLE | [analysis](../investigations/copilot-findings/automationrunCAI-RIALTO-B2A-trunk/build-333-analysis.md) |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
