# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #310  
Date: 2026-07-25 13:31:05 UTC  
Status: `UNSTABLE`  
Total Tests: 14  
Passed: 13  
Failed: 1  
Pass Rate: 92.9%

### Failing Tests / Steps

- User perform CASS GET API - #1.1 (`tc_getMHTC06`)

---

## Root Cause Groups

## discountType field not propagated to MediaHouse — Change Date, Size & Placement

**Affected Features:**
- `rialtoB2A(CASS TC7 Change Date, Size & Placement)`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - Change Date, Size & Placement (`tc_getMHTC06`)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`

**Evidence:**
- `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- Assertion error raised at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`
- `failedSince: 310` — first occurrence in this build

**Impact:** 1 failure

**Confidence:** High
