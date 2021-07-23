from users.models import ClientModel
from products.models import ProductModel

""" Clase del modelo tipo de pago. """
class TypePaymentModel():

    def __init__(self, type_of_payment):
        if(type_of_payment):
            self.name = type_of_payment["name"]
            self.other_details = type_of_payment["other_details"] if "other_details" in type_of_payment.keys() else None

""" Clase del modelo factura. """
class InvoiceModel():

    def __init__(self, invoice):
        if(invoice):
            self.client_id = invoice["client_id"]
            self.type_of_payment_id = invoice["type_of_payment_id"]
            self.code = None
    
    def setCode(self, code):
        self.code = code

""" Clase del modelo detalle de factura. """
class InvoiceDetailModel():

    def __init__(self, invoice_detail):
        if(invoice_detail):
            self.invoice_id = invoice_detail["invoice_id"]
            self.product_id = invoice_detail["product_id"]
            self.units = invoice_detail["units"]
            self.price = invoice_detail["price"]