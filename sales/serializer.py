# imports
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from app.database import TypePayment, Invoice, InvoiceDetail
from users.serializer import ClientSchema
from products.serializer import ProductSchema

class TypePaymentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: TypePayment
        fields = ('id', 'name', 'other_details',)
        load_instance = True

class InvoiceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Invoice
        fields = ('id', 'code', 'client_id', 'client', 'type_of_payment_id', 'typePayment', )
        include_relationships = True
        load_instance = True
    
    client = fields.Nested(ClientSchema)
    typePayment = fields.Nested(TypePaymentSchema)

class InvoiceDetailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: InvoiceDetail
        fields = ('id', 'units', 'price', 'invoice_id', 'invoice', 'product_id', 'product', )
        include_relationships = True
        load_instance = True
    
    invoice = fields.Nested(InvoiceSchema)
    product = fields.Nested(ProductSchema)

