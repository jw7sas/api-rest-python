# imports
import json
from flask.views import MethodView
from flask_jwt import jwt_required
from flask import jsonify, request
# Modulos de app
from app.models import ResponseModel
from app.validators import validate_json_rest, pre_request_log
# Modulos de users
from users.services import UserService, ClientService
from users.models import UserModel, ClientModel
from users.serializer import UserSchema, ClientSchema


class UserView(MethodView):
    """ Clase API de usuarios. """
    def __init__(self):
        super().__init__()
        self.view = "user"

    @jwt_required()
    @pre_request_log
    def get(self, user_id):
        if user_id is None:
            # retornar el listado de usuarios
            serv = UserService()
            results = serv.selectAll()
            schema = UserSchema()
            results = [schema.dump(u) for u in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un usuario especifico
            serv = UserService()
            response = serv.selectByPK(user_id)
            response = UserSchema().dump(response)
            return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un usuario
        userJson = json.loads(request.data)
        user = UserModel(userJson["data"])
        serv = UserService()
        response = serv.create(user)
        response["sequenceNumber"] = userJson["info"]["secuence_number"] 
        return jsonify(response)
    
    @jwt_required()
    @pre_request_log
    def delete(self, user_id):
        # eliminar un usuario
        serv = UserService()
        response = serv.delete(user_id)
        return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, user_id):
        # actualizar un usuario
        userJson = json.loads(request.data)
        user = UserModel(userJson["data"])
        serv = UserService()
        response = serv.update(user, user_id)
        response["sequenceNumber"] = userJson["info"]["secuence_number"] 
        return jsonify(response)

    
    

class ClientView(MethodView):
    """ Clase API de clientes. """
    def __init__(self):
        super().__init__()
        self.view = "client"
        
    @jwt_required()
    @pre_request_log
    def get(self, client_id):
        if client_id is None:
            # retornar el listado de clientes
            serv = ClientService()
            results = serv.selectAll()
            schema = ClientSchema()
            results = [schema.dump(c) for c in results]
            response = ResponseModel({"response": results, "error": False}).getResponseResults()
            response["info"]["count"] = len(results)
            return jsonify(response)
        else:
            # retornar un cliente especifico
            serv = ClientService()
            response = serv.selectByPK(client_id)
            response = ClientSchema().dump(response)
            return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def post(self):
        # crear un cliente
        clientJson = json.loads(request.data)
        client = ClientModel(clientJson["data"])
        serv = ClientService()
        response = serv.create(client)
        response["sequenceNumber"] = clientJson["info"]["secuence_number"] 
        return jsonify(response)

    @jwt_required()
    @pre_request_log
    def delete(self, client_id):
        # eliminar un cliente
        serv = ClientService()
        response = serv.delete(client_id)
        return jsonify(response)

    @jwt_required()
    @validate_json_rest
    @pre_request_log
    def put(self, client_id):
        # actualizar un cliente
        clientJson = json.loads(request.data)
        client = ClientModel(clientJson["data"])
        serv = ClientService()
        response = serv.update(client, client_id)
        response["sequenceNumber"] = clientJson["info"]["secuence_number"] 
        return jsonify(response)