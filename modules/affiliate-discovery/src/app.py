from __future__ import annotations

import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE = Path(__file__).resolve().parents[1]
DATA_PATH = BASE / "data" / "programs.json"

app = FastAPI(title="Affiliate Discovery")
templates = Jinja2Templates(directory=str(BASE / "templates"))


def load_programs():
    return json.loads(DATA_PATH.read_text())


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    programs = load_programs()
    counts = {
        "total": len(programs),
        "to_research": sum(1 for p in programs if p["status"] == "to_research"),
        "approved": sum(1 for p in programs if p["status"] == "approved"),
        "applied": sum(1 for p in programs if p["status"] == "applied"),
    }
    return templates.TemplateResponse("index.html", {"request": request, "programs": programs, "counts": counts})
