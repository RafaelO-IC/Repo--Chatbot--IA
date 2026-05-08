import os
import logging
from langchain_community.document_loaders import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_community.document_loaders.parsers.language import Language

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cargar_repositorio_python(ruta_repo: str):
    """
    Tarea 1: Carga y parseo de código fuente Python.
    Recorre un repositorio, carga archivos .py e ignora carpetas no relevantes.
    """
    if not os.path.isdir(ruta_repo):
        logger.error(f"La ruta '{ruta_repo}' no existe o no es un directorio.")
        return []

    try:
        loader = GenericLoader.from_path(
            ruta_repo,
            glob="**/*.py",
            exclude=[
                "**/.git/**",
                "**/__pycache__/**",
                "**/venv/**",
                "**/env/**",
                "**/node_modules/**",
                "**/.ipynb_checkpoints/**",
                "**/tests/**"
            ],
            parser=LanguageParser(
                language=Language.PYTHON,
                parser_threshold=500
            )
        )

        documentos = loader.load()
        logger.info(f"Éxito: {len(documentos)} documentos/fragmentos cargados.")
        return documentos

    except Exception as e:
        logger.exception("Error durante la carga del repositorio")
        return []