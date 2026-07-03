# 🤖 Enterprise AI Assistant

An AI-powered Enterprise Assistant built using **FastAPI**, **LangGraph**, **LangChain**, and **Groq LLM**.

The assistant can understand natural language questions, classify user intent using an LLM, and perform business actions such as:

- 👨‍💼 Fetch Employee Information
- 🎫 Create Support Tickets
- 📊 Generate Monthly Reports

This project was built as part of an AI Solutions Engineer coding assignment.

---

# 🚀 Features

- FastAPI REST API
- LangGraph workflow
- Groq Llama 3.3 70B LLM
- Intent Detection using LLM
- Employee Lookup Tool
- Ticket Creation Tool
- Report Generation Tool
- Request Validation using Pydantic
- Error Handling
- Modular Project Architecture

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
| LangGraph | AI Workflow |
| LangChain | LLM Integration |
| Groq | LLM Provider |
| Pydantic | Request Validation |
| JSON | Mock Database |

---

# 📁 Project Structure

```text
enterprise-ai-assistant/
│
├── app/
│   ├── api/
│   │      routes.py
│   │
│   ├── graph/
│   │      assistant_graph.py
│   │
│   ├── llm/
│   │      client.py
│   │
│   ├── prompts/
│   │      system_prompt.py
│   │
│   ├── state/
│   │      assistant_state.py
│   │
│   ├── tools/
│   │      employee_tool.py
│   │      ticket_tool.py
│   │      report_tool.py
│   │
│   ├── data/
│   │      employees.json
│   │      tickets.json
│   │
│   └── utils/
│          helpers.py
│
├── tests/
├── main.py
├── .env
├── pyproject.toml
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <your-github-url>

cd enterprise-ai-assistant
```

---

## Create Virtual Environment

```bash
uv venv
```

Activate environment

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
uv sync
```

or

```bash
uv add fastapi
uv add uvicorn
uv add langchain
uv add langchain-groq
uv add langgraph
uv add python-dotenv
uv add pydantic
```

---

## Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Application

```bash
uvicorn main:app --reload
```

Server starts at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📬 API Endpoint

## POST

```
/ask
```

---

## Request

```json
{
    "question":"Who is Rahul Sharma?"
}
```

---

## Response

```json
{
    "response":"Rahul Sharma works in Engineering department."
}
```

---

# 💡 Example Queries

### Employee Lookup

```json
{
    "question":"Who is Rahul Sharma?"
}
```

---

### Ticket Creation

```json
{
    "question":"Create ticket for Login Issue"
}
```

---

### Report Generation

```json
{
    "question":"Generate monthly report"
}
```

---

### General AI Question

```json
{
    "question":"Explain Artificial Intelligence"
}
```

---

# 🧠 AI Workflow

```text
                User
                  │
                  ▼
            FastAPI Endpoint
                  │
                  ▼
             LangGraph Graph
                  │
                  ▼
          Groq LLM (Intent Detection)
                  │
      ┌───────────┼────────────┐
      │           │            │
      ▼           ▼            ▼
 Employee     Ticket Tool   Report Tool
    Tool
      │
      ▼
    Response
```

---

# 🛡 Engineering Decisions

### Why LangGraph?

LangGraph provides a structured workflow for AI applications where different nodes perform different responsibilities.

In this project:

- LangGraph manages the AI workflow.
- The LLM determines user intent.
- Based on the detected intent, the workflow routes the request to the appropriate business tool.

---

### Why LangChain?

LangChain simplifies interaction with the LLM by providing abstractions for prompts, models, and tool integration.

---

### Why Groq?

Groq provides extremely fast inference for open-source large language models, making it suitable for real-time AI assistants.

---

# ✅ Engineering Improvement

This implementation includes:

- Request Validation using Pydantic
- Error Handling with FastAPI
- LLM-based Intent Classification
- Modular AI Workflow using LangGraph

---

# 🚀 Future Improvements

- Conversation Memory
- Authentication & Authorization
- Database Integration
- Vector Database (RAG)
- Multi-Agent Workflow
- Streaming Responses
- Role-Based Access Control
- Audit Logs
- Docker Support
- Deployment on AWS

---

# 📷 Demo

The application demonstrates:

- Employee Information Retrieval
- Ticket Creation
- Report Generation
- AI-based Intent Classification
- FastAPI REST API

---

# 👨‍💻 Author

**Sagar Rana**

 AI Engineer


---

# ⭐ Assignment Highlights

✔ FastAPI REST API

✔ LangGraph Workflow

✔ LangChain Integration

✔ Groq LLM

✔ AI Intent Detection

✔ Business Tool Calling

✔ Modular Architecture

✔ Request Validation

✔ Error Handling

✔ Clean Code Structure
