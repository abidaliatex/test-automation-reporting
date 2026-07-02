# test-automation-reporting

A centralised repository for tracking, analysing, and reporting on automated test and build failures.

## Purpose

This repository serves as a single source of truth for:

- **Build failure reports** — structured records of CI/CD pipeline failures generated automatically after each broken build.
- **Root cause investigations** — Copilot-assisted analyses that identify the underlying cause of failures and suggest remediation steps.
- **Weekly dashboards** — trend summaries that surface recurring failure patterns over time.

## Repository Structure

```
test-automation-reporting/
│
├── README.md                          ← overview of the repo purpose
├── AGENTS.md                          ← instructions for Copilot
├── .github/
│     └── copilot-instructions.md     ← Copilot behaviour instructions
│
├── reports/
│     └── build-failures/
│           ├── build-250.md          ← auto-generated failure report
│           └── build-251.md
│
├── investigations/
│     └── copilot-findings/
│           └── build-250-analysis.md ← Copilot root cause analysis
│
└── dashboards/
      └── weekly-summary.md           ← weekly test failure trends
```

## Workflow

1. A CI build fails → a new `reports/build-failures/build-<id>.md` file is created automatically.
2. Copilot analyses the failure report and writes its findings to `investigations/copilot-findings/build-<id>-analysis.md`.
3. A weekly job aggregates the week's failures into `dashboards/weekly-summary.md`.

## Contributing

- Follow the conventions in [AGENTS.md](AGENTS.md) when writing or reviewing reports.
- Do not edit auto-generated files manually; rerun the generation pipeline instead.
