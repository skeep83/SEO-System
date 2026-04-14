from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    verdicts = json.loads((base / 'data' / 'product_verdicts.json').read_text())
    by_name = {item['name']: item for item in verdicts}
    content_dir = base / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        if '## Product records' in text:
            continue
        lines = ['## Product records', '']
        for name in ['Jobber', 'Housecall Pro', 'ServiceTitan', 'HubSpot']:
            item = by_name[name]
            lines.append(f"### {name} record")
            lines.append(f"- Best fit: {item['best_fit']}")
            lines.append(f"- Adoption score: {item['adoption_score']}/10")
            lines.append(f"- Workflow depth score: {item['workflow_depth_score']}/10")
            lines.append(f"- Marketing score: {item['marketing_score']}/10")
            lines.append(f"- Complexity: {item['complexity']}")
            lines.append(f"- Verdict: {item['verdict']}")
            lines.append('')
        text = text.replace('## Recommended products\n', '\n'.join(lines) + '\n## Recommended products\n')
        file.write_text(text)
        updated += 1
    print(f'Added structured product records to {updated} files')


if __name__ == '__main__':
    main()
