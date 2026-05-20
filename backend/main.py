from fastapi import FastAPI

from orchestrator.workflow import run_workflow

from tracing.service import (
    get_all_traces,
    get_trace
)

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


@app.get("/traces")
def traces():

    return get_all_traces()


@app.get("/trace/{trace_id}")
def trace(trace_id: str):

    return get_trace(trace_id)
