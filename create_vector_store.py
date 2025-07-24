from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from extract_and_chunk import extract_text_chunks  
import os  # ✅ Add this to the top

def create_vector_store(pdf_path, index_path="vector_index"):
    print("🔍 Extracting chunks...")

    # ✅ Add this debug line
    print(f"🔎 Looking for PDF at: {os.path.abspath(pdf_path)}")

    chunks = extract_text_chunks(pdf_path)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)
    print("✅ Vector store created.")

if __name__ == "__main__":
    create_vector_store("data/BAJHLIP23020V012223.pdf")  # ✅ run from root folder
