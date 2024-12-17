from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# 1. Cargar archivo de texto
print("Cargando archivo de texto...")
loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()

# 2. Dividir texto
print("Dividiendo texto en fragmentos...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# 3. Crear embeddings con HuggingFace (modelo local)
print("Generando embeddings locales...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Crear base de datos vectorial con ChromaDB
db = Chroma.from_documents(texts, embeddings, persist_directory=os.path.expanduser("~/chroma_db"))
print("Base de datos vectorial creada y guardada.")

print("Verificando documentos en la base de datos...")
print(db.get())
