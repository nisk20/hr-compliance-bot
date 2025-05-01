# 🤖 HR Compliance Copilot — Multi-Agent AI Assistant

> A privacy-respecting, open-source multi-agent chatbot built to help Canadian and North American users understand **Labor Laws**, **Human Rights**, and **Workplace Safety**.

---

## 🚀 Overview

**HR Compliance Copilot** is an AI-powered assistant that classifies HR compliance queries and routes them to specialized AI agents using a multi-agent architecture. Now enhanced with:

- ✅ **Chainlit UI** – Sleek real-time chat interface
- ✅ **Mistral-7B-Instruct** – Open-source LLM hosted via Hugging Face
- ✅ **PostgreSQL** – For persistent chat history and logging
- ✅ **Azure AI Foundry** – Final deployment for public web access

---

## 🧠 Architecture

---

## ⚙️ Tech Stack

| Component         | Tool/Library                               |
|------------------|--------------------------------------------|
| Frontend UI      | [Chainlit](https://docs.chainlit.io/)      |
| LLM Model        | [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) |
| Agents Framework | Python, FastAPI, Langchain                 |
| Storage          | PostgreSQL (open-source local or cloud)    |
| Hosting          | Azure AI Foundry (Optional)                |

---

## 🧩 Multi-Agent System

Each message is classified by a **Supervisor Agent**, then routed to:

- **Labor Law Agent**: Handles questions about Canadian and U.S. employment standards, wages, terminations.
- **Human Rights Agent**: Answers queries on workplace harassment, discrimination, equal opportunity.
- **OHS Agent**: Provides info on safety compliance, WSIB, workplace conditions.

---

## 🛠️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/nisk20/hr-compliance-bot.git
cd hr-compliance-bot

