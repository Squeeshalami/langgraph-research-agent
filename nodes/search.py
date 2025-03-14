from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

load_dotenv()

def tavily_search(state: dict) -> dict:
    """
    For each subquery, perform a Tavily search using the TavilySearchResults class and aggregate the results.
    """
    subqueries = state.get("subqueries", [])
    all_sources = []
    all_web_results = []

    print("[Search] Starting Tavily search for each subquery...")
    for subquery in subqueries:
        print(f"[Search] Processing subquery: {subquery}")
        try:
            # Instantiate TavilySearchResults and perform the search
            tavily_search = TavilySearchResults(max_results=5)
            results = tavily_search.invoke(subquery)
        except Exception as e:
            print(f"[Search] Exception during search for subquery '{subquery}':", e)
            continue

        if not results or not isinstance(results, list):
            print(f"[Search] No valid results found for subquery: {subquery}")
            continue
            
        # Extract URL and snippet from each result
        sources = [result.get('url', 'N/A') for result in results if isinstance(result, dict)]
        web_results = [result.get('content', '') for result in results if isinstance(result, dict)]
        print(f"[Search] Found {len(sources)} sources for subquery '{subquery}'")
        all_sources.extend(sources)
        all_web_results.extend(web_results)
    
    state["sources"] = all_sources
    state["web_results"] = all_web_results
    print("[Search] Aggregated sources:", all_sources)
    print("[Search] Aggregated web results count:", len(all_web_results))
    return {"sources": all_sources, "web_results": all_web_results}
