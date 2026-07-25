# Build 308 — Root Cause Analysis

**Source report:** [build-308.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-308.md)

---

## Summary

Build 308 is `UNSTABLE` with 3 failures out of 15 tests (80% pass rate). All 3 failures are in TC29 (Magazine — change to Uppslag/Spread/Panorama) and have been continuously failing since build 298 (`failedSince: 298`). The failures are identical across recent runs, indicating a persistent environment or data state issue rather than a newly introduced regression.

---

## Root Cause

**RC1 — `discountType` not populated in MediaHouse original-state verification**

The `orders.printDetails.discountType` field returns `null` instead of the expected value `RIALTO` when verifying the initial order state in MediaHouse. This suggests the field is not being set during order creation or propagation from Rialto to MediaHouse.

**RC2 — Placement/pricing revert not applied after Uppslag change**

After the MH patch updates two order lines to Uppslag, the subsequent verification steps (both in MH and Rialto) expect the basket to revert to the original HALVLIGG (full-page) state, but the system still returns UPPSLAG placement with spread-level dimensions and pricing. The revert/undo flow does not appear to propagate back through the integration pipeline.

---

## Affected Components

- **MediaHouse** — basket order state verification (`getMHB2A.csv`: `tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b`)
- **Rialto** — order detail verification after state change (`getRialtoB2A.csv`: `tc_getIntegrationRialtoMZN04b`)
- **B2A Integration pipeline** — order propagation and revert flow between Rialto and MediaHouse

---

## Recommended Fix

- Investigate why `discountType` is `null` after Rialto→MediaHouse propagation; verify the field mapping in the B2A integration layer.
- Trace the MH PATCH response through to Rialto to determine why the revert to HALVLIGG is not reflected; check if the reverse-sync trigger is functioning.

---

## Prevention

- Add a dedicated assertion on `discountType` at the point of order creation to catch missing field mapping earlier in the flow.
- Add monitoring/alerting for persistent failures (`failedSince` spanning many builds) to escalate unresolved environment-level issues sooner.
