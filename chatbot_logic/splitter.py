# splitter.py
# Divide archivos de código en fragmentos manejables

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List


def dividir_codigo(documentos: List[Document]) -> List[Document]:
    """
    Divide una lista de documentos en fragmentos más pequeños (chunks)
    manteniendo la estructura del código.

    :param documentos: Lista de documentos con código fuente
    :return: Lista de documentos fragmentados
    """

    try:
        # Configuración del splitter específica para Python
        splitter = RecursiveCharacterTextSplitter.from_language(
            language="python",
            chunk_size=500,       # tamaño máximo del fragmento
            chunk_overlap=50      # traslape entre fragmentos
        )

        # Dividir documentos
        documentos_divididos = splitter.split_documents(documentos)

        return documentos_divididos

    except Exception as e:
        print("Error al dividir documentos:", e)
        return []


# ============== PRUEBA LOCAL ==============

if __name__ == "__main__":
    # Simulación de documento de código
    codigo_ejemplo = """
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

class Calculadora:
    def multiplicar(self, a, b):
        return a * b
"""

    documentos = [Document(page_content=codigo_ejemplo)]

    chunks = dividir_codigo(documentos)

    print("Fragmentos generados:\n")

    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk.page_content)
        print()