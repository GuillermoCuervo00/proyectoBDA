from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
import os

# 1. Cargar la base de datos Chroma existente
print("Cargando la base de datos de Chroma...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=os.path.expanduser("~/chroma_db"), embedding_function=embeddings)

# 2. Configurar el modelo LLM con Ollama
print("Configurando el modelo de lenguaje Llama2...")
llm = OllamaLLM(model="llama2")  # Cambia a "tinyllama" si lo prefieres

# 3. Crear la cadena de preguntas y respuestas
print("Creando el sistema de preguntas y respuestas...")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

# 4. Función para interactuar con el sistema
def ask_question():
    print("\n¡Sistema RAG listo! Escribe tu pregunta (o 'exit' para salir):")
    while True:
        query = input("\nTu pregunta: ")
        if query.lower() == "exit":
            print("Saliendo del sistema...")
            break
        response = qa_chain.invoke({"query": query})
        print(f"Respuesta: {response}")

if __name__ == "__main__":
    ask_question()

