from __future__ import annotations

from pathlib import Path

PAGES = {
    'about-servicehub.md': """# About ServiceHub

ServiceHub publishes practical software buying guides for small service businesses. The goal is simple: help owners and operators make better software decisions without wasting time on generic comparison lists.

## What we cover
- CRM tools for small service businesses
- dispatch and scheduling software
- pricing comparisons
- alternatives pages
- implementation-oriented software guidance

## How recommendations work
Recommendations are based on workflow fit, operational usefulness, and likely suitability for small service teams.

## Affiliate disclosure
Some links on this site may be affiliate links. That should not change the recommendation logic.
""",
    'contact.md': """# Contact

If you want help narrowing down software options for your service business, contact ServiceHub through the contact path that will be added here.

## Best fit for outreach
- owners comparing CRM or dispatch tools
- teams deciding between Jobber, Housecall Pro, HubSpot, or similar platforms
- small operators trying to avoid overbuying software
""",
    'editorial-policy.md': """# Editorial Policy

ServiceHub aims to publish practical, commercially aware, but useful software comparisons.

## Editorial standards
- prioritize fit over hype
- avoid generic rankings with no workflow logic
- distinguish small-team needs from enterprise complexity
- improve content over time as better data becomes available
""",
}


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    created = 0
    for filename, content in PAGES.items():
        path = content_dir / filename
        path.write_text(content)
        created += 1
    print(f'Built {created} trust pages')


if __name__ == '__main__':
    main()
