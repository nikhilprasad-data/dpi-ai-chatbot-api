from langchain_core.prompts import ChatPromptTemplate
from src.prompts import system_message, human_message
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from src.config import Config


# writer llm

writer_llm = ChatGoogleGenerativeAI(
     api_key= SecretStr(Config.GOOGLE_API_KEY),
     model= Config.READER_LLM,
     temperature= 0,
)


writer_prompt = ChatPromptTemplate.from_messages([
     ('system', system_message),
     ('human', human_message)
])

writer_chain = writer_prompt | writer_llm | StrOutputParser()
