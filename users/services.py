# imports
import sqlite3
from app import properties as p
from app.models import ResponseModel
from app.database import db, User, Client

""" Clase de servicio de usuarios DB. """
class UserService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False

    def create(self, user):
        try:
            u = User(
                username=user.username,
                is_admin=user.is_admin
            )
            u.set_password(user.password)

            db.session.add(u)
            db.session.commit()
            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()


    def update(self, user, user_id):
        try:

            u = self.selectByPK(user_id)
            u.username = user.username
            u.password = user.password
            u.is_admin = user.is_admin

            db.session.commit()
            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def delete(self, user_id):
        try:
            u = self.selectByPK(user_id)

            db.session.delete(u)
            db.session.commit()
            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def selectAll(self):
        return User.query.all()

    def selectByPK(self, user_id):
        return User.query.get(user_id)
    
    def selectUserByUsername(self, username):
        return User.query.filter_by(username=username).first()


""" Clase de servicios de clientes a la Base de Datos. """
class ClientService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False

    def create(self, client):
        try:
            c = Client(
                document=client.document,
                name=client.name,
                lastname=client.lastname,
                address=client.address,
                date_of_birth=client.date_of_birth,
                phones=client.phones,
                email=client.email
            )
            
            db.session.add(c)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def update(self, client, client_id):
        try:
            c = self.selectByPK(client_id)
            c.document = client.document
            c.name = client.name
            c.lastname = client.lastname
            c.address = client.address
            c.date_of_birth = client.date_of_birth
            c.phones = client.phones
            c.email = client.email

            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def delete(self, client_id):
        try:
            c = self.selectByPK(client_id)

            db.session.delete(c)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def selectAll(self):
        return Client.query.all()

    def selectByPK(self, client_id):
        return Client.query.get(client_id)
