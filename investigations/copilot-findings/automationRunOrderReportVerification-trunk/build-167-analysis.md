## Summary

- Build 167 was **UNSTABLE**: 101 of 108 tests passed; 7 failed (93.52%).
- Jenkins reports four Net-value mismatches, two unexpected filtered order numbers, and one timeout waiting for the Net column header.
- See the [build report](../../../reports/build-failures/automationRunOrderReportVerification-trunk/build-167.md) for the failure evidence and scenario-step names.

## Root Cause

- The order report checks observed incorrect Net values and unexpected order numbers in filtered results. Jenkins establishes these mismatches but not their underlying cause.
- The correction-code report check could not find the Net header within 10 seconds; the logs do not establish why it was unavailable.
- Jenkins does not expose test-case IDs for these failed scenarios.

## Affected Components

- `createorder.feature` — `User verify generated report data "Order Data"` (`:2537`)
- `printstockoforders.feature` — `User verify filtered order no "OnlyOrder"` (`:51`)
- `stockOfOrdersCorrCode.feature` — `User verify generated report data "Order Data"` (`:24`)

## Recommended Fix

- Compare the generated Net values and filtered results with their expected test data.
- Check the report state when the correction-code test waits for the Net header.

## Prevention

- Keep report-value, filtering, and header-visibility checks deterministic, and preserve the expected-versus-actual values in future failure output.
