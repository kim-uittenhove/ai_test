# tasks/fetch.py

import os
import yaml
from fetchers import (
    semantic_scholar_fetch,
    crossref_fetch,
    scopus_fetch,
    wos_fetch
)

FETCHERS_TO_RUN = ["semantic_scholar", "scopus", "wos"]

def run():
    print("🚀 Running fetch step")

    with open("config/reference_queries.yaml") as f:
        config = yaml.safe_load(f)

    queries = config.get("queries", [])

    for q in queries:
        name = q["name"]
        key = q["key"]
        search_terms = q.get("search_terms", {})

        print(f"\n📚 Fetching for: {name}")
        out_dir = f"data/new/raw/{key}"
        os.makedirs(out_dir, exist_ok=True)

        if "semantic_scholar" in FETCHERS_TO_RUN:
            query = search_terms.get("semantic_scholar")
            if query:
                print("▶ Semantic Scholar")
                output = os.path.join(out_dir, "semantic_scholar.jsonl")
                semantic_scholar_fetch.fetch(query, output)

        if "crossref" in FETCHERS_TO_RUN:
            query = search_terms.get("crossref")
            if query:
                print("▶ Crossref")
                output = os.path.join(out_dir, "crossref.jsonl")
                crossref_fetch.fetch(query, output)

        if "scopus" in FETCHERS_TO_RUN:
            query = search_terms.get("scopus")
            if query:
                print("▶ Scopus")
                output = os.path.join(out_dir, "scopus.jsonl")
                scopus_fetch.fetch(query, output)

        if "wos" in FETCHERS_TO_RUN:
            query = search_terms.get("wos")
            if query:
                print("▶ Web of Science")
                output = os.path.join(out_dir, "wos.jsonl")
                wos_fetch.fetch(query, output)
