# TOLVYN Models

Open-source AI model pricing database. Apache 2.0.

Maintained by [TOLVYN](https://tolvyn.io) — the financial control plane for AI infrastructure.

## What this is

A community-maintained, automatically-verified pricing database for AI models.
Every entry is cross-referenced against provider pricing pages daily.

## Why open source?

AI pricing changes frequently. Wrong pricing data costs companies money.
We open-source our pricing database so the whole community benefits.

## Structure

```
models/{provider}/{model_id}.json — one file per model
index.json                        — all models in one file for easy consumption
```

## Usage

### Install via npm (coming soon)
```bash
npm install @tolvyn/models
```

### Direct JSON
```bash
curl https://raw.githubusercontent.com/tolvyn/tolvyn-models/main/index.json
```

### In your code
```js
const models = await fetch('https://raw.githubusercontent.com/tolvyn/tolvyn-models/main/index.json').then(r => r.json())
const gpt4o = models.models.find(m => m.model_id === 'gpt-4o')
console.log(gpt4o.pricing.input_per_mtok) // 2.50
```

## Model JSON schema

```json
{
  "model_id": "gpt-4o",
  "provider": "openai",
  "display_name": "GPT-4o",
  "model_family": "gpt-4o",
  "modality": "text",
  "context_window": 128000,
  "pricing": {
    "input_per_mtok": 2.50,
    "output_per_mtok": 10.00,
    "cached_per_mtok": 1.25,
    "currency": "USD",
    "unit": "per_million_tokens"
  },
  "pricing_updated_at": "2026-05-15",
  "pricing_source": "https://openai.com/api/pricing",
  "deprecated": false,
  "tolvyn_verified": true,
  "last_synced": "2026-05-15T03:00:00Z"
}
```

## Current models (18)

| Provider   | Model                | Input $/MTok | Output $/MTok | Context    |
|------------|----------------------|-------------:|--------------:|------------|
| OpenAI     | gpt-4o               | 2.50         | 10.00         | 128k       |
| OpenAI     | gpt-4o-mini          | 0.15         | 0.60          | 128k       |
| OpenAI     | o1                   | 15.00        | 60.00         | 200k       |
| OpenAI     | o1-mini              | 3.00         | 12.00         | 128k       |
| OpenAI     | o3                   | 10.00        | 40.00         | 200k       |
| OpenAI     | o3-mini              | 1.10         | 4.40          | 200k       |
| OpenAI     | gpt-4-turbo          | 10.00        | 30.00         | 128k       |
| OpenAI     | gpt-3.5-turbo        | 0.50         | 1.50          | 16k        |
| Anthropic  | claude-opus-4-6      | 5.00         | 25.00         | 200k       |
| Anthropic  | claude-sonnet-4-6    | 3.00         | 15.00         | 200k       |
| Anthropic  | claude-haiku-4-5     | 0.80         | 4.00          | 200k       |
| Anthropic  | claude-3-5-sonnet    | 3.00         | 15.00         | 200k       |
| Anthropic  | claude-3-opus        | 15.00        | 75.00         | 200k       |
| Google     | gemini-2.5-pro       | 1.25         | 10.00         | 1M         |
| Google     | gemini-2.5-flash     | 0.15         | 0.60          | 1M         |
| Google     | gemini-2.0-flash     | 0.10         | 0.40          | 1M         |
| Google     | gemini-1.5-pro       | 1.25         | 5.00          | 2M         |
| Google     | gemini-1.5-flash     | 0.075        | 0.30          | 1M         |

## Data accuracy

- Prices are verified against official provider documentation daily
- Changes are reviewed by the TOLVYN team before merging
- Pricing source URL included for every model
- Last sync timestamp on every record

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome for new models or pricing corrections.
All corrections reviewed within 24 hours.

## License

Apache 2.0 — free to use commercially. Attribution appreciated but not required.

---

Built with ❤️ by [TOLVYN](https://tolvyn.io)
