from __future__ import annotations

from pathlib import Path

BLOCK = """
## Comparison summary
- Best if you need dispatch and scheduling first: field-service-first tools like Jobber or Housecall Pro.
- Best if you need broader CRM and marketing flexibility: HubSpot.
- Best if you run a larger operation with heavier process complexity: ServiceTitan.
"""


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        if '## Comparison summary' in text:
            continue
        if '## Comparison table' in text:
            text = text.replace('## Comparison table\n', BLOCK + '\n## Comparison table\n')
            file.write_text(text)
            updated += 1
    print(f'Added comparison summaries to {updated} files')


if __name__ == '__main__':
    main()
