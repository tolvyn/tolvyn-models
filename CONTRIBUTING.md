# Contributing to tolvyn-models

## Adding a new model

1. Create `models/{provider}/{model_id}.json` using the schema in README.md
2. Add the model to `index.json`
3. Include `pricing_source` URL (official provider docs only)
4. Open a PR — reviewed within 24 hours

## Correcting pricing

1. Edit the model JSON file
2. Update `pricing_updated_at` to today's date
3. Include the source URL in your PR description
4. Open a PR

## Automated sync

This repo syncs nightly from TOLVYN's verified pricing database.
Manual PRs are also welcome and reviewed by the TOLVYN team.
