# imports
import uuid 
from app.database import db, Category, Product, Client, TypePayment, Invoice, InvoiceDetail, User

""" Clase de migración para datos base de nuestra aplicación. """
class MigrateDatabase():
    def __init__(self):
        super().__init__()

    def create_db(self):
        """ Método de creación de la base de datos. """
        db.drop_all()
        db.create_all()

    def create_default_data(self):
        """ Método para generar data por defecto en las tablas. """
        # Categorias
        category_1 = Category(
            name="Electrodomesticos"
        )
        # Productos
        product_1 = Product(
            name="Celular S10", 
            stock=2, 
            category_id=1
        )
        product_2 = Product(
            name="Nevera", 
            stock=5, 
            category_id=1
        )
        product_3 = Product(
            name="Televisor", 
            stock=20, 
            category_id=1
        )
        # Clientes
        cliente_1 = Client(
            document="101010202020",
            name="Asperos",
            lastname="Geek",
            address="Carrera 7 Este",
            date_of_birth="19991022",
            phones="3125665656-3214578489",
            email="asGeek@example.com"
        )
        # Tipos de pago
        type_payment_1 = TypePayment(
            name="Tarjeta Crédito"
        )
        type_payment_2 = TypePayment(
            name="Efectivo"
        )
        # Facturas
        invoice_1 = Invoice(
            code=str(uuid.uuid1()),
            client_id=1,
            type_of_payment_id=1
        )
        # Detalles de factura
        invoice_detail_1 = InvoiceDetail(
            invoice_id=1,
            product_id=1,
            units=1,
            price=2700000
        )
        invoice_detail_2 = InvoiceDetail(
            invoice_id=1,
            product_id=2,
            units=1,
            price=2100000
        )
        invoice_detail_3 = InvoiceDetail(
            invoice_id=1,
            product_id=3,
            units=2,
            price=1500000
        )
        # Usuarios de autenticacion
        user_1 = User(
            username="asperosGeek",
            is_admin=True
        )
        user_1.set_password("123Admin")

        # Agregar registros a la base de datos
        db.session.add(category_1)
        db.session.add(product_1)
        db.session.add(product_2)
        db.session.add(product_3)
        db.session.add(cliente_1)
        db.session.add(type_payment_1)
        db.session.add(type_payment_2)
        db.session.add(invoice_1)
        db.session.add(invoice_detail_1)
        db.session.add(invoice_detail_2)
        db.session.add(invoice_detail_3)
        db.session.add(user_1)
        db.session.commit()
        # Cerrar session
        db.session.close()

    def migrate_database(self):
        """ Método de migración de la base de datos. """
        self.create_db()
        self.create_default_data()