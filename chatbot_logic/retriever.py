# retriever.py
# Tarea 5: Función de Búsqueda por Similitud
# Recibe una pregunta en lenguaje natural y retorna los fragmentos
# de código más relevantes desde el almacén vectorial ChromaDB.
 
import os
from langchain_core.documents import Document
from typing import List
from vector_store import cargar_almacen_vectorial
 
 
def buscar_fragmentos_relevantes(query: str, k: int = 3, persist_directory: str = "./db") -> List[Document]:
    """
    Convierte una pregunta en lenguaje natural a vector y recupera
    los k fragmentos de código más similares desde ChromaDB.
 
    Parámetros:
        query (str):
            Pregunta o descripción en lenguaje natural del usuario.
 
        k (int):
            Número de fragmentos relevantes a retornar. Por defecto: 3.
 
        persist_directory (str):
            Ruta de la carpeta donde está guardada la base de datos vectorial.
            Por defecto: "./db"
 
    Retorna:
        List[Document]:
            Lista de fragmentos de código más relevantes para la consulta.
            Lista vacía si ocurre algún error.
    """
 
    if persist_directory is None or persist_directory == "./db":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        persist_directory = os.path.join(base_dir, "db")
        
    if not query or not query.strip():
        print("La consulta no puede estar vacía.")
        return []
 
    try:
 
        # Cargar el almacén vectorial desde disco
        vector_store = cargar_almacen_vectorial(persist_directory)
 
        if vector_store is None:
            print("No se pudo cargar el almacén vectorial.")
            return []
 
        # Buscar los k fragmentos más similares a la consulta
        resultados = vector_store.similarity_search(query, k=k)
 
        print(f"Se encontraron {len(resultados)} fragmentos relevantes para: '{query}'")
 
        return resultados
 
    except Exception as e:
        print("Error durante la búsqueda por similitud:")
        print(e)
        return []