# -+- coding: utf-8 -*-
# imports

# Modulos de flask
from flask import Flask
from flask_jwt import JWT

# Archivos de configuración de la app
from .routes import * 
from .config import Config 
from .jwt import authenticate, identity
from app.database import db
from app.log_routes import log, before_request_api, after_request_api

def create_app():
    """ Método para la creación y la configuración de la App. """
    app = Flask(__name__)
    # Configuración básica
    app.config.from_object(Config)
    # Configuración de vistas
    app = appRoutes(app)
    app = productRoutes(app)
    app = categoryRoutes(app)
    app = userRoutes(app)
    app = clientRoutes(app)
    app = typePaymentRoutes(app)
    app = invoiceRoutes(app)
    app = invoiceDetailRoutes(app)
    
    # configuración JWT
    jwt = JWT(app, authenticate, identity)
    # Configuración de rutas de errores y validaciones
    app.register_blueprint(log)
    app.before_request(before_request_api)
    app.after_request(after_request_api)
    # Configuración de la base de datos
    db.init_app(app)

    return app