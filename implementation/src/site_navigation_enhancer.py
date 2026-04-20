from __future__ import annotations

from pathlib import Path

BLOCK = """
## Site navigation
- [Home](/)
- [About ServiceHub](/about-servicehub)
- [Editorial Policy](/editorial-policy)
- [Contact](/contact)
"""


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        if '## Site navigation' in text:
            continue
        text += '\n' + BLOCK
        file.write_text(text)
        updated += 1
    print(f'Added site navigation blocks to {updated} files')


if __name__ == '__main__':
    main()
