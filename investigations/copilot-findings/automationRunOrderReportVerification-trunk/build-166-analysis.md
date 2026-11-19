## Summary

Build 166 finished UNSTABLE: 102/108 tests passed and 6 failed (94.44%). The failures fall into three observed patterns, detailed in the [build report](../../../reports/build-failures/automationRunOrderReportVerification-trunk/build-166.md).

## Root Cause

- Three `createorder.feature` checks reported expected order-data values different from displayed values.
- One `stockOfOrdersCorrCode.feature` check timed out waiting for the Net header.
- Two `printstockoforders.feature` checks found order numbers where the filtered result was expected to be empty.
- Jenkins evidence establishes the failed assertions and timeout, but not their underlying causes.
- Jenkins provides failing step names and feature locations, not scenario titles or TC identifiers.

## Affected Components

- Order report data verification: `User verify generated report data "Order Data"` (`createorder.feature:2537`)
- Stock-of-orders Net header verification: `User verify generated report data "Order Data"` (`stockOfOrdersCorrCode.feature:24`)
- Filtered order-number verification: `User verify filtered order no "OnlyOrder"` (`printstockoforders.feature:51`)

## Recommended Fix

Compare the displayed report values and filter results with their expected test data, and verify why the Net header was not visible before changing test expectations.

## Prevention

Retain focused checks for report values, the Net header, and filtered-order results; confirm expected and displayed data when these checks fail.
