from search_sources import main as build_sources
from candidate_merger import main as merge_candidates


if __name__ == "__main__":
    build_sources()
    merge_candidates()
