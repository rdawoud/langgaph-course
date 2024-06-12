#llm.py
import os
from dotenv import load_dotenv
load_dotenv()
# Set up OpenAI API key
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    openai_api_key = os.getenv("openai_api_key"),
    model = os.getenv("openai_model"),
    temperature = 0
)

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("openai_api_key"),

)
