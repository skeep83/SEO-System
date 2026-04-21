from __future__ import annotations

import json
import re
from pathlib import Path


def detect_meta(text: str) -> tuple[str, str]:
    page_type = re.search(r'page_type: "([^"]+)"', text)
    subtype = re.search(r'page_subtype: "([^"]+)"', text)
    return (page_type.group(1) if page_type else 'general', subtype.group(1) if subtype else 'general')


def product_order(page_type: str, subtype: str) -> list[str]:
    if page_type == 'best_of' and subtype == 'fsm':
        return ['Jobber', 'Housecall Pro', 'ServiceTitan', 'HubSpot']
    if page_type == 'best_of' and subtype == 'invoicing':
        return ['Jobber', 'Housecall Pro', 'HubSpot', 'ServiceTitan']
    if page_type == 'comparison' and subtype == 'crm_vs_fsm':
        return ['Jobber', 'HubSpot', 'Housecall Pro', 'ServiceTitan']
    if page_type == 'comparison' and subtype == 'simple_vs_complex':
        return ['Jobber', 'ServiceTitan', 'Housecall Pro', 'HubSpot']
    if page_type == 'alternatives' and subtype == 'workflow_pain':
        return ['Housecall Pro', 'Jobber', 'ServiceTitan', 'HubSpot']
    return ['Jobber', 'Housecall Pro', 'ServiceTitan', 'HubSpot']


def cta_overrides(page_type: str, subtype: str) -> dict[str, str]:
    if page_type == 'best_of' and subtype == 'fsm':
        return {
            'Jobber': 'Try Jobber if you want the clearest all-round FSM fit for a small team',
            'Housecall Pro': 'Try Housecall Pro if dispatch coordination, payments, and communication matter more',
            'ServiceTitan': 'Request a ServiceTitan demo only if your operation is already too complex for lighter tools',
            'HubSpot': 'Try HubSpot only if sales pipeline and marketing matter more than field workflow',
        }
    if page_type == 'best_of' and subtype == 'invoicing':
        return {
            'Jobber': 'Try Jobber if you want invoicing tied directly to jobs, estimates, and customer records',
            'Housecall Pro': 'Try Housecall Pro if payments and field workflow need to stay tightly connected',
            'ServiceTitan': 'Request a ServiceTitan demo only if your service operation is already much more complex',
            'HubSpot': 'Try HubSpot only if revenue pipeline matters more than invoicing workflow itself',
        }
    if page_type == 'comparison' and subtype == 'crm_vs_fsm':
        return {
            'Jobber': 'Try Jobber if field execution is the real bottleneck in the business',
            'HubSpot': 'Try HubSpot if lead management and marketing automation matter more than technician workflow',
            'Housecall Pro': 'Try Housecall Pro if you want another field-service-first option with stronger communication flow',
            'ServiceTitan': 'Request a ServiceTitan demo only if you already know lighter field tools are not enough',
        }
    if page_type == 'comparison' and subtype == 'simple_vs_complex':
        return {
            'Jobber': 'Try Jobber if faster adoption and easier day-to-day execution matter most',
            'ServiceTitan': 'Request a ServiceTitan demo only if your workflow depth clearly justifies the extra complexity',
            'Housecall Pro': 'Try Housecall Pro if you want a middle-ground option with stronger communication and dispatch',
            'HubSpot': 'Try HubSpot only if your real issue is CRM and pipeline management, not field operations',
        }
    if page_type == 'alternatives' and subtype == 'workflow_pain':
        return {
            'Housecall Pro': 'Try Housecall Pro if you want a stronger workflow alternative with better communication and dispatch flow',
            'Jobber': 'Stay with or retry Jobber only if the workflow still mostly fits and the pain is minor',
            'ServiceTitan': 'Request a ServiceTitan demo only if the pain comes from outgrowing simpler tools entirely',
            'HubSpot': 'Try HubSpot only if the real mismatch is around CRM and automation rather than service workflow',
        }
    return {}


def build_block(by_product: dict, page_type: str, subtype: str) -> str:
    lines = ['## Offers', '']
    overrides = cta_overrides(page_type, subtype)
    for product in product_order(page_type, subtype):
        item = by_product[product]
        cta = overrides.get(product, item['cta'])
        lines.append(f'- [{cta}]({item["placeholder_url"]})')
    lines.append('')
    return '\n'.join(lines)


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    links = json.loads((base / 'data' / 'affiliate_placeholders.json').read_text())
    by_product = {item['product']: item for item in links}
    content_dir = base / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        page_type, subtype = detect_meta(text)
        block = build_block(by_product, page_type, subtype)
        if '## Offers' in text:
            text = re.sub(r'## Offers\n(?:.*\n)*?(?=\n## |\Z)', block + '\n', text, flags=re.MULTILINE)
        else:
            text += '\n' + block
        file.write_text(text)
        updated += 1
    print(f'Injected or refreshed offers in {updated} files')


if __name__ == '__main__':
    main()
