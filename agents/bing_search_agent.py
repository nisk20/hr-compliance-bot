from langchain_community.tools.bing_search.tool import BingSearchResults
import os

def run_bing_search(query):
    api_key = os.getenv("BING_SEARCH_API_KEY")
    if not api_key:
        return "⚠️ Missing Bing API key in environment."

    tool = BingSearchResults(api_key=api_key, k=3)
    return tool.run(query)
