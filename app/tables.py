""" Archivo de variables constantes de las tablas. """
# Tabla de categorias
TCATEGORY = "categories"
TCATEGORY_ID = "id"
TCATEGORY_NAME = "name"
TCATEGORY_DESCRIPTION = "description"

# Tabla de productos
TPRODUCT = "products"
TPRODUCT_ID = "id"
TPRODUCT_NAME = "name"
TPRODUCT_STOCK = "stock"
TPRODUCT_CATEGORY_ID = "category_id"

# Tabla de tipos de pago
TTYPEPAYMENT = "type_of_payments"
TTYPEPAYMENT_ID = "id"
TTYPEPAYMENT_NAME = "name"
TTYPEPAYMENT_OTHER_DETAILS = "other_details"

# Tabla de clientes
TCLIENT = "clients"
TCLIENT_ID = "id"
TCLIENT_DOCUMENT = "document"
TCLIENT_NAME = "name"
TCLIENT_LASTNAME = "lastname"
TCLIENT_ADDRESS = "address"
TCLIENT_DATE_OF_BIRTH = "date_of_birth"
TCLIENT_PHONES = "phones"
TCLIENT_EMAIL = "email"

# Tabla de facturas
TINVOICE = "invoices"
TINVOICE_ID = "id"
TINVOICE_CODE = "code"
TINVOICE_CLIENT_ID = "client_id"
TINVOICE_TYPE_OF_PAYMENT_ID = "type_of_payment_id"

# Tabla de detalle de facturas
TINVOICEDETAIL = "invoice_details"
TINVOICEDETAIL_ID = "id"
TINVOICEDETAIL_INVOICE_ID = "invoice_id"
TINVOICEDETAIL_PRODUCT_ID = "product_id"
TINVOICEDETAIL_UNITS = "units"
TINVOICEDETAIL_PRICE = "price"

# Tabla de usuarios
TUSER = "users"
TUSER_ID = "id"
TUSER_USERNAME = "username"
TUSER_PASSWORD = "password"
TUSER_IS_ADMIN = "is_admin"
