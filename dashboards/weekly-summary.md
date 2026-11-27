# Weekly Test Failure Summary

**Period:** 2026-11-20 → 2026-11-26<br>
**Generated:** 2026-11-27<br>
**Observed builds:** 5 | **Failed/Unstable builds:** 5 | **Jobs affected:** 5

---

## Root Cause Groups

| Root Cause | Affected Jobs | Total Failures | First Seen | Still Active | Confidence |
|---|---|---:|---|---|---|
| Subscription order OK button unavailable | `automationRunMiscellaneousCases-trunk` | 1 | 2026-11-23 | Yes | Medium |
| Subscription order EAN not visible | `automationRunMiscellaneousCases-trunk` | 1 | 2026-11-23 | Yes | Medium |
| Material editor control not visible | `automationRunOrderCreation-trunk` | 12 | 2026-11-22 | Yes | High |
| Job Notes edit button not visible | `automationRunOrderCreation-trunk` | 5 | 2026-11-22 | Yes | High |
| Job Notes value missing from search results | `automationRunOrderCreation-trunk` | 4 | 2026-11-22 | Yes | High |
| Online Job Notes input file unavailable | `automationRunOrderCreation-trunk` | 6 | 2026-11-22 | Yes | High |
| Order save click intercepted | `automationRunOrderCreation-trunk` | 5 | 2026-11-22 | Yes | High |
| Revised-order action not visible | `automationRunOrderCreation-trunk` | 2 | 2026-11-22 | Yes | High |
| Sales Forecast order not found | `automationRunOrderCreation-trunk` | 2 | 2026-11-22 | Yes | High |
| Undefined test steps | `automationRunOrderCreation-trunk` | 2 | 2026-11-22 | Yes | High |
| Duplicate-module save button not clickable | `automationRunOrderCreation-trunk` | 1 | 2026-11-22 | Yes | High |
| Commission order query returned no rows | `automationRunOrderCreation-trunk` | 1 | 2026-11-22 | Yes | High |
| Online job type control not visible | `automationRunOrderCreation-trunk` | 1 | 2026-11-22 | Yes | High |
| Generated Order Net-Value Mismatches | `automationRunOrderReportVerification-trunk` | 4 | 2026-11-23 | Yes | Medium |
| Filtered Order Number Mismatch | `automationRunOrderReportVerification-trunk` | 2 | 2026-11-23 | Yes | Medium |
| Net Column Visibility Timeout | `automationRunOrderReportVerification-trunk` | 1 | 2026-11-23 | Yes | Medium |
| Offer report data mismatch | `automationRunReports-trunk` | 1 | 2026-11-22 | Yes | High |
| Stock Orders filter dialog timeout | `automationRunReports-trunk` | 1 | 2026-11-22 | Yes | Medium |
| Missing adapter/adspace or invalid order fixture data | `automationrunCAI-trunk` | 5 | 2026-11-23 | Yes | High |
| Hibernate session/lazy-loading failure | `automationrunCAI-trunk` | 3 | 2026-11-23 | Yes | High |
| Stale or changed API response fixtures | `automationrunCAI-trunk` | 8 | 2026-11-23 | Yes | High |

---

## Root Cause Group Details

The weekly window contains the latest available report for each affected job. Root-cause names and confidence levels follow those reports; the failure total is summed across the groups.

