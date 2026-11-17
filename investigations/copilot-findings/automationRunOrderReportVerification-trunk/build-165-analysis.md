# Investigation Analysis — Build 165

**Source Report:** [build-165.md](../../../reports/build-failures/automationRunOrderReportVerification-trunk/build-165.md)

## Summary

Build 165 was UNSTABLE: 8 of 108 tests failed (92.6% passed). Failures concern order-report values, order-number filtering, and visibility of the Net column.

## Root Cause

- Five order-report assertions returned values different from expected data.
- Two order-number filter checks returned order rows when none were expected.
- One test timed out waiting for the Net column header.

Jenkins identifies these failure patterns but does not provide scenario titles or TC identifiers, nor does the available evidence establish whether the causes are application behavior, test data, or test expectations.

## Affected Components

- `createorder.feature`
- `printstockoforders.feature`
- `stockOfOrdersCorrCode.feature`

## Recommended Fix

- Compare the reported values and filtered rows against the expected test data and build environment.
- Check why the Net column was unavailable to the test.

## Prevention

- Preserve scenario titles and TC identifiers in Jenkins test results to make future failures traceable.
