from agents.planner import planner_agent

def run_workflow(task: str):

    planner_output = planner_agent(task)

    return {
        "task": task,
        "planner_output": planner_output
    }
