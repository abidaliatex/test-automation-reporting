# Weekly Test Failure Summary

**Period:** 2026-08-21 → 2026-08-27  
**Generated:** 2026-08-28  
**Observed builds:** 16 | **Failed/Unstable builds:** 16 | **Jobs affected:** 2

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| Trunk StoreStatus payload mismatch (`tc_getRialtoB2A05`) | `automationrunCAI-RIALTO-B2A-trunk` | 11 | 2026-08-21 | Yes | High |
| Trunk self-service pricing halved (`tc_postRialtoB2A03`) | `automationrunCAI-RIALTO-B2A-trunk` | 11 | 2026-08-21 | Yes | High |
| Trunk StoreStatus response-code regression (`N200` vs `N202`) | `automationrunCAI-RIALTO-B2A-trunk` | 2 | 2026-08-25 | Yes | High |
| Internal single-order placement and pricing drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 25 | 2026-08-21 | Yes | High |
| Internal multi-line sequencing and field-mapping drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 50 | 2026-08-21 | Yes | High |
| Internal transaction rollback on MH updates (N400) | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 38 | 2026-08-24 | Yes | High |
| Internal revert-flow and identifier propagation failures | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 30 | 2026-08-21 | Yes | High |
| Internal magazine pricing, discount, and status drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 78 | 2026-08-21 | Yes | High |

---

## Root Cause Group Details

