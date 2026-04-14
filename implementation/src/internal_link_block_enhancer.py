from __future__ import annotations

from pathlib import Path

BLOCK = """
## Related guides
- [Compare Jobber and Housecall Pro](housecall-pro-vs-jobber.html)
- [See Jobber alternatives](jobber-alternatives.html)
- [Understand CRM for plumbers](crm-for-plumbers.html)
- [Understand CRM for electricians](crm-for-electricians.html)
"""


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        if '## Related guides' in text:
            continue
        text += '\n' + BLOCK
        file.write_text(text)
        updated += 1
    print(f'Added internal link blocks to {updated} files')


if __name__ == '__main__':
    main()
