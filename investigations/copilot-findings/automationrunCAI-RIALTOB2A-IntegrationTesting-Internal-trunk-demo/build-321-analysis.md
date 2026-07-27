# Build 321 — Root Cause Analysis

**Source Report:** [build-321.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-321.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-27

---

## Build Summary

Build: 321
Total Tests: 16
Passed: 15
Failed: 1
Pass Rate: 93.8%

---

## Root Cause Groups

## Missing `discountType` Mapping in MediaHouse Order Payload

**Affected Features:**
- `rialtoB2A` — CASS TC29 Magazine (change to Uppslag/Spread/Panorama)

**Affected Scenarios:**
- Verify original full-page order state in MediaHouse (`tc_getMHTC_MZN04a`)

**Failure Pattern:**
`orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`

**Evidence:**
- Jenkins JUnit report shows a single failed assertion in `MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1`
- Console output repeats the same assertion failure for `tc_getMHTC_MZN04a`
- The test has `failedSince: 314`, while the related update and revert scenarios in build 321 are marked fixed/passed

**Impact:** 1 failure

**Confidence:** High

## Summary

- Build 321 is mostly healthy; 15 of 16 tests passed.
- The remaining instability is isolated to one MediaHouse verification scenario checking the original full-page order state.

## Root Cause

- The MediaHouse basket response is still omitting `orders.printDetails.discountType` for the original-state verification path.
- Because the expected source marker `RIALTO` is missing and all other related steps succeed, this points to a data-mapping/serialization gap rather than a broader API outage.

## Affected Components

- MediaHouse basket order response payload
- `orders.printDetails.discountType` field mapping for the TC29 original-state flow

## Recommended Fix

- Trace how `discountType` is populated for the original MediaHouse basket response and compare it with the flows that now pass in build 321.
- Prioritize changes around the regression window starting at build 314.

## Prevention

- Add or strengthen an assertion that validates `discountType` is non-null in the original-state MediaHouse verification flow before downstream comparisons.
