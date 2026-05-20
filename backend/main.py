from fastapi import FastAPI
from orchestrator.workflow import run_workflow

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "Orqora"
    }

@app.post("/run")
def run(task: str):
    return run_workflow(task)
