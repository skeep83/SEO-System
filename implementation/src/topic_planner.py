from __future__ import annotations

import json
from pathlib import Path


def slugify(value: str) -> str:
    return (
        value.lower()
        .replace(" vs ", "-vs-")
        .replace(" ", "-")
        .replace("/", "-")
        .replace("?", "")
    )


def page_title(keyword: str, page_type: str) -> str:
    if page_type == "best_of":
        return keyword.title() + " in 2026"
    if page_type == "comparison":
        return keyword.title() + ": Which Is Better?"
    if page_type == "alternatives":
        return keyword.title().replace("Alternatives", "Alternatives to Consider")
    return keyword.title()


def make_outline(page_type: str) -> list[str]:
    common = ["Overview", "Who this is for", "Key considerations"]
    variants = {
        "best_of": ["Top picks", "Comparison table", "How to choose", "Final recommendation"],
        "comparison": ["Quick verdict", "Feature comparison", "Pricing", "Best fit by scenario"],
        "use_case": ["Why this niche needs a CRM", "Top options", "Implementation tips", "Recommendation"],
        "alternatives": ["Why people look for alternatives", "Best alternatives", "How to switch"],
        "faq": ["Short answer", "Detailed explanation", "Common questions"],
    }
    return common + variants.get(page_type, ["Recommendation"])


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    seeds = json.loads((base / "data" / "topic_seed_crm_small_service_businesses.json").read_text())
    pages = []
    for item in seeds:
        pages.append(
            {
                "slug": slugify(item["keyword"]),
                "title": page_title(item["keyword"], item["page_type"]),
                "page_type": item["page_type"],
                "primary_keyword": item["keyword"],
                "search_intent": item["intent"],
                "audience": item["audience"],
                "problem_statement": f"Users searching for '{item['keyword']}' need a fast, trustworthy answer with actionable recommendations.",
                "recommended_products": [],
                "source_urls": [],
                "outline": make_outline(item["page_type"]),
                "faq": [],
                "call_to_action": "See the recommended tools and compare the best fit for your business.",
                "monetization_type": "affiliate",
                "review_required": item["intent"] == "commercial",
            }
        )
    out = base / "output" / "planned_pages.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(pages, ensure_ascii=False, indent=2))
    print(f"Planned {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
