# Weekly Test Failure Summary

**Period:** 2026-08-15 → 2026-08-21  
**Generated:** 2026-08-21  
**Observed builds:** 15 | **Failed/Unstable builds:** 15 | **Jobs affected:** 2

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| Trunk StoreStatus payload mismatch (`tc_getRialtoB2A05`) | `automationrunCAI-RIALTO-B2A-trunk` | 10 | 2026-08-15 | Yes | High |
| Trunk StoreStatus response-code regression (`N200` vs `N202`) | `automationrunCAI-RIALTO-B2A-trunk` | 7 | 2026-08-15 | Yes | High |
| Trunk self-service pricing halved (`tc_postRialtoB2A03`) | `automationrunCAI-RIALTO-B2A-trunk` | 10 | 2026-08-15 | Yes | High |
| Trunk transient JSON parse and UUID path cascade (build 378) | `automationrunCAI-RIALTO-B2A-trunk` | 2 | 2026-08-16 | No | Medium |
| Internal single-order placement and pricing drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 22 | 2026-08-15 | Yes | High |
| Internal multi-line sequencing and field-mapping drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 34 | 2026-08-15 | Yes | High |
| Internal revert-flow and identifier propagation failures | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 25 | 2026-08-15 | Yes | High |
| Internal magazine pricing, discount, and status drift | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 60 | 2026-08-15 | Yes | High |

---

## Root Cause Group Details

