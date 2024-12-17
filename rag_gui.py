import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
import os

# 1. Cargar la base de datos vectorial
print("Cargando la base de datos de Chroma...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=os.path.expanduser("~/chroma_db"), embedding_function=embeddings)

# 2. Configurar el modelo LLM con Ollama
print("Configurando el modelo de lenguaje TinyLlama...")
llm = OllamaLLM(model="tinyllama")

# 3. Crear la cadena RAG
print("Creando el sistema de preguntas y respuestas...")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

# 4. Función para responder preguntas
def query_rag(question):
    response = qa_chain.invoke({"query": question})
    return response

# 5. Configurar la interfaz Gradio
interface = gr.Interface(
    fn=query_rag,
    inputs="text",
    outputs="text",
    title="Sistema RAG con TinyLlama y ChromaDB",
    description="Escribe una pregunta relacionada con tu base de datos y obtén una respuesta."
)

# 6. Lanzar la aplicación
if __name__ == "__main__":
    interface.launch()
