# Orqora

AI observability and orchestration platform for multi-agent workflows.

---

## Overview

Orqora is a local-first AI infrastructure platform designed to orchestrate, monitor, and inspect autonomous AI workflows.

The platform provides:

- Multi-agent workflow orchestration
- Execution tracing
- Persistent trace storage
- Trace inspection APIs
- Observability dashboards
- Dynamic execution analysis

Orqora is built to evolve into a production-grade observability layer for autonomous AI systems.

---

## Features

### Multi-Agent Workflow Engine

- Planner agent
- Reviewer agent
- Workflow orchestration layer
- Modular agent architecture

### Observability

- Execution tracing
- Trace duration tracking
- Agent metadata
- Task logging
- Persistent execution history

### Backend

- FastAPI APIs
- SQLite persistence
- REST endpoints
- Local-first architecture

### Frontend Dashboard

- Next.js frontend
- Dynamic trace inspection pages
- Trace history dashboard
- Dark-mode observability UI

---

## Architecture

```text
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
Workflow Orchestrator
        ↓
AI Agents
        ↓
SQLite Trace Storage
```

---

## Tech Stack

### Frontend

- Next.js
- TypeScript
- TailwindCSS

### Backend

- Python
- FastAPI
- SQLite

### AI Stack

- Ollama
- LangChain
- Multi-agent orchestration

---

## Project Structure

```text
orqora/
│
├── backend/
│   ├── agents/
│   │   ├── planner.py
│   │   └── reviewer.py
│   │
│   ├── orchestrator/
│   │   └── workflow.py
│   │
│   ├── tracing/
│   │   └── logger.py
│   │
│   ├── database/
│   │   └── db.py
│   │
│   ├── main.py
│   └── orqora.db
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   └── trace/
│   │       └── [id]/
│   │           └── page.tsx
│   │
│   ├── package.json
│   └── next.config.ts
│
└── README.md
```

---

## APIs

### Run Workflow

```http
POST /run?task=Build%20an%20AI%20platform
```

Runs a multi-agent workflow and stores execution traces.

---

### Get All Traces

```http
GET /traces
```

Returns all stored workflow traces.

---

### Get Single Trace

```http
GET /trace/{id}
```

Returns a single trace with full execution output.

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/Jampurampavan1903/orqora.git
cd orqora
```

---

## Backend Setup

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install fastapi uvicorn langchain ollama
```

### Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

### Install Dependencies

```bash
cd frontend
npm install
```

### Run Frontend

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

---

## Current Capabilities

- Multi-agent orchestration
- Execution persistence
- Trace retrieval APIs
- Dynamic trace inspection UI
- SQLite-backed observability
- End-to-end local execution

---

## Example Workflow

1. User submits a task
2. Workflow orchestrator receives task
3. Planner agent generates execution plan
4. Reviewer agent validates output
5. Trace is persisted in SQLite
6. Frontend dashboard visualizes execution

---

## Roadmap

### Phase 1
- [x] Workflow orchestration
- [x] SQLite trace persistence
- [x] Trace dashboard
- [x] Dynamic trace pages

### Phase 2
- [ ] OpenTelemetry integration
- [ ] LangGraph support
- [ ] CrewAI support
- [ ] Real-time trace streaming
- [ ] WebSocket updates

### Phase 3
- [ ] Distributed agent execution
- [ ] Cloud deployment
- [ ] Kubernetes support
- [ ] Production observability
- [ ] Enterprise monitoring

---

## Vision

Orqora aims to become an observability and orchestration layer for autonomous AI systems.

The long-term goal is to provide developers and enterprises with deep visibility into AI agent execution, reasoning flows, failures, latency, and coordination.

---

## Screenshots

### Observability Dashboard

- Trace history dashboard
- Execution metadata
- Agent monitoring
- Dynamic trace inspection

### Trace Inspection

- Full execution output
- Workflow metadata
- Agent activity
- Duration tracking

---

## Future Improvements

- Real-time workflow streaming
- Distributed execution engine
- Cloud-native deployment
- Authentication and RBAC
- Metrics and telemetry
- Workflow graph visualization
- Agent memory systems
- Production monitoring

---

## Author

Sai Pavan Kalyan Jampuram

GitHub:
https://github.com/Jampurampavan1903

---

## Repository

https://github.com/Jampurampavan1903/orqora
