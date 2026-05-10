from chain import chain


def mostrar_bienvenida():
    print("=" * 60)
    print("MiniRodri - Chatbot IA de EDA2")
    print("Sistema RAG para consultas sobre algoritmos y código")
    print("=" * 60)
    print("Pregunta sobre estructuras de datos y algoritmos.")
    print("Para salir escribe: salir, exit o q")
    print()


def iniciar_chat():
    mostrar_bienvenida()

    while True:

        pregunta = input("Tú: ").strip()

        # Comandos para salir
        if pregunta.lower() in ["salir", "exit", "q"]:
            print("\nMiniRodri finalizado.")
            break

        # Evitar preguntas vacías
        if not pregunta:
            print("Por favor, escribe una pregunta.\n")
            continue

        try:
            print("\nMiniRodri: Procesando consulta...\n")


            respuesta = chain.invoke(pregunta)


            print("MiniRodri:")
            print(respuesta)
            print()


        except Exception as error:
            print("Ocurrió un error al procesar la consulta.")
            print(f"Detalle: {error}")
            print()




if __name__ == "__main__":
    iniciar_chat()

