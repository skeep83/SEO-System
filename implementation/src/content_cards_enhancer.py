from __future__ import annotations

import re
from pathlib import Path


def detect_meta(text: str) -> tuple[str, str]:
    page_type = re.search(r'page_type: "([^"]+)"', text)
    subtype = re.search(r'page_subtype: "([^"]+)"', text)
    return (page_type.group(1) if page_type else 'general', subtype.group(1) if subtype else 'general')


def quick_verdict(page_type: str, subtype: str) -> str:
    if page_type == 'best_of' and subtype == 'fsm':
        return 'Most small teams should shortlist Jobber first, Housecall Pro second, and treat ServiceTitan as the exception rather than the default.'
    if page_type == 'best_of' and subtype == 'invoicing':
        return 'For most service businesses, invoicing works best when it stays connected to jobs, estimates, and payments instead of living in an isolated tool.'
    if page_type == 'comparison' and subtype == 'crm_vs_fsm':
        return 'The fastest good decision is figuring out whether your bigger problem is field execution or sales pipeline management.'
    if page_type == 'comparison' and subtype == 'simple_vs_complex':
        return 'This decision is usually about whether you need easier adoption now or deeper operational control badly enough to justify more complexity.'
    if page_type == 'alternatives' and subtype == 'workflow_pain':
        return 'The best alternative is the one that fixes the workflow mismatch without creating a worse adoption problem elsewhere.'
    return 'This page should help a buyer narrow the shortlist fast, not just learn vocabulary.'


def decision_shortcuts(page_type: str, subtype: str) -> list[str]:
    if page_type == 'best_of' and subtype == 'fsm':
        return [
            'Choose Jobber if you want the safest all-round fit for a small field team.',
            'Choose Housecall Pro if communication, payments, and dispatch coordination need more weight.',
            'Eliminate ServiceTitan unless workflow depth clearly outweighs complexity cost.',
        ]
    if page_type == 'best_of' and subtype == 'invoicing':
        return [
            'Choose a field-service-first tool if invoices usually come directly from jobs and estimates.',
            'Choose an accounting-led path only if bookkeeping is the bigger bottleneck.',
            'Eliminate heavy platforms unless your billing process is already much more complex.',
        ]
    if page_type == 'comparison' and subtype == 'crm_vs_fsm':
        return [
            'Choose Jobber if technicians, scheduling, and invoicing drive the business.',
            'Choose HubSpot if lead management and marketing automation are the bigger problem.',
            'Do not treat CRM and FSM tools as equal substitutes unless the workflow really overlaps.',
        ]
    if page_type == 'comparison' and subtype == 'simple_vs_complex':
        return [
            'Choose Jobber if you want faster adoption and less operational drag.',
            'Choose ServiceTitan only if your process complexity already justifies it.',
            'Use Housecall Pro as a middle-ground benchmark before going full enterprise.',
        ]
    if page_type == 'alternatives' and subtype == 'workflow_pain':
        return [
            'Switch only if the current workflow mismatch is slowing execution consistently.',
            'Prefer lighter alternatives before jumping to enterprise-level complexity.',
            'Do not switch just to trade one set of annoyances for a worse implementation burden.',
        ]
    return [
        'Choose a field-service-first tool if scheduling and dispatch are central.',
        'Choose a broader CRM if pipeline, automation, and marketing matter more than technician workflows.',
        'Eliminate options that are too complex for your current team size.',
    ]


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        page_type, subtype = detect_meta(text)
        qv = '## Quick verdict\n' + quick_verdict(page_type, subtype) + '\n'
        ds_lines = ['## Decision shortcuts'] + [f'- {line}' for line in decision_shortcuts(page_type, subtype)]
        ds = '\n'.join(ds_lines) + '\n'
        if '## Quick verdict' in text:
            text = re.sub(r'## Quick verdict\n.*?(?=\n## )', qv, text, flags=re.S)
        else:
            text = text.replace('## Call to action\n', qv + '\n## Call to action\n')
        if '## Decision shortcuts' in text:
            text = re.sub(r'## Decision shortcuts\n.*?(?=\n## |\Z)', ds, text, flags=re.S)
        else:
            text += '\n' + ds
        file.write_text(text)
        updated += 1
    print(f'Enhanced decision content in {updated} files')


if __name__ == '__main__':
    main()
