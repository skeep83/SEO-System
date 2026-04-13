from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    links = json.loads((base / "data" / "affiliate_placeholders.json").read_text())
    by_product = {item["product"]: item for item in links}
    content_dir = base / "output" / "content"
    updated = 0
    for file in content_dir.glob("*.md"):
        text = file.read_text()
        if "## Offers" in text:
            continue
        block = ["## Offers", ""]
        for product in ["Jobber", "Housecall Pro", "ServiceTitan", "HubSpot"]:
            item = by_product[product]
            block.append(f"- [{item['cta']}]({item['placeholder_url']})")
        block.append("")
        text += "\n" + "\n".join(block)
        file.write_text(text)
        updated += 1
    print(f"Injected offers into {updated} files")


if __name__ == "__main__":
    main()
