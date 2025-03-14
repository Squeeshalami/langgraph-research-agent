from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

MODEL = "gemma3:12b" ## Lasger Model for Final Results

generate_response_template = """
Given the original research query and the following summarized results,
generate a final,very detailed,and well-organized response that comprehensively answers the query.
You should be in the form of a long form research report, that organizes the summarized results
into a cohesive and comprehensive research paper.
Original Query: {query}
Summaries:
{sub_summaries}

Final Answer:
"""

def generate_response(state: dict) -> dict:
    #Combine the summarized results into one final answer.
    print("[Synthesis] Combining summarized results for final synthesis...")
    model = ChatOllama(model=MODEL)
    prompt = ChatPromptTemplate.from_template(generate_response_template)
    chain = prompt | model
    
    sub_summaries = "\n\n".join(state.get("summarized_results", []))
    print("[Synthesis] Aggregated summaries:\n", sub_summaries)
    result = chain.invoke({"query": state["query"], "sub_summaries": sub_summaries})
    # Clean the final response.
    final_response = result.content
    state["response"] = final_response
    print("[Synthesis] Final generated response:", final_response)
    return {"response": final_response}