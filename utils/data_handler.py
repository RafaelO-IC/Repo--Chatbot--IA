import os
import json
import ast

class DataFormatter:
    def __init__(self, source_folder: str, output_file: str):
        """
        Constructor de la clase. 
        Usamos doble guion bajo '__' para hacer los atributos PRIVADOS.
        Así aplicamos un encapsulamiento elevado.
        """
        self.__source_folder = source_folder
        self.__output_file = output_file
        self.__data = []  # Lista privada donde guardaremos los diccionarios

    def read_algorithms(self):
        """Método público para iniciar la lectura de los repositorios."""
        # Verificamos que la carpeta exista
        if not os.path.exists(self.__source_folder):
            print(f"Error: La carpeta {self.__source_folder} no existe.")
            return

        # Recorremos todos los archivos en la carpeta
        for filename in os.listdir(self.__source_folder):
            if filename.endswith(".py"):
                filepath = os.path.join(self.__source_folder, filename)
                # Llamamos a nuestro método privado para procesar el archivo
                self.__extract_info_from_file(filepath, filename)
                
        print(f"Archivos leídos y procesados en memoria de la carpeta: {self.__source_folder}")

    def __extract_info_from_file(self, filepath: str, filename: str):
        """
        Método PRIVADO (nota los dos guiones bajos). 
        Solo la misma clase puede usar este método para extraer los datos.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                source_code = file.read()

            # Convertimos el texto del archivo en un Árbol de Sintaxis Abstracta (AST)
            tree = ast.parse(source_code)

            # Buscamos todas las funciones dentro del archivo
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Armamos un diccionario con la info estructurada
                    function_info = {
                        "archivo_origen": filename,
                        "tipo": "funcion",
                        "nombre": node.name,
                        "descripcion": ast.get_docstring(node) or "Sin descripción proporcionada.",
                        "codigo_fuente": ast.get_source_segment(source_code, node)
                    }
                    self.__data.append(function_info)
                    
        except Exception as e:
            print(f"Error al procesar el archivo {filename}: {e}")

    def save_to_json(self):
        """Método público para exportar la información estructurada."""
        if not self.__data:
            print("No hay datos para guardar. ¿Ejecutaste read_algorithms() primero?")
            return

        try:
            # Aseguramos que la carpeta de destino exista (crea la carpeta 'data/' si no existe)
            os.makedirs(os.path.dirname(self.__output_file), exist_ok=True)
            
            with open(self.__output_file, 'w', encoding='utf-8') as file:
                # Usamos indent=4 para que el JSON sea legible para humanos
                json.dump(self.__data, file, indent=4, ensure_ascii=False)
            
            print(f"¡Éxito! Datos estructurados guardados cabrón en: {self.__output_file}")
        except Exception as e:
            print(f"Ocurrió un error al guardar el JSON: {e}")

# ==========================================
# BLOQUE DE PRUEBA 
# ==========================================
if __name__ == "__main__":
   
    
   
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
  
    carpeta_origen = os.path.join(directorio_actual, "..", "repositorios_fuente")
    archivo_destino = os.path.join(directorio_actual, "..", "data", "algoritmos_estructurados.json")
 
    formateador = DataFormatter(carpeta_origen, archivo_destino)
    formateador.read_algorithms()
    formateador.save_to_json()