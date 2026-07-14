from src.config import Config
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from src.tools.tavily_search import tavily_search
from pydantic import SecretStr


# llm

llm = ChatGroq(
     api_key= SecretStr(Config.GROQ_API_KEY),
     model= Config.SEARCH_LLM,
     temperature= 0,
)

# agent

def create_search_llm():

     search_llm = create_agent(
          llm,
          tools= [tavily_search]
     )

     return search_llm
