import re
import json

def corregir_json(archivo_entrada, archivo_salida):
    try:
        # Leer el archivo original
        with open(archivo_entrada, "r", encoding="utf-8") as file:
            contenido = file.read()
        
        # Eliminar caracteres innecesarios o inválidos (opcional según sea necesario)
        contenido = re.sub(r"\s+", " ", contenido)  # Reducir espacios en blanco
        
        # Paso 1: Agregar comas faltantes entre objetos
        contenido = re.sub(r"}\s*{", "},\n{", contenido)  # Asegura comas entre objetos
        
        # Paso 2: Verificar y envolver en un array si es necesario
        if not contenido.strip().startswith("["):
            contenido = f"[{contenido.strip()}]"
        
        # Validar el JSON resultante
        try:
            datos = json.loads(contenido)  # Validar el formato JSON
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al validar el JSON corregido: {e}")
        
        # Paso 3: Escribir el archivo corregido
        with open(archivo_salida, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
        
        print(f"Archivo JSON corregido y guardado en: {archivo_salida}")
    
    except Exception as e:
        print(f"Error al procesar el archivo JSON: {e}")


archivo_entrada = "data.json"
archivo_salida = "archivo_corregido.json"
corregir_json(archivo_entrada, archivo_salida)
