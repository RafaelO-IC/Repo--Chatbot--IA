from langchain.prompts import PromptTemplate

# String multilínea con las variables {context} y {question}
template = """
Eres un asistente experto en análisis de algoritmos y código.
Utiliza ÚNICAMENTE el siguiente código como fuente de información para responder.
Si la respuesta no se encuentra en el código proporcionado, indica que no tienes
suficiente información en el contexto dado.

=== CÓDIGO PROPORCIONADO ===
{context}
===========================

Pregunta del usuario: {question}

Respuesta (basada exclusivamente en el código anterior):

"""

# Crear el objeto PromptTemplate con las variables declaradas
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)