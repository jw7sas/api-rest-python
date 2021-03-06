# imports
import socket

""" Clase Model, para el manejo del log de la app. """
class TransactionLogModel():
    def __init__(self, args, view, method, user_id):
        self.secuence_number = args["secuence_number"] if "secuence_number" in args.keys() else None 
        self.trx_date = args["trx_date"] if "trx_date" in args.keys() else None
        self.trx_time = args["trx_time"] if "trx_time" in args.keys() else None
        self.view = view
        self.method = method
        self.user_id = user_id
        self.ip_address = self.getIpAddress()

    def getIpAddress(self):
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return f"Ip: [{ip_address}] Hostname: [{host_name}]"


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
