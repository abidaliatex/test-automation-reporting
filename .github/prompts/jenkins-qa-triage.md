# Jenkins QA Triage Prompt

Use this prompt with the Jenkins AI pipeline step (or any LLM integration) to generate a concise root cause analysis from a build's test output.

---

## Prompt

```
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
- Scenario Name (TC14)

**Failure Pattern:**
discountType expected [RIALTO] found [null]

**Evidence:**
- Example 1
- Example 2

**Impact:** 15 failures

**Confidence:** High / Medium / Low
```

---

## Usage in Jenkins Pipeline

Reference this prompt file in your `Jenkinsfile` AI step. Pass it together with the build log or test report XML/JSON as context:

```groovy
stage('QA Triage') {
    steps {
        script {
            def triagePrompt = readFile('prompts/jenkins-qa-triage.md')
            // Pass triagePrompt + currentBuild test output to your AI provider step
        }
    }
}
```

## Notes

- The prompt is intentionally strict to avoid bloated output — do not relax the "under 2 pages" rule.
- `Confidence` should reflect how clearly the evidence ties all grouped failures to a single root cause.
- If a failure does not fit any group, list it under a catch-all **Unclassified** root cause group.
