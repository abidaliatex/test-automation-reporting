# Weekly Test Failure Summary

**Period:** 2026-08-03 → 2026-08-09  
**Generated:** 2026-08-09  
**Observed builds:** 18 | **Failed/Unstable builds:** 18 | **Jobs affected:** 2

---

## Root Cause Groups

### 1. Pricing, totals, and precision mismatches

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~223 grouped failure instances this week |
| First Seen | 2026-08-03 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — StoreStatus payload still returns `276757.2` vs expected `369009.6` in builds `#352-#353` and `#365`.
  - `tc_postRialtoB2A03` — Self-service price calculation stays halved (`89392.58` expected vs `44696.29`).
- `rialtoB2A(CASS)TestCase11.feature, ...15.feature, ...21.feature, ...23.feature, ...24.feature`
  - `User perform CASS GET/POST API - #1.1` — `totalInclVat`, `vat`, `netAmount`, `priceNet`, and `priceNetExComm` repeatedly drift from the fixtures.
  - `Verify MediaHouse basket state - #1.1` — Large `orderDiscount`, `netPrice`, and commission mismatches continue after update/revert flows.
- `rialtoB2A(CASS)TestCase26.feature, ...28.feature, ...30.feature, ...31.feature, ...32.feature, ...33.feature, ...34.feature, ...35.feature, ...36.feature, ...37.feature`
  - `Magazine verification steps` — Magazine scenarios keep returning unexpected `orderDiscount`, `sumDiscount`, `commission`, and basket totals.

### 2. Discount-type and status propagation regression

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~37 grouped failure instances this week |
| First Seen | 2026-08-03 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase1-2.feature, ...3.feature, ...4.feature, ...6.feature`
  - `User perform CASS POST API - #1.1` — `orderHeader.statusFlags` keeps returning `[]` instead of `[PRELIMINARY]` in TC1/3/4/6.
- `rialtoB2A(CASS)TestCase4.feature, ...9.feature, ...11.feature, ...15.feature, ...27.feature, ...37.feature`
  - `User perform CASS GET API - #1.1` — `discountType` flips between `RIALTO`, `NONE`, and `null`, which then corrupts downstream pricing assertions.
  - `MEDIAHOUSE / RIALTO verification steps` — Latest failures still show propagated discount-state errors in TC27 and TC37.

### 3. Order-line sequencing and reverted-state drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~54 grouped failure instances this week |
| First Seen | 2026-08-03 |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15.feature, ...18.feature`
  - `User perform CASS POST API - #1.1` — `packageId`, `productId`, and `moduleCode` arrays continue to return in the wrong order.
- `rialtoB2A(CASS)TestCase23.feature, ...24.feature`
  - `Verify updated/reverted MediaHouse basket state - #1.1` — `paCode`, `plaCode`, `prodCode`, `placementId`, and `issueDate` stay stale or come back reordered after revert flows.
- `rialtoB2A(CASS)TestCase35.feature, ...37.feature`
  - `RIALTO / MEDIAHOUSE verification steps` — Placement, depth, and issue-date changes are still not restored to the requested state.

### 4. Basket identity and path-parameter drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~19 grouped failure instances this week |
| First Seen | 2026-08-03 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — Build `#364` failed because the required `uuid` path parameter was undefined.
- `rialtoB2A(CASS)TestCase1-2.feature, ...24.feature, ...35.feature`
  - `User perform CASS POST API / Verify reverted state - #1.1` — `mhBasketOrderId`/`uuid` propagation breaks in TC1/2 and TC24, while TC35 still reports `MH basket ID` vs `Agency Prisa ID` drift.

### 5. Backend rollback and parsing failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 7 grouped failure instances this week |
| First Seen | 2026-08-03 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_patchRialtoB2A01` — Build `#364` briefly regressed to `Failed to parse the JSON document` while updating the order.
- `rialtoB2A(CASS)TestCase18.feature, ...23.feature, ...24.feature`
  - `User perform CASS POST API / revert flows` — Internal builds continue to hit rollback-only HTTP 500 responses during multi-line update and revert scenarios.

### 6. StoreStatus response-code regression (`N200` vs `N202`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 9 failed checks this week |
| First Seen | 2026-08-03 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — Builds `#352`, `#353`, `#356`, and `#360-#365` returned `N202` where `N200` is expected.
  - `tc_getRialtoB2A05` — Build `#364` also surfaced the same response-code break on the StoreStatus-of-Order check.

---

## Key Observations

- All 18 observed builds in this window were `UNSTABLE` (0% build-level pass rate).
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` produced 348 of 382 failed tests this week (91.1%) even though it accounted for only 6 of the 18 builds.
- The trunk job stayed near its 2-3 recurring failures for most of the week, but build `#364` temporarily spiked to 4 failures when JSON parsing and `uuid` path-parameter issues reappeared together.
- The internal job narrowed from 64 failed tests on 2026-08-03 to 55-58 failures per run afterward, but the same pricing, state-propagation, and revert-flow defects remained active in the latest build (`#165`).
- No `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` reports were generated in this weekly window.

## Recommended Actions

1. Fix the internal discount-state contract so `discountType`, `discountAmount`, and `[PRELIMINARY]` status flags stay aligned across POST/GET transitions before addressing downstream fixture noise.
2. Stabilise MediaHouse/Rialto revert flows in TC18/23/24/35 by restoring consistent order-line identity (`packageId`, `productId`, `uuid`, basket IDs) and placement/date state after updates.
3. Investigate the magazine pricing path separately from the core trunk failures; TC26-TC37 still dominate the internal basket/commission mismatches.
4. Resolve the trunk StoreStatus contract break (`N200` → `N202`) and confirm that the transient build `#364` parsing/path-parameter regression does not recur.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #365](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-365.md) | 2026-08-09 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #364](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-364.md) | 2026-08-09 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #363](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-363.md) | 2026-08-08 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #362](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-362.md) | 2026-08-08 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #165](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-165.md) | 2026-08-08 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #361](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-361.md) | 2026-08-07 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #360](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-360.md) | 2026-08-07 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #164](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-164.md) | 2026-08-07 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #163](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-163.md) | 2026-08-06 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #357](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-357.md) | 2026-08-05 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #356](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-356.md) | 2026-08-05 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #162](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-162.md) | 2026-08-05 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #355](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-355.md) | 2026-08-04 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #354](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-354.md) | 2026-08-04 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #161](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-161.md) | 2026-08-04 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #353](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-353.md) | 2026-08-03 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #352](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-352.md) | 2026-08-03 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #160](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-160.md) | 2026-08-03 | UNSTABLE | n/a |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
