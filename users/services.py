# imports
from app.base_service import BaseService
from app.models import ResponseModel
from app import tables as t, properties as p 

""" Clase de servicio de usuarios hacia la Base de datos. """
class UserService(BaseService):
    def __init__(self):
        super().__init__()

    def create(self, user):
        query = f"INSERT INTO {t.TUSER} ({t.TUSER_USERNAME}, {t.TUSER_PASSWORD}) values (?,?)" if user.is_admin is None else f"INSERT INTO {t.TUSER} ({t.TUSER_USERNAME}, {t.TUSER_PASSWORD}, {t.TUSER_IS_ADMIN}) values (?,?,?)"
        params = [user.username, user.password] 
        if user.is_admin is not None:
            params.append(user.is_admin)

        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, user, user_id):
        query = f"UPDATE {t.TUSER} SET {t.TUSER_USERNAME} = ?"
        query += "" if user.password is None else f", {t.TUSER_PASSWORD} = ?" 
        query += "" if user.is_admin is None else f", {t.TUSER_IS_ADMIN} = ?"
        query += f" WHERE {t.TUSER_ID} = ?"
        print(query)
        params = [user.username]
        if user.password is not None:
            params.append(user.password)
        
        if user.is_admin is not None:
            params.append(user.is_admin)

        params.append(user_id)

        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def delete(self, user_id):
        query = f"DELETE FROM {t.TUSER} WHERE {t.TUSER_ID} = ?"
        params = [user_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def selectAll(self):
        query = f"SELECT {t.TUSER_USERNAME}, {t.TUSER_IS_ADMIN} FROM {t.TUSER}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, user_id):
        query = f"SELECT * FROM {t.TUSER} WHERE {t.TUSER_ID} = ?"
        response = self.executeQueryOne(query, [user_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()
    
    def selectUserByUsername(self, user):
        query = f"SELECT * FROM {t.TUSER} WHERE {t.TUSER_USERNAME} = ?"
        response = self.executeQueryOne(query, [user.username])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()


""" Clase de servicios de clientes a la Base de Datos. """
class ClientService(BaseService):
    def __init__(self):
        super().__init__()

    def create(self, client):
        query = f"INSERT INTO {t.TCLIENT} ({t.TCLIENT_DOCUMENT}, {t.TCLIENT_NAME}, {t.TCLIENT_LASTNAME}, {t.TCLIENT_ADDRESS}, {t.TCLIENT_DATE_OF_BIRTH}, {t.TCLIENT_PHONES}, {t.TCLIENT_EMAIL})"
        query += " values (?,?,?,?,?,?,?)"
        params = [client.document, client.name, client.lastname, client.address, client.date_of_birth, client.phones, client.email]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, client, client_id):
        query = f"UPDATE {t.TCLIENT} SET {t.TCLIENT_DOCUMENT}=?, {t.TCLIENT_NAME}=?, {t.TCLIENT_LASTNAME}=?, {t.TCLIENT_ADDRESS}=?, {t.TCLIENT_DATE_OF_BIRTH}=?, {t.TCLIENT_PHONES}=?, {t.TCLIENT_EMAIL}=? WHERE {t.TCLIENT_ID} = ?"
        params = [client.document, client.name, client.lastname, client.address, client.date_of_birth, client.phones, client.email, client_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def delete(self, client_id):
        query = f"DELETE FROM {t.TCLIENT} WHERE {t.TCLIENT_ID} = ?"
        params = [client_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def selectAll(self):
        query = f"SELECT * FROM {t.TCLIENT}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, client_id):
        query = f"SELECT * FROM {t.TCLIENT} WHERE {t.TCLIENT_ID} = ?"
        response = self.executeQueryOne(query, [client_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()
