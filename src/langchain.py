from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf_chunks(file_name: str):
  loader = PyPDFLoader(f"storage/{file_name}.pdf", extract_images=False)
  pages = loader.load_and_split()

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 4000,
    chunk_overlap = 20,
    length_function = len,
    add_start_index = True
  )

  return text_splitter.split_documents(pages)
