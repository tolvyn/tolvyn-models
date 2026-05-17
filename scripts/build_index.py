#!/usr/bin/env python3
"""Build index.json from all model JSON files."""
import json, os, glob
from datetime import datetime, timezone

models = []
for path in sorted(glob.glob('models/**/*.json', recursive=True)):
    with open(path) as f:
        models.append(json.load(f))

index = {
    'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'model_count': len(models),
    'providers': sorted(set(m['provider'] for m in models)),
    'models': models
}

with open('index.json', 'w') as f:
    json.dump(index, f, indent=2)
    f.write('\n')

print(f'Built index.json with {len(models)} models')
