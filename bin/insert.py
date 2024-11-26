from src.env import load_dotenv
from src.vector import insert_chunks
from src.langchain import load_pdf_chunks
from src.embedding import create_embedding_model

load_dotenv()

insert_chunks(
  embedding=create_embedding_model(),
  chunks=load_pdf_chunks("pec_42_2023")
)
