def simple_router(query):
    keywords = {
        "labor": ["minimum wage", "termination"],
        "rights": ["harassment", "discrimination"],
        "safety": ["injury", "hazard"]
    }

    for category, terms in keywords.items():
        for term in terms:
            if term in query.lower():
                return category
    return "unknown"
