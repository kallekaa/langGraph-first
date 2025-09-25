from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num: float) -> float:
    """The function Triples a float number.
    pram num: float: A float number to be tripled.
    return: float: The tripled float number.
    """
    return float(num) * 3

tools = [triple, TavilySearch(max_results=1)]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)

response = llm.invoke("What is triple 5.5?")

print(response)

