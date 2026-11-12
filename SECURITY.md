# Security Policy

## Supported Versions

This repository contains pricing data only — no executable code that processes user input.
Security vulnerabilities are not applicable to JSON data files.

## Reporting Concerns

If you find incorrect pricing data that could mislead users:
1. Open an issue with the label `data-correction`
2. Include the model, current value, correct value, and source URL

If you believe the GitHub Actions workflow has a security issue, email
**security@tolvyn.io** and do not open a public issue. The full policy is in
[tolvyn/.github](https://github.com/tolvyn/.github/blob/main/SECURITY.md).

Researchers who have reported security issues are credited on the security page:
https://tolvyn.io/pages/security#acknowledgments

## Data Integrity

All pricing data is:
- Cross-referenced against official provider documentation
- Reviewed by the TOLVYN team before merging
- Timestamped with source URLs for verification
- Auto-synced daily from TOLVYN's verified pricing database