### 1. Trunk StoreStatus payload mismatch (`tc_getRialtoB2A05`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 10 (all 10 trunk builds this week) |
| First Seen | 2026-08-15 (originally build 231) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — "Returns StoreStatus of Order": element `[3]` iterator mismatch `276757.2` expected vs `369009.6` found. Present in every trunk run (#376–#385) except build 378 where the same test failed earlier on the status-code step (N202) instead.

---

### 2. Trunk StoreStatus response-code regression (`N200` vs `N202`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 7 (builds #376, #377, #378, #379, #380, #384, #385) |
| First Seen | 2026-08-15 (originally build 231) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — "Returns StoreStatus of Update Order": status code step returns `N202` where `N200` is required. Absent in builds #381, #382, #383, confirming the defect remains intermittent.

---

### 3. Trunk self-service pricing halved (`tc_postRialtoB2A03`)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 10 (all 10 trunk builds this week) |
| First Seen | 2026-08-15 (originally build 231) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A03` — "Calculate price for self service": response body fields return `[44696.29, 44696.29]` where `[89392.58, 89392.58]` (exactly double) is expected. Present in every trunk run this week.

---

### 4. Trunk transient JSON parse and UUID path cascade (build 378 only)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 2 (build #378 only) |
| First Seen | 2026-08-16 |
| Still Active | No |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_patchRialtoB2A01` — "Update ad (Order) for self service": `Failed to parse the JSON document` on the POST request step.
  - `tc_getRialtoB2A06` — cascading `uuid` path-parameter failure (`Expected 1, was 0. Undefined path parameters are: uuid`) following the JSON parse failure above.

---

### 5. Internal single-order placement and pricing drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~22 grouped failures across builds #172–#176 |
| First Seen | 2026-08-15 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature`
  - `CASS TC4 Change Placement` — `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]` (all 5 builds).
- `rialtoB2A(CASS)TestCase5.feature`
  - `CASS TC5 change to Uppslag/Spread/Panorama` — `discountAmount` expected `0.0` found `63660.63`; `priceGross` expected `250000.00` found `192192.0` (all 5 builds).
- `rialtoB2A(CASS)TestCase6.feature`
  - `CASS TC6 change date and size` — `priceNet`/`priceGross`/`commission` mismatches after size change (all 5 builds).
- `rialtoB2A(CASS)TestCase9.feature`
  - `CASS TC9 change size from Rialto` — `discountAmount`/`priceNetExComm` mismatch on POST; `depth`/`moduleCode` mismatch on GET (all 5 builds).

---

### 6. Internal multi-line sequencing and field-mapping drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~34 grouped failures across builds #172–#176 |
| First Seen | 2026-08-15 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase14.feature`
  - `CASS TC14 change Product, Size, Placement & Date from Rialto` — HTTP 500 (`N500` instead of `N200`) on POST (builds #174, #175, #176); `paCode`/`prodCode`/`plaCode` and amount mismatches on GET.
- `rialtoB2A(CASS)TestCase15.feature`
  - `CASS TC15 2 products change date MH on head order line` — `paCode`/`prodCode`/`issueDate` array ordering wrong on GET; `packageId`/`productId` ordering mismatch on POST (all 5 builds).
- `rialtoB2A(CASS)TestCase18.feature`
  - `CASS TC18 2 products change size (non-head) from MH` — `moduleCode` expected `[58, 54]` found `[58, 58]` (build #174).
- `rialtoB2A(CASS)TestCase19.feature`
  - `CASS TC19 2 products change placement on head order from MH` — `packageId`/`productId` ordering mismatch (builds #174, #175, #176).
- `rialtoB2A(CASS)TestCase20.feature`
  - `CASS TC20 2 products change placement (non-head) from MH` — `placementId` expected `[TEXT, SIDAN3]` found `[TEXT, TEXT]` (builds #174, #175, #176).
- `rialtoB2A(CASS)TestCase22.feature`
  - `CASS TC22 in MH change from Full page to uppslag` — `paCode`/`prodCode` ordering and `netAmount`/`grossAmount` value mismatches across three GET calls (all 5 builds).

---

### 7. Internal revert-flow and identifier propagation failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~25 grouped failures across builds #172–#176 |
| First Seen | 2026-08-15 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase23.feature`
  - `CASS TC23 in MH change from Full page to uppslag (two orderlines)` — `netAmount` rounding and `orderDiscount` (`0.00` vs `323621.09`) mismatch on updated basket; `netAmount` incorrect on reverted basket (all 5 builds).
- `rialtoB2A(CASS)TestCase24.feature`
  - `CASS TC24 in MH change from uppslag to Full page` — HTTP 500 rollback-only on revert POST (all 5 builds); `plaCode` remains `UPPSLAG` after revert; `paCode`/`prodCode` ordering mismatch; redundant `agencyPrisaId` path parameter and undefined `uuid` causing API errors (all 5 builds).

---

### 8. Internal magazine pricing, discount, and status drift

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~60 grouped failures across builds #172–#176 |
| First Seen | 2026-08-15 |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase28.feature`
  - `CASS TC28 Magazine (change size)` — `statusFlags` expected `[PRELIMINARY]` found `[]` on Rialto revert verify (all 5 builds).
- `rialtoB2A(CASS)TestCase29.feature`
  - `CASS TC29 Magazine (change to Uppslag/Spread/Panorama)` — same `statusFlags` `[PRELIMINARY]` vs `[]` regression (all 5 builds).
- `rialtoB2A(CASS)TestCase31.feature`
  - `CASS TC31 Magazine (change Date, Size & Placement)` — `priceNet` expected `5000.0` found `4845.0`; `commissionAmount` `0.0` vs `155.0` after revert (all 5 builds).
- `rialtoB2A(CASS)TestCase35.feature`
  - `CASS TC35 Magazine (change Date Size & Placement from Rialto)` — `placementId` expected `SIDAN2` found `HALVLIGG`; wrong `issueDate`/`depth`/`price` on Rialto; `orBoxid` vs Agency Prisa ID basket mismatch on MediaHouse (all 5 builds).
- `rialtoB2A(CASS)TestCase36.feature`
  - `CASS TC36 Magazine (change Product Size Placement & Date from Rialto)` — `orderDiscount`/`sumDiscount`/`netPrice` wrong on both original and updated MediaHouse state (all 5 builds).
- `rialtoB2A(CASS)TestCase37.feature`
  - `CASS TC37 2 Products Magazine (changes the size in MH)` — `totalInclVat`/`vat`/`commission`/`orderbasketSummary` wrong on MediaHouse original and updated state; `placementId`/`depth`/`statusFlags` mismatch on Rialto verify (all 5 builds).

---

## Key Observations

- All 15 observed builds were `UNSTABLE` (0% build-level pass rate).
- `automationrunCAI-RIALTO-B2A-trunk` ran 10 builds (#376–#385); all three chronic regressions (`tc_getRialtoB2A05`, `tc_getRialtoB2A06`, `tc_postRialtoB2A03`) carried over from the previous week and remain unresolved.
- The `N200→N202` regression in `tc_getRialtoB2A06` is intermittent: absent in builds #381, #382, #383 but returned in #384 and #385, suggesting an environmental or race condition rather than a hard regression.
- Build #378 introduced two additional transient failures (`tc_patchRialtoB2A01` JSON parse and a cascading `uuid` path-parameter error); neither appeared in any other build this week.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` ran 5 builds (#172–#176); total failures ranged from 26 to 30 per build (141 total).
- TC14 escalated this week: builds #174, #175, and #176 hit HTTP 500 (`N500`) on the CASS POST call, which was not seen in #172 or #173, possibly indicating a new back-end regression introduced mid-week.
- TC18 returned a `moduleCode` mismatch only in build #174; may be transient.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` produced no new builds this week (latest report is build-326, dated 2026-07-28).

---

## Recommended Actions

1. **Prioritise the trunk StoreStatus contract** — `tc_getRialtoB2A05` (payload mismatch) and `tc_postRialtoB2A03` (price halved) have been failing since build 231 and hit every single trunk run; they should be the immediate fix target.
2. **Investigate the N200→N202 intermittency in `tc_getRialtoB2A06`** — the defect cleared for three consecutive builds (#381–#383) then returned; check whether a deployment or data reset correlates with the intermittent passes.
3. **Resolve the TC14 N500 escalation in the internal job** — the HTTP 500 rollback appearing from build #174 onwards suggests a back-end change; root-cause and revert or patch before it spreads further.
4. **Fix the `uuid` path parameter in TC24** — the `agencyPrisaId` redundant parameter and undefined `uuid` are causing hard API errors on every revert step; this blocks the entire TC23/TC24 scenario group.
5. **Stabilise the magazine scenarios (TC28–TC37)** — discount, `statusFlags`, commission, and basket-ID propagation are all stale after update/revert flows and account for the largest share (~43%) of internal failures this week.
6. **Re-run demo job** — no builds have been observed since 2026-07-28; verify whether the job is still scheduled.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #385](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-385.md) | 2026-08-19 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTO-B2A-trunk #384](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-384.md) | 2026-08-19 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #176](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-176.md) | 2026-08-19 | UNSTABLE | 94.4% |
| [automationrunCAI-RIALTO-B2A-trunk #383](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-383.md) | 2026-08-18 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #382](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-382.md) | 2026-08-18 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #175](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-175.md) | 2026-08-18 | UNSTABLE | 94.6% |
| [automationrunCAI-RIALTO-B2A-trunk #381](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-381.md) | 2026-08-17 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #380](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-380.md) | 2026-08-17 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #174](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-174.md) | 2026-08-17 | UNSTABLE | 94.2% |
| [automationrunCAI-RIALTO-B2A-trunk #379](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-379.md) | 2026-08-16 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTO-B2A-trunk #378](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-378.md) | 2026-08-16 | UNSTABLE | 76.5% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #173](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-173.md) | 2026-08-16 | UNSTABLE | 94.6% |
| [automationrunCAI-RIALTO-B2A-trunk #377](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-377.md) | 2026-08-15 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTO-B2A-trunk #376](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-376.md) | 2026-08-15 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #172](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-172.md) | 2026-08-15 | UNSTABLE | 94.9% |

---

*This dashboard is regenerated weekly. Do not edit manually — rerun the weekly summary pipeline instead.*
