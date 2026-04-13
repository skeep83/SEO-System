from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA_PATH = BASE / "data" / "programs.json"

DISCOVERY_MAP = {
    "Jobber": {
        "program_type": "affiliate_or_referral",
        "network": "manual_research",
        "program_url": "https://www.google.com/search?q=Jobber+affiliate+program",
        "status": "research_started",
        "fit_score": 9,
        "notes": "High fit for field service pages. Verify whether direct affiliate, referral, or partner program is available."
    },
    "Housecall Pro": {
        "program_type": "affiliate_or_referral",
        "network": "manual_research",
        "program_url": "https://www.google.com/search?q=Housecall+Pro+affiliate+program",
        "status": "research_started",
        "fit_score": 9,
        "notes": "Strong commercial fit. Confirm direct or network-based partner path."
    },
    "HubSpot": {
        "program_type": "affiliate",
        "network": "manual_research",
        "program_url": "https://www.google.com/search?q=HubSpot+affiliate+program",
        "status": "research_started",
        "fit_score": 8,
        "notes": "Likely accessible partner path. Good broad CRM fallback option."
    },
    "Zoho CRM": {
        "program_type": "affiliate_or_partner",
        "network": "manual_research",
        "program_url": "https://www.google.com/search?q=Zoho+CRM+affiliate+program",
        "status": "research_started",
        "fit_score": 7,
        "notes": "Worth checking as lower-friction SMB CRM option."
    }
}


def main() -> None:
    programs = json.loads(DATA_PATH.read_text())
    updated = 0
    for item in programs:
        patch = DISCOVERY_MAP.get(item.get("product"))
        if not patch:
            continue
        item.update(patch)
        updated += 1
    DATA_PATH.write_text(json.dumps(programs, ensure_ascii=False, indent=2))
    print(f"Discovery worker updated {updated} programs")


if __name__ == "__main__":
    main()
