from __future__ import annotations

import json
import re
from pathlib import Path


def build_block(by_product: dict) -> str:
    lines = ["## Offers", ""]
    for product in ["Jobber", "Housecall Pro", "ServiceTitan", "HubSpot"]:
        item = by_product[product]
        lines.append(f"- [{item['cta']}]({item['placeholder_url']})")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    links = json.loads((base / "data" / "affiliate_placeholders.json").read_text())
    by_product = {item["product"]: item for item in links}
    content_dir = base / "output" / "content"
    updated = 0
    for file in content_dir.glob("*.md"):
        text = file.read_text()
        block = build_block(by_product)
        if "## Offers" in text:
            text = re.sub(r"## Offers\n(?:.*\n)*?(?=\n## |\Z)", block + "\n", text, flags=re.MULTILINE)
        else:
            text += "\n" + block
        file.write_text(text)
        updated += 1
    print(f"Injected or refreshed offers in {updated} files")


if __name__ == "__main__":
    main()
