# search-console module

Utilities for reading Google Search Console performance data for ServiceHub.

## Files
- `src/fetch_gsc_summary.py` — fetches summary, top pages, and top queries
- `output/latest_summary.json` — latest fetched snapshot
- `output/latest_summary.md` — readable report

## Credentials
Set the service account JSON path in `GSC_CREDENTIALS_PATH` or place it at workspace root as `servicehub-search-console.json`.
