import os
import shutil
import subprocess
import sys

def preparar_entorno():
    print("Iniciando configuración del entorno para el Chatbot...")
    
    # 1. Configuración de Variables de Entorno
    env_file = ".env"
    env_example = ".env.example"
    
    if not os.path.exists(env_file):
        if os.path.exists(env_example):
            shutil.copy(env_example, env_file)
            print(f"✅ Se creó el archivo {env_file} a partir de la plantilla.")
            print("   -> ¡IMPORTANTE! Abre el archivo .env y coloca tus API Keys reales.")
        else:
            print(f"⚠️ No se encontró la plantilla {env_example}. Crea tu .env manualmente.")
    else:
        print(f"✅ El archivo {env_file} ya existe. Saltando paso.")

    # 2. Instalación de dependencias (requirements.txt)
    req_file = "requirements.txt"
    
    if os.path.exists(req_file):
        print(f"\n📦 Instalando dependencias de {req_file}...")
        try:
            # Esto ejecuta 'pip install -r requirements.txt' directo en la terminal
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
            print("✅ Dependencias instaladas correctamente.")
        except subprocess.CalledProcessError:
            print("❌ Ocurrió un error al instalar las dependencias. Revisa tu consola.")
    else:
        print(f"⚠️ No se encontró el archivo {req_file}. No se instalaron librerías.")

if __name__ == "__main__":
    preparar_entorno()