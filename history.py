from operacion import Operacion
import json

class History:

	def __init__(self):
		self.history = []

	def add(self, operacion):
		self.history.append(operacion)

	def get_history(self):
		return json.dumps([operacion.dump() for operacion in self.history])