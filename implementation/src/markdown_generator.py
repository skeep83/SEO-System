from __future__ import annotations

import json
from pathlib import Path


def frontmatter(page: dict) -> str:
    lines = [
        '---',
        f'title: "{page["title"]}"',
        f'slug: "{page["slug"]}"',
        f'page_type: "{page["page_type"]}"',
        f'primary_keyword: "{page["primary_keyword"]}"',
        f'search_intent: "{page["search_intent"]}"',
        f'audience: "{page["audience"]}"',
        f'monetization_type: "{page["monetization_type"]}"',
        f'review_required: {str(page["review_required"]).lower()}',
        '---',
    ]
    return "\n".join(lines)


def best_of_sections(page: dict) -> list[str]:
    keyword = page['primary_keyword']
    audience = page['audience']
    return [
        f"# {page['title']}",
        '',
        page['problem_statement'],
        '',
        '## Overview',
        f"The best choice for {keyword} should help {audience} make a shortlist quickly, not trap them in generic software-list content. The real goal is to find the strongest fit for day-to-day workflow, team size, and commercial priorities.",
        '',
        '## Who this is for',
        f"This page is for {audience} who want a practical shortlist instead of a bloated feature dump.",
        '',
        '## Key considerations',
        'Look at workflow fit first, then ease of adoption, pricing posture, and whether the tool solves the main operational bottleneck without adding unnecessary complexity.',
        '',
        '## Top picks',
        'The strongest shortlist should separate the safest all-round choice from the stronger second option and from heavier tools that only make sense in more complex environments.',
        '',
        '## Comparison table',
        'The comparison table should make it obvious which tool is best for simplicity, workflow depth, growth stage, and operational fit.',
        '',
        '## How to choose',
        'Start by identifying whether your main problem is field workflow, sales pipeline, dispatch complexity, or finance/admin drag. Then eliminate tools built for a very different operating model.',
        '',
        '## Final recommendation',
        'The best option should be the one that improves execution fastest with the least operational friction, not the one with the longest feature list.',
        '',
        '## Call to action',
        page['call_to_action'],
        '',
    ]


def comparison_sections(page: dict) -> list[str]:
    keyword = page['primary_keyword']
    return [
        f"# {page['title']}",
        '',
        page['problem_statement'],
        '',
        '## Overview',
        f"{keyword.title()} is usually not about picking the platform with the most features. It is about choosing the tool that fits the business model, team size, and workflow pressure with the least wasted motion.",
        '',
        '## Who this is for',
        f"This page is for {page['audience']} who want a fast answer on which tool belongs on the shortlist and which one probably does not.",
        '',
        '## Key considerations',
        'The comparison should focus on operational fit, ease of adoption, quoting and scheduling depth, communication flow, pricing posture, and how much complexity the team can realistically absorb.',
        '',
        '## Quick verdict',
        'A strong comparison should tell you quickly which option is safer for smaller teams, which one is better for heavier workflow needs, and whether either tool is solving the wrong problem entirely.',
        '',
        '## Feature comparison',
        'The feature comparison should focus on the buying decision, not generic checklists. Buyers care about whether the software actually improves day-to-day work.',
        '',
        '## Pricing',
        'Pricing should be judged by fit and implementation drag, not just the headline subscription number.',
        '',
        '## Best fit by scenario',
        'Different products win when the business priorities change, so the page should make those scenario boundaries obvious.',
        '',
        '## Call to action',
        page['call_to_action'],
        '',
    ]


def use_case_sections(page: dict) -> list[str]:
    keyword = page['primary_keyword']
    return [
        f"# {page['title']}",
        '',
        page['problem_statement'],
        '',
        '## Overview',
        f"The best answer for {keyword} depends on the trade workflow, not just generic CRM features. The right software should reduce admin drag and support the way this business type actually books, schedules, follows up, and gets paid.",
        '',
        '## Who this is for',
        f"This page is for {page['audience']} who need software that fits the realities of their trade instead of a vague all-purpose tool.",
        '',
        '## Key considerations',
        'The most important factors are quoting, scheduling, follow-up, invoicing, repeat work, and how easy the system is for a small team to adopt consistently.',
        '',
        '## Why this niche needs a CRM',
        'This trade-specific page should explain the workflow pressure points that make dedicated software useful instead of treating every service business as identical.',
        '',
        '## Top options',
        'The shortlist should prioritize tools that fit the trade-specific workflow first and only then consider broader CRM flexibility.',
        '',
        '## Implementation tips',
        'The best tool still fails if setup is messy, so implementation guidance should stay practical and adoption-focused.',
        '',
        '## Recommendation',
        'The best choice should be the one that matches how the crew already works while reducing missed follow-up and admin friction.',
        '',
        '## Call to action',
        page['call_to_action'],
        '',
    ]


def alternatives_sections(page: dict) -> list[str]:
    keyword = page['primary_keyword']
    return [
        f"# {page['title']}",
        '',
        page['problem_statement'],
        '',
        '## Overview',
        f"People searching {keyword} are usually not asking for random substitutions. They want to know which replacement fits better if the original tool feels too expensive, too heavy, or just mismatched to the workflow.",
        '',
        '## Why people look for alternatives',
        'Most buyers switch when they hit pricing pressure, missing workflow depth, or a mismatch between the software and the way the team actually operates day to day.',
        '',
        '## Best alternatives to consider',
        'The shortlist should separate lighter, simpler options from broader or more operationally complex platforms.',
        '',
        '## How to compare alternatives',
        'Compare alternatives by what problem they solve better, not by counting features in a vacuum.',
        '',
        '## Final recommendation',
        'The best alternative is the one that fixes the current pain point without adding a worse one elsewhere in the workflow.',
        '',
        '## Call to action',
        page['call_to_action'],
        '',
    ]


def default_sections(page: dict) -> list[str]:
    sections = [f"# {page['title']}", '', page['problem_statement'], '']
    for item in page['outline']:
        sections.append(f'## {item}')
        sections.append(f'Draft notes for: {item}.')
        sections.append('')
    sections.append('## Call to action')
    sections.append(page['call_to_action'])
    sections.append('')
    return sections


def body(page: dict) -> str:
    page_type = page['page_type']
    if page_type == 'best_of':
        return '\n'.join(best_of_sections(page))
    if page_type == 'comparison':
        return '\n'.join(comparison_sections(page))
    if page_type == 'use_case':
        return '\n'.join(use_case_sections(page))
    if page_type == 'alternatives':
        return '\n'.join(alternatives_sections(page))
    return '\n'.join(default_sections(page))


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    planned = json.loads((base / 'output' / 'planned_pages.json').read_text())
    out_dir = base / 'output' / 'content'
    out_dir.mkdir(parents=True, exist_ok=True)
    for page in planned:
        content = frontmatter(page) + '\n\n' + body(page)
        (out_dir / f"{page['slug']}.md").write_text(content)
    print(f'Generated {len(planned)} markdown files in {out_dir}')


if __name__ == '__main__':
    main()
