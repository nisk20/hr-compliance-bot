from fastapi import FastAPI
from agents.supervisor_agent import classify_and_route

app = FastAPI()

@app.get("/query")
def handle_query(q: str):
    return {"response": classify_and_route(q)}
