from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def planner_agent(task: str):

    prompt = f"""
    You are an AI planning agent.

    Break the following task into clear execution steps.

    Task:
    {task}
    """

    response = llm.invoke(prompt)

    return response
