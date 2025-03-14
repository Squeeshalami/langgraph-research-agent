# LangGraph Research Agent

A basic research assistant built with LangGraph that helps you find answers to complex questions by breaking them down, searching the web, and organizing the information.

## Overview

This project implements a multi-step research system using LangGraph, a framework for building stateful, multi-agent workflows.

The application is built with a Streamlit frontend for easy interaction.

## Features

- **Query Decomposition**: Breaks down complex questions into manageable subqueries
- **Web Search**: Uses Tavily Search API to find relevant information
- **Result Summarization**: Condenses search results into key insights
- **Response Generation**: Creates comprehensive answers based on the gathered information
- **Conversation History**: Maintains a record of your research session

## Architecture

The system is built using a LangGraph workflow with the following components:

- **StateGraph**: Manages the flow of information between agents
- **Agent Nodes**:
  - `decompose_query`: Breaks down the main query
  - `search_web`: Searches for information on each subquery
  - `summarize_results`: Condenses the search results
  - `generate_response`: Creates the final answer

## Requirements

- Python 3.8+
- Ollama (for local LLM inference)
- Tavily API key (for web search)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/langgraph-research-agent.git
   cd langgraph-research-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root (or modify the existing one)
   - Add your Tavily API key:
     ```
     TAVILY_API_KEY="your-tavily-api-key"
     ```

5. Install and run Ollama:
   - Follow the instructions at [ollama.ai](https://ollama.ai) to install Ollama
   - Pull the Gemma model:
     ```bash
     ollama pull gemma3:4b # Recommended Model for Fast Results
     ollama pull gemma3:12b # Recommended Model for Final Results
     ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter your research query in the text input field and click "Submit Query"

4. The agent will:
   - Break down your query
   - Search for information
   - Summarize the results
   - Generate a comprehensive response
   - Display sources used

5. Your conversation history will be maintained during the session

## Customization

### Changing the LLM

The default model is set to run `gemma3:4b`(summarization) and `gemma3:12b` (final response) locally using Ollama. To use a different model:

1. Open the node files in the `nodes/` directory
2. Change the `MODEL` variable to your preferred model

### Modifying the Search Provider

The application uses Tavily for web search by default. You can modify `nodes/search.py` to use different search providers.

## Troubleshooting

- **API Key Issues**: Ensure your Tavily API key is correctly set in the `.env` file
- **Ollama Connection**: Make sure Ollama is running and the specified model is available
- **Search Limitations**: Be aware that Tavily has usage limits on their free tier

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for the multi-agent framework
- [LangChain](https://github.com/langchain-ai/langchain) for LLM integration tools
- [Streamlit](https://streamlit.io/) for the web interface
- [Tavily](https://tavily.com/) for the search API
- [Ollama](https://ollama.ai/) for local LLM inference 