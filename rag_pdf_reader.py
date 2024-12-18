from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
import os

# 1. Cargar la base de datos vectorial
print("Cargando la base de datos de PDFs desde ChromaDB...")
persist_directory = os.path.expanduser("~/chroma_pdf_db")  # Ruta donde se guardó la base de datos
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# 2. Configurar el modelo de lenguaje con Ollama
print("Iniciando el modelo LLM TinyLlama...")
llm = OllamaLLM(model="tinyllama")  # Usa "llama2" si prefieres un modelo más grande

# 3. Crear la cadena RAG (búsqueda y generación)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

# 4. Función para realizar consultas
def ask_question():
    print("\n¡Sistema RAG listo! Escribe tu pregunta (o 'exit' para salir):")
    while True:
        query = input("Tu pregunta: ")
        if query.lower() == "exit":
            print("Saliendo del sistema...")
            break
        response = qa_chain.invoke({"query": query})
        print(f"Respuesta: {response}")

if __name__ == "__main__":
    ask_question()
