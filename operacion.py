
class Operacion:

    def __init__(self, parm_a, parm_b, operation_type):
        self.date = self.get_date()
        self.parm_a = parm_a
        self.parm_b = parm_b
        self.operation_type = operation_type
        self.result = "NO HAY RESULTADO"

    def get_date(self):
    	return 'fecha'

    def dump(self):
        return {
            'fecha': self.date,
            'a': int(self.parm_a),
            'b': int(self.parm_b),
            'tipo': self.operation_type,
            'resultado': self.result
        }

    def run(self):
    	result = {'result': 'NO RESULTADO', 'message': 'NO MENSAJE'}

    	if self.operation_type == 'suma':
    		result['result'] = self.parm_a + self.parm_b
    		result['message'] = 'EXITO'

    	return result