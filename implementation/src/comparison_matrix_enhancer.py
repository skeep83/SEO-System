from __future__ import annotations

from pathlib import Path

MATRIX = """
## Comparison matrix
- Ease of adoption: Jobber > Housecall Pro > HubSpot > ServiceTitan
- Field-service workflow depth: ServiceTitan > Housecall Pro > Jobber > HubSpot
- Small-team simplicity: Jobber > HubSpot > Housecall Pro > ServiceTitan
- Marketing and pipeline flexibility: HubSpot > ServiceTitan > Housecall Pro > Jobber
"""


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        if '## Comparison matrix' in text:
            continue
        if '## Comparison summary' in text:
            text = text.replace('## Comparison table\n', MATRIX + '\n## Comparison table\n')
            file.write_text(text)
            updated += 1
    print(f'Added comparison matrices to {updated} files')


if __name__ == '__main__':
    main()
