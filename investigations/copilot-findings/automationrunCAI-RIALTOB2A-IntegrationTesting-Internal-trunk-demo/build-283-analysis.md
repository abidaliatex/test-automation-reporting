# Root Cause Analysis — Build #283

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Build:** [#283](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-283.md)  
**Date:** 2026-07-10  
**Status:** UNSTABLE — 3 failed / 14 total

---

## Summary

Build #283 is the third consecutive UNSTABLE run for this job (preceded by #271, #270, #269). All 3 failures occur within the single feature `rialtoB2A (CASS TC4 Change Placement)` and are identical in nature to the failures first seen in build #246 (`failedSince: 246`). The root causes fall into two groups: (1) the B2A integration not propagating `discountType` or correctly computing pricing when an order arrives in MediaHouse; and (2) the Rialto order not reflecting the updated state (status flags, commission, depth) after a MediaHouse placement change.

---

## Root Cause

### RC-1 — discountType and pricing not propagated correctly to MH order basket

**Affected tests:** `tc_getMHTC03`, `tc_getMHTC03a`

- On initial order arrival in MH (`tc_getMHTC03`): `orders[0].printDetails.discountType` is `null` instead of `RIALTO`. The B2A message possibly does not include the `discountType` field, or the MH adapter ignores/drops it.
- On post-change verification (`tc_getMHTC03a`): `discountType` is still `RIALTO` instead of `NONE`, and commission/sum/VAT totals do not match, suggesting the placement-change event is not updating pricing or discount state in MH.
- Both tests have been failing since build #246, indicating a persistent regression rather than a fluke.

### RC-2 — Rialto order state not updated after MH placement change

**Affected tests:** `tc_getIntegrationRialto05b`

- After the MH PATCH (`tc_patchIntegrationMH03`), the Rialto order retrieved by PRISA ID still shows `statusFlags: []` instead of `[PRELIMINARY]`, `commissionAmount: 620.0` instead of `7750.00`, and `depth: 372` instead of `184`.
- The pricing fields show near-correct gross values with decimal precision mismatches (`250000.0` vs `250000.00`) alongside significant commission differences (`620.0` vs `7750.00`), pointing to a commission-rate configuration issue rather than a full data-loss scenario.
- This test has also been failing since build #246.

---

## Affected Components

- **B2A integration layer** — responsible for translating Rialto orders into MH basket format; may not be mapping `discountType` or recomputing pricing on placement-change events.
- **MH order basket API** (`getMHB2A.csv`, endpoint used by `tc_getMHTC03` / `tc_getMHTC03a`) — returns stale or incorrectly computed discount and pricing fields.
- **Rialto order API** (`getRialtoB2A.csv`, endpoint used by `tc_getIntegrationRialto05b`) — order status and commission are not reflecting MH placement change.

---

## Recommended Fix

- Investigate the B2A event handler for placement-change events: verify `discountType` is included in the outbound message and that the MH adapter persists it.
- Check the commission-rate lookup used when a placement changes: `620.0` vs `7750.00` suggests the rate applied is `~0.248%` instead of the expected `~3.1%`.
- Review `statusFlags` update logic in Rialto: the order should transition to `PRELIMINARY` after a confirmed MH placement change.

---

## Prevention

- Add contract tests covering `discountType` propagation and pricing recalculation on placement-change events in the B2A integration layer.
- Monitor `failedSince` age on these test cases — failures dating back to build #246 indicate the regression has been open for 37+ builds without resolution.
