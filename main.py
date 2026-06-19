from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

from langchain_tavily import TavilySearch

# tavily = TavilyClient()  # Initialize the Tavily client

# @tool
# def search(query: str) -> str:
#     """
#     Toll that searches over internet
#     Args:
#         query (str): The search query
#     Returns:
#         str: The search results
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)  # Use the Tavily client to perform the search"


llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from udemy-class!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather like in Tokyo?")})
    print(result)




if __name__ == "__main__":
    main()
