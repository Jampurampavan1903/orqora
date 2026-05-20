from agents.planner import planner_agent
from tracing.logger import create_trace, close_trace

def run_workflow(task: str):

    trace = create_trace(
        agent_name="planner_agent",
        task=task
    )

    planner_output = planner_agent(task)

    completed_trace = close_trace(
        trace,
        planner_output
    )

    return completed_trace
