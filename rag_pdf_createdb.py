from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# 1. Cargar y procesar PDFs
def load_pdfs(pdf_paths):
    print("Cargando archivos PDF...")
    all_texts = []
    for pdf_path in pdf_paths:
        print(f"Procesando {pdf_path}...")
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        all_texts.extend(documents)
    return all_texts

# 2. Dividir los textos en fragmentos
def split_texts(documents):
    print("Dividiendo textos en fragmentos...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_documents(documents)

# 3. Crear base de datos vectorial en ChromaDB
def create_chroma_db(texts, persist_directory):
    print("Creando la base de datos vectorial en ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)
    print(f"Base de datos guardada en: {persist_directory}")
    return db

if __name__ == "__main__":
    # Rutas a los archivos PDF
    pdf_files = ["documento1.pdf", "documento2.pdf"]  # Coloca aquí los nombres de tus PDFs
    persist_directory = os.path.expanduser("~/chroma_pdf_db")  # Directorio donde se guardará ChromaDB

    # Ejecutar el flujo
    print("Iniciando el procesamiento de PDFs...")
    documents = load_pdfs(pdf_files)
    texts = split_texts(documents)
    db = create_chroma_db(texts, persist_directory)

    print("¡Base de datos vectorial creada con éxito!")
