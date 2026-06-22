from dotenv import load_dotenv

load_dotenv()


from pydantic import BaseModel, Field

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


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for the agent's response"""

    answer: str = Field(description="The answer provided by the agent")
    sources: list[Source] = Field(description="A list of sources used to generate the answer")

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from udemy-class!")
    result = agent.invoke({"messages": HumanMessage(content="Top three firmware/embedded software engieer job in NYC area on linkedin?")})
    print(result)




if __name__ == "__main__":
    main()
