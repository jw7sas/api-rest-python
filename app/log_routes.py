# imports
import json
import flask
from flask import jsonify, session
# Módulo de app
from app.database import db
from app.models import ResponseModel

log = flask.Blueprint('log', __name__)

# ----------------------------------------------
# RUTAS DE ERRORES
# ----------------------------------------------
@log.app_errorhandler(405)
def method_not_allowed(error):
    """ Método de error 405. """
    response = ResponseModel(
        dict(
            response=f"[405 - METODO NO PERMITIDO] | {str(error)}", 
            error=True
        )
    ).getResponseBasic()
    response["responseCode"] = "405"
    return jsonify(response)

@log.app_errorhandler(404)
def error404(error):
    """ Método de error 404. """
    response = ResponseModel(
        dict(
            response=f"[404 - PAGINA NO ENCONTRADA] | {str(error)}", 
            error=True
        )
    ).getResponseBasic()
    response["responseCode"] = "404"
    return jsonify(response)

@log.app_errorhandler(500)
def error500(error):
    """ Método de error 500. """
    response = ResponseModel(
        dict(
            response=f"[500 - ERROR INTERNO DEL SERVIDOR] | {str(error)}", 
            error=True
        )
    ).getResponseBasic()
    response["responseCode"] = "500"
    return jsonify(response)


# ----------------------------------------------
# FUNCIONES DE VALIDACIONES DE LOG
# ----------------------------------------------
def before_request_api():
    """ Método previo a la redirección de nuestro request de API REST. """
    session["log"] = None
    print("<-------------- COMIENZA FLUJO DE TRANSACCIÓN | API REST | ASPEROS GEEK ---------------------->")


def after_request_api(response):
    """ Método posterior a la respuest de nuestra API REST. """
    print(f"<-------------- TERMINA FLUJO DE TRANSACCIÓN | API REST | ASPEROS GEEK [{response.status_code}] ---------------------->")
    if session.get("log") is not None:
        log_l = session.get("log")
        log_l.response_status = str(response.status)
        db.session.commit()
        db.session.close()
    session.clear()
    return after_request(response)


def after_request(response):
    """
    Habilite CORS. Deshabilítelo si no necesita CORS
    """
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response
