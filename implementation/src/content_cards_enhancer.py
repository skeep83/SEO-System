from __future__ import annotations

from pathlib import Path


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / "output" / "content"
    updated = 0
    for file in content_dir.glob("*.md"):
        text = file.read_text()
        if "## Quick verdict" not in text:
            text = text.replace(
                "## Call to action\n",
                "## Quick verdict\nThis page should help a buyer narrow the shortlist fast, not just learn vocabulary.\n\n## Call to action\n",
            )
        if "## Decision shortcuts" not in text:
            text += "\n## Decision shortcuts\n- Choose a field-service-first tool if scheduling and dispatch are central.\n- Choose a broader CRM if pipeline, automation, and marketing matter more than technician workflows.\n- Eliminate options that are too complex for your current team size.\n"
        file.write_text(text)
        updated += 1
    print(f"Enhanced decision content in {updated} files")


if __name__ == "__main__":
    main()
