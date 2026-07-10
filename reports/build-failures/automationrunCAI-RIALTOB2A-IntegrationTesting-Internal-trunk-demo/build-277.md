# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #277  
Date: 2026-07-10 12:46 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse discount and pricing assertions still drift after placement change

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- MediaHouse retrieval checks

**Affected Scenarios:**
- `verify that order arrived in MH from rialto - placement` (`tc_getMHTC03`)
- `verify that order arrived in MH from rialto - placement - after change` (`tc_getMHTC03a`)

**Failure Pattern:**
`discountType` and downstream basket totals still do not match the expected MediaHouse fixture values after the placement-change flow.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `RIALTO`, found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`; `orders[0].vat` expected `31136.73`, found `47051.88`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `NONE`, found `RIALTO`; `orderBasketPriceSummary.commission` expected `7750.00`, found `12500.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50`, found `296875.00`.

**Impact:** 2 failures

**Confidence:** High

### Rialto placement recalculation response still differs from the expected post-update state

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- Rialto retrieval checks

**Affected Scenarios:**
- `get order in rialto using prisa id- check if placement updated` (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
The post-update Rialto GET response still returns unexpected state and amount fields after the placement change.

**Evidence:**
- `orderHeader.statusFlags` expected `PRELIMINARY`, found empty; `orderHeader.commissionAmount` expected `7750.00`, found `620.0`.
- `orderAdDetails[0].depth` expected `184`, found `372`; `orderAdDetails[0].priceNet` expected `250000.00`, found `249380.0`.

**Impact:** 1 failure

**Confidence:** High

---

## Failing Tests / Steps

- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

## Error Output

```text
--- tc_getMHTC03 ---
Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
Mismatch on field: orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
Mismatch on field: orders[0].vat expected [31136.73] but found [47051.88]

--- tc_getMHTC03a ---
Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [12500.00]
Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [296875.00]

--- tc_getIntegrationRialto05b ---
Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
Mismatch on field: orderAdDetails[0].priceNet expected [250000.00] but found [249380.0]
```
