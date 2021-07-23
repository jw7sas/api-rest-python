# imports
import flask
from flask import jsonify
from app.models import ResponseModel

errors = flask.Blueprint('error_handlers', __name__)

@errors.app_errorhandler(405)
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

@errors.app_errorhandler(404)
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

@errors.app_errorhandler(500)
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