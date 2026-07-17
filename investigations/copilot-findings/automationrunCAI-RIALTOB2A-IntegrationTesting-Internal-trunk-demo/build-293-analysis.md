# Build 293 Root Cause Analysis

Source report: [build-293.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-293.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #293 ended `UNSTABLE` with 3 failed tests out of 14.
- All failures are assertion mismatches in the TC4 placement-change flow.
- Failures split into two clusters: MediaHouse discount/financial mismatch and Rialto post-update projection mismatch.

## Root Cause

1. **MediaHouse discount and totals mismatch**
   - `tc_getMHTC03`: `discountType` is `null` instead of `RIALTO`, with inflated VAT/totalInclVat.
   - `tc_getMHTC03a`: after change flow, `discountType` remains `RIALTO` instead of `NONE`, and commission/totals diverge from expected values.

2. **Rialto post-update projection mismatch**
   - `tc_getIntegrationRialto05b`: response shows empty `statusFlags`, incorrect `commissionAmount`, changed `depth`, and precision/value mismatches for pricing fields.

## Affected Components

- Feature: `rialtoB2A(CASS)TestCase4.feature`
- MediaHouse GET validations: `MediaHouse/getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto GET validations: `Rialto/RialtoB2A/getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)

## Recommended Fix

- Validate discount propagation/reset behavior across initial order and placement-change update in the MH projection path.
- Verify placement-change recalculation outputs for `statusFlags`, commission, depth, and totals before final GET assertions.
- Reconcile expected TC4 numeric precision/value baselines with current service responses.

## Prevention

- Add a checkpoint assertion after update processing completion for key fields (`discountType`, `statusFlags`, `commissionAmount`, `totalInclVat`).
- Track TC4 placement-change mismatch signatures as a recurring failure cluster until stabilized.
