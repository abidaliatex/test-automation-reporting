# Build 161 — Investigation Analysis

**Source report:** [build-161.md](../../../reports/build-failures/automationRunMiscellaneousCases-trunk/build-161.md)

## Summary

- Build 161 was **UNSTABLE**: 106 of 108 tests passed (98.1%).
- Both failures were in `subscriptionorder.feature`.

## Root Cause

- The EAN verification timed out waiting for its expected element to appear.
- The order confirmation step timed out waiting for the OK button to become clickable.
- Jenkins provides the failing waits and page-object methods, but does not establish why either element was unavailable.

## Affected Components

- `subscriptionorder.feature` — `User creating a subscription order` (feature lines 349 and 475; test case IDs were not exposed).
- `SubscriptionOrderPage.verifyEANNumber` and `SubscriptionOrderPage.clickOk`.

## Recommended Fix

- Check the order-page state and element readiness at each failing step before changing locators or wait behavior.

## Prevention

- Keep the order flow's test data and UI state deterministic, and assert readiness before interacting with the EAN and OK button.
