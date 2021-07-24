# imports
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.database import User, Client

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: User
        fields = ('id', 'username', 'is_admin',)
        load_instance = True

class ClientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Client
        fields = ('id', 'document', 'name', 'lastname', 'address', 'date_of_birth', 'phones', 'email',)
        load_instance = True
    

