import os
from dotenv import load_dotenv

from langchain_core. messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, END

from nodes import run_agent_reasoning, tool_node

load_dotenv()

AGENT_REASON="agent_reasoning"
ACT="act"
LAST = -1

def should_continue(state: MessagesState) -> bool:
    if not state["messages"][LAST].tool_calls:
        return False
    return True

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)   

flow.add_conditional_edges(AGENT_REASON, should_continue, {
    True: ACT,
    False: END})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")

def main():
    print("Hello from langgraph-first!")
    # print(os.getenv("OPENAI_API_KEY"))
    

if __name__ == "__main__":
    main()
