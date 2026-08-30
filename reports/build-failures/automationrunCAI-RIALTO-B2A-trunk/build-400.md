# Build Failure Report

**Build ID:** 400
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-30 21:02:15 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/400/

## Test Summary

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 13 |
| Failed | 4 |
| Skipped | 0 |
| Pass Rate | 76.5% |

## Failing Tests / Steps

### rialtoB2A(CASS) — User perform CASS POST API - #1.1 (occurrence 1)
- **Error:** `expected [N200] but found [N202]`
- **Step:** `User verify the status code "Response Code"`
- **Class:** `stepDefinition.ApiStepDefinition.user_verify_the_status_code` (line 237)

### rialtoB2A(CASS) — User perform CASS POST API - #1.1 (occurrence 2)
- **Error:** `Failed to parse the JSON document` — `The JSON input text should neither be null nor empty.`
- **Class:** `stepDefinition.ApiStepDefinition.user_perfrom_request_with_request_body_and_alterd_IDs_from_recent_created_ad`

### rialtoB2A(CASS) — User perform CASS POST API - #1.1 (occurrence 3)
- **Error:** `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

### rialtoB2A(CASS) — User perform CASS POST API - #1.1 (occurrence 4)
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Class:** `stepDefinition.ApiStepDefinition.user_verify_the_response_body_fields`
