# Weekly Test Failure Summary

**Period:** 2026-08-10 → 2026-08-14  
**Generated:** 2026-08-14  
**Observed builds:** 10 | **Failed/Unstable builds:** 10 | **Jobs affected:** 2

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| Trunk StoreStatus payload and self-service pricing mismatches | `automationrunCAI-RIALTO-B2A-trunk` | 16 failed checks | 2026-08-10 | Yes | High |
| Trunk StoreStatus response-code regression (`N200` vs `N202`) | `automationrunCAI-RIALTO-B2A-trunk` | 4 failed checks | 2026-08-10 | Yes | High |
| Internal order-line sequencing and field-mapping drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 17 grouped failures | 2026-08-11 | Yes | High |
| Internal revert-flow and identifier propagation failures | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 8 grouped failures | 2026-08-11 | Yes | High |
| Internal magazine pricing, discount, and status drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 31 grouped failures | 2026-08-11 | Yes | High |
| Internal single-order placement and pricing drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 12 grouped failures | 2026-08-11 | Yes | High |

## Root Cause Group Details

### 1. Trunk StoreStatus payload and self-service pricing mismatches

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 16 failed checks this week |
| First Seen | 2026-08-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — Builds `#366-#373` repeatedly returned a StoreStatus payload mismatch at element `[3]` (`276757.2` expected vs `369009.6`).
  - `tc_postRialtoB2A03` — Builds `#366-#373` repeatedly returned halved self-service price values (`89392.58` expected vs `44696.29`).

### 2. Trunk StoreStatus response-code regression (`N200` vs `N202`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 4 failed checks this week |
| First Seen | 2026-08-10 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — Builds `#367`, `#370`, `#372`, and `#373` returned `N202` where `N200` is expected on the update-order StoreStatus check.

### 3. Internal order-line sequencing and field-mapping drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 17 grouped failures this week |
| First Seen | 2026-08-11 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase15.feature`, `...19.feature`, `...22.feature`, `...23.feature`, `...24.feature`
  - `TC15 / TC19 / TC22 / TC23 / TC24` — Builds `#168` and `#169` reordered `packageId`, `paCode`, `prodCode`, `plaCode`, `placementId`, `issueDate`, and related amount fields during multi-line updates.

### 4. Internal revert-flow and identifier propagation failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 8 grouped failures this week |
| First Seen | 2026-08-11 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase23.feature`, `...24.feature`, `...35.feature`
  - `TC23 / TC24 / TC35` — Builds `#168` and `#169` hit rollback-only HTTP 500 responses during revert, kept Uppslag payload values after revert, missed required `uuid` path parameters, and drifted between MediaHouse and Agency basket identifiers.

### 5. Internal magazine pricing, discount, and status drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 31 grouped failures this week |
| First Seen | 2026-08-11 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase26.feature`, `...27.feature`, `...28.feature`, `...29.feature`, `...30.feature`, `...31.feature`, `...32.feature`, `...33.feature`, `...34.feature`, `...35.feature`, `...36.feature`, `...37.feature`
  - `TC26-TC37` — Builds `#168` and `#169` kept stale `discountType`, `discountAmount`, `orderDiscount`, commission, placement/date, and `PRELIMINARY` status values after magazine update and revert flows.

### 6. Internal single-order placement and pricing drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 12 grouped failures this week |
| First Seen | 2026-08-11 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase3.feature`, `...4.feature`, `...5.feature`, `...6.feature`, `...9.feature`
  - `TC3 / TC4 / TC5 / TC6 / TC9` — Builds `#168` and `#169` returned unexpected depth, placement, discount, net-price, and status values after single-order size and placement changes.

---

## Key Observations

- All 10 observed builds in this window were `UNSTABLE` (0% build-level pass rate).
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` produced 68 of 88 grouped failures this week (77.3%) across builds `#168` and `#169`.
- `automationrunCAI-RIALTO-B2A-trunk` produced 20 failed checks across 8 builds; the payload mismatch in `tc_getRialtoB2A05` and the halved-price regression in `tc_postRialtoB2A03` were present in every observed run.
- The trunk `N200` → `N202` regression resurfaced in 4 of 8 trunk builds (`#367`, `#370`, `#372`, and `#373`), so the update-order StoreStatus defect is still intermittent rather than resolved.
- No `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` reports were generated in this weekly window.

## Recommended Actions

1. Fix the trunk StoreStatus contract first by correcting both the recurring payload mismatch in `tc_getRialtoB2A05` and the `N200` → `N202` response-code regression in `tc_getRialtoB2A06`.
2. Stabilise internal multi-line mapping and revert flows in TC15/19/22/23/24 so `packageId`, placement/date fields, `uuid`, and basket identifiers survive update and revert sequences.
3. Investigate the internal magazine path separately from the single-order path; TC26-TC37 continue to dominate the weekly failure volume through stale discount, commission, and status propagation.
4. Re-verify single-order size and placement changes in TC3/4/5/6/9 after the revert-flow fixes land because those scenarios still show coupled placement and pricing drift.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Triage |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #373](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-373.md) | 2026-08-13 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #372](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-372.md) | 2026-08-13 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #169](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-169.md) | 2026-08-12 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #371](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-371.md) | 2026-08-12 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #370](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-370.md) | 2026-08-12 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #369](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-369.md) | 2026-08-11 | UNSTABLE | n/a |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #168](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-168.md) | 2026-08-11 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #368](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-368.md) | 2026-08-11 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #367](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-367.md) | 2026-08-10 | UNSTABLE | n/a |
| [automationrunCAI-RIALTO-B2A-trunk #366](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-366.md) | 2026-08-10 | UNSTABLE | n/a |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
