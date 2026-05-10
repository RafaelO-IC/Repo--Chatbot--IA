import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

# Importaciones de tus archivos locales
from retriever import buscar_fragmentos_relevantes
from prompt_template import prompt_template

# 1. Configuración de API Key
# Usamos solo la estándar de LangChain
os.environ["GOOGLE_API_KEY"] = "AIzaSyDArvCYNqgSH8pzbwmV1q65Lr_tSQL_Zuw"

# 2. Inicialización del LLM
# Usamos el modelo que la documentación te sugirió y que ya validamos
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", 
    temperature=0,
    client_options={"api_endpoint": "https://generativelanguage.googleapis.com"}
)

# 3. Formateo de fragmentos recuperados
def format_docs(docs):
    if not docs:
        return "No se encontró información en la base de datos para esta consulta."
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

# 4. TAREA 7: Construcción de la Cadena (RAG Chain)
chain = (
    {
        "context": RunnableLambda(lambda x: buscar_fragmentos_relevantes(x)) | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt_template 
    | llm 
    | StrOutputParser()
)

# 5. Ejecución de prueba
if __name__ == "__main__":
    pregunta = "¿Qué operaciones puede realizar la clase Calculadora que está en el código?"
    
    print(f"\n--- CONSULTANDO A {llm.model} ---")
    try:
        respuesta = chain.invoke(pregunta)
        print(f"\nRespuesta:\n{respuesta}")
    except Exception as e:
        print(f"\nError en la comunicación: {e}")