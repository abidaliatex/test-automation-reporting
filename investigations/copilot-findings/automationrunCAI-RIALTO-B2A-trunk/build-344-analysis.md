# Investigation — automationrunCAI-RIALTO-B2A-trunk #344

Source report: [build-344.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-344.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #344  
Total Tests: 17  
Passed: 14  
Failed: 3  
Pass Rate: 82.4%

---

## Root Cause Groups

## StoreStatus assertion drift after order update flow

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
StoreStatus-related GET assertions no longer match the current response content/state.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `expected [N200] but found [N202]`
- Both failures occur in `Rialto\\RialtoB2A\\getRialtoB2A.csv` StoreStatus scenarios.

**Impact:** 2 failures

**Confidence:** Medium

## Price expectation mismatch in self-service calculation

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Calculated price fields returned lower values than the scenario baseline expects.

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- Failure occurs during `Response Body Fields` validation for `Rialto\\RialtoB2A\\postRialtoB2A.csv`.

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #344 is unstable because two StoreStatus validation scenarios and one self-service pricing scenario no longer match the current API responses.
- Jenkins checked out revision `040c0e44eda6533bb8f3f482543aab4e24e6e4d5` with commit message `updated testcase 16 to 20`, which may explain why the current scenario baselines changed.

## Root Cause

- The failing assertions point to expected-value drift in test data or service behavior rather than infrastructure failure.
- The two GET failures appear related to StoreStatus validation in the order/update-order flow.

## Affected Components

- `rialtoB2A(CASS).feature`
- `Rialto\\RialtoB2A\\getRialtoB2A.csv`
- `Rialto\\RialtoB2A\\postRialtoB2A.csv`
- API assertion steps in `ApiStepDefinition`

## Recommended Fix

- Rebaseline the expected StoreStatus outputs for `tc_getRialtoB2A05` and `tc_getRialtoB2A06` against the current order lifecycle response.
- Recheck the expected price values for `tc_postRialtoB2A03` against the current pricing response or updated fixture data.

## Prevention

- Review expected-value updates together with API contract/data changes before merging testcase-only commits.
- Add a lightweight check for StoreStatus and pricing baseline drift in the affected CSV-driven scenarios.
