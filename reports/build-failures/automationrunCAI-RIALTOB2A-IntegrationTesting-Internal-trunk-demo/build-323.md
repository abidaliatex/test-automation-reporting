# Build Failure Report

**Build ID:** 323  
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo  
**Date:** 2026-07-27  
**Status:** UNSTABLE  
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/323/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 14 |
| Passed | 10 |
| Failed | 4 |
| Skipped | 0 |
| Pass Rate | 71.4% |
| Duration | ~2m 05s |

---

## Failing Tests / Steps

### Failure 1 — User perform CASS GET API - #1.1
- **Scenario:** `tc_getMHTC01` — verify order created in Rialto from MH
- **Flow:** `MediaHouse\\getMHB2A.csv`
- **Error:** `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`

### Failure 2 — User perform CASS POST API - #1.1
- **Scenario:** `tc_patchIntegrationMH01` — the scenario with one order with only one order line and where the Media house changes the date in the order
- **Flow:** `MediaHouse\\patchMHB2A.csv`
- **Error:** `body.orderAdDetailUpdates[0].issueDate expected [2026-07-21] but found [2026-12-21]`

### Failure 3 — User perform CASS GET API - #1.1
- **Scenario:** `tc_getMHTC01a` — get order created in Rialto from MH - after change
- **Flow:** `MediaHouse\\getMHB2A.csv`
- **Error (key mismatches):**
  - `orders[0].printDetails.discountType expected [[NONE]] but found [[null]]`
  - `orderBasketPriceSummary.orderDiscount expected [0.00] but found [63660.63]`
  - `orderBasketPriceSummary.netPrice expected [192192.00] but found [128531.37]`

### Failure 4 — User perform CASS POST API - #1.1
- **Scenario:** `tc_getIntegrationRialto02` — get order in rialto using risa id - check if issue date updated
- **Flow:** `Rialto\\RialtoB2A\\getRialtoB2A.csv`
- **Error (key mismatches):**
  - `discountAmount expected [0.0] but found [63660.63]`
  - `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
  - `orderHeader.priceNetExComm expected [192192.0] but found [128531.37]`
