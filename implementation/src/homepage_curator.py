from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / 'output' / 'homepage_sections.json'

DATA = {
    'featured_money_pages': [
        {'slug': 'best-crm-for-small-service-business', 'label': 'Best CRM for Small Service Business'},
        {'slug': 'housecall-pro-vs-jobber', 'label': 'Housecall Pro vs Jobber'},
        {'slug': 'jobber-alternatives', 'label': 'Jobber Alternatives'},
        {'slug': 'jobber-pricing-review', 'label': 'Jobber Pricing Review'},
    ],
    'trust_pages': [
        {'slug': 'about-servicehub', 'label': 'About ServiceHub'},
        {'slug': 'editorial-policy', 'label': 'Editorial Policy'},
        {'slug': 'contact', 'label': 'Contact'},
    ],
    'clusters': [
        {'name': 'Field Service CRM', 'items': ['crm-for-plumbers', 'crm-for-electricians', 'best-crm-for-hvac-companies']},
        {'name': 'Comparisons and Alternatives', 'items': ['housecall-pro-vs-jobber', 'jobber-alternatives', 'service-titan-alternatives-for-small-businesses']},
    ]
}


def main() -> None:
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=2))
    print(f'Built homepage curation data at {OUT}')


if __name__ == '__main__':
    main()
