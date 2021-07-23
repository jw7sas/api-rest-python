# imports
import json
from flask.views import MethodView
from flask import jsonify, request
from users.services import UserService, ClientService
from users.models import UserModel, ClientModel
from app.validators import validate_json_rest

class UserView(MethodView):
    """ Clase API de usuarios. """
    def __init__(self):
        super().__init__()
        self.view = "user"

    def get(self, user_id):
        if user_id is None:
            # retornar el listado de usuarios
            serv = UserService()
            response = serv.selectAll()
            response["info"]["count"] = len(response["results"])
            return jsonify(response)
        else:
            # retornar un usuario especifico
            serv = UserService()
            response = serv.selectByPK(user_id)
            return jsonify(response)

    @validate_json_rest
    def post(self):
        # crear un usuario
        userJson = json.loads(request.data)
        user = UserModel(userJson["data"])
        if "password" in userJson["data"]:
            user.set_password(userJson["data"]["password"])
        serv = UserService()
        response = serv.create(user)
        response["sequenceNumber"] = userJson["info"]["secuence_number"] 
        return jsonify(response)

    def delete(self, user_id):
        # eliminar un usuario
        serv = UserService()
        response = serv.delete(user_id)
        return jsonify(response)

    @validate_json_rest
    def put(self, user_id):
        # actualizar un usuario
        userJson = json.loads(request.data)
        user = UserModel(userJson["data"])
        if "password" in userJson["data"]:
            user.set_password(userJson["data"]["password"])
        serv = UserService()
        response = serv.update(user, user_id)
        response["sequenceNumber"] = userJson["info"]["secuence_number"] 
        return jsonify(response)

    
    

class ClientView(MethodView):
    """ Clase API de clientes. """
    def __init__(self):
        super().__init__()
        self.view = "client"
        

    def get(self, client_id):
        if client_id is None:
            # retornar el listado de clientes
            serv = ClientService()
            response = serv.selectAll()
            response["info"]["count"] = len(response["results"])
            return jsonify(response)
        else:
            # retornar un cliente especifico
            serv = ClientService()
            response = serv.selectByPK(client_id)
            return jsonify(response)

    @validate_json_rest
    def post(self):
        # crear un cliente
        clientJson = json.loads(request.data)
        client = ClientModel(clientJson["data"])
        serv = ClientService()
        response = serv.create(client)
        response["sequenceNumber"] = clientJson["info"]["secuence_number"] 
        return jsonify(response)

    def delete(self, client_id):
        # eliminar un cliente
        serv = ClientService()
        response = serv.delete(client_id)
        return jsonify(response)

    @validate_json_rest
    def put(self, client_id):
        # actualizar un cliente
        clientJson = json.loads(request.data)
        client = ClientModel(clientJson["data"])
        serv = ClientService()
        response = serv.update(client, client_id)
        response["sequenceNumber"] = clientJson["info"]["secuence_number"] 
        return jsonify(response)