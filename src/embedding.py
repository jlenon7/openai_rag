from os import environ
from langchain_openai import OpenAIEmbeddings

def create_embedding_model():
  return OpenAIEmbeddings(
    api_key=environ.get("OPENAI_API_KEY")
  )
