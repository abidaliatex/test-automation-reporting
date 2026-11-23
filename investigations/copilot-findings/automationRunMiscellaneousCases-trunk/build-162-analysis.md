# Build 162 — Investigation Analysis

**Source report:** [build-162.md](../../../reports/build-failures/automationRunMiscellaneousCases-trunk/build-162.md)

## Summary

- Build 162 was **UNSTABLE**: 106 of 108 tests passed (98.1%).
- Two Selenium waits failed in `subscriptionorder.feature`.

## Root Cause

- **EAN visibility:** The expected EAN `5798007304591` was not visible within 10 seconds.
- **Confirmation button:** The Subscription Order OK button was not clickable within 10 seconds.
- Jenkins confirms the unavailable UI elements but not their underlying application or data cause.

## Affected Components

- `subscriptionorder.feature`
- Scenario: `User creating a subscription order` (TC unavailable)
- `SubscriptionOrderPage.verifyEANNumber`
- `SubscriptionOrderPage.clickOk`

## Recommended Fix

- Verify the order state and page readiness before the EAN visibility check.
- Verify the confirmation dialog state before the OK button interaction.

## Prevention

- Use deterministic order test data and UI readiness checks in the subscription order flow.
