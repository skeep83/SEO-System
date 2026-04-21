from __future__ import annotations

import re
from pathlib import Path

DEFAULT_BLOCK = """
## Comparison summary
- Best if you need dispatch and scheduling first: field-service-first tools like Jobber or Housecall Pro.
- Best if you need broader CRM and marketing flexibility: HubSpot.
- Best if you run a larger operation with heavier process complexity: ServiceTitan.
"""

FSM_BLOCK = """
## Comparison summary
- Best if you want the safest all-round field-service fit: Jobber.
- Best if communication, payments, and dispatch coordination matter more: Housecall Pro.
- Best only if your operation is already much more complex: ServiceTitan.
- Best only if field workflow is not the main issue: HubSpot.
"""

INVOICING_BLOCK = """
## Comparison summary
- Best if invoices need to stay connected to estimates and jobs: Jobber.
- Best if payments and customer communication need a tighter workflow: Housecall Pro.
- Best only if invoicing complexity comes from a much larger operation: ServiceTitan.
- Best only if sales pipeline matters more than invoicing execution: HubSpot.
"""

CRM_VS_FSM_BLOCK = """
## Comparison summary
- Best if field execution is the bottleneck: Jobber.
- Best if sales pipeline and automation are the bottleneck: HubSpot.
- Best if you want another field-service-first benchmark: Housecall Pro.
- Best only if the business is already much more operationally complex: ServiceTitan.
"""

SIMPLE_VS_COMPLEX_BLOCK = """
## Comparison summary
- Best if you want faster adoption and cleaner day-to-day execution: Jobber.
- Best only if deeper workflow control clearly outweighs complexity cost: ServiceTitan.
- Best if you want a middle-ground benchmark with stronger communication and dispatch: Housecall Pro.
- Best only if the real problem is CRM and marketing, not field operations: HubSpot.
"""

WORKFLOW_PAIN_BLOCK = """
## Comparison summary
- Best if you want a stronger workflow alternative without jumping to enterprise software: Housecall Pro.
- Best if the current workflow still mostly fits and the pain is limited: Jobber.
- Best only if the pain comes from outgrowing simpler tools entirely: ServiceTitan.
- Best only if the real mismatch is around CRM and automation: HubSpot.
"""


def detect_meta(text: str) -> tuple[str, str]:
    page_type = re.search(r'page_type: "([^"]+)"', text)
    subtype = re.search(r'page_subtype: "([^"]+)"', text)
    return (page_type.group(1) if page_type else 'general', subtype.group(1) if subtype else 'general')


def block_for(page_type: str, subtype: str) -> str:
    if page_type == 'best_of' and subtype == 'fsm':
        return FSM_BLOCK
    if page_type == 'best_of' and subtype == 'invoicing':
        return INVOICING_BLOCK
    if page_type == 'comparison' and subtype == 'crm_vs_fsm':
        return CRM_VS_FSM_BLOCK
    if page_type == 'comparison' and subtype == 'simple_vs_complex':
        return SIMPLE_VS_COMPLEX_BLOCK
    if page_type == 'alternatives' and subtype == 'workflow_pain':
        return WORKFLOW_PAIN_BLOCK
    return DEFAULT_BLOCK


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / 'output' / 'content'
    updated = 0
    for file in content_dir.glob('*.md'):
        text = file.read_text()
        page_type, subtype = detect_meta(text)
        block = block_for(page_type, subtype)
        if '## Comparison summary' in text:
            text = re.sub(r'## Comparison summary\n.*?(?=\n## )', block.rstrip() + '\n', text, flags=re.S)
        elif '## Comparison table' in text:
            text = text.replace('## Comparison table\n', block + '\n## Comparison table\n')
        else:
            continue
        file.write_text(text)
        updated += 1
    print(f'Updated comparison summaries on {updated} files')


if __name__ == '__main__':
    main()
