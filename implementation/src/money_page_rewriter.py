from __future__ import annotations

from pathlib import Path

REWRITES = {
    "best-crm-for-small-service-business.md": {
        "## Overview\nThis page is designed to help small service businesses compare CRM options without wasting time on generic software lists.\n": "## Overview\nSmall service businesses usually do not fail because they lack software options. They fail because they choose tools built for the wrong workflow. The best CRM for this category should reduce admin drag, support quoting and scheduling, and help the team follow jobs from lead to payment.\n",
        "## Final recommendation\nFor most small service businesses, a field-service-first CRM is usually a better starting point than a generic CRM.\n": "## Final recommendation\nFor most small service businesses, Jobber or Housecall Pro will make more sense than a broad CRM because dispatch, estimates, invoicing, and customer follow-up are operational necessities, not optional extras. HubSpot is better when the business cares more about pipeline visibility and marketing automation than technician workflow.\n",
    },
    "housecall-pro-vs-jobber.md": {
        "## Quick verdict\nThis comparison should quickly tell the reader which product fits smaller teams versus more complex service operations.\n": "## Quick verdict\nJobber is usually the safer choice for smaller service teams that want a cleaner learning curve. Housecall Pro becomes more attractive when communication, payments, and dispatch coordination need to feel more connected in one workflow.\n",
    },
    "jobber-alternatives.md": {
        "## Why people look for alternatives\nUsers usually look for alternatives when cost, complexity, or missing workflow features start to slow the team down.\n": "## Why people look for alternatives\nMost buyers look for Jobber alternatives when they hit one of three walls: pricing pressure, missing workflow depth, or a mismatch between the product and the way their crew actually operates day to day.\n",
    },
}


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for filename, replacements in REWRITES.items():
        target = content_dir / filename
        if not target.exists():
            continue
        text = target.read_text()
        before = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != before:
            target.write_text(text)
            updated += 1
    print(f'Rewrote {updated} money pages')


if __name__ == '__main__':
    main()
