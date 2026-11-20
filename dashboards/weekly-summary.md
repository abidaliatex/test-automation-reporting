# Weekly Test Failure Summary

**Period:** 2026-11-16 → 2026-11-22<br>
**Generated:** 2026-11-20<br>
**Observed builds:** 10 | **Failed/Unstable builds:** 10 | **Jobs affected:** 5

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| Subscription-order EAN not visible | `automationRunMiscellaneousCases-trunk` | 2 | 2026-11-17 | Yes | Low |
| Subscription-order confirmation button unavailable | `automationRunMiscellaneousCases-trunk` | 2 | 2026-11-17 | Yes | Low |
| Selenium UI controls unavailable or intercepted | `automationRunOrderCreation-trunk` | 57 | 2026-11-16 | Yes | High |
| Online job notes fixture unavailable | `automationRunOrderCreation-trunk` | 12 | 2026-11-16 | Yes | High |
| Sales Forecast orders not found | `automationRunOrderCreation-trunk` | 4 | 2026-11-16 | Yes | Medium |
| Undefined Cucumber step definitions | `automationRunOrderCreation-trunk` | 4 | 2026-11-16 | Yes | High |
| Database result-set access error | `automationRunOrderCreation-trunk` | 2 | 2026-11-16 | Yes | Medium |
| Job Notes values missing from order search | `automationRunOrderCreation-trunk` | 5 | 2026-11-16 | Yes | High |
| Generated order report data mismatch | `automationRunOrderReportVerification-trunk` | 8 | 2026-11-17 | Yes | Medium |
| Order-number filter returns unexpected rows | `automationRunOrderReportVerification-trunk` | 4 | 2026-11-17 | Yes | Medium |
| Net column unavailable for sorting | `automationRunOrderReportVerification-trunk` | 2 | 2026-11-17 | Yes | Medium |
| Stock Orders filter save timeout | `automationRunReports-trunk` | 2 | 2026-11-16 | Yes | Medium |
| Offer report data mismatch | `automationRunReports-trunk` | 2 | 2026-11-16 | Yes | High |
| MC order creation references an unavailable adspace | `automationrunCAI-trunk` | 4 | 2026-11-17 | Yes | High |
| Adapter GET requests return errors | `automationrunCAI-trunk` | 4 | 2026-11-17 | Yes | Medium |
| BASE response values differ from expectations | `automationrunCAI-trunk` | 4 | 2026-11-17 | Yes | Medium |
| Unexpected customer results | `automationrunCAI-trunk` | 6 | 2026-11-17 | Yes | Medium |
| DWL response data differs from expectations | `automationrunCAI-trunk` | 4 | 2026-11-17 | Yes | Medium |
| MC order PATCH rejects a zero order number | `automationrunCAI-trunk` | 2 | 2026-11-17 | Yes | High |
| Print order POST lazy initialization error | `automationrunCAI-trunk` | 6 | 2026-11-17 | Yes | High |
| Suggested-services response order differs from expectation | `automationrunCAI-trunk` | 1 | 2026-11-19 | Yes | High |

---

## Root Cause Group Details

Jenkins reports suite labels or feature files and steps; where scenario IDs or titles were not provided, they are identified as unavailable.

