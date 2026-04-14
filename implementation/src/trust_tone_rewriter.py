from __future__ import annotations

from pathlib import Path

REPLACEMENTS = {
    'about-servicehub.md': {
        'ServiceHub publishes practical software buying guides for small service businesses. The goal is simple: help owners and operators make better software decisions without wasting time on generic comparison lists.': 'ServiceHub is a focused software-buying publication for small service businesses. It exists to help owners evaluate CRM, dispatch, quoting, invoicing, and workflow tools with more practical judgment and less generic listicle noise.',
        'Recommendations are based on workflow fit, operational usefulness, and likely suitability for small service teams.': 'Recommendations should be based on workflow fit, operational usefulness, and likely suitability for smaller service teams rather than hype, vendor branding, or enterprise feature bloat.',
    },
    'contact.md': {
        'If you want help narrowing down software options for your service business, contact ServiceHub through the contact path that will be added here.': 'If you need help narrowing down software options for your service business, use this page as the current contact and assistance route. The long-term goal is to offer clearer shortlist guidance for buyers comparing practical options.',
    },
    'editorial-policy.md': {
        'ServiceHub aims to publish practical, commercially aware, but useful software comparisons.': 'ServiceHub aims to publish commercially aware but genuinely useful software comparisons for small service businesses.',
    },
}


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for filename, replacements in REPLACEMENTS.items():
        path = content_dir / filename
        if not path.exists():
            continue
        text = path.read_text()
        before = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != before:
            path.write_text(text)
            updated += 1
    print(f'Rewrote trust tone on {updated} pages')


if __name__ == '__main__':
    main()
