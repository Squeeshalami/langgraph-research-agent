import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


MODEL = "gemma3:4b" ## Smaller Model for faster results

decomposition_template = """
Your task is to break down a complex research query into a list
 of distinct subqueries for a web search deep dive.
The answer must be a valid JSON array of strings with no additional text.
For example, if the query is "what permits do I need to build a house", then a valid answer would be:
["What permits are needed for building a house?", "Who issues building permits?", "How to apply for building permits?", "What are the fees for permits?", "What are the legal requirements for building permits?"]

Original Query: {query}
JSON Array:
"""

def decompose_query(state: dict) -> dict:
    print("Decomposing query...")
    model = ChatOllama(model=MODEL)
    prompt = ChatPromptTemplate.from_template(decomposition_template)
    chain = prompt | model
    decomposed_query = chain.invoke({"query": state["query"]})
    
    print(f"Decomposed query: {decomposed_query.content}")

    try:
        subqueries = json.loads(decomposed_query.content)
        if not isinstance(subqueries, list):
            raise ValueError("The response is not a valid JSON array")
        state["subqueries"] = subqueries
        return state
    except Exception as e:
        print("[Decomposition] JSON parsing error:", e)
        subqueries = [line.strip() for line in decomposed_query.content.split("\n") if line.strip()]

    # Limit to a maximum number of subqueries if needed.
    subqueries = subqueries[:5]
    state["subqueries"] = subqueries
    return state