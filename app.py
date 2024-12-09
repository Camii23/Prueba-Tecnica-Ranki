from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Cargar datos desde el archivo JSON
try:
    with open('archivo_corregido.json', encoding='utf-8') as f:
        keywords_data = json.load(f)
except FileNotFoundError:
    print("Error: El archivo 'archivo_corregido.json' no fue encontrado.")
    keywords_data = []

# Función para procesar y filtrar los datos
def process_keywords(data):
    valid_keywords = []
    for item in data:
        try:
            # Extraer el volumen de búsqueda del nivel anidado
            search_volume = item.get('keyword_info', {}).get('search_volume')
            keyword = item.get('keyword')

            # Validar que ambos valores existan y sean correctos
            if search_volume is not None and isinstance(search_volume, (int, float)) and keyword:
                valid_keywords.append({
                    'keyword': keyword,
                    'search_volume': search_volume
                })
        except Exception as e:
            print(f"Error procesando el item: {item}. Detalle: {e}")

    return valid_keywords

# Procesar los datos al inicio
processed_keywords = process_keywords(keywords_data)

@app.route('/api/keywords', methods=['GET'])
def get_keywords():
    # Ordenar los datos por volumen de búsqueda en orden descendente
    sorted_keywords = sorted(processed_keywords, key=lambda x: x['search_volume'], reverse=True)
    return jsonify(sorted_keywords)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
