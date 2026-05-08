from langchain_huggingface import HuggingFaceEmbeddings
from typing import List


def crear_modelo_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def generar_embeddings(textos: List[str]) -> List[List[float]]:
    if not textos:
        return []

    try:
        modelo = crear_modelo_embeddings()
        vectores = modelo.embed_documents(textos)

        print(f"Se generaron {len(vectores)} embeddings.")

        return vectores

    except Exception as e:
        print("Error al generar embeddings:")
        print(e)
        return []


if __name__ == "__main__":

    textos_prueba = [
        "def suma(a, b): return a + b",
        "def resta(a, b): return a - b"
    ]

    embeddings = generar_embeddings(textos_prueba)

    print("Cantidad de vectores:", len(embeddings))

    if embeddings:
        print("Dimensión del primer vector:", len(embeddings[0]))