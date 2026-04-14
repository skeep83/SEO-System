from __future__ import annotations

from pathlib import Path

SCHEMA = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"ServiceHub","url":"https://servicehub.md"}</script>'''


def main() -> None:
    site_dir = Path(__file__).resolve().parents[1] / 'output' / 'site'
    updated = 0
    for file in site_dir.glob('*.html'):
        text = file.read_text()
        if 'application/ld+json' in text:
            continue
        text = text.replace('</head>', SCHEMA + '\n</head>')
        file.write_text(text)
        updated += 1
    print(f'Injected schema into {updated} pages')


if __name__ == '__main__':
    main()
