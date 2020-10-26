from . import operacion
import json

class history:

	def __init__(self):
		self.history = []

	def get_history(self):
		return json.dumps([operacion.dump() for operacion in self.history])