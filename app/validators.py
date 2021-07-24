# -+- coding: utf-8 -*-
# imports
import json
from flask import request, jsonify, session
from flask_jwt import current_identity
# Modulo de app
from app.properties import *
from app.models import ResponseModel, TransactionLogModel
from app.services import TransactionLogService


def getError(errorMessage):
    """ Método para retornar errores de validaciones. """
    return ResponseModel(
        dict(
            response=errorMessage, 
            error=True
        )
    ).getResponseBasic()

def validate_json_rest(func):
    """ Decorador para validar el Json de las diferentes peticiones. """
    def wrapper(*args, **kwargs):
        
        ## VARIABLES
        method = request.method
        fields = f"request_{method}_{args[0].view}".upper()
        if (request.data is None) or (not request.data):
            return jsonify(getError(ERROR_REQUETS))

        jsonData = json.loads(request.data)

        if "data" not in jsonData:
            return jsonify(getError(ERROR_REQUETS_DATA))

        ## VALIDACIÓN CAMPOS
        response = validate_request_fields(jsonData["data"], args[0].view, fields)
        if response["error"] is True:
            return jsonify(getError(response["errorMessage"]))
        else:
            ## CONTINUAR CON EL PROCESO ...
            return func(*args, **kwargs)

    return wrapper

def pre_request_log(func):
    """ Decorador para generar el log de las transacciones. """
    def wrapper(*args, **kwargs):
        user_id = current_identity.id if current_identity else None
        method = request.method
        if method in ["POST", "PUT"]:
            if (request.data is None) or (not request.data):
                return jsonify(getError(ERROR_REQUETS))

            jsonData = json.loads(request.data)

            if "info" not in jsonData:
                return jsonify(getError(ERROR_REQUETS_INFO))
            ## VALIDACIÓN CAMPOS
            response = validate_request_fields(jsonData["info"], "LOG", "REQUEST_LOG")
            if response["error"] is True:
                return jsonify(getError(response["errorMessage"]))

            # CREAR LOG ...
            tl = TransactionLogModel(jsonData["info"], args[0].view, method, user_id)
            serv = TransactionLogService()
            t_log = serv.create(tl)
            session["log"] = t_log
        else:
            # CREAR LOG ...
            tl = TransactionLogModel({}, args[0].view, method, user_id)
            serv = TransactionLogService()
            t_log = serv.create(tl)
            session["log"] = t_log

        ## CONTINUAR CON EL PROCESO ...
        return func(*args, **kwargs)


    return wrapper

def validate_request_fields(data, view, fields):
    """ Método para validar las propiedades y elementos de nuestros JSON. """
    # validaciones: 0=key, 1=required, 2=type, 3=MAX [LENGTH], 4=MIN [LENGTH]
    try:
        fields = globals()[fields]
        elemFields = [globals()[f"{view}_FIELD_{field}".upper()] for field in fields]
        for field in elemFields:
            # validar campos requeridos
            if field["required"] is True:
                if field["key"] not in data.keys():
                    raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE SER OBLIGATORIO]")

                # Validacion longitud mínima
                if len(str(data[field["key"]])) < field["min"]:
                    raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE TENER UNA LONGITUD MÍNIMA DE ({field['min']}) CARACTERES]")
                # Validacion longitud máxima
                if len(str(data[field["key"]])) > field["max"]:
                    raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE TENER UNA LONGITUD MÁXIMA DE ({field['max']}) CARACTERES]")
            else:
                if (field["key"] in data.keys()) and data[field["key"]] is not None:
                    if (field["type"] != "boolean") and (len(data[field["key"]]) is not None) and (len(str(data[field["key"]])) > 0):
                        # Validacion longitud mínima
                        if len(str(data[field["key"]])) < field["min"]:
                            raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE TENER UNA LONGITUD MÍNIMA DE ({field['min']}) CARACTERES]")
                        # Validacion longitud máxima
                        if len(str(data[field["key"]])) > field["max"]:
                            raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE TENER UNA LONGITUD MÁXIMA DE ({field['max']}) CARACTERES]")
        return {"error": False}

    except ValueError as err:
        return {"error": True, "errorMessage": str(err)}
