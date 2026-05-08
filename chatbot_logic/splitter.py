# splitter.py
# Módulo encargado de dividir archivos de código en fragmentos más pequeños para facilitar su procesamiento.

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List


def dividir_codigo(
    documentos: List[Document],
    chunk_size: int = 500,
    chunk_overlap: int = 50
) -> List[Document]:

    """
    Divide documentos de código Python en fragmentos más pequeños
    para facilitar su procesamiento por el modelo de IA.

    Parámetros:
        documentos (List[Document]):
            Lista de documentos que contienen el código fuente.

        chunk_size (int):
            Tamaño máximo de cada fragmento (en caracteres).

        chunk_overlap (int):
            Número de caracteres compartidos entre fragmentos.

    Retorna:
        List[Document]:
            Lista de documentos divididos en fragmentos (chunks).

    """
        
    # Verificar que existan documentos
    if not documentos:

        print("No se recibieron documentos.")
        return []

    try:

        # Crear splitter especializado para Python
        splitter = RecursiveCharacterTextSplitter.from_language(
            language="python",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        # Dividir documentos
        documentos_divididos = splitter.split_documents(documentos)

        print(f"Se generaron {len(documentos_divididos)} fragmentos.")

        return documentos_divididos

    except Exception as e:

        print("Error al dividir documentos:")
        print(e)

        return []


# ======================================
# PRUEBA LOCAL
# ======================================

if __name__ == "__main__":

    # Código de ejemplo
    codigo_ejemplo = """
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

class Calculadora:

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):

        if b == 0:
            return "Error"

        return a / b
"""

    # Crear documento de prueba
    documento = Document(page_content=codigo_ejemplo)

    # Guardar en lista
    documentos = [documento]

    # Ejecutar función
    chunks = dividir_codigo(documentos)

    # Mostrar resultados
    print("\n===== FRAGMENTOS GENERADOS =====\n")

    for i, chunk in enumerate(chunks, start=1):

        print(f"--- Chunk {i} ---")
        print(chunk.page_content)
        print()