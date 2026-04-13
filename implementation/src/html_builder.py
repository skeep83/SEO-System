from __future__ import annotations

import json
from pathlib import Path
import html
from site_settings import SITE_NAME, SITE_TAGLINE


def parse_markdown_sections(text: str) -> tuple[str, list[tuple[str, list[str]]]]:
    lines = text.splitlines()
    title = "Untitled"
    sections: list[tuple[str, list[str]]] = []
    current_heading = None
    current_body: list[str] = []
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            if current_heading is not None:
                sections.append((current_heading, current_body[:]))
            current_heading = line[3:].strip()
            current_body = []
        elif current_heading is not None:
            if line.strip():
                current_body.append(line)
    if current_heading is not None:
        sections.append((current_heading, current_body[:]))
    return title, sections


def render_page(title: str, sections: list[tuple[str, list[str]]]) -> str:
    body = [f"<h1>{html.escape(title)}</h1>"]
    for heading, lines in sections:
        body.append(f"<section><h2>{html.escape(heading)}</h2>")
        for line in lines:
            if line.startswith("- "):
                body.append(f"<p>{html.escape(line)}</p>")
            else:
                body.append(f"<p>{html.escape(line)}</p>")
        body.append("</section>")
    return """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{title}</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 820px; margin: 40px auto; padding: 0 16px; line-height: 1.6; }}
    h1, h2 {{ line-height: 1.2; }}
    section {{ margin: 28px 0; }}
    .nav {{ margin-bottom: 24px; color: #666; }}
  </style>
</head>
<body>
  <div class=\"nav\"><a href=\"index.html\">← Home</a></div>
  {body}
</body>
</html>
""".format(title=html.escape(title), body="\n  ".join(body))


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    content_dir = base / "output" / "content"
    site_dir = base / "output" / "site"
    site_dir.mkdir(parents=True, exist_ok=True)
    pages = []
    for md_file in sorted(content_dir.glob("*.md")):
        text = md_file.read_text()
        title, sections = parse_markdown_sections(text)
        slug = md_file.stem
        html_page = render_page(title, sections)
        (site_dir / f"{slug}.html").write_text(html_page)
        pages.append((slug, title))
    index_lines = [f"<h1>{SITE_NAME}</h1>", f"<p>{SITE_TAGLINE}</p>", "<ul>"]
    for slug, title in pages:
        index_lines.append(f'<li><a href="{slug}.html">{html.escape(title)}</a></li>')
    index_lines.append("</ul>")
    index_html = "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>Site Index</title></head><body style='font-family:Arial,sans-serif;max-width:820px;margin:40px auto;padding:0 16px'>" + "".join(index_lines) + "</body></html>"
    (site_dir / "index.html").write_text(index_html)
    print(f"Built HTML site in {site_dir}")


if __name__ == "__main__":
    main()
