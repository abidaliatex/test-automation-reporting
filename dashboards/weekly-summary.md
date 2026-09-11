# Weekly Test Failure Summary

**Period:** 2026-08-25 → 2026-08-31  
**Generated:** 2026-09-11  
**Observed builds:** 14 | **Failed/Unstable builds:** 14 | **Jobs affected:** 2

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| `tc_getRialtoB2A05` StoreStatus payload mismatch | `automationrunCAI-RIALTO-B2A-trunk` | 7 | 2026-08-25 | Yes | High |
| `tc_postRialtoB2A03` self-service pricing halved | `automationrunCAI-RIALTO-B2A-trunk` | 8 | 2026-08-25 | Yes | High |
| Cross-job path parameter / basket ID propagation failures | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 21 | 2026-08-25 | Yes | High |
| `N200` vs `N202` response-code regression | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 5 | 2026-08-25 | Yes | Medium |
| Internal order field / array-order drift after update flows | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | ~305 | 2026-08-25 | Yes | High |
| Internal MediaHouse transaction rollback / API 500 regression | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | ~67 | 2026-08-25 | Yes | High |

---

## Root Cause Group Details

### 1. `tc_getRialtoB2A05` StoreStatus payload mismatch

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 7 (builds #394–#399 and #401) |
| First Seen | 2026-08-25 (build #394) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A05` — "Returns StoreStatus of Order": iterator mismatch `276757.2` expected vs `369009.6` found in 7 of the 8 trunk builds this week.

---

### 2. `tc_postRialtoB2A03` self-service pricing halved

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk` |
| Total Failures | 8 (builds #394–#401) |
| First Seen | 2026-08-25 (build #394) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_postRialtoB2A03` — "Calculate price for self service": returned `[44696.29, 44696.29]` where `[89392.58, 89392.58]` is expected. Present in every trunk build in this reporting window.

---

### 3. Cross-job path parameter / basket ID propagation failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 21 (internal builds #181, #182, #183, #184, #186, #187 plus trunk build #400) |
| First Seen | 2026-08-25 (build #181) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - Trunk build `#400` — update-order POST flow failed with `Undefined path parameters are: uuid`.
- `rialtoB2A(CASS)TestCase24.feature`
  - `TC24` — redundant `agencyPrisaId` and missing `uuid` path parameters persisted through revert validation.
- `rialtoB2A(CASS)TestCase35.feature`
  - `TC35` — `orBoxid` / Agency Prisa ID mismatches continued across MediaHouse verification.
- `rialtoB2A(CASS)TestCase36.feature`
  - `TC36` — basket lookup and `mhBasketOrderId` synchronization failures remained active.

---

### 4. `N200` vs `N202` response-code regression

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 5 (1 each in trunk builds #394, #396, #400 plus 2 failures in internal build #187) |
| First Seen | 2026-08-25 (build #394) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS).feature`
  - `tc_getRialtoB2A06` — "Returns StoreStatus of Update Order": expected `N200` but received `N202` in three trunk builds this week.
- `rialtoB2A(CASS)TestCase21.feature`
  - `TC21` — internal POST flow reported 2 response-code mismatches with `expected [N200] but found [N202]` in build `#187`.

---

### 5. Internal order field / array-order drift after update flows

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~305 across builds #181, #182, #183, #184, #186, #187 |
| First Seen | 2026-08-25 (build #181) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase4.feature`
  - `TC4` — `orderHeader.statusFlags` and related order-field assertions drifted after change/revert flows.
- `rialtoB2A(CASS)TestCase14.feature`
  - `TC14` — package, placement, and issue-date ordering mismatches persisted on POST and GET validation.
- `rialtoB2A(CASS)TestCase16.feature` / `TestCase17.feature` / `TestCase18.feature`
  - `printDetails` ordering remained unstable in multi-product scenarios.
- `rialtoB2A(CASS)TestCase22.feature` / `TestCase23.feature` / `TestCase24.feature`
  - MediaHouse update/revert flows continued to return reordered arrays and incorrect correlated field values.
- `rialtoB2A(CASS)TestCase35.feature` / `TestCase36.feature` / `TestCase37.feature`
  - Magazine scenarios still showed field-order drift, pricing side-effects, and basket-state mismatches.

---

### 6. Internal MediaHouse transaction rollback / API 500 regression

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | ~67 across builds #181, #182, #183, #184, #186, #187 |
| First Seen | 2026-08-25 (build #181) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `rialtoB2A(CASS)TestCase14.feature`
  - `TC14` — POST requests intermittently returned `N500` with `{"errorCode":1,"message":null}`.
- `rialtoB2A(CASS)TestCase22.feature` / `TestCase23.feature` / `TestCase24.feature`
  - Update and revert operations repeatedly failed with `Transaction rolled back because it has been marked as rollback-only`.
- `rialtoB2A(CASS)TestCase37.feature`
  - `TC37` — MediaHouse head-line updates continued to trigger rollback failures.

---

## Key Observations

- All 14 observed builds in this reporting window were `UNSTABLE`.
- `automationrunCAI-RIALTO-B2A-trunk` reported 8 consecutive unstable builds (#394–#401). The chronic StoreStatus payload mismatch stayed red in 7 builds, while the self-service pricing defect appeared in all 8.
- The `N200` vs `N202` contract drift was no longer isolated to trunk: internal build `#187` showed the same response-code regression on `TC21`.
- Shared path-parameter and basket-ID propagation failures now span both active jobs, with trunk build `#400` and six internal builds all surfacing missing IDs or mismatched basket references.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` dominated the weekly failure volume with ~305 order-field/array-order mismatches and ~67 rollback/API-500 failures across six builds.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` had no new build reports in this window; the latest recorded run remains build `#326` from `2026-07-28`.

---

## Recommended Actions

1. **Prioritise the trunk contract defects** — fix `tc_getRialtoB2A05` and `tc_postRialtoB2A03` first, because they remained the most stable recurring failures across the active trunk window.
2. **Repair shared identifier propagation** — the missing `uuid`, `mhBasketOrderId`, and `orBoxid` / Agency Prisa mismatches now affect both jobs and are likely amplifying follow-on failures.
3. **Investigate the internal rollback / N500 regression** — correlate the repeated rollback-only and `{"errorCode":1}` responses with the most recent backend deployment or transaction-handling change.
4. **Normalise ordering and state comparison logic** — the internal suite still shows widespread array-order and correlated field drift after update flows, so a central comparison or sorting fix is likely needed.
5. **Check demo-job freshness** — there were still no new demo reports, so the schedule or reporting pipeline for the demo job should be verified.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---|
| [automationrunCAI-RIALTO-B2A-trunk #401](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-401.md) | 2026-08-31 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #187](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-187.md) | 2026-08-31 | UNSTABLE | 89.7% |
| [automationrunCAI-RIALTO-B2A-trunk #400](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-400.md) | 2026-08-30 | UNSTABLE | 76.5% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #186](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-186.md) | 2026-08-30 | UNSTABLE | 88.1% |
| [automationrunCAI-RIALTO-B2A-trunk #399](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-399.md) | 2026-08-29 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #398](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-398.md) | 2026-08-28 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #184](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-184.md) | 2026-08-28 | UNSTABLE | 89.1% |
| [automationrunCAI-RIALTO-B2A-trunk #397](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-397.md) | 2026-08-27 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #183](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-183.md) | 2026-08-27 | UNSTABLE | 89.1% |
| [automationrunCAI-RIALTO-B2A-trunk #396](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-396.md) | 2026-08-26 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #182](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-182.md) | 2026-08-26 | UNSTABLE | 88.7% |
| [automationrunCAI-RIALTO-B2A-trunk #395](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-395.md) | 2026-08-25 | UNSTABLE | 88.2% |
| [automationrunCAI-RIALTO-B2A-trunk #394](../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-394.md) | 2026-08-25 | UNSTABLE | 82.4% |
| [automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk #181](../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-181.md) | 2026-08-25 | UNSTABLE | 90.9% |

---

*This dashboard is regenerated weekly from the build reports in `reports/build-failures/`. Do not edit manually — rerun the weekly summary pipeline instead.*
