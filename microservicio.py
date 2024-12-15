from flask import Flask, jsonify, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Rutas de ejemplo
@app.route('/api/saludo', methods=['GET'])
def saludo():
    """Servicio que devuelve un saludo."""
    return jsonify({"mensaje": "¡Hola, bienvenido al microservicio!"})

@app.route('/api/suma', methods=['POST'])
def suma():
    """Servicio que calcula la suma de dos números."""
    try:
        datos = request.get_json()
        numero1 = datos.get('numero1')
        numero2 = datos.get('numero2')
        if numero1 is None or numero2 is None:
            return jsonify({"error": "Por favor, proporciona 'numero1' y 'numero2'."}), 400
        resultado = numero1 + numero2
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

@app.route('/api/multiplicacion', methods=['POST'])
def multiplicacion():
    """Servicio que calcula el producto de dos números."""
    datos = request.get_json()
    numero1 = datos.get('numero1')
    numero2 = datos.get('numero2')
    if numero1 is None or numero2 is None:
        return jsonify({"error": "Por favor, proporciona 'numero1' y 'numero2'."}), 400
    resultado = numero1 * numero2
    return jsonify({"resultado": resultado})

# Ruta para manejar errores 404
@app.errorhandler(404)
def pagina_no_encontrada(e):
    """Manejo de rutas no encontradas."""
    return jsonify({"error": "Recurso no encontrado."}), 404

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
