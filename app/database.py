# imports
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=True)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

class TypePayment(db.Model):
    __tablename__ = 'type_of_payments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    other_details = db.Column(db.String(250), nullable=True)

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.String(50), nullable=False)
    phones = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id', ondelete='CASCADE'), nullable=False)
    client = db.relationship('Client', backref=db.backref('invoices', lazy=True))
    type_of_payment_id = db.Column(db.Integer, db.ForeignKey('type_of_payments.id', ondelete='CASCADE'), nullable=False)
    typePayment = db.relationship('TypePayment', backref=db.backref('invoices', lazy=True))


class InvoiceDetail(db.Model):
    __tablename__ = 'invoice_details'

    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id', ondelete='CASCADE'), nullable=False)
    invoice = db.relationship('Invoice', backref=db.backref('invoice_details', lazy=True))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    product = db.relationship('Product', backref=db.backref('invoice_details', lazy=True))

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class TransactionLog(db.Model):
    __tablename__ = 'transaction_logs'

    id = db.Column(db.Integer, primary_key=True)
    secuence_number = db.Column(db.String(12), nullable=True)
    trx_date = db.Column(db.String(8), nullable=True)
    trx_time = db.Column(db.String(7), nullable=True)
    method = db.Column(db.String(6), nullable=False)
    view = db.Column(db.String(50), nullable=False)
    ip_address = db.Column(db.String(250), nullable=False)
    response_status = db.Column(db.String(250), nullable=True)
    current_at = db.Column(db.DateTime, default=datetime.datetime.now)
    update_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    user = db.relationship('User', backref=db.backref('transaction_logs', lazy=True))