| Root Cause | Affected Feature Files & Scenarios |
|---|---|
| Subscription order OK button unavailable | `subscriptionorder.feature` — User creating a subscription order; `User click on Ok "SubscriptionOrder" page` timed out waiting for the OK button. |
| Subscription order EAN not visible | `subscriptionorder.feature` — User creating a subscription order; `User verify EAN number through DB "query"` timed out waiting for the EAN. |
| Material editor control not visible | `createorder.feature` — User Creates new print order (`tc_cno50`, `tc_cno52`, `tc_cno53`, `tc_cno54`, `tc_cno56`, `tc_cno58`, `tc_cno60`, `tc_cno66`, `tc_cno69`, `tc_cno70`, `tc_cno72`, `tc_cno74`); the material accordion button visibility wait timed out. |
| Job Notes edit button not visible | `jobNotes.feature` — User Testing Job Notes (`tc_jobNotes01`, `tc_jobNotes03`, `tc_jobNotes04`, `tc_jobNotes05`, `tc_jobNotes06`); the edit button visibility wait timed out. |
| Job Notes value missing from search results | `jobNotes.feature` — User Testing Job Notes (`tc_jobNotes02`, `tc_jobNotes07`, `tc_jobNotes08`, `tc_jobNotes09`); expected `Automation`, but search returned an empty value. |
| Online Job Notes input file unavailable | `onlineJobNotes.feature` — User Testing Online Job Notes (`tc_jobNotes01`–`tc_jobNotes06`); `onlinejobNotes.csv` was unavailable. |
| Order save click intercepted | `toporder.feature` — User Creates new order (`tc_topord02`, `tc_topord03`, `tc_topord04`, `tc_topord05`, `tc_topord06`); another element intercepted the save-button click. |
| Revised-order action not visible | `revisedOrder.feature` — User Creates new online order (`tc_revonline02`, `tc_revonline03`); the “Revise” control visibility wait timed out. |
| Sales Forecast order not found | `salesForecast.feature` — Create order for order with amount less than Sales Forecast (`tc_sf_order01`); Verify order within forecast amount links and saves normally (`tc_sf03`); `SF_LessAmount` was not found in Recent Orders. |
| Undefined test steps | `minmaxplacementcol.feature` — User updated placement codes for automation execution (`tc_minplacol01`); `salesForecast.feature` — Verify cumulative order amounts trigger info message on Sales Forecast (`tc_sf04`); the database max-value update and opening-a-forecast steps were undefined. |
| Duplicate-module save button not clickable | `duplicateOrders.feature` — User Creates Module (`tc_cno01`); the save-button clickable wait timed out. |
| Commission order query returned no rows | `commissionorders.feature` — User creates new online order for verifying commission (`tc_commord01`); the query returned “Result set after last row.” |
| Online job type control not visible | `onlineJob.feature` — User verify online jobs (`tc_onlinejobtype01`); the `changeJobType` visibility wait timed out. |
| Generated Order Net-Value Mismatches | `createorder.feature` — `User verify generated report data "Order Data"` (`createorder.feature:2537`); expected net values differed from generated report values (4 failures). |
| Filtered Order Number Mismatch | `printstockoforders.feature` — `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`); expected no order number but found rows (2 failures). |
| Net Column Visibility Timeout | `stockOfOrdersCorrCode.feature` — `User verify generated report data "Order Data"` (`stockOfOrdersCorrCode.feature:24`); timed out waiting for the Net column header. |
| Offer report data mismatch | `report_offer.feature` — `User verifying offer reports` (test-case ID not exposed); the generated user value differed from the expected value. |
| Stock Orders filter dialog timeout | `reports_stockoforders.feature` — `Perform Filter Actions for Stock of Order` (`tc_pfa01`); the dialog OK button did not become clickable while saving the filter. |
| Missing adapter/adspace or invalid order fixture data | `adapters.feature`, `mc_orders.feature` — Adapter GETs failed, POSTs could not find an adspace for variant 3, and PATCH rejected a null or zero order number (`tc_getadapters02`, `tc_getadapters05`, `tc_mc_ord_post_03`, `tc_mc_ord_post_05`, `tc_mc_ord_patch_09`). |
| Hibernate session/lazy-loading failure | `print_orders.feature` — Create new print order (`tc_print_ord_post_01`), with or without `orTypeofsplit` (`tc_print_ord_post_07`, `tc_print_ord_post_08`); lazy loading failed after the persistence session closed. |
| Stale or changed API response fixtures | `base.feature`, `customerapi.feature`, `dwl.feature`, `print_orders.feature` — BASE production-flow/database-version checks (`tc_getbase10`, `tc_getbase22`), customer activity and information checks (`tc_cust24`, `tc_cust25`, `tc_cust29`), DWL row checks (`tc_getdwl01`, `tc_getdwl02`), and suggested services (`tc_print_ord_post_05`) returned changed values, records, or ordering. |

---

## Key Observations

- The five reports cover 811 tests: 743 passed and 68 failed, for a weighted pass rate of 91.6%.
- All five builds were unstable; every affected job has one report in this weekly window.
- The 21 root-cause groups account for all 68 reported failures.
- Order creation contributed 41 failures across 11 groups; CAI contributed 16 failures across three groups.
- Each listed cause appears in its job's latest available report in the window; no later build report was available to confirm resolution.

---

## Recommended Actions

1. **Stabilize order-creation UI interactions** — investigate the repeated material, Job Notes, save-button, revised-order, and online-job control failures.
2. **Restore and verify test fixtures** — check the missing online Job Notes file, Sales Forecast data, adapter/adspace setup, and API response fixtures.
3. **Reconcile order/report data** — review generated net values, filtered order results, the Net column, offer data, and the Stock Orders filter dialog.
4. **Fix CAI service handling** — initialize service-fee data while the persistence session is active and verify the affected API response expectations.
5. **Resolve remaining test setup issues** — implement the undefined steps, validate the commission-order query data, and confirm subscription-order EAN and OK-button behavior.

---

## Latest Build Triage Snapshot

| Build | Date | Status | Pass Rate |
|---|---|---|---:|
| [automationRunMiscellaneousCases-trunk #162](../reports/build-failures/automationRunMiscellaneousCases-trunk/build-162.md) | 2026-11-23 | UNSTABLE | 98.1% |
| [automationRunOrderCreation-trunk #163](../reports/build-failures/automationRunOrderCreation-trunk/build-163.md) | 2026-11-22 | UNSTABLE | 85.5% |
| [automationRunOrderReportVerification-trunk #167](../reports/build-failures/automationRunOrderReportVerification-trunk/build-167.md) | 2026-11-23 | UNSTABLE | 93.52% |
| [automationRunReports-trunk #163](../reports/build-failures/automationRunReports-trunk/build-163.md) | 2026-11-22 | UNSTABLE | 96.2% |
| [automationrunCAI-trunk #193](../reports/build-failures/automationrunCAI-trunk/build-193.md) | 2026-11-23 | UNSTABLE | 93.85% |

---

*This dashboard is regenerated weekly from the build reports in `reports/build-failures/`.*
