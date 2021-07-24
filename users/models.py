""" Clase del modelo usuarios. """
class UserModel():

    def __init__(self, user):
        self.username = user["username"]
        self.is_admin = user["is_admin"] if "is_admin" in user else None
        self.password = user["password"]
    
""" Clase del modelo clientes. """
class ClientModel():

    def __init__(self, client):
        self.document = client["document"]
        self.name = client["name"]
        self.lastname = client["lastname"]
        self.address = client["address"]
        self.date_of_birth = client["date_of_birth"]
        self.phones = client["phones"]
        self.email = client["email"]