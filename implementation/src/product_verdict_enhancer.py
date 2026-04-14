from __future__ import annotations

from pathlib import Path

VERDICT_BLOCK = """
## Verdict snapshot
- Jobber: strongest fit for smaller field-service teams that want simplicity and operational coverage.
- Housecall Pro: strong choice when communication, dispatch coordination, and payments matter more.
- ServiceTitan: heavier platform, usually better only if operations are already more complex.
- HubSpot: better when pipeline management and marketing matter more than technician workflows.
"""


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        if '## Verdict snapshot' in text:
            continue
        if '## Recommended products' in text:
            text = text.replace('## Recommended products\n', VERDICT_BLOCK + '\n## Recommended products\n')
            file.write_text(text)
            updated += 1
    print(f'Added verdict snapshots to {updated} files')


if __name__ == '__main__':
    main()
