from src.vector import ask
from src.env import load_dotenv
from src.llm import create_llm_model
from src.embedding import create_embedding_model

load_dotenv()

llm = create_llm_model()
embedding = create_embedding_model()

result, context = ask(
  llm=llm, 
  embedding=embedding, 
  question="Como a PEC de numero 42 impacta os militares?"
)

print(result)
