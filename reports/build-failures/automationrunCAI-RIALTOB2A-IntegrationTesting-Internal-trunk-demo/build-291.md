# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #291
Date: 2026-07-15 22:36:15 UTC
Status: `UNSTABLE`
Total Tests: 14
Passed: 11
Failed: 3
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse discount and basket total mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rialto - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`discountType` and financial summary fields (commission/VAT/totalInclVat/orderbasketSum) return unexpected values in MH GET validation.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `RIALTO` found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`; `orders[0].vat` expected `31136.73` found `47051.88`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `NONE` found `RIALTO`; `orderBasketPriceSummary.commission` expected `7750.00` found `12500.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50` found `296875.00`.

**Impact:** 2 failures

**Confidence:** High

## Rialto post-update placement and pricing mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Post-change Rialto GET response does not match expected placement and pricing state.

**Evidence:**
- `orderAdDetails[0].placementId` expected `SIDAN3` found `TEXT`; `orderAdDetails[0].depth` expected `184` found `372`.
- `discountAmount` expected `0.0` found `63660.63`; `orderHeader.priceNetExComm` expected `250000.00` found `128531.37`; `orderHeader.commissionAmount` expected `7750.00` found `3984.47`.

**Impact:** 1 failure

**Confidence:** High
