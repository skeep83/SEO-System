# affiliate-discovery

A module for discovering, ranking, and tracking affiliate programs for products mentioned on ServiceHub.

## Run locally

```bash
cd modules/affiliate-discovery
python3 -m venv .venv
. .venv/bin/activate
pip install fastapi uvicorn jinja2 python-multipart
uvicorn src.app:app --host 0.0.0.0 --port 8790
```

## Current features
- JSON registry
- dashboard UI
- manual status updates
- seeded discovery worker

## Worker
Run the seed discovery worker:

```bash
. .venv/bin/activate
python src/discovery_worker.py
```
