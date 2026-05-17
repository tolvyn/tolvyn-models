#!/usr/bin/env python3
"""Update individual model JSON files from TOLVYN API response."""
import json, sys, os
from datetime import datetime, timezone

def main():
    with open(sys.argv[1]) as f:
        data = json.load(f)

    models = data.get('data', data.get('models', []))
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

    for model in models:
        provider = model['provider']
        model_id = model['model_id']

        out = {
            'model_id': model_id,
            'provider': provider,
            'display_name': model.get('display_name', model_id),
            'model_family': model.get('model_family'),
            'modality': model.get('modality', 'text'),
            'context_window': model.get('context_window'),
            'pricing': {
                'input_per_mtok': float(model.get('pricing_input_per_mtok') or 0),
                'output_per_mtok': float(model.get('pricing_output_per_mtok') or 0),
                'cached_per_mtok': float(model.get('pricing_cached_per_mtok') or 0),
                'currency': 'USD',
                'unit': 'per_million_tokens'
            },
            'pricing_updated_at': today,
            'pricing_source': model.get('pricing_source', ''),
            'deprecated': model.get('deprecated_at') is not None,
            'tolvyn_verified': True,
            'last_synced': now
        }

        path = f'models/{provider}/{model_id}.json'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(out, f, indent=2)
            f.write('\n')
        print(f'Updated {path}')

if __name__ == '__main__':
    main()
