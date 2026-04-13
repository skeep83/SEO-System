#!/usr/bin/env bash
set -euo pipefail
BASE="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$BASE/src/niche_scoring.py"
python3 "$BASE/src/topic_planner.py"
python3 "$BASE/src/markdown_generator.py"
python3 "$BASE/src/content_enricher.py"
python3 "$BASE/src/site_index_builder.py"
python3 "$BASE/src/monitoring_registry.py"
python3 "$BASE/src/review_queue_builder.py"
python3 "$BASE/src/html_builder.py"
python3 "$BASE/src/metadata_builder.py"
python3 "$BASE/src/sitemap_builder.py"
echo "Build complete"
