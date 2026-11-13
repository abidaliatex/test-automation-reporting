# Weekly Test Failure Summary

**Period:** 2026-11-09 → 2026-11-15<br>
**Generated:** 2026-11-13<br>
**Observed builds:** 1 | **Failed/Unstable builds:** 1 | **Jobs affected:** 1

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| `tc_getRialtoB2A05` StoreStatus payload mismatch | `automationrunCAI-RIALTO-B2A-trunk` | 7 | 2026-08-25 | Yes | High |
| `tc_postRialtoB2A03` self-service pricing halved | `automationrunCAI-RIALTO-B2A-trunk` | 8 | 2026-08-25 | Yes | High |
| Cross-job path parameter / basket ID propagation failures | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 21 | 2026-08-25 | Yes | High |
| `N200` vs `N202` response-code regression | `automationrunCAI-RIALTO-B2A-trunk`, `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 5 | 2026-08-25 | Yes | Medium |
| Internal order field / array-order drift after update flows | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 305 | 2026-08-25 | Yes | High |
| Internal MediaHouse transaction rollback / API 500 regression | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` | 67 | 2026-08-25 | Yes | High |

---

## Root Cause Group Details

Jenkins provides suite labels, not feature filenames; suite labels are shown below.

### 1. Missing adspace for variant 3

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-13 (build #190) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `ADAPTERS APIs` / `MC ORDER APIs`
  - `tc_mc_ord_post_05` — Create new order (for adapter), ONLINE, MC, POST.
  - `tc_mc_ord_post_03` — Create new order, ONLINE, MC, POST.
  - Both POST validations could not find an adspace for variant 3.

---

### 2. Adapter GET failures

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-13 (build #190) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `ADAPTERS APIs`
  - `tc_getadapters02` — Get mapped data about an order-line; HTTP 400 instead of 200.
  - `tc_getadapters05` — Get info about mapped adspaces; HTTP 400 instead of 200 and a `NullPointerException`.

---

### 3. BASE reference and version mismatches

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-13 (build #190) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `BASE APIs`
  - `tc_getbase10` — Get non-expired production flows for print; actual response also included `PROD2`.
  - `tc_getbase22` — Get database version; expected `8.8`, received `8.9`.

---

### 4. Unexpected customer activity results

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 3 |
| First Seen | 2026-11-13 (build #190) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `CUSTOMER APIs`
  - `tc_cust29` — Customer information objects for salesman and legal person combination; 4 results returned instead of 2.
  - `tc_cust24` — Get customer activities; response included unexpected activity IDs.
  - `tc_cust25` — Get salesman activities; response included unexpected activity IDs.

---

### 5. DWL response content mismatches

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-13 (build #190) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `DWL APIs`
  - `tc_getdwl01` — Get Netsale rows; returned rows differed from expectations.
  - `tc_getdwl02` — Get Online rows; the expected order ID `906588` was absent from the returned rows.

---

### 6. MC order PATCH rejects zero order number

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 305 across builds #181, #182, #183, #184, #186, #187 |
| First Seen | 2026-08-25 (build #181) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `MC ORDER APIs`
  - `tc_mc_ord_patch_09` — Update order, ONLINE, MC, PATCH; rejected because `ono=0`.

---

### 7. Print order POST lazy initialization error

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` |
| Total Failures | 67 across builds #181, #182, #183, #184, #186, #187 |
| First Seen | 2026-08-25 (build #181) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `PRINT ORDER APIs`
  - `tc_print_ord_post_01` — Create new print order.
  - `tc_print_ord_post_07` — Create new print order with `orTypeofsplit`.
  - `tc_print_ord_post_08` — Create new print order without `orTypeofsplit`.
  - All three failed when service-fee prices were accessed after the persistence session closed.

---

## Key Observations

- All 14 observed builds in this reporting window were `UNSTABLE`.
- No build reports newer than 2026-08-31 were available; this is the latest report-backed window, not a current-week snapshot.
- `automationrunCAI-RIALTO-B2A-trunk` reported 8 consecutive unstable builds (#394–#401). The chronic StoreStatus payload mismatch stayed red in 7 builds, while the self-service pricing defect appeared in all 8.
- The `N200` vs `N202` contract drift was no longer isolated to trunk: internal build `#187` showed the same response-code regression on `TC21`.
- Shared path-parameter and basket-ID propagation failures now span both active jobs, with trunk build `#400` and six internal builds all surfacing missing IDs or mismatched basket references.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` dominated the weekly failure volume with 305 order-field/array-order mismatches and 67 rollback/API-500 failures across six builds.
- `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` had no new build reports in this window; the latest recorded run remains build `#326` from `2026-07-28`.

---

## Recommended Actions

1. **Check variant-3 test data** — confirm the configured adspace is present for the order POST scenarios.
2. **Investigate Adapter GET responses** — address the unexpected HTTP 400 responses and the mapped-adspaces null dereference.
3. **Reconcile BASE expectations** — verify the production-flow data and database version expected by the tests.
4. **Review customer and DWL test data** — confirm expected result counts, activity IDs, and returned rows match the test environment.
5. **Validate PATCH inputs** — ensure the test supplies a nonzero order number where required.
6. **Fix print-order session handling** — ensure service-fee prices are initialized while the persistence session is available.
7. **Check report coverage for other jobs** — confirm their runs are being captured in the weekly reporting pipeline.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---|
| [automationrunCAI-trunk #190](../reports/build-failures/automationrunCAI-trunk/build-190.md) | 2026-11-13 | UNSTABLE | 92.5% |

---

*This dashboard is regenerated weekly from the build reports in `reports/build-failures/`.*
