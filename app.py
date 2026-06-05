from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta base para verificar que la aplicación funciona en el pipeline
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "online",
        "message": "Calculadora API ejecutándose con éxito"
    }), 200

# Ruta para realizar las operaciones de la calculadora
@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.get_json()
    
    # Validar que los datos existan
    if not datos or 'num1' not in datos or 'num2' not in datos or 'operacion' not in datos:
        return jsonify({"error": "Faltan parámetros requeridos: num1, num2 u operacion"}), 400

    try:
        num1 = float(datos['num1'])
        num2 = float(datos['num2'])
        operacion = datos['operacion'].lower()
    except ValueError:
        return jsonify({"error": "Los valores de num1 y num2 deben ser números"}), 400

    # Procesar la operación seleccionada
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        if num2 == 0:
            return jsonify({"error": "No se puede dividir entre cero"}), 400
        resultado = num1 / num2
    else:
        return jsonify({"error": "Operación no válida. Usa: suma, resta, multiplicacion o division"}), 400

    return jsonify({
        "num1": num1,
        "num2": num2,
        "operacion": operacion,
        "resultado": resultado
    }), 200

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000 configurado en tu workflow
    app.run(host='0.0.0.0', port=5000, debug=True)
