from datetime import datetime
import math

class Operacion:

    def __init__(self, parm_a, parm_b, operation_type):
        self.date = self.get_date()
        self.parm_a = int(parm_a)
        self.parm_b = int(parm_b)
        self.operation_type = operation_type
        self.result = "NO HAY RESULTADO"

    def get_date(self):
    	return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def dump(self):
        return {
            'fecha': self.date,
            'a': self.parm_a,
            'b': self.parm_b,
            'tipo': self.operation_type,
            'resultado': self.result
        }

    def run(self):
    	result = {'result': 'NO RESULTADO', 'message': 'NO MENSAJE'}

    	if self.operation_type == 'suma':
    		result['result'] = self.parm_a + self.parm_b
    		result['message'] = 'EXITO'

    	if self.operation_type == 'resta':
    		result['result'] = self.parm_a - self.parm_b
    		result['message'] = 'EXITO'

    	if self.operation_type == 'multiplicacion':
    		result['result'] = self.parm_a * self.parm_b
    		result['message'] = 'EXITO'

    	if self.operation_type == 'division':
          if(self.parm_b == 0): 
             result['message'] = 'ERROR SYNTAX'
            
          else:
             result['message'] = 'EXITO'
             result['result'] = self.parm_a / self.parm_b
        
    	if self.operation_type == 'raiz':
          if(self.parm_a == 0): 
             result['message'] = 'ERROR SYNTAX'
            
          else:
             result['message'] = 'EXITO'
             result['result'] =  pow((self.parm_b),(1/self.parm_a))
            
    	if self.operation_type == 'potencia':
          if(self.parm_b == 0): 
             result['message'] = 'EXITO'
             result['result'] = 1
            
          else:
             result['message'] = 'EXITO'
             result['result'] = pow(self.parm_a, self.parm_b)
    	self.result = result['result']
    	return result