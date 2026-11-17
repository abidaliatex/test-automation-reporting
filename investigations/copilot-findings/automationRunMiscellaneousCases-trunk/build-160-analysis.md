## Summary

Build 160 of `automationRunMiscellaneousCases-trunk` was **UNSTABLE**: 106 of 108 tests passed (98.15%), with two failures. See the [build report](../../../reports/build-failures/automationRunMiscellaneousCases-trunk/build-160.md).

## Root Cause

- The subscription-order EAN lookup timed out waiting for the expected value to appear.
- The subscription-order confirmation step timed out waiting for its button to become clickable. The console also reports a `No Discount` / `No discount` text mismatch in that scenario.
- Available logs confirm the symptoms but do not establish their underlying causes.

## Affected Components

- `subscriptionorder.feature`: “User creating a subscription order,” Jenkins cases 33 and 41. The Jenkins report does not include `TCxx` identifiers.

## Recommended Fix

- Verify the EAN test data and rendered result for the first failure.
- Inspect the confirmation button state and validate the expected discount label casing for the second.

## Prevention

- Capture the page state when these waits time out and keep the subscription-order test data and expected UI labels aligned.
