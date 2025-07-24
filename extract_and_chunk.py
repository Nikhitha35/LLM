import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def extract_text_chunks(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.create_documents([text])
    return docs
