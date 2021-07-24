# imports
import json
from flask import request, jsonify
from flask_jwt import jwt_required
from flask.views import MethodView
# Modulos de app
from app.models import ResponseModel
from app.validators import validate_json_rest, pre_request_log
# Modulo de products
from products.models import CategoryModel, ProductModel
from products.services import CategoryService, ProductService
from products.serializer import CategorySchema, ProductSchema

""" Clase API de productos. """
class ProductView(MethodView):
    def __init__(self):
        super().__init__()
        self.view = "product"

    def get(self, product_id):
        if product_id is None:
            # retornar el listado de productos
            serv = ProductService()
            results = serv.selectAll()
            schema = ProductSchema()
            results = [schema.dump(c) for c in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un producto especifico
            serv = ProductService()
            response = serv.selectByPK(product_id)
            response = ProductSchema().dump(response)
            return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un producto
        productJson = json.loads(request.data)
        product = ProductModel(productJson["data"])
        serv = ProductService()
        response = serv.create(product)
        response["sequenceNumber"] = productJson["info"]["secuence_number"] 
        return jsonify(response)
    
    @jwt_required()
    @pre_request_log
    def delete(self, product_id):
        # eliminar un producto
        serv = ProductService()
        response = serv.delete(product_id)
        return jsonify(response)
    
    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, product_id):
        # actualizar un producto
        productJson = json.loads(request.data)
        product = ProductModel(productJson["data"])
        serv = ProductService()
        response = serv.update(product, product_id)
        response["sequenceNumber"] = productJson["info"]["secuence_number"] 
        return jsonify(response)



""" Clase API de categorias. """
class CategoryView(MethodView):
    def __init__(self):
        super().__init__()
        self.view = "category"

    def get(self, category_id):
        if category_id is None:
            # retornar el listado de categorias
            serv = CategoryService()
            results = serv.selectAll()
            schema = CategorySchema()
            results = [schema.dump(c) for c in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un categoria especifico
            serv = CategoryService()
            response = serv.selectByPK(category_id)
            response = CategorySchema().dump(response)
            return jsonify(response)
    
    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un categoria
        categoryJson = json.loads(request.data)
        category = CategoryModel(categoryJson["data"])
        serv = CategoryService()
        response = serv.create(category)
        response["sequenceNumber"] = categoryJson["info"]["secuence_number"] 
        return jsonify(response)
    
    @jwt_required()
    @pre_request_log
    def delete(self, category_id):
        # eliminar un categoria
        serv = CategoryService()
        response = serv.delete(category_id)
        return jsonify(response)
    
    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, category_id):
        # actualizar un categoria
        categoryJson = json.loads(request.data)
        category = CategoryModel(categoryJson["data"])
        serv = CategoryService()
        response = serv.update(category, category_id)
        response["sequenceNumber"] = categoryJson["info"]["secuence_number"] 
        return jsonify(response)