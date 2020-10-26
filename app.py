from flask import Flask, request, jsonify
from flask_cors import CORS
from operacion import operacion
HISTORY = []

app = Flask(__name__)
CORS(app)

def mis_datos():
	return {"carne": 201801510, "nombre": "Edgar Antonio Guzman Martinez"}

def invert_string(string=""):
	return string[::-1]

@app.route("/")
def index():
	nombre = 'Bienvenido'
	return "<H1>" + nombre + "</H1>"

@app.route('/suma', methods=['POST'])
def suma():
	if request.method == 'POST':
        type = 'suma'
		a = request.form.get('a')
        b = request.form.get('b')

		suma = new operacion()
		return {
			"resultado": new_string
		}

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)

