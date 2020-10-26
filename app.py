from flask import Flask, request, jsonify
from flask_cors import CORS
from operacion import Operacion
from history import History

app = Flask(__name__)
CORS(app)
HISTORY = History()

@app.route("/")
def index():
    nombre = 'Bienvenido'
    return "<H1>" + nombre + "</H1>"

@app.route('/suma', methods=['POST'])
def suma():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        operation = Operacion(a, b , 'suma')
        result = operation.run()
        HISTORY.add(operation)
        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

@app.route('/resta', methods=['POST'])
def resta():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        operation = Operacion(a, b , 'resta')
        result = operation.run()
        HISTORY.add(operation)
        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        operation = Operacion(a, b , 'multiplicacion')
        result = operation.run()
        HISTORY.add(operation)
        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

@app.route('/division', methods=['POST'])
def division():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        operation = Operacion(a, b , 'division')
        result = operation.run()
        HISTORY.add(operation)
        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

@app.route('/raiz', methods=['POST'])
def raiz():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        operation = Operacion(a, b , 'raiz')
        result = operation.run()
        HISTORY.add(operation)
        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

@app.route('/potencia', methods=['POST'])
def potencia():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        operation = Operacion(a, b , 'potencia')
        result = operation.run()
        HISTORY.add(operation)
        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

@app.route('/historial', methods=['POST'])
def historial():
    if request.method == 'POST':
        print(HISTORY.get_history())
        return {
            "resultado": HISTORY.get_history()
        }

if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)

