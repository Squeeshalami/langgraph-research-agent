from langgraph.graph import START, END, StateGraph
from typing import TypedDict

# Import the agent functions
from nodes.query_decomposition import decompose_query
from nodes.search import tavily_search, ddg_search
from nodes.summarize_results import summarize_results
from nodes.response import generate_response


# Define state types for LangGraph
class ResearchState(TypedDict):
    query: str
    subqueries: list
    sources: list
    web_results: list
    summarized_results: list
    response: str

class ResearchStateInput(TypedDict):
    query: str

class ResearchStateOutput(TypedDict):
    sources: list
    response: str


def build_graph():
    builder = StateGraph(ResearchState, input=ResearchStateInput, output=ResearchStateOutput)

    # Add agent nodes with print statements inside each agent
    builder.add_node("decompose_query", decompose_query)
    builder.add_node("search_web", tavily_search) # Search the web for each subquery
    builder.add_node("summarize_results", summarize_results) # Summarize the web results for each subquery
    builder.add_node("generate_response", generate_response) # Generate a final response from the summarized results
    
    # Define the workflow by adding edges
    builder.add_edge(START, "decompose_query")
    builder.add_edge("decompose_query", "search_web")
    builder.add_edge("search_web", "summarize_results")
    builder.add_edge("summarize_results", "generate_response")
    builder.add_edge("generate_response", END)

    return builder.compile()