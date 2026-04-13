from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROGRAMS_PATH = BASE / "data" / "programs.json"
CANDIDATES_PATH = BASE / "data" / "candidate_sources.json"


def main() -> None:
    programs = json.loads(PROGRAMS_PATH.read_text())
    candidates = json.loads(CANDIDATES_PATH.read_text()) if CANDIDATES_PATH.exists() else []
    by_product = {item['product']: item for item in candidates}
    updated = 0
    for program in programs:
        c = by_product.get(program['product'])
        if not c:
            continue
        program['candidate_sources'] = c['sources']
        updated += 1
    PROGRAMS_PATH.write_text(json.dumps(programs, ensure_ascii=False, indent=2))
    print(f"Merged candidate sources into {updated} programs")


if __name__ == "__main__":
    main()
