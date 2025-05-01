from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from agents.supervisor_agent import classify_and_route
from datetime import datetime
import json
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def get_chat_ui():
    return FileResponse("chat.html")

# 🔥 Add chat logging here
def log_chat(query: str, response: str):
    log_file = "chat_log.json"
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": query,
        "bot": response
    }

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=2)

@app.get("/query")
def handle_query(q: str):
    response = classify_and_route(q)
    log_chat(q, response)  # 👈 Log every chat here
    return {"response": response}


