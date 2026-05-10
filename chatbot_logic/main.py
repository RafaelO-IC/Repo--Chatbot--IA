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

        aqui pega tu parte Nour, en esta linea