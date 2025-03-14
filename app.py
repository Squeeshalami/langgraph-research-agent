import streamlit as st
from graph import build_graph

st.title("Research Agent")

# Initialize session state variables if not already set.
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []  # List of messages with role and content.
if 'conversation_state' not in st.session_state:
    st.session_state.conversation_state = {}

# New query submission form at the top.
with st.form(key="new_query_form", clear_on_submit=True):
    new_query = st.text_input("Enter your query")
    submitted = st.form_submit_button("Submit Query")
    
    if submitted and new_query:
        # Append the user's query to the conversation history.
        st.session_state.conversation_history.append({"role": "user", "content": new_query})
        with st.spinner("Processing your query..."):
            pass
        
        # Process the query using the multi-agent graph.
        graph = build_graph()
        result = graph.invoke({"query": new_query})
        response = result.get("response", "")
        
        # Append the assistant's response.
        st.session_state.conversation_history.append({"role": "assistant", "content": response})
        
        # Optionally, append sources if available.
        if result.get("sources"):
            sources_text = "\n".join([f"* {source}" for source in result.get("sources", [])])
            st.session_state.conversation_history.append(
                {"role": "assistant", "content": f"**Sources:**\n{sources_text}"}
            )

# Display conversation history after processing the form.
st.markdown("---")
st.header("Conversation History")
for msg in st.session_state.conversation_history:
    if msg["role"] == "user":
        st.markdown(f"**User:** {msg['content']}")
    else:
        st.markdown(f"**Assistant:** {msg['content']}")
