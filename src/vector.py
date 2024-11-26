from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

def insert_chunks(chunks, embedding):
  Chroma.from_documents(chunks, embedding=embedding, persist_directory="storage/text_index")

def get_vector_db(embedding):
  return Chroma(persist_directory="storage/text_index", embedding_function=embedding)

def ask(question, llm, embedding):
  vector_db = get_vector_db(embedding)
  retriever = vector_db.as_retriever(search_kwargs={"k": 3})
  documents = retriever.invoke(question)

  chain = create_stuff_documents_chain(
    llm=llm, 
    prompt=ChatPromptTemplate.from_template("Summarize this content: {context}")
  )

  result = chain.invoke({"context": documents})

  return result, documents

