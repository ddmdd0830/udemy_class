from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


load_dotenv()  # Load environment variables from .env file

@tool
def triple(num:float) -> float:
    """Returns the triple of the input number."""
    return float(num) * 3

tools = [triple, TavilySearch(max_results=1)]

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0).bind_tools(tools)


