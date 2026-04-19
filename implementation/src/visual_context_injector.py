from __future__ import annotations

from pathlib import Path

TARGETS = {
    'best-crm-for-small-service-business.html': ('assets/visuals/best-crm-for-small-service-business.svg', 'CRM buyer dashboard illustration'),
    'housecall-pro-vs-jobber.html': ('assets/visuals/housecall-pro-vs-jobber.svg', 'Software comparison illustration'),
    'jobber-alternatives.html': ('assets/visuals/jobber-alternatives.svg', 'Alternatives comparison illustration'),
    'service-titan-alternatives-for-small-businesses.html': ('assets/visuals/service-titan-alternatives-for-small-businesses.svg', 'ServiceTitan alternatives illustration'),
}


def main() -> None:
    site_dir = Path(__file__).resolve().parents[1] / 'output' / 'site'
    updated = 0
    for filename, (src, alt) in TARGETS.items():
        path = site_dir / filename
        if not path.exists():
            continue
        text = path.read_text()
        if 'hero-visual' in text:
            continue
        block = f'''<div class="hero-visual panel panel-soft"><img src="{src}" alt="{alt}" style="width:100%;height:auto;border-radius:20px;display:block"></div>'''
        text = text.replace('</aside>\n    </section>', '</aside>\n      ' + block + '\n    </section>', 1)
        text = text.replace('.hero-shell {\n      display:grid; grid-template-columns: 1.5fr .9fr; gap: 22px; margin-bottom: 26px;\n    }', '.hero-shell {\n      display:grid; grid-template-columns: 1.2fr .8fr; gap: 22px; margin-bottom: 26px;\n    }')
        path.write_text(text)
        updated += 1
    print(f'Injected contextual visuals into {updated} pages')


if __name__ == '__main__':
    main()
