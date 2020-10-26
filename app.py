from flask import Flask, request, jsonify
from flask_cors import CORS
from operacion import Operacion


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    nombre = 'Bienvenido'
    return "<H1>" + nombre + "</H1>"

@app.route('/suma', methods=['POST'])
def suma():
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')

        suma = Operacion(a, b , 'suma')
        result = suma.run()

        return {
            "resultado": result['result'],
            "mensaje": result['message']
        }

if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)

