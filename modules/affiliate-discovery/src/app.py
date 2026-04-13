from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .registry import load_programs, update_program

BASE = Path(__file__).resolve().parents[1]
app = FastAPI(title="Affiliate Discovery")
templates = Jinja2Templates(directory=str(BASE / "templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    programs = load_programs()
    counts = {
        "total": len(programs),
        "to_research": sum(1 for p in programs if p["status"] == "to_research"),
        "research_started": sum(1 for p in programs if p["status"] == "research_started"),
        "applied": sum(1 for p in programs if p["status"] == "applied"),
        "approved": sum(1 for p in programs if p["status"] == "approved"),
    }
    return templates.TemplateResponse(
        request,
        "index.html",
        {"programs": programs, "counts": counts},
    )


@app.post("/update")
async def update_status(product: str = Form(...), status: str = Form(...), notes: str = Form("")):
    update_program(product, {"status": status, "notes": notes})
    return RedirectResponse(url="/", status_code=303)
