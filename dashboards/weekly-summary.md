# Weekly Test Failure Summary

**Period:** 2026-08-28 → 2026-09-03  
**Generated:** 2026-09-04  
**Observed builds:** 7 | **Failed/Unstable builds:** 7 | **Jobs affected:** 2

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| `tc_getRialtoB2A05` StoreStatus payload mismatch | `automationrunCAI-RIALTO-B2A-trunk` | 4 | 2026-08-28 | Yes | High |
| `tc_postRialtoB2A03` self-service pricing halved | `automationrunCAI-RIALTO-B2A-trunk` | 4 | 2026-08-28 | Yes | High |
| `N200` vs `N202` response-code regression | `automationrunCAI-RIALTO-B2A-trunk` | 1 | 2026-08-30 | Yes | Medium |
| Internal order field and array-order drift after update flows | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | ~153 | 2026-08-28 | Yes | High |
| Internal MediaHouse transaction rollback (N400) | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | ~30 | 2026-08-28 | Yes | High |
| Internal path parameter / basket ID propagation failures | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | ~8 | 2026-08-28 | Yes | High |

---

## Root Cause Group Details

### 1. `tc_getRialtoB2A05` StoreStatus payload mismatch

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 4 (builds #398–#401) |
| First Seen | 2026-08-28 (build #398) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — "Returns StoreStatus of Order": iterator mismatch `276757.2` expected vs `369009.6` found. Present in every trunk build in this reporting week.

---

### 2. `tc_postRialtoB2A03` self-service pricing halved

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 4 (builds #398–#401) |
| First Seen | 2026-08-28 (build #398) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A03` — "Calculate price for self service": returned `[44696.29, 44696.29]` where `[89392.58, 89392.58]` is expected. Repeated in every trunk build this week.

---

### 3. `N200` vs `N202` response-code regression

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 1 (build #400) |
| First Seen | 2026-08-30 (build #400) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — "Returns StoreStatus of Update Order": expected `N200` but received `N202` in the latest trunk run.

---

### 4. Internal order field and array-order drift after update flows

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~153 across builds #184, #186, #187 |
| First Seen | 2026-08-28 (build #184) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature`
  - `CASS TC4 Change Placement` — `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`.
- `rialtoB2A(CASS)TestCase5.feature`
  - `CASS TC5 change to Uppslag/Spread/Panorama` — `discountAmount`/`priceGross` mismatches after update.
- `rialtoB2A(CASS)TestCase14.feature`
  - `CASS TC14 change Product, Size, Placement & Date from Rialto` — package and placement ordering mismatches on POST/GET.
- `rialtoB2A(CASS)TestCase16.feature` / `TestCase17.feature` / `TestCase18.feature`
  - `printDetails` ordering mismatch observed in the latest internal builds.
- `rialtoB2A(CASS)TestCase22.feature`
  - `CASS TC22 in MH change from Full page to uppslag` — ordering and amount mismatches persisted across the week.
- `rialtoB2A(CASS)TestCase35.feature`
  - `CASS TC35 Magazine (change Date, Size & Placement from Rialto)` — field-order and basket-ID drift continue to fail.

---

### 5. Internal MediaHouse transaction rollback (N400)

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~30 across builds #184, #186, #187 |
| First Seen | 2026-08-28 (build #184) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase22.feature`
  - `CASS TC22 in MH change from Full page to uppslag` — `Transaction rolled back because it has been marked as rollback-only` on update/revert steps.
- `rialtoB2A(CASS)TestCase23.feature`
  - `CASS TC23 in MH change from Full page to uppslag (two orderlines)` — rollback on both POST update and revert operations.
- `rialtoB2A(CASS)TestCase24.feature`
  - `CASS TC24 in MH change from uppslag to Full page` — rollback errors persisted in the latest internal runs.
- `rialtoB2A(CASS)TestCase37.feature`
  - `CASS TC37 2 Products Magazine (changes the size in MH)` — rollback on head-line date change.

---

### 6. Internal path parameter / basket ID propagation failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~8 across builds #184, #186, #187 |
| First Seen | 2026-08-28 (build #184) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase24.feature`
  - `CASS TC24 in MH change from uppslag to Full page` — redundant `agencyPrisaId` and undefined `uuid` path parameters during revert validation.
- `rialtoB2A(CASS)TestCase35.feature`
  - `CASS TC35 Magazine (change Date, Size & Placement from Rialto)` — `orBoxid`/Agency Prisa ID mismatch observed in MediaHouse verification.
- `rialtoB2A(CASS)TestCase36.feature`
  - `CASS TC36 Magazine (change Product Size Placement & Date from Rialto)` — basket lookup and ID synchronization failures remain active.

---

## Key Observations

- All 7 observed builds this week were `UNSTABLE`.
- `automationrunCAI-RIALTO-B2A-trunk` reported 4 consecutive unstable builds (#398–#401). The two chronic issues (`tc_getRialtoB2A05` and `tc_postRialtoB2A03`) remained active throughout the week.
- The `N200` vs `N202` response-code regression reappeared in build #400, indicating the status-code contract remains unstable on the trunk path.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` reported 3 active builds in this reporting window (#184, #186, #187), with elevated field-ordering drift and transaction rollback counts continuing to dominate the weekly failure profile.
- The rollback regression remains persistent in the MediaHouse update/revert flows and is now the clearest new back-end issue in the internal job.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` had no new build reports this week; the latest recorded run remains build #326 from 2026-07-28.

---

## Recommended Actions

1. **Prioritise the trunk payload and pricing contract** — `tc_getRialtoB2A05` and `tc_postRialtoB2A03` remained red in every trunk build and should be treated as the immediate remediation target.
2. **Investigate the rollback regression in MediaHouse update/revert flows** — the N400 pattern is the clearest new regression in the internal job and should be correlated with the most recent backend deployment or data change.
3. **Fix path parameter / basket ID propagation** — undefined `uuid` and `orBoxid`/Agency Prisa mismatches are compounding the internal failures and need a focused contract fix.
4. **Address array-ordering drift across multi-line scenarios** — the ordering mismatches in `printDetails` and related arrays are likely caused by a single comparison/sorting issue and should be handled centrally.
5. **Re-run or verify the demo job** — there were no new demo builds in this reporting window, so the job schedule or reporting pipeline should be checked.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #401](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-401.md) | 2026-08-31 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #187](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-187.md) | 2026-08-31 | UNSTABLE | 89.7% |
| [automationrunCAI-RIALTO-B2A-trunk #400](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-400.md) | 2026-08-30 | UNSTABLE | 76.5% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #186](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-186.md) | 2026-08-30 | UNSTABLE | 88.1% |
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
