from __future__ import annotations

import json
from pathlib import Path


def relevant_products(page: dict, products: list[dict]) -> list[dict]:
    keyword = page["primary_keyword"].lower()
    results = []
    for product in products:
        haystacks = [product["name"].lower(), product["category"].lower()] + [x.lower() for x in product["best_for"]]
        if any(token in keyword for token in ["crm", "service", "plumber", "electrician", "jobber", "housecall"]):
            results.append(product)
    seen = set()
    unique = []
    for product in results:
        if product["name"] not in seen:
            seen.add(product["name"])
            unique.append(product)
    return unique[:4]


def enrich_markdown(page: dict, products: list[dict]) -> str:
    chosen = relevant_products(page, products)
    lines = []
    lines.append("## Recommended products")
    for product in chosen:
        lines.append(f"### {product['name']}")
        lines.append(f"- Best for: {', '.join(product['best_for'])}")
        lines.append(f"- Strengths: {', '.join(product['strengths'])}")
        lines.append(f"- Weaknesses: {', '.join(product['weaknesses'])}")
        lines.append(f"- Pricing note: {product['pricing_note']}")
        lines.append(f"- Source: {product['source_url']}")
        lines.append("")
    lines.append("## Editor note")
    lines.append("This page should be reviewed before publication, especially if it carries affiliate links or product claims.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    pages = json.loads((base / "output" / "planned_pages.json").read_text())
    products = json.loads((base / "data" / "products_crm_small_service_businesses.json").read_text())
    content_dir = base / "output" / "content"
    for page in pages:
        target = content_dir / f"{page['slug']}.md"
        text = target.read_text()
        if "## Recommended products" in text:
            continue
        text += "\n" + enrich_markdown(page, products)
        target.write_text(text)
    print(f"Enriched {len(pages)} content files")


if __name__ == "__main__":
    main()
