# imports
import uuid 
import json
from flask.views import MethodView
from flask_jwt import jwt_required
from flask import request, jsonify
# Modulos de app
from app.validators import validate_json_rest, pre_request_log
from app.models import ResponseModel
# Modulos de sales
from sales.services import TypePaymentService, InvoiceService, InvoiceDetailService
from sales.models import TypePaymentModel, InvoiceModel, InvoiceDetailModel
from sales.serializer import TypePaymentSchema, InvoiceSchema, InvoiceDetailSchema

class TypePaymentView(MethodView):
    """ Clase API de tipo de pago. """
    def __init__(self):
        super().__init__()
        self.view = "type_of_payment"

    def get(self, type_payment_id):
        if type_payment_id is None:
            # retornar el listado de tipo de pagos
            serv = TypePaymentService()
            results = serv.selectAll()
            schema = TypePaymentSchema()
            results = [schema.dump(t) for t in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un tipo de pago especifico
            serv = TypePaymentService()
            response = serv.selectByPK(type_payment_id)
            response = TypePaymentSchema().dump(response)
            return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un tipo de pago
        typePaymentJson = json.loads(request.data)
        type_payment = TypePaymentModel(typePaymentJson["data"])
        serv = TypePaymentService()
        response = serv.create(type_payment)
        response["sequenceNumber"] = typePaymentJson["info"]["secuence_number"] 
        return jsonify(response)

    @jwt_required()
    @pre_request_log
    def delete(self, type_payment_id):
        # eliminar un tipo de pago
        serv = TypePaymentService()
        response = serv.delete(type_payment_id)
        return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, type_payment_id):
        # actualizar un tipo de pago
        typePaymentJson = json.loads(request.data)
        type_payment = TypePaymentModel(typePaymentJson["data"])
        serv = TypePaymentService()
        response = serv.update(type_payment, type_payment_id)
        response["sequenceNumber"] = typePaymentJson["info"]["secuence_number"] 
        return jsonify(response)


class InvoiceView(MethodView):
    """ Clase API de factura. """
    def __init__(self):
        super().__init__()
        self.view = "invoice"

    @jwt_required()
    @pre_request_log
    def get(self, invoice_id):
        if invoice_id is None:
            # retornar el listado de facturas
            serv = InvoiceService()
            results = serv.selectAll()
            schema = InvoiceSchema()
            results = [schema.dump(i) for i in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un factura especifico
            serv = InvoiceService()
            response = serv.selectByPK(invoice_id)
            response = InvoiceSchema().dump(response)
            return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un factura
        invoiceJson = json.loads(request.data)
        invoice = InvoiceModel(invoiceJson["data"])
        serv = InvoiceService()
        response = serv.create(invoice)
        response["sequenceNumber"] = invoiceJson["info"]["secuence_number"] 
        return jsonify(response)

    @jwt_required()
    @pre_request_log
    def delete(self, invoice_id):
        # eliminar un factura
        serv = InvoiceService()
        response = serv.delete(invoice_id)
        return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, invoice_id):
        # actualizar un factura
        invoiceJson = json.loads(request.data)
        invoice = InvoiceModel(invoiceJson["data"])
        serv = InvoiceService()
        response = serv.update(invoice, invoice_id)
        response["sequenceNumber"] = invoiceJson["info"]["secuence_number"] 
        return jsonify(response)


class InvoiceDetailView(MethodView):
    """ Clase API de factura. """
    def __init__(self):
        super().__init__()
        self.view = "invoice_detail"

    @jwt_required()
    @pre_request_log
    def get(self, invoice_detail_id):
        if invoice_detail_id is None:
            # retornar el listado de detalle de facturas
            serv = InvoiceDetailService()
            results = serv.selectAll()
            schema = InvoiceDetailSchema()
            results = [schema.dump(ids) for ids in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un detalle de factura especifico
            serv = InvoiceDetailService()
            response = serv.selectByPK(invoice_detail_id)
            response = InvoiceDetailSchema().dump(response)
            return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un detalle de factura
        invoiceDetailJson = json.loads(request.data)
        invoice_detail = InvoiceDetailModel(invoiceDetailJson["data"])
        serv = InvoiceDetailService()
        response = serv.create(invoice_detail)
        response["sequenceNumber"] = invoiceDetailJson["info"]["secuence_number"] 
        return jsonify(response)

    @jwt_required()
    @pre_request_log
    def delete(self, invoice_detail_id):
        # eliminar un detalle de factura
        serv = InvoiceDetailService()
        response = serv.delete(invoice_detail_id)
        return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, invoice_detail_id):
        # actualizar un detalle de factura
        invoiceDetailJson = json.loads(request.data)
        invoice_detail = InvoiceDetailModel(invoiceDetailJson["data"])
        serv = InvoiceDetailService()
        response = serv.update(invoice_detail, invoice_detail_id)
        response["sequenceNumber"] = invoiceDetailJson["info"]["secuence_number"] 
        return jsonify(response)