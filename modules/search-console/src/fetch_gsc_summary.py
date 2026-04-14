from __future__ import annotations

import json
import os
from datetime import date, timedelta
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

BASE = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SITE_URL = "sc-domain:servicehub.md"
CREDENTIALS_PATH = os.environ.get(
    "GSC_CREDENTIALS_PATH",
    str(Path('/home/skeep/.openclaw/workspace/servicehub-search-console.json')),
)
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def query(service, body: dict) -> dict:
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()


def main() -> None:
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=27)
    body_base = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "rowLimit": 10,
    }

    summary = query(service, body_base)
    pages = query(service, {**body_base, "dimensions": ["page"]})
    queries = query(service, {**body_base, "dimensions": ["query"]})

    payload = {
        "site": SITE_URL,
        "startDate": body_base["startDate"],
        "endDate": body_base["endDate"],
        "summary": summary,
        "topPages": pages.get("rows", []),
        "topQueries": queries.get("rows", []),
    }
    (OUTPUT_DIR / "latest_summary.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = [
        f"# GSC Summary for {SITE_URL}",
        "",
        f"Period: {body_base['startDate']} to {body_base['endDate']}",
        "",
    ]
    if summary.get("rows"):
        row = summary["rows"][0]
        lines += [
            f"- Clicks: {row.get('clicks', 0)}",
            f"- Impressions: {row.get('impressions', 0)}",
            f"- CTR: {row.get('ctr', 0)}",
            f"- Position: {row.get('position', 0)}",
            "",
        ]
    else:
        lines += ["- No performance rows yet", ""]

    lines.append("## Top pages")
    if payload["topPages"]:
        for row in payload["topPages"]:
            lines.append(f"- {row['keys'][0]} | clicks={row.get('clicks',0)} impressions={row.get('impressions',0)} position={row.get('position',0)}")
    else:
        lines.append("- No page data yet")
    lines.append("")

    lines.append("## Top queries")
    if payload["topQueries"]:
        for row in payload["topQueries"]:
            lines.append(f"- {row['keys'][0]} | clicks={row.get('clicks',0)} impressions={row.get('impressions',0)} position={row.get('position',0)}")
    else:
        lines.append("- No query data yet")
    lines.append("")

    (OUTPUT_DIR / "latest_summary.md").write_text("\n".join(lines))
    print((OUTPUT_DIR / "latest_summary.md").read_text())


if __name__ == "__main__":
    main()
