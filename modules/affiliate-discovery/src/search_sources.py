from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE = Path(__file__).resolve().parents[1]
QUERIES_PATH = BASE / "data" / "search_queries.json"
OUTPUT_PATH = BASE / "data" / "candidate_sources.json"


def main() -> None:
    queries = json.loads(QUERIES_PATH.read_text())
    output = []
    for item in queries:
        q = item["query"]
        output.append(
            {
                "product": item["product"],
                "query": q,
                "sources": [
                    f"https://www.google.com/search?q={quote_plus(q)}",
                    f"https://www.bing.com/search?q={quote_plus(q)}",
                    f"https://duckduckgo.com/?q={quote_plus(q)}",
                ],
            }
        )
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print(f"Built candidate source list for {len(output)} products")


if __name__ == "__main__":
    main()
