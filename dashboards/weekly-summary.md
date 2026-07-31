# Weekly Test Failure Summary

**Period:** 2026-07-25 → 2026-07-31  
**Generated:** 2026-07-31  
**Observed builds:** 28 | **Failed/Unstable builds:** 28 | **Jobs affected:** 3

---

## Root Cause Groups

### 1. Discount-type and pricing-rule regression

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~175+ this week |
| First Seen | 2026-07-25 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature`, `...5.feature`, `...9.feature`, `...11.feature`, `...15.feature`, `...22.feature`, `...26.feature`, `...27.feature`, `...28.feature`, `...30.feature`, `...31.feature`, `...32.feature`, `...33.feature`, `...34.feature`, `...35.feature`, `...36.feature`, `...37.feature`
  - `User perform CASS GET API - #1.1` — `discountType` expected `RIALTO/NONE` but found `null`
  - `MediaHouse basket/order verification - #1.1` — discount and total fields diverge after updates/reverts

### 2. Financial amount/value mismatches (including precision drift)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~120+ this week |
| First Seen | 2026-07-25 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — amount iterator mismatch (`276757.2` vs `369009.6`)
  - `tc_postRialtoB2A03` — price calculation mismatch (`89392.58` vs `44696.28999999999`)
- `rialtoB2A(CASS)TestCase1.feature`, `...3.feature`, `...4.feature`, `...5.feature`, `...6.feature`, `...9.feature`, `...11.feature`, `...14.feature`, `...15.feature`, `...21.feature`, `...22.feature`, `...23.feature`, `...24.feature`
  - `User perform CASS POST API - #1.1` — floating-point and total-field drift

### 3. CASS endpoint outage with cascade failures (HTTP 404)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 30 (builds #334-#336) |
| First Seen | 2026-07-25 |
| Still Active | No |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A01`–`tc_postRialtoB2A04`, `tc_getRialtoB2A01`, `tc_getRialtoB2A02`, `tc_getRialtoB2A04` — `/cass/*` endpoints returned HTTP 404
  - `tc_patchRialtoB2A01` — JSON parse failure from HTML 404 body
  - `tc_getRialtoB2A05`, `tc_getRialtoB2A06` — cascade `uuid` path-parameter failures

### 4. Store-status code mismatch (N200 vs N202)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 6 |
| First Seen | 2026-07-27 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — expected `N200` but found `N202`

### 5. Path-parameter / basket-ID handoff drift and rollback errors

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| Total Failures | ~20+ this week |
| First Seen | 2026-07-25 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`, `rialtoB2A(CASS)TestCase35.feature`
  - `Revert two MediaHouse order lines to full page - #1.1` — rollback-only HTTP 500/400 path
  - `Verify Rialto reflects reverted full-page state - #1.1` — `uuid` undefined / redundant `agencyPrisaId`
  - `MEDIAHOUSE ... MZN04a/MZN04b` — MH basket ID (`orBoxid`) differs from Agency Prisa ID

### 6. Two-product/TestContext and order-line sequencing instability

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~28+ this week |
| First Seen | 2026-07-25 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase16.feature`, `...17.feature`, `...18.feature`, `...19.feature`, `...20.feature`
  - `User perform CASS GET API - #1.1` — index out-of-bounds and missing MH `odIds` cascade
- `rialtoB2A(CASS)TestCase15.feature`, `...18.feature`, `...22.feature`, `...23.feature`, `...24.feature`, `...35.feature`
  - `User perform CASS POST API - #1.1` / verification steps — order-line sequencing and stale placement/date state

---

## Key Observations

- All 28 observed builds in this week window were UNSTABLE (0% pass rate at build level).
- `automationrunCAI-RIALTO-B2A-trunk` shifted from endpoint-outage failures (builds #334-#336) to a smaller, repeatable 2-3 failure pattern from build #337 onward.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` remained the largest contributor by failure volume; build #156 still showed 65 failures.
- Demo job failures concentrated around `discountType`/pricing and MH↔Agency ID correlation checks.

## Recommended Actions

1. Prioritise discount/pricing-rule stabilization (`discountType`, order discounts, VAT/net totals) across internal and demo suites.
2. Fix `tc_getRialtoB2A06` status handling (`N200` vs `N202`) to clear the persistent trunk regression.
3. Resolve path-parameter and basket-ID handoff drift (`uuid`, `agencyPrisaId`, `orBoxid`) across TC23/24/29/35 flows.
4. Address internal two-product parser/index handling to stop TestContext cascade failures.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #156](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-156.md) | 2026-07-31 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #345](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-345.md) | 2026-07-30 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #344](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-344.md) | 2026-07-30 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #343](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-343.md) | 2026-07-29 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #342](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-342.md) | 2026-07-29 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #326](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-326.md) | 2026-07-28 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #341](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-341.md) | 2026-07-28 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #325](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-325.md) | 2026-07-27 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #152](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-152.md) | 2026-07-27 | UNSTABLE | n/a |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
