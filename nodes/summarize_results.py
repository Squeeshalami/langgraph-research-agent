from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

MODEL = "gemma3:4b" ## Smaller Model for faster results

summary_template = """
Summarize the following content into a concise, yet detailed report that directly addresses the subquery.
Subquery: {subquery}
Content: {content}
"""

def summarize_results(state: dict) -> dict:
    print("[Summarization] Starting summarization of web results...")
    model = ChatOllama(model=MODEL)
    prompt = ChatPromptTemplate.from_template(summary_template)
    chain = prompt | model
    
    summarized_results = []
    for idx, content in enumerate(state.get("web_results", []), start=1):
        print(f"[Summarization] Summarizing result {idx}/{len(state.get('web_results', []))}")
        summary = chain.invoke({"subquery": state["query"], "content": content})
        # Clean each summary before appending.
        clean_summary = summary.content
        summarized_results.append(clean_summary)
        print(f"[Summarization] Summary {idx}: {clean_summary}")
    
    state["summarized_results"] = summarized_results
    print("[Summarization] Completed summarization for all results.")
    return {"summarized_results": summarized_results}