### 1. Trunk StoreStatus payload mismatch (`tc_getRialtoB2A05`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 11 (all 11 trunk builds this week) |
| First Seen | 2026-08-21 (build #386; originally build 231) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — "Returns StoreStatus of Order": element `[3]` iterator mismatch `276757.2` expected vs `369009.6` found. Present in every trunk run this week (#386–#397, excluding #391 which has no report file).

---

### 2. Trunk self-service pricing halved (`tc_postRialtoB2A03`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 11 (all 11 trunk builds this week) |
| First Seen | 2026-08-21 (build #386; originally build 231) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A03` — "Calculate price for self service": response body fields return `[44696.29, 44696.29]` where `[89392.58, 89392.58]` (exactly double) is expected. Present in every trunk run this week.

---

### 3. Trunk StoreStatus response-code regression (`N200` vs `N202`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 2 (builds #394, #396) |
| First Seen | 2026-08-25 (build #394) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — "Returns StoreStatus of Update Order": status code step returns `N202` where `N200` is required. Appeared on 2026-08-25 and 2026-08-26; absent from #386–#393 and #395, #397 — intermittent pattern consistent with prior weeks.

---

### 4. Internal single-order placement and pricing drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~25 grouped failures across builds #177, #180–#183 |
| First Seen | 2026-08-21 (build #177) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature`
  - `CASS TC4 Change Placement` — `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]` (all 5 builds).
- `rialtoB2A(CASS)TestCase5.feature`
  - `CASS TC5 change to Uppslag/Spread/Panorama` — `discountAmount` expected `0.0` found `63660.63`; `priceGross` mismatch (all 5 builds).
- `rialtoB2A(CASS)TestCase6.feature`
  - `CASS TC6 change date and size` — `priceNetExComm`/`priceGross`/`commission` mismatches after size change (all 5 builds).
- `rialtoB2A(CASS)TestCase9.feature`
  - `CASS TC9 change size from Rialto` — `discountAmount`/`priceNetExComm` mismatch on POST; `depth`/`moduleCode` mismatch on GET (all 5 builds).

---

### 5. Internal multi-line sequencing and field-mapping drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~50 grouped failures across builds #177, #180–#183 |
| First Seen | 2026-08-21 (build #177) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase14.feature`
  - `CASS TC14 change Product, Size, Placement & Date from Rialto` — HTTP 500 (`N500` instead of `N200`) on POST (all 5 builds); `paCode`/`prodCode`/`plaCode` and amount mismatches on GET.
- `rialtoB2A(CASS)TestCase15.feature`
  - `CASS TC15 2 products change date MH on head order line` — `paCode`/`prodCode`/`issueDate` array ordering wrong on GET; `packageId`/`productId` ordering mismatch on POST (all 5 builds).
- `rialtoB2A(CASS)TestCase16.feature` / `TestCase17.feature` / `TestCase18.feature`
  - TC16, TC17, TC18 — `printDetails` field ordering mismatch on POST and GET (builds #182, #183; newly escalating).
- `rialtoB2A(CASS)TestCase19.feature`
  - `CASS TC19 2 products change placement on head order from MH` — `packageId`/`productId` ordering mismatch (all 5 builds).
- `rialtoB2A(CASS)TestCase20.feature`
  - `CASS TC20 2 products change placement (non-head) from MH` — `placementId` expected `[TEXT, SIDAN3]` found `[TEXT, TEXT]` (all 5 builds).
- `rialtoB2A(CASS)TestCase22.feature`
  - `CASS TC22 in MH change from Full page to uppslag` — `paCode`/`prodCode` ordering and `netAmount`/`grossAmount` value mismatches (all 5 builds); transaction rollback (N400) on POST introduced from build #180.

---

### 6. Internal transaction rollback on MediaHouse updates (N400)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~38 failures across builds #180–#183 |
| First Seen | 2026-08-24 (build #180) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase22.feature`
  - `CASS TC22 in MH change from Full page to uppslag` — `Transaction rolled back because it has been marked as rollback-only`; expected `N200` but got `N400` on POST (builds #180–#183).
- `rialtoB2A(CASS)TestCase23.feature`
  - `CASS TC23 in MH change from Full page to uppslag (two orderlines)` — rollback on both update and revert POST steps (builds #180–#183).
- `rialtoB2A(CASS)TestCase24.feature`
  - `CASS TC24 in MH change from uppslag to Full page` — rollback on update and revert POST steps (builds #180–#183).
- `rialtoB2A(CASS)TestCase37.feature`
  - `CASS TC37 2 Products Magazine (changes the size in MH)` — rollback on MH head-line date change (builds #180–#183).

**Note:** This pattern was absent from build #177 (2026-08-21) and first appeared in build #180 (2026-08-24), suggesting a mid-week back-end regression.

---

### 7. Internal revert-flow and identifier propagation failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~30 grouped failures across builds #177, #180–#183 |
| First Seen | 2026-08-21 (build #177) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase23.feature`
  - `CASS TC23 in MH change from Full page to uppslag (two orderlines)` — `netAmount` rounding and `orderDiscount` mismatch on updated and reverted baskets (all 5 builds).
- `rialtoB2A(CASS)TestCase24.feature`
  - `CASS TC24 in MH change from uppslag to Full page` — `placementId` remains `UPPSLAG` after revert (all 5 builds); redundant `agencyPrisaId` path parameter and undefined `uuid` causing hard API errors on Rialto verify step (all 5 builds); HTTP 500 on revert POST (builds #177, #180–#183).

---

### 8. Internal magazine pricing, discount, and status drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~78 grouped failures across builds #177, #180–#183 |
| First Seen | 2026-08-21 (build #177) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase28.feature`
  - `CASS TC28 Magazine (change size)` — `statusFlags` expected `[PRELIMINARY]` found `[]` on Rialto revert verify (all 5 builds).
- `rialtoB2A(CASS)TestCase29.feature`
  - `CASS TC29 Magazine (change to Uppslag/Spread/Panorama)` — same `statusFlags` `[PRELIMINARY]` vs `[]` regression (all 5 builds).
- `rialtoB2A(CASS)TestCase35.feature`
  - `CASS TC35 Magazine (change Date, Size & Placement from Rialto)` — `placementId` expected `SIDAN2` found `HALVLIGG`; wrong `issueDate`/`depth`/`price` on Rialto; `orBoxid` vs Agency Prisa ID basket mismatch on MediaHouse (all 5 builds).
- `rialtoB2A(CASS)TestCase36.feature`
  - `CASS TC36 Magazine (change Product Size Placement & Date from Rialto)` — `orderDiscount`/`sumDiscount`/`netPrice` wrong on both original and updated MediaHouse state (all 5 builds).
- `rialtoB2A(CASS)TestCase37.feature`
  - `CASS TC37 2 Products Magazine (changes the size in MH)` — `totalInclVat`/`vat`/`commission`/`orderbasketSummary` wrong on MediaHouse original and updated state; `placementId`/`depth`/`statusFlags` mismatch on Rialto verify (all 5 builds).

---

## Key Observations

- All 16 observed builds were `UNSTABLE` (0% build-level pass rate).
- `automationrunCAI-RIALTO-B2A-trunk` ran 11 builds (#386–#397, noting #391 absent from reports); the two chronic regressions (`tc_getRialtoB2A05`, `tc_postRialtoB2A03`) are now 160+ builds old and hit every single run with no sign of resolution.
- The `N200→N202` regression in `tc_getRialtoB2A06` reappeared in builds #394 and #396 (absent from #386–#393, #395, #397), continuing the intermittent pattern observed in prior weeks.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` ran 5 builds (#177, #180–#183; #178 and #179 have no report files). **Total failures escalated significantly week-over-week**: build #177 had 33 failures, builds #180–#181 had 47 each, build #182 had 58, build #183 had 56.
- **New escalation — Transaction rollback (N400):** A new wave of `Transaction rolled back because it has been marked as rollback-only` errors on TC22, TC23, TC24, and TC37 first appeared in build #180 (2026-08-24) and persisted through build #183. This was absent from build #177 and from the previous week, pointing to a back-end regression introduced on or around 2026-08-24.
- **TC16, TC17, TC18 newly failing:** These scenarios had not been listed in prior weeks but appear in builds #182 and #183 with field-ordering mismatches, indicating the array-ordering regression is spreading to additional TCs.
- **TC21 newly failing in build #183:** HTTP 500 on CASS POST, not seen previously.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` produced no new builds this week (latest report remains build-326, dated 2026-07-28).

---

## Recommended Actions

1. **Prioritise the trunk StoreStatus contract** — `tc_getRialtoB2A05` (payload mismatch) and `tc_postRialtoB2A03` (price halved) have been failing since build 231 and hit every trunk run; they should remain the immediate fix target.
2. **Investigate the N400 transaction-rollback regression** — first seen in internal build #180 (2026-08-24) and affecting TC22–TC24 and TC37; correlate with any deployment or data change on that date and revert or patch before failure count climbs further.
3. **Fix the `uuid` path parameter in TC24** — the `agencyPrisaId` redundant parameter and undefined `uuid` cause hard API errors on every revert step and compound the rollback failures.
4. **Address the widening array-ordering regression** — TC14–TC22 and now TC16, TC17, TC18 all show `printDetails`/`orderAdDetails` field-ordering mismatches; a single fix to the comparison or sorting logic may resolve the bulk of the 50+ multi-line failures.
5. **Stabilise the magazine scenarios (TC28–TC37)** — discount, `statusFlags`, commission, and basket-ID propagation remain stale after update/revert flows and account for the largest share (~35%) of internal failures.
6. **Investigate TC21 HTTP 500** — first appeared in build #183; confirm whether this is a new regression or a transient environment issue.
7. **Re-run or verify the demo job** — no builds have been observed since 2026-07-28; confirm whether the job is still scheduled or has been disabled.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #397](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-397.md) | 2026-08-27 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #183](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-183.md) | 2026-08-27 | UNSTABLE | 89.1% |
| [automationrunCAI-RIALTO-B2A-trunk #396](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-396.md) | 2026-08-26 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #182](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-182.md) | 2026-08-26 | UNSTABLE | 88.7% |
| [automationrunCAI-RIALTO-B2A-trunk #395](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-395.md) | 2026-08-25 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #394](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-394.md) | 2026-08-25 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #181](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-181.md) | 2026-08-25 | UNSTABLE | 90.9% |
| [automationrunCAI-RIALTO-B2A-trunk #393](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-393.md) | 2026-08-24 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #392](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-392.md) | 2026-08-24 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #180](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-180.md) | 2026-08-24 | UNSTABLE | 90.9% |
| [automationrunCAI-RIALTO-B2A-trunk #390](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-390.md) | 2026-08-23 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #389](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-389.md) | 2026-08-22 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #388](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-388.md) | 2026-08-22 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #387](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-387.md) | 2026-08-21 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #386](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-386.md) | 2026-08-21 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #177](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-177.md) | 2026-08-21 | UNSTABLE | 93.6% |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
