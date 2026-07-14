from .writer_chain import writer_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompts import critic_human_message, critic_system_message
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from pydantic import SecretStr
from src.config import Config


critic_llm = ChatGroq(
     api_key= SecretStr(Config.GROQ_API_KEY),
     model= Config.SEARCH_LLM,
     temperature= 0,
)

critic_prompt = ChatPromptTemplate.from_messages([
     ('system' , critic_system_message),
     ('human', critic_human_message)
])

critic_chain = critic_prompt | critic_llm | StrOutputParser()
