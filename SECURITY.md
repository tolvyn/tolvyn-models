# Security Policy

## Supported Versions

This repository contains pricing data only — no executable code that processes user input.
Security vulnerabilities are not applicable to JSON data files.

## Reporting Concerns

If you find incorrect pricing data that could mislead users:
1. Open an issue with the label `data-correction`
2. Include the model, current value, correct value, and source URL

If you believe the GitHub Actions workflow has a security issue:
Email: founder@tolvyn.io
Response time: within 48 hours

## Data Integrity

All pricing data is:
- Cross-referenced against official provider documentation
- Reviewed by the TOLVYN team before merging
- Timestamped with source URLs for verification
- Auto-synced daily from TOLVYN's verified pricing database
