# imports
from users.models import UserModel
from users.services import UserService


def authenticate(username, password):
    """ Método de autenticación JWT. """
    print("here ... auth")
    user = UserModel({"username": username})
    serv = UserService()
    response = serv.selectUserByUsername(user)
    if response and ("error" not in response.keys()):
        user.set_pwd(response["password"])
        if user.check_password(password):
            user.setUser(response)
            return user

def identity(payload):
    """ Verificar identidad del usuario. """
    print("here ... identity")
    print(payload)
    user_id = payload['identity']
    user = UserModel(None)
    serv = UserService()
    response = serv.selectByPK(user_id)
    print(response)
    if response:
        user.setUser(response)
    else:
        user = None
    return user  


