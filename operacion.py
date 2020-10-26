class Pokemon:

    def __init__(self, parm_a, parm_b, operation_type):
        self.date = self.get_date()
        self.parm_a = parm_a
        self.parm_b = parm_b
        self.operation_type = operation_type


    def get_date(self):
    	return 'fecha'

    def dump(self):

        return {

            'date': self.date,

        }

     def run(self):
     	if self.operation_type == 'suma':
     		return a * b,  'Satisfactorio'