### 1. Subscription-order EAN not visible

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunMiscellaneousCases-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-17 (build #160) |
| Still Active | Yes |
| Confidence | Low |

**Affected Feature Files & Scenarios:**
- `subscriptionorder.feature`
  - User creating a subscription order — case 33 in build #160; test case ID unavailable in build #161.
  - `User verify EAN number through DB "query"` — timed out waiting for the EAN to become visible.

### 2. Subscription-order confirmation button unavailable

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunMiscellaneousCases-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-17 (build #160) |
| Still Active | Yes |
| Confidence | Low |

**Affected Feature Files & Scenarios:**
- `subscriptionorder.feature`
  - User creating a subscription order — case 41 in build #160; test case ID unavailable in build #161.
  - `User click on Ok "SubscriptionOrder" page` — timed out waiting for the confirmation button to become clickable.

### 3. Selenium UI controls unavailable or intercepted

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderCreation-trunk` |
| Total Failures | 57 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `createorder.feature`, `jobNotes.feature`, `duplicateOrders.feature`, `onlineJob.feature`, `revisedOrder.feature`, `PrintProductionCode.feature`, and `toporder.feature`
  - Build #161 recorded 24 visibility/clickability timeouts and 7 intercepted clicks across print-order creation, job notes, duplicate orders, online jobs, revised orders, production code, and top orders.
  - Build #162 recorded control timeouts for material ad text (12), job-note editing (5), revised-order actions (2), and online job type editing (1); save clicks were intercepted for top orders (5), and a duplicate-module save timed out (1).
  - Specific examples include waiting for the material accordion button, the print-order edit button, and the “Revise” control, or clicking intercepted Save/Add Production Code buttons.

### 4. Online job notes fixture unavailable

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderCreation-trunk` |
| Total Failures | 12 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `onlineJobNotes.feature`
  - `User Testing Online Job Notes` (`tc_jobNotes01`–`tc_jobNotes06`) in builds #161 and #162.
  - All cases failed because `testdata/onlinejobNotes.csv` was unavailable; build #162 reports `NoSuchFileException`.

### 5. Sales Forecast orders not found

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderCreation-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `salesForecast.feature`
  - Verify order within forecast amount links and saves normally.
  - Verify cumulative order amounts trigger an info message on Sales Forecast.
  - The expected `SF_LessAmount` order was absent from Recent Orders in both builds.

### 6. Undefined Cucumber step definitions

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderCreation-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `salesForecast.feature`
  - `User opens Sales Forecast "SF Name"` — undefined in builds #161 and #162.
- `minmaxplacementcol.feature`
  - `user set column max value "UpdateMaxQuery" through db` — undefined in builds #161 and #162.

### 7. Database result-set access error

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderCreation-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `commissionorders.feature`
  - User creates a new online order for verifying commission; build #162 identifies the customer search and selection step.
  - Both builds report `SQLException: Result set after last row`.

### 8. Job Notes values missing from order search

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderCreation-trunk` |
| Total Failures | 5 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `jobNotes.feature`
  - User Testing Job Notes — build #161 reports an empty value instead of `Automation`; build #162 reports missing notes/manuscript values in order-search and header verification.

### 9. Generated order report data mismatch

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderReportVerification-trunk` |
| Total Failures | 8 |
| First Seen | 2026-11-17 (build #165) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `createorder.feature`
  - `User verify generated report data "Order Data"` (`createorder.feature:2537`) — 5 failures in build #165 and 3 in build #166.
  - Reported mismatches include expected net `7,905.60` versus `7,115.04`, and expected `103.00` versus `102.00`.

### 10. Order-number filter returns unexpected rows

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderReportVerification-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-17 (build #165) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `printstockoforders.feature`
  - `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`) — expected no matching rows but received order numbers `926332` or `90000353`.

### 11. Net column unavailable for sorting

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunOrderReportVerification-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-17 (build #165) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `stockOfOrdersCorrCode.feature`
  - `User verify generated report data "Order Data"` (`stockOfOrdersCorrCode.feature:24`) — timed out waiting for the Net column header.

### 12. Stock Orders filter save timeout

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunReports-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- `reports_stockoforders.feature`
  - Save created filter as "Filter Name" — timed out waiting for the dialog’s OK button to become clickable while saving as CSV in builds #161 and #162.

### 13. Offer report data mismatch

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationRunReports-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-16 (build #161) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `report_offer.feature`
  - User verifying offer reports (`tc_offer01`) in build #161; the generated user value also mismatched in build #162 (test case ID unavailable).

### 14. MC order creation references an unavailable adspace

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- Build #191 suite labels: `ADAPTERS APIs` and `MC ORDER APIs`; build #192 feature files: `adapters.feature` and `mc_orders.feature`.
  - Create new order (for adapter), ONLINE, MC, POST (`tc_mc_ord_post_05`).
  - Create new order, ONLINE, MC, POST (`tc_mc_ord_post_03`).
  - Both POST validations returned HTTP 400 because no adspace was found for variant 3.

### 15. Adapter GET requests return errors

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- Build #191 suite label: `ADAPTERS APIs`; build #192 feature file: `adapters.feature`.
  - Get mapped data about an order-line — ADAPTER — GET (`tc_getadapters02`); HTTP 400 instead of 200.
  - Get info about mapped adspaces — ADAPTER — GET (`tc_getadapters05`); HTTP 500 with a `NullPointerException`.

### 16. BASE response values differ from expectations

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- Build #191 suite label: `BASE APIs`; build #192 feature file: `base.feature`.
  - Get non-expired production flows for print (`tc_getbase10`) — actual response also included `PROD2`.
  - Get database version (`tc_getbase22`) — expected `8.8`, received `8.9`.

### 17. Unexpected customer results

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 6 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- Build #191 suite label: `CUSTOMER APIs`; build #192 feature files: `customerapi.feature` and `getcustomeractivitiesapi.feature`.
  - Customer information objects — salesman and legal person combination (`tc_cust29`) — expected 2 results, received 4.
  - Get customer activities (`tc_cust24`) and get salesman activities (`tc_cust25`) — returned activity IDs differed from expected lists.

### 18. DWL response data differs from expectations

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 4 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | Medium |

**Affected Feature Files & Scenarios:**
- Build #191 suite label: `DWL APIs`; build #192 feature file: `dwl.feature`.
  - Get Netsale rows (`tc_getdwl01`) — returned row data differed from expectations.
  - Get Online rows (`tc_getdwl02`) — expected order ID `906588` was absent.

### 19. MC order PATCH rejects a zero order number

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 2 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- Build #191 suite label: `MC ORDER APIs`; build #192 feature file: `mc_orders.feature`.
  - Update order, ONLINE, MC, PATCH (`tc_mc_ord_patch_09`) — rejected because `ono` was zero.

### 20. Print order POST lazy initialization error

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 6 |
| First Seen | 2026-11-17 (build #191) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- Build #191 suite label: `PRINT ORDER APIs`; build #192 feature file: `print_orders.feature`.
  - Create new print order (`tc_print_ord_post_01`).
  - Create new print order with `orTypeofsplit` (`tc_print_ord_post_07`).
  - Create new print order without `orTypeofsplit` (`tc_print_ord_post_08`).
  - All failed while lazily loading service-fee data after the persistence session closed.

### 21. Suggested-services response order differs from expectation

| Field | Detail |
|-------|--------|
| Affected Jobs | `automationrunCAI-trunk` |
| Total Failures | 1 |
| First Seen | 2026-11-19 (build #192) |
| Still Active | Yes |
| Confidence | High |

**Affected Feature Files & Scenarios:**
- `print_orders.feature`
  - Get suggested services — PRINT — POST (`tc_print_ord_post_05`) — expected `[ESP, MIL]`, received `[MIL, ESP]`.

---

## Key Observations

- The reporting window contains 10 unstable builds across five jobs; no successful build report was observed.
- Across the reports, 1,424 of 1,561 tests passed and 137 failed, for a weighted pass rate of 91.2%.
- The 21 grouped root causes account for all 137 reported failures.
- Every grouped cause appears in the latest observed build for its job.
- Several root causes recur in consecutive builds, including missing test fixtures, Sales Forecast results, order-report values, the CAI adspace validation, Adapter GET responses, and print-order service-fee initialization.

---

## Recommended Actions

1. **Restore and verify order-creation test data** — add the missing online job notes fixture, confirm Sales Forecast orders and Job Notes values are available, and investigate database result-set access and undefined step definitions.
2. **Review UI test interactions** — investigate the recurring unavailable or intercepted controls in order creation, including material editing, save actions, job-note editing, and revised-order actions.
3. **Check report data and filters** — reconcile generated order and offer report values, validate filtered order-number expectations, and investigate the missing Net header and Stock Orders filter dialog timeout.
4. **Investigate subscription-order UI state** — verify the EAN is displayed and the confirmation button becomes clickable in both recent builds.
5. **Reconcile CAI test fixtures and API behavior** — validate variant-3 adspace setup, Adapter GET responses, BASE/CUSTOMER/DWL fixtures, and the zero-order-number PATCH input.
6. **Fix print-order service handling and assertions** — initialize service-fee data while the persistence session is active, and verify suggested-service ordering expectations.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---:|
| [automationRunMiscellaneousCases-trunk #161](../reports/build-failures/automationRunMiscellaneousCases-trunk/build-161.md) | 2026-11-19 | UNSTABLE | 98.1% |
| [automationRunOrderCreation-trunk #162](../reports/build-failures/automationRunOrderCreation-trunk/build-162.md) | 2026-11-18 | UNSTABLE | 85.5% |
| [automationRunOrderReportVerification-trunk #166](../reports/build-failures/automationRunOrderReportVerification-trunk/build-166.md) | 2026-11-19 | UNSTABLE | 94.44% |
| [automationRunReports-trunk #162](../reports/build-failures/automationRunReports-trunk/build-162.md) | 2026-11-18 | UNSTABLE | 96.2% |
| [automationrunCAI-trunk #192](../reports/build-failures/automationrunCAI-trunk/build-192.md) | 2026-11-19 | UNSTABLE | 93.85% |

---

*This dashboard is regenerated weekly from the build reports in `reports/build-failures/`.*
