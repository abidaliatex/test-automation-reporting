# Build Failure Report

**Build ID:** 326
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-28
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/326/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 14 |
| Passed | 11 |
| Failed | 3 |
| Skipped | 0 |
| Pass Rate | 78.6% |
| Duration | ~2m 09s |

---

## Failing Tests / Steps

### Failure 1 — User perform CASS GET API - #1.1

- **Scenario:** `tc_getMHTC01` — verify order created in Rialto from MH
- **Flow:** `MediaHouse\\getMHB2A.csv`

**Error:**
```text
Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
```

### Failure 2 — User perform CASS GET API - #1.1

- **Scenario:** `tc_getMHTC01a` — get order created in Rialto from MH - after change
- **Flow:** `MediaHouse\\getMHB2A.csv`

**Error (key mismatches):**
```text
orders[0].printDetails.discountType expected [[NONE]] but found [[null]]
orderBasketPriceSummary.orderDiscount expected [0.00] but found [63660.63]
orderBasketPriceSummary.netPrice expected [192192.00] but found [128531.37]
orders[0].orderTotalInclVat expected [232792.56] but found [155683.63]
```

### Failure 3 — User perform CASS POST API - #1.1

- **Scenario:** `tc_getIntegrationRialto02` — get order in rialto using risa id - check if issue date updated
- **Flow:** `Rialto\\RialtoB2A\\getRialtoB2A.csv`

**Error (key mismatches):**
```text
discountAmount expected [0.0] but found [63660.63]
orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
orderHeader.priceNetExComm expected [192192.0] but found [128531.37]
orderAdDetails[0].priceNet expected [186234.05] but found [124546.9]
```
