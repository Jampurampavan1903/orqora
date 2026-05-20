from agents.planner import planner_agent
from agents.reviewer import reviewer_agent

from tracing.logger import create_trace, close_trace

def run_workflow(task: str):

    trace = create_trace(
        agent_name="multi_agent_workflow",
        task=task
    )

    planner_output = planner_agent(task)

    reviewer_output = reviewer_agent(
        planner_output
    )

    final_output = {
        "planner_output": planner_output,
        "reviewer_output": reviewer_output
    }

    completed_trace = close_trace(
        trace,
        str(final_output)
    )

    completed_trace["workflow_output"] = final_output

    return completed_trace
