# Weekly Test Failure Summary

**Period:** 2026-08-01 → 2026-08-06  
**Generated:** 2026-08-07  
**Observed builds:** 16 | **Failed/Unstable builds:** 16 | **Jobs affected:** 2

---

## Root Cause Groups

### 1. Monetary value and precision mismatches

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~110+ this week |
| First Seen | 2026-08-01 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — iterator/value mismatch on StoreStatus payload (`276757.2` vs `369009.6`)
  - `tc_postRialtoB2A03` — self-service price calculation halves expected totals (`89392.58` vs `44696.29`)
- `rialtoB2A(CASS)TestCase1.feature`, `...3.feature`, `...4.feature`, `...5.feature`, `...6.feature`, `...7.feature`, `...11.feature`, `...14.feature`, `...15.feature`, `...21.feature`, `...22.feature`, `...23.feature`, `...24.feature`
  - `User perform CASS POST API - #1.1` — floating-point residuals in `discountAmount`, `priceNet`, `priceNetExComm`
  - `User perform CASS GET API - #1.1` / verification steps — `netAmount`, `grossAmount`, `vat`, `totalInclVat`, and basket totals drift from expected values

### 2. Discount-type and pricing-state regression

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~45+ this week |
| First Seen | 2026-08-01 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase3.feature`, `...4.feature`, `...5.feature`, `...9.feature`, `...11.feature`, `...15.feature`, `...22.feature`, `...27.feature`, `...37.feature`
  - `User perform CASS GET API - #1.1` — `discountType` flips between `RIALTO`, `NONE`, and `null`
  - `User perform CASS POST API - #1.1` — non-zero `discountAmount` persists after changes/reverts
  - `MEDIAHOUSE` verification steps — commission, VAT, and basket totals diverge after the wrong discount state propagates

### 3. Missing `PRELIMINARY` status flag on POST responses

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 20 this week |
| First Seen | 2026-08-01 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase1.feature`, `...3.feature`, `...4.feature`, `...5.feature`, `...6.feature`
  - `User perform CASS POST API - #1.1` — `orderHeader.statusFlags` returns `[]` where `[PRELIMINARY]` is expected immediately after POST

### 4. Order-line sequencing, stale placement, and basket handoff drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~50+ this week |
| First Seen | 2026-08-01 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15.feature`, `...18.feature`, `...19.feature`, `...20.feature`, `...22.feature`, `...23.feature`, `...24.feature`, `...35.feature`, `...37.feature`
  - `User perform CASS POST API - #1.1` — `packageId`, `productId`, `moduleCode`, and order-line arrays return in the wrong sequence
  - `Verify updated/reverted MediaHouse basket state - #1.1` — `paCode`, `plaCode`, `prodCode`, `issueDate`, and placement values stay stale after update/revert cycles
  - `RIALTO - Verify updated Agency order after Rialto change - #1.1` — placement/date/depth state drifts from the requested update

### 5. Magazine basket discount and commission regressions

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~95+ this week |
| First Seen | 2026-08-01 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase26.feature`, `...27.feature`, `...28.feature`, `...30.feature`, `...31.feature`, `...32.feature`, `...33.feature`, `...34.feature`, `...35.feature`, `...36.feature`, `...37.feature`
  - `MEDIAHOUSE` basket verification steps — `orderDiscount`/`sumDiscount` is applied when zero is expected, or applied at the wrong amount (`3600`, `4000`, `4800`, `8800`)
  - `MEDIAHOUSE` / `RIALTO` verification steps — commission, `priceNet`, `netPrice`, and totals diverge after magazine date/size/placement updates
  - `TC35` — MH basket ID and Agency Prisa ID drift apart during the updated-magazine verification flow

### 6. Transaction rollback and path-parameter binding failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~15+ this week |
| First Seen | 2026-08-01 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_patchRialtoB2A01` — JSON parsing failed in build `#350`
  - `tc_getRialtoB2A06` — build `#350` reported missing required `uuid` path parameters
- `rialtoB2A(CASS)TestCase18.feature`, `...23.feature`, `...24.feature`
  - `User perform CASS POST API - #1.1` / revert flows — backend returns rollback-only HTTP 500 / N400 errors
  - `Verify Rialto reflects the reverted full-page state - #1.1` — `agencyPrisaId` is passed while required `uuid` is undefined

### 7. Store-status code regression (`N200` vs `N202`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 5 this week |
| First Seen | 2026-08-01 |
| Still Active | No |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — builds `#348`, `#349`, `#351`, and `#352` returned `N202` instead of `N200`
  - `tc_getRialtoB2A05` — build `#350` also surfaced the same response-code contract break

---

## Key Observations

- All 16 observed builds in this window were `UNSTABLE` (0% build-level pass rate).
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` accounted for 371 of 399 failed tests this week and remained the dominant source of instability.
- The magazine-focused TC26-TC37 flows produced the highest sustained failure volume and remained active in the latest internal build (`#163`).
- `automationrunCAI-RIALTO-B2A-trunk` improved from 3-4 failures early in the week to 2-3 failures by 2026-08-04/05, but the `tc_getRialtoB2A05` and `tc_postRialtoB2A03` monetary mismatches persisted throughout.
- No new `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` reports were present in this weekly window.

## Recommended Actions

1. Prioritise the magazine basket discount and commission regressions across TC26-TC37, especially the repeated `orderDiscount`, `netPrice`, and commission mismatches.
2. Fix the internal discount-state contract so `discountType`, `discountAmount`, and `[PRELIMINARY]` status flags stay consistent after POST/GET transitions.
3. Resolve sequencing and rollback/path-parameter drift in TC18/23/24/35 so update/revert flows stop corrupting `uuid`, placement, and order-line identity state.
4. Stabilise the trunk contract mismatches in `tc_getRialtoB2A05` and `tc_postRialtoB2A03`; the transient `N200`→`N202` issue appears cleared after build `#352`, but the value assertions remain active.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #163](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-163.md) | 2026-08-06 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #162](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-162.md) | 2026-08-05 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #357](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-357.md) | 2026-08-05 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #356](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-356.md) | 2026-08-05 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #161](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-161.md) | 2026-08-04 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #355](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-355.md) | 2026-08-04 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #354](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-354.md) | 2026-08-04 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #160](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-160.md) | 2026-08-03 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #353](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-353.md) | 2026-08-03 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #352](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-352.md) | 2026-08-03 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #159](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-159.md) | 2026-08-02 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #351](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-351.md) | 2026-08-02 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #350](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-350.md) | 2026-08-02 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #158](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-158.md) | 2026-08-01 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #349](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-349.md) | 2026-08-01 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #348](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-348.md) | 2026-08-01 | UNSTABLE | n/a |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
