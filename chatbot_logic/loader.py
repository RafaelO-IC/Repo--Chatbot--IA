import os
import logging
import requests
import tempfile
import shutil
import subprocess
from langchain_community.document_loaders import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_community.document_loaders.parsers.language import Language

logging.basicConfig(level=logging.INFO)
# CORRECCIÓN 1: Llevaba doble guion bajo en __name__
logger = logging.getLogger(__name__) 

BACKEND_REPO_URL = "https://github.com/FranciscoCou077/Proyecto-EDAII-Backend.git"

def cargar_repositorio_python(ruta_repo: str = None):
    # Lógica estructural: Si hay ruta local, la usa. Si no (en Render), clona de internet.
    if ruta_repo and os.path.isdir(ruta_repo):
        repo_path = ruta_repo
        temp_dir = None
    else:
        temp_dir = tempfile.mkdtemp()
        logger.info(f"Clonando repo backend en {temp_dir}...")
        subprocess.run(
            ["git", "clone", "--depth=1", BACKEND_REPO_URL, temp_dir],
            check=True
        )
        repo_path = os.path.join(temp_dir, "app", "algoritmos")

    try:
        loader = GenericLoader.from_path(
            repo_path,
            # CORRECCIÓN 2: El glob necesita doble asterisco para buscar en subcarpetas
            glob="**/*.py", 
            exclude=[
                "**/.git/**",
                # CORRECCIÓN 3: __pycache__ lleva dobles guiones bajos
                "**/__pycache__/**", 
                "**/venv/**",
            ],
            parser=LanguageParser(
                language=Language.PYTHON,
                parser_threshold=500
            )
        )
        documentos = loader.load()
        logger.info(f"Éxito: {len(documentos)} documentos cargados.")
        return documentos
        
    except Exception as e:
        logger.exception("Error durante la carga del repositorio")
        return []
        
    finally:
        # Excelente práctica: Limpiar el espacio de memoria temporal del servidor
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
