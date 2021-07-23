# imports
import app.error_handlers
from flask import Flask
from flask_jwt import JWT
from .routes import * 
from .config import Config 
from .jwt import authenticate, identity
# imports Database
from app.database import Database

def create_app():
    """ Método para la creación y la configuración de la App. """
    app = Flask(__name__)

    app.config.from_object(Config)

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

    # Configuración de errores
    app.register_blueprint(error_handlers.errors)

    return app