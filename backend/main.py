from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from orchestrator.workflow import run_workflow

app = FastAPI(
    title="Orqora API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "Orqora"
    }

@app.post("/run")
async def run(task: str):
    result = run_workflow(task)

    return {
        "task": task,
        "result": result
    }

@app.get("/health")
async def health():
    return {
        "healthy": True
    }
