from __future__ import annotations

import re
from pathlib import Path

DEFAULT_BLOCK = """
## Verdict snapshot
- Jobber: strongest fit for smaller field-service teams that want simplicity and operational coverage.
- Housecall Pro: strong choice when communication, dispatch coordination, and payments matter more.
- ServiceTitan: heavier platform, usually better only if operations are already more complex.
- HubSpot: better when pipeline management and marketing matter more than technician workflows.
"""

FSM_BLOCK = """
## Verdict snapshot
- Jobber: best starting point for most small teams that need quoting, scheduling, invoicing, and dispatch without extra complexity.
- Housecall Pro: stronger choice when communication, payments, and dispatch coordination carry more weight in the workflow.
- ServiceTitan: only makes sense when the operation is already complex enough to justify heavier process depth.
- HubSpot: weaker fit here unless sales pipeline matters more than field execution.
"""

INVOICING_BLOCK = """
## Verdict snapshot
- Jobber: strongest fit when invoicing needs to stay tied to jobs, estimates, and customer records.
- Housecall Pro: strong choice when payments and customer communication need to stay tightly connected to field workflow.
- ServiceTitan: more software than most small teams need for invoicing unless the operation is already much larger.
- HubSpot: poor primary fit for invoicing-first buyers unless revenue pipeline is the bigger concern.
"""

CRM_VS_FSM_BLOCK = """
## Verdict snapshot
- Jobber: better fit when the business runs on quoting, scheduling, dispatch, and invoicing.
- HubSpot: better fit when lead management, pipeline visibility, and marketing automation are more important than technician workflow.
- Housecall Pro: still relevant if you want a stronger field-service comparison set.
- ServiceTitan: usually unnecessary unless operational complexity is already much higher.
"""

SIMPLE_VS_COMPLEX_BLOCK = """
## Verdict snapshot
- Jobber: better default for smaller teams that need faster adoption and cleaner day-to-day execution.
- ServiceTitan: only the better choice when workflow depth clearly outweighs complexity cost.
- Housecall Pro: useful middle-ground benchmark if you want stronger communication and dispatch without going full enterprise.
- HubSpot: separate path entirely if the problem is CRM and marketing rather than field operations.
"""

WORKFLOW_PAIN_BLOCK = """
## Verdict snapshot
- Jobber: keep it if the workflow still fits and the pain is minor.
- Housecall Pro: stronger alternative when communication, dispatch, and payments need to feel more connected.
- ServiceTitan: not a default alternative for small teams unless the pain comes from outgrowing simpler tools.
- HubSpot: only makes sense if the real pain is around pipeline and automation instead of field workflow.
"""


def detect_meta(text: str) -> tuple[str, str]:
    page_type = re.search(r'page_type: "([^"]+)"', text)
    subtype = re.search(r'page_subtype: "([^"]+)"', text)
    return (page_type.group(1) if page_type else 'general', subtype.group(1) if subtype else 'general')


def verdict_block(page_type: str, subtype: str) -> str:
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
        block = verdict_block(page_type, subtype)
        if '## Verdict snapshot' in text:
            text = re.sub(r'## Verdict snapshot\n.*?(?=\n## )', block.rstrip() + '\n', text, flags=re.S)
            file.write_text(text)
            updated += 1
            continue
        if '## Recommended products' in text:
            text = text.replace('## Recommended products\n', block + '\n## Recommended products\n')
            file.write_text(text)
            updated += 1
    print(f'Updated verdict snapshots on {updated} files')


if __name__ == '__main__':
    main()
