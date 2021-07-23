# -+- coding: utf-8 -*-
#imports
import json
from inspect import getmembers
from pprint import pprint
from flask import request, jsonify
from app.properties import *
from app.models import ResponseModel


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
        jsonData = json.loads(request.data)

        ## VALIDACIÓN CAMPOS
        response = validate_request_fields(jsonData["data"], args[0].view, fields)
        if response["error"] is True:
            return jsonify(getError(response["errorMessage"]))
        else:
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
                if (field["key"] in data.keys()) and (len(data[field["key"]]) is not None) and (len(str(data[field["key"]])) > 0):
                    # Validacion longitud mínima
                    if len(str(data[field["key"]])) < field["min"]:
                        raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE TENER UNA LONGITUD MÍNIMA DE ({field['min']}) CARACTERES]")
                    # Validacion longitud máxima
                    if len(str(data[field["key"]])) > field["max"]:
                        raise ValueError(f"ERROR - CAMPO [{field['key']}] | [DEBE TENER UNA LONGITUD MÁXIMA DE ({field['max']}) CARACTERES]")
        return {"error": False}

    except ValueError as err:
        return {"error": True, "errorMessage": str(err)}


# def validar_request_variables(view, method, url_params): 
#     """ Método para validar variables en la url del request. """
#     try:
#         methods = ["PUT", "DELETE"]
#         if method in methods:
#             if (url_params is None) or (bool(url_params) is False):
#                 baseUrl = f"{view}_BASE_URL_ELEM".upper()
#                 raise ValueError(f"ERROR - URL NO VÁLIDA | ESTRUCTURA [{globals()[baseUrl]}]")
        
#         return {"error": False}
#     except ValueError as err:
#         return {"error": True, "errorMessage": str(err)}