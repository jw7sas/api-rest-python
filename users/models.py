# imports
from werkzeug.security import generate_password_hash, check_password_hash 

""" Clase del modelo usuarios. """
class UserModel():

    def __init__(self, user):
        if(user):
            self.username = user["username"]
            self.is_admin = user["is_admin"] if "is_admin" in user else None
            self.password = None
    
    def setUser(self, jsonUser):
        self.id = jsonUser["id"]
        self.username = jsonUser["username"]
        self.password = jsonUser["password"]
        self.is_admin = jsonUser["is_admin"]
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def set_pwd(self, password):
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password, password)


""" Clase del modelo clientes. """
class ClientModel():

    def __init__(self, client):
        if(client):
            self.document = client["document"]
            self.name = client["name"]
            self.lastname = client["lastname"]
            self.address = client["address"]
            self.date_of_birth = client["date_of_birth"]
            self.phones = client["phones"]
            self.email = client["email"]