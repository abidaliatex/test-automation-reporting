# Build 378 — Root Cause Analysis

**Job:** automationrunCAI-RIALTO-B2A-trunk
**Report:** [build-378.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-378.md)

---

## Build Summary

Build: 378
Total Tests: 17
Passed: 13
Failed: 4
Pass Rate: 76.5%

---

## Root Cause Groups

## StoreStatus response still pending

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)

**Failure Pattern:**
expected [N200] but found [N202]

**Evidence:**
- `tc_getRialtoB2A05` sends `GET /cass/orders/storeStatus/{uuid}` and fails immediately on status validation.
- The request reached the service with a populated `uuid` path parameter, but the API still returned `202 Accepted` instead of the expected `200 OK`.

**Impact:** 1 failure

**Confidence:** High

## Update-order response is not parseable, causing downstream UUID loss

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Update ad(Order) for self service (tc_patchRialtoB2A01)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
Failed to parse the JSON document

**Evidence:**
- `tc_patchRialtoB2A01` fails in `user_perfrom_request_with_request_body_and_alterd_IDs_from_recent_created_ad(...)` with `Failed to parse the JSON document`.
- The next scenario, `tc_getRialtoB2A06`, then fails with `Undefined path parameters are: uuid`, which is consistent with the prior update flow not producing/storing the expected UUID.

**Impact:** 2 failures

**Confidence:** High

## Pricing assertion drift

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]

**Evidence:**
- `tc_postRialtoB2A03` completes the POST and status-code checks, then fails only on response-body field validation.
- The actual response values are exactly half the expected values, which points to stale expected data or changed pricing logic rather than transport failure.

**Impact:** 1 failure

**Confidence:** High

---

## Summary

**Root Cause:** Build 378 contains three distinct failure groups: a standalone `202` StoreStatus timing/contract mismatch, a non-JSON update-order response that cascades into a missing-UUID GET failure, and a separate pricing-value assertion drift.

**Affected Components:** Rialto B2A CASS StoreStatus flow, update-order flow, and self-service pricing validation.

**Recommended Fix:**
- Verify whether `storeStatus` is now intentionally asynchronous and update the assertion or polling accordingly.
- Inspect the response returned by `tc_patchRialtoB2A01` and restore a valid JSON payload/UUID handoff before `tc_getRialtoB2A06`.
- Reconcile the expected pricing data for `tc_postRialtoB2A03` with the current backend output.

**Prevention:**
- Add validation around update-flow UUID capture so downstream scenarios fail with the primary cause instead of a secondary missing-parameter error.
