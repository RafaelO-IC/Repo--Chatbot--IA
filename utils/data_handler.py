import os
import json

class DataFormatter:
    def __init__(self, source_folder, output_file):
        # Atributos privados para un buen encapsulamiento
        self.__source_folder = source_folder
        self.__output_file = output_file
        self.__data = [] # Aquí guardaremos la información estructurada

    def read_algorithms(self):
        # Aquí irá la lógica para recorrer las carpetas, 
        # abrir los archivos .py del otro repo y extraer el código.
        pass

    def save_to_json(self):
        # Convertimos nuestra lista de datos a un archivo JSON estructurado
        try:
            with open(self.__output_file, 'w', encoding='utf-8') as file:
                json.dump(self.__data, file, indent=4, ensure_ascii=False)
            print(f"¡Éxito! Datos guardados en {self.__output_file}")
        except Exception as e:
            print(f"Ocurrió un error al guardar el JSON: {e}")