""" Clase model, para devolver respuesta de errores. """
class ResponseModel():

    def __init__(self, args):
        self.response = args["response"]
        self.error = args["error"]
    
    def getResponseBasic(self):
        """ Método para retorno de respuesta básica. | methods: [create, update, delete] """
        if self.error is False:
            return {
                "error": None,
                "errorMessage": None,
                "responseCode": "OK",
                "responseMessage": str(self.response),
                "sequenceNumber": None
            }
        else:
            return {
                "error": True,
                "errorMessage": str(self.response),
                "responseCode": "ERR99",
                "responseMessage": None,
                "sequenceNumber": None
            }
        
    def getResponseResults(self):
        """ Método para retornar resultados JSON. | methods: [selectAll] """
        if self.error is False:
            return {
                'info': {
                    'count': None
                },
                'results': self.response
            }
        else:
            return self.getResponseBasic()

    def getResponseOneResult(self):
        """ Método para retornar un solo resultado JSON. | methods: [selectByPK] """
        if self.error is False:
            return self.response
        else:
            return self.getResponseBasic()
