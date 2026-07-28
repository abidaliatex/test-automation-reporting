# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #340

## Build Details

- **Build ID:** 340
- **Date:** 2026-07-28 21:02:19 UTC
- **Status:** UNSTABLE
- **URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/340/

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #340  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

## Response Amount/Value Assertions Do Not Match Actual API Output

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric payload assertions failed due to expected vs actual amount/value differences.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`

**Impact:** 2 failures

**Confidence:** High
