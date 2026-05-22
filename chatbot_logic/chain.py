import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv

# Importaciones de tus archivos locales
from prompt_template import prompt_template
<<<<<<< HEAD

# 1. Configuración de API Key
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise RuntimeError(
        "Falta GOOGLE_API_KEY. Crea un archivo .env con tu clave de Google Gemini."
    )

os.environ["GOOGLE_API_KEY"] = google_api_key
=======
from retriever import buscar_fragmentos_relevantes
>>>>>>> 61065101412f2d992c48f251e1b78c51097e1ae6

# 2. Inicialización del LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0.1,
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
    
    print(f"\n--- CONSULTANDO A MiniRodri ---")
    try:
        respuesta = chain.invoke(pregunta)
        print(f"\nRespuesta:\n{respuesta}")
    except Exception as e:
        print(f"\nError en la comunicación: {e}")