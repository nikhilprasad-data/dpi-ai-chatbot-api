from src.config import Config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from src.tools.url_scraper import url_scrapper
from pydantic import SecretStr


# llm

llm = ChatGoogleGenerativeAI(
     api_key= SecretStr(Config.GOOGLE_API_KEY),
     model= Config.READER_LLM,
     temperature= 0,
)

# agent

def create_reader_llm():

     reader_llm = create_agent(
          llm,
          tools= [url_scrapper]
     )

     return reader_llm
