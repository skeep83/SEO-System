from __future__ import annotations

from pathlib import Path

REPLACEMENTS = {
    'best-crm-for-small-service-business.md': {
        '## Who this is for\nIt is for owners and operators who need quoting, scheduling, invoicing, customer follow-up, and basic pipeline visibility in one place.\n': '## Who this is for\nThis page is for owners of small service businesses who are tired of juggling estimates, customer follow-up, job scheduling, invoicing, and basic sales tracking across too many disconnected tools. It is especially relevant for teams that do not have time for a long software rollout and need something operationally useful fast.\n',
        '## How to choose\nChoose based on company size, dispatch complexity, budget tolerance, and whether you need a field-service-first tool or a broader CRM.\n': '## How to choose\nStart by deciding whether your real bottleneck is field operations or sales process. If your team lives inside scheduling, dispatch, job history, and invoices, pick the best operational fit first. If your growth bottleneck is pipeline visibility, automation, and follow-up, a broader CRM may matter more. Do not overbuy complexity if your team is still small.\n',
    },
    'housecall-pro-vs-jobber.md': {
        '## Comparison table\nA comparison table should highlight best fit, strengths, weaknesses, and pricing posture for each tool.\n': '## Comparison table\nThe practical comparison comes down to simplicity versus workflow depth. Jobber is usually easier to roll out and feels cleaner for smaller teams. Housecall Pro becomes more compelling when you need stronger communication loops, payments, and tighter job coordination.\n',
    },
    'jobber-alternatives.md': {
        '## Best alternatives\nAlternatives should be grouped by best fit, budget sensitivity, and operational complexity.\n': '## Best alternatives\nThe strongest alternatives to Jobber depend on what you are trying to fix. If you want a more connected communication and payments workflow, Housecall Pro is the obvious alternative. If you need heavier operational control, ServiceTitan enters the conversation. If you care more about CRM and marketing than field workflow, HubSpot becomes more relevant.\n',
    },
    'jobber-pricing-review.md': {
        '## Overview\nThis page is designed to help small service businesses compare CRM options without wasting time on generic software lists.\n': '## Overview\nJobber pricing only makes sense in context. A tool can look expensive on paper but still be worth it if it removes enough admin drag from quoting, scheduling, invoicing, and customer follow-up. This page should help buyers judge whether Jobber is expensive or simply aligned with the way a small field-service team actually works.\n',
    },
    'housecall-pro-review-for-small-business.md': {
        '## Overview\nThis page is designed to help small service businesses compare CRM options without wasting time on generic software lists.\n': '## Overview\nHousecall Pro can be a strong fit for small service businesses, but only if the business actually benefits from its communication, dispatch, and payments workflow. This page should help a buyer decide whether Housecall Pro is a practical upgrade or unnecessary complexity.\n',
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
    print(f'Manually upgraded {updated} priority pages')


if __name__ == '__main__':
    main()
