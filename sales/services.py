# imports
from app.base_service import BaseService
from app.models import ResponseModel
from app import tables as t, properties as p

""" Clase de servicio de tipos de pago, hacia la base de datos. """ 
class TypePaymentService(BaseService):
    def __init__(self):
        super().__init__()

    def create(self, type_payment):
        query = f"INSERT INTO {t.TTYPEPAYMENT} ({t.TTYPEPAYMENT_NAME}, {t.TTYPEPAYMENT_OTHER_DETAILS}) values (?,?)"
        params = [type_payment.name, type_payment.other_details]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, type_payment, type_payment_id):
        query = f"UPDATE {t.TTYPEPAYMENT} SET {t.TTYPEPAYMENT_NAME} = ?, {t.TTYPEPAYMENT_OTHER_DETAILS} = ? WHERE {t.TTYPEPAYMENT_ID} = ?"
        params = [type_payment.name, type_payment.other_details, type_payment_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def delete(self, type_payment_id):
        query = f"DELETE FROM {t.TTYPEPAYMENT} WHERE {t.TTYPEPAYMENT_ID} = ?"
        params = [type_payment_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def selectAll(self):
        query = f"SELECT * FROM {t.TTYPEPAYMENT}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, type_payment_id):
        query = f"SELECT * FROM {t.TTYPEPAYMENT} WHERE {t.TTYPEPAYMENT_ID} = ?"
        response = self.executeQueryOne(query, [type_payment_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()


""" Clase de servicio de facturas, hacia la base de datos. """
class InvoiceService(BaseService):
    def __init__(self):
        super().__init__()

    def create(self, invoice):
        query = f"INSERT INTO {t.TINVOICE} ({t.TINVOICE_CODE}, {t.TINVOICE_CLIENT_ID}, {t.TINVOICE_TYPE_OF_PAYMENT_ID}) values (?,?,?)"
        params = [invoice.code, invoice.client_id, invoice.type_of_payment_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, invoice, invoice_id):
        query = f"UPDATE {t.TINVOICE} SET {t.TINVOICE_CLIENT_ID}=?, {t.TINVOICE_TYPE_OF_PAYMENT_ID}=? WHERE {t.TINVOICE_ID} = ?"
        params = [invoice.client_id, invoice.type_of_payment_id, invoice_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def delete(self, invoice_id):
        query = f"DELETE FROM {t.TINVOICE} WHERE {t.TINVOICE_ID} = ?"
        params = [invoice_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def selectAll(self):
        query = f"SELECT * FROM {t.TINVOICE}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, invoice_id):
        query = f"SELECT * FROM {t.TINVOICE} WHERE {t.TINVOICE_ID} = ?"
        response = self.executeQueryOne(query, [invoice_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()


""" Clase de detalle de factura, hacia la base de datos. """
class InvoiceDetailService(BaseService):
    def __init__(self):
        super().__init__()

    def create(self, invoice_detail):
        query = f"INSERT INTO {t.TINVOICEDETAIL} ({t.TINVOICEDETAIL_INVOICE_ID}, {t.TINVOICEDETAIL_PRODUCT_ID}, {t.TINVOICEDETAIL_UNITS}, {t.TINVOICEDETAIL_PRICE}) values (?,?,?,?)"
        params = [invoice_detail.invoice_id, invoice_detail.product_id, invoice_detail.units, invoice_detail.price]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, invoice_detail, invoice_detail_id):
        query = f"UPDATE {t.TINVOICEDETAIL} SET {t.TINVOICEDETAIL_INVOICE_ID}=?, {t.TINVOICEDETAIL_PRODUCT_ID}=?, {t.TINVOICEDETAIL_UNITS}=?, {t.TINVOICEDETAIL_PRICE}=? WHERE {t.TINVOICEDETAIL_ID} = ?"
        params = [invoice_detail.invoice_id, invoice_detail.product_id, invoice_detail.units, invoice_detail.price, invoice_detail_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def delete(self, invoice_detail_id):
        query = f"DELETE FROM {t.TINVOICEDETAIL} WHERE {t.TINVOICEDETAIL_ID} = ?"
        params = [invoice_detail_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def selectAll(self):
        query = f"SELECT * FROM {t.TINVOICEDETAIL}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, invoice_detail_id):
        query = f"SELECT * FROM {t.TINVOICEDETAIL} WHERE {t.TINVOICEDETAIL_ID} = ?"
        response = self.executeQueryOne(query, [invoice_detail_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()
    