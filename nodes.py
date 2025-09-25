from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful AI assistant that helps people with their questions.
You have access to tools.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """Runs the agent reasoning step."""

    # if state.messages[-1].content == "stop":
    #     return state.add_message("Agent stopped.")
    response = llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])

    return {"messages": [response]}

tool_node = ToolNode(tools)
