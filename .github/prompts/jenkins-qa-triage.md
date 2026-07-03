Analyze the latest Jenkins build and provide a concise QA triage report.

Rules:
- Keep the report under 2 pages.
- Focus on investigation, not documentation.
- Group failures by likely root cause.
- Show only the most important evidence.
- Do NOT generate long recommendations, ownership analysis, code guesses, or executive summaries.
- Affected Scenarios: write all affected scenarios with the test case names.

Output format:

---

## Build Summary

Build:
Total Tests:
Passed:
Failed:
Pass Rate:

---

## Root Cause Groups

For each root cause, show:

### <Root Cause Name>

**Affected Features:**
- Feature1.feature
- Feature2.feature

**Affected Scenarios:**
- Scenario Name (TC01)
- Scenario Name (TC05)

**Failure Pattern:**
discountType expected [RIALTO] found [null]

**Evidence:**
- Example 1
- Example 2

**Impact:** 15 failures

**Confidence:** High / Medium / Low
