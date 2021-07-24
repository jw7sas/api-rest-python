# imports
from app.database import User

def authenticate(username, password):
    """ Método de autenticación JWT. """
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

def identity(payload):
    """ Verificar identidad del usuario. """
    user_id = payload['identity']
    return User.query.get(user_id)


