""" Clase con los elementos de configruación de nuestra aplicación API REST. """
class Config:
    """ Clase de configuración de flask. """
    SECRET_KEY = 'python_api_rest_asperos_geek'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
