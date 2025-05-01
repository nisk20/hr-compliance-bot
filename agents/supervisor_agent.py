from agents import labor_laws_agent, human_rights_agent, ohs_agent
from agents.bing_search_agent import run_bing_search

def classify_and_route(query):
    query_lower = query.lower()

    if "harass" in query_lower or "discrimination" in query_lower:
        return human_rights_agent.handle_query(query)
    elif "minimum wage" in query_lower or "overtime" in query_lower:
        return labor_laws_agent.handle_query(query)
    elif "injury" in query_lower or "workplace safety" in query_lower:
        return ohs_agent.handle_query(query)
    else:
        return f"🔎 Bing Search Agent: {run_bing_search(query)}"
