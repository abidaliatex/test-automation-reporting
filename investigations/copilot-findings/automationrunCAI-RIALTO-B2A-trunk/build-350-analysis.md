# Investigation — automationrunCAI-RIALTO-B2A-trunk #350

Source report: [build-350.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-350.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #350  
Total Tests: 17  
Passed: 13  
Failed: 4  
Pass Rate: 76.5%

---

## Root Cause Groups

## Store status assertion drift

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)

**Failure Pattern:**
`expected [N200] but found [N202]`

**Evidence:**
- `Then User verify the status code "Response Code"...failed`
- Assertion mismatch on expected vs actual order status code.

**Impact:** 1 failure

**Confidence:** High

---

## UUID-dependent flow break (patch/get chain)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Update ad(Order) for self service (`tc_patchRialtoB2A01`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Patch flow fails to produce/propagate valid JSON and UUID; downstream GET runs without required `uuid` path parameter.

**Evidence:**
- `Failed to parse the JSON document`
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

**Impact:** 2 failures

**Confidence:** High

---

## Price baseline mismatch

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
`expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`

**Evidence:**
- Response body field assertions failed while request and status code steps passed.
- Actual value is approximately 50% of expected baseline.

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #350 is UNSTABLE with 4 failures concentrated in status assertion, UUID propagation chain, and pricing baseline checks.

## Root Cause

- Assertions and test data baselines are out of sync with current API behavior for status and pricing.
- The update-order test chain likely has a malformed/non-JSON intermediate response, causing UUID extraction failure and subsequent GET parameter failure.

## Affected Components

- `rialtoB2A(CASS).feature`
- `Rialto/RialtoB2A/getRialtoB2A.csv`
- `Rialto/RialtoB2A/patchRialtoB2A.csv`
- `Rialto/RialtoB2A/postRialtoB2A.csv`

## Recommended Fix

- Rebaseline expected status/price assertions for `tc_getRialtoB2A05` and `tc_postRialtoB2A03`.
- Validate patch response schema/content before JSON parsing in `tc_patchRialtoB2A01`; fail fast with explicit payload logging.
- Gate `tc_getRialtoB2A06` on successful UUID capture from upstream step.

## Prevention

- Add scenario-level guard checks for required dynamic fields (for example `uuid`) before dependent API calls.
- Add lightweight contract checks to detect status-code and key pricing-field drift before strict value assertions.
