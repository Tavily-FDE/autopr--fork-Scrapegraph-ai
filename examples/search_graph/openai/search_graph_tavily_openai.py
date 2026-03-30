"""
Example of Search Graph using Tavily as the search engine.

Requires the TAVILY_API_KEY environment variable to be set (e.g. in a .env
file).  Authentication is handled automatically by TavilyClient via this
env var; there is no separate config key for the Tavily API key.
"""

import os

from dotenv import load_dotenv

from scrapegraphai.graphs import SearchGraph

load_dotenv()

# ************************************************
# Define the configuration for the graph
# ************************************************

openai_key = os.getenv("OPENAI_API_KEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "openai/gpt-4o",
    },
    "search_engine": "tavily",
    "max_results": 2,
    "verbose": True,
}

# ************************************************
# Create the SearchGraph instance and run it
# ************************************************

search_graph = SearchGraph(
    prompt="List me Chioggia's famous dishes", config=graph_config
)

result = search_graph.run()
print(result)
