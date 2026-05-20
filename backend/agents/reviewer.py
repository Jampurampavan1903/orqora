from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def reviewer_agent(plan: str):

    prompt = f"""
    You are a senior AI systems reviewer.

    Review the following execution plan.

    Improve it.
    Identify missing steps.
    Suggest optimizations.

    Plan:
    {plan}
    """

    response = llm.invoke(prompt)

    return response
