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


def body(page: dict) -> str:
    sections = [f"# {page['title']}", "", page["problem_statement"], ""]
    for item in page["outline"]:
        sections.append(f"## {item}")
        sections.append(f"Draft notes for: {item}.")
        sections.append("")
    sections.append("## Call to action")
    sections.append(page["call_to_action"])
    sections.append("")
    return "\n".join(sections)


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    planned = json.loads((base / "output" / "planned_pages.json").read_text())
    out_dir = base / "output" / "content"
    out_dir.mkdir(parents=True, exist_ok=True)
    for page in planned:
        content = frontmatter(page) + "\n\n" + body(page)
        (out_dir / f"{page['slug']}.md").write_text(content)
    print(f"Generated {len(planned)} markdown files in {out_dir}")


if __name__ == "__main__":
    main()
