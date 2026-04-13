from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE = Path(__file__).resolve().parents[1]
DATA_PATH = BASE / "data" / "programs.json"


def load_programs() -> list[dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    return json.loads(DATA_PATH.read_text())


def save_programs(programs: list[dict[str, Any]]) -> None:
    DATA_PATH.write_text(json.dumps(programs, ensure_ascii=False, indent=2))


def update_program(product: str, fields: dict[str, Any]) -> bool:
    programs = load_programs()
    updated = False
    for item in programs:
        if item.get("product") == product:
            item.update(fields)
            updated = True
            break
    if updated:
        save_programs(programs)
    return updated
