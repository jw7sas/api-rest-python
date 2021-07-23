# imports
from .views import WelcomeView
from products.views import ProductView, CategoryView
from users.views import UserView, ClientView
from sales.views import TypePaymentView, InvoiceView, InvoiceDetailView
# ---------------------------------------
# Definición de rutas
# ---------------------------------------

# vistas de la aplicación
def appRoutes(app):
    """ Método para agregar las rutas de la app principal. """
    app.add_url_rule('/', view_func=WelcomeView.as_view('as_geek_api'))
    return app

# Productos
def productRoutes(app):
    """ Método para agregar la ruta de productos a nuestra app principal. """
    product_view = ProductView.as_view('product_api')
    app.add_url_rule('/products/', defaults={'product_id': None}, view_func=product_view, methods=['GET',])
    app.add_url_rule('/products/', view_func=product_view, methods=['POST',])
    app.add_url_rule('/products/<int:product_id>', view_func=product_view, methods=['GET', 'PUT', 'DELETE'])
    return app

# Categorias
def categoryRoutes(app):
    """ Método para agregar la ruta de categorias a nuestra app principal. """
    category_view = CategoryView.as_view('category_api')
    app.add_url_rule('/categories/', defaults={'category_id': None}, view_func=category_view, methods=['GET',])
    app.add_url_rule('/categories/', view_func=category_view, methods=['POST',])
    app.add_url_rule('/categories/<int:category_id>', view_func=category_view, methods=['GET', 'PUT', 'DELETE'])
    return app

# Usuarios
def userRoutes(app):
    """ Método para agregar la ruta de usuarios a nuestra app principal. """
    user_view = UserView.as_view('user_api')
    app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET',])
    app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
    app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])
    return app

# clientes
def clientRoutes(app):
    """ Método para agregar la ruta de usuarios a nuestra app principal. """
    client_view = ClientView.as_view('client_api')
    app.add_url_rule('/clients/', defaults={'client_id': None}, view_func=client_view, methods=['GET',])
    app.add_url_rule('/clients/', view_func=client_view, methods=['POST',])
    app.add_url_rule('/clients/<int:client_id>', view_func=client_view, methods=['GET', 'PUT', 'DELETE'])
    return app

# Tipos de pago
def typePaymentRoutes(app):
    """ Método para agregar la ruta de usuarios a nuestra app principal. """
    type_payment_view = TypePaymentView.as_view('type_payment_api')
    app.add_url_rule('/type/payments/', defaults={'type_payment_id': None}, view_func=type_payment_view, methods=['GET',])
    app.add_url_rule('/type/payments/', view_func=type_payment_view, methods=['POST',])
    app.add_url_rule('/type/payments/<int:type_payment_id>', view_func=type_payment_view, methods=['GET', 'PUT', 'DELETE'])
    return app

# Facturas
def invoiceRoutes(app):
    """ Método para agregar la ruta de usuarios a nuestra app principal. """
    invoice_view = InvoiceView.as_view('invoice_api')
    app.add_url_rule('/invoices/', defaults={'invoice_id': None}, view_func=invoice_view, methods=['GET',])
    app.add_url_rule('/invoices/', view_func=invoice_view, methods=['POST',])
    app.add_url_rule('/invoices/<int:invoice_id>', view_func=invoice_view, methods=['GET', 'PUT', 'DELETE'])
    return app

# Detalle de Factura
def invoiceDetailRoutes(app):
    """ Método para agregar la ruta de detalles de factura a nuestra app principal. """
    invoice_detail_view = InvoiceDetailView.as_view('invoice_detail_api')
    app.add_url_rule('/invoice/details/', defaults={'invoice_detail_id': None}, view_func=invoice_detail_view, methods=['GET',])
    app.add_url_rule('/invoice/details/', view_func=invoice_detail_view, methods=['POST',])
    app.add_url_rule('/invoice/details/<int:invoice_detail_id>', view_func=invoice_detail_view, methods=['GET', 'PUT', 'DELETE'])
    return app