# imports
import uuid 
import sqlite3
# Modulos de app
from app import properties as p
from app.models import ResponseModel
from app.database import db, TypePayment, Invoice, InvoiceDetail

""" Clase de servicio de tipos de pago DB. """
class TypePaymentService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False

    def create(self, type_payment):
        try:
            t = TypePayment(
                name=type_payment.name,
                other_details=type_payment.other_details
            )

            db.session.add(t)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def update(self, type_payment, type_payment_id):
        try:
            t = self.selectByPK(type_payment_id)
            t.name = type_payment.name
            t.other_details = type_payment.other_details

            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def delete(self, type_payment_id):
        try:
            t = self.selectByPK(type_payment_id)

            db.session.delete(t)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def selectAll(self):
        return TypePayment.query.all()

    def selectByPK(self, type_payment_id):
        return TypePayment.query.get(type_payment_id)


""" Clase de servicio de facturas DB. """
class InvoiceService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False

    def create(self, invoice):
        try:
            i = Invoice(
                code=str(uuid.uuid1()),
                client_id=invoice.client_id,
                type_of_payment_id=invoice.type_of_payment_id
            )

            db.session.add(i)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()


    def update(self, invoice, invoice_id):
        try:
            i = self.selectByPK(invoice_id)
            i.client_id = invoice.client_id
            i.type_of_payment_id = invoice.type_of_payment_id

            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def delete(self, invoice_id):
        try:
            i = self.selectByPK(invoice_id)

            db.session.delete(i)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def selectAll(self):
        return Invoice.query.all()

    def selectByPK(self, invoice_id):
        return Invoice.query.get(invoice_id)


""" Clase de servicio de detalle de facturas DB. """
class InvoiceDetailService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False

    def create(self, invoice_detail):
        try:
            idt = InvoiceDetail(
                invoice_id=invoice_detail.invoice_id,
                product_id=invoice_detail.product_id,
                units=invoice_detail.units,
                price=invoice_detail.price
            )

            db.session.add(idt)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def update(self, invoice_detail, invoice_detail_id):
        try:
            idt = self.selectByPK(invoice_detail_id)
            idt.invoice_id = invoice_detail.invoice_id
            idt.product_id = invoice_detail.product_id
            idt.units = invoice_detail.units
            idt.price = invoice_detail.price

            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def delete(self, invoice_detail_id):
        try:
            idt = self.selectByPK(invoice_detail_id)

            db.session.delete(idt)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def selectAll(self):
        return InvoiceDetail.query.all()

    def selectByPK(self, invoice_detail_id):
        return InvoiceDetail.query.get(invoice_detail_id)
    