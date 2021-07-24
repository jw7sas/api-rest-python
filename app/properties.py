""" Archivo con las propiedades por defecto de la aplicación. """
# Mensajes de CRUD
SUCCESSFUL_CREATE = "Registro Creado Correctamente"
SUCCESSFUL_UPDATE = "Registro Actualizado Correctamente"
SUCCESSFUL_DELETE = "Registro Eliminado Correctamente"

ERROR_CREATE = "Error al Crear el Registro"
ERROR_UPDATE = "Error al Actualizar el Registro"
ERROR_DELETE = "Error al Eliminar el Registro"

# Validaciones API REST

# -----------------. VALIDACION DE CAMPOS -------------------------
# validaciones: 0=key, 1=required, 2=type, 3=MAX [LENGTH], 4=MIN [LENGTH]
# -----------------------------------------------------------------
# categorias
CATEGORY_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
CATEGORY_FIELD_1={"key": "name", "required": True, "type": "string", "min": 3, "max": 50}
CATEGORY_FIELD_2={"key": "description", "required": False, "type": "string", "min": 5, "max": 150}
# categorias - campos de validación según proceso
REQUEST_POST_CATEGORY=[1,2]
REQUEST_PUT_CATEGORY=[1,2]
# productos
PRODUCT_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
PRODUCT_FIELD_1={"key": "name", "required": True, "type": "string", "min": 3, "max": 50}
PRODUCT_FIELD_2={"key": "stock", "required": True, "type": "numeric", "min": 1, "max": 7}
PRODUCT_FIELD_3={"key": "category_id", "required": True, "type": "numeric", "min": 1, "max": 11}
# productos - campos de validación según proceso
REQUEST_POST_PRODUCT=[1,2,3]
REQUEST_PUT_PRODUCT=[1,2,3]
# Tipo de pago
TYPE_OF_PAYMENT_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
TYPE_OF_PAYMENT_FIELD_1={"key": "name", "required": True, "type": "string", "min": 2, "max": 50}
TYPE_OF_PAYMENT_FIELD_2={"key": "other_details", "required": False, "type": "string", "min": 5, "max": 250}
# Tipo de pago - campos de validación según proceso
REQUEST_POST_TYPE_OF_PAYMENT=[1,2]
REQUEST_PUT_TYPE_OF_PAYMENT=[1,2]
# Clientes
CLIENT_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
CLIENT_FIELD_1={"key": "document", "required": True, "type": "string", "min": 7, "max": 12}
CLIENT_FIELD_2={"key": "name", "required": True, "type": "string", "min": 2, "max": 50}
CLIENT_FIELD_3={"key": "lastname", "required": True, "type": "string", "min": 2, "max": 50}
CLIENT_FIELD_4={"key": "address", "required": True, "type": "string", "min": 2, "max": 100}
CLIENT_FIELD_5={"key": "date_of_birth", "required": True, "type": "numeric", "min": 8, "max": 8}
CLIENT_FIELD_6={"key": "phones", "required": True, "type": "string", "min": 7, "max": 250}
CLIENT_FIELD_7={"key": "email", "required": True, "type": "string", "min": 5, "max": 250}
# Clientes - campos de validación según proceso
REQUEST_POST_CLIENT=[1,2,3,4,5,6,7]
REQUEST_PUT_CLIENT=[1,2,3,4,5,6,7]
# Facturas
INVOICE_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
INVOICE_FIELD_1={"key": "code", "required": True, "type": "string", "min": 36, "max": 36}
INVOICE_FIELD_2={"key": "client_id", "required": True, "type": "numeric", "min": 1, "max": 11}
INVOICE_FIELD_3={"key": "type_of_payment_id", "required": True, "type": "numeric", "min": 1, "max": 11}
# Facturas - campos de validación según proceso
REQUEST_POST_INVOICE=[2,3]
REQUEST_PUT_INVOICE=[2,3]
# Detalle de la Factura
INVOICE_DETAIL_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
INVOICE_DETAIL_FIELD_1={"key": "invoice_id", "required": True, "type": "numeric", "min": 1, "max": 11}
INVOICE_DETAIL_FIELD_2={"key": "product_id", "required": True, "type": "numeric", "min": 1, "max": 11}
INVOICE_DETAIL_FIELD_3={"key": "units", "required": True, "type": "numeric", "min": 1, "max": 7}
INVOICE_DETAIL_FIELD_4={"key": "price", "required": True, "type": "string", "min": 1, "max": 15}
# Detalle de la Factura - campos de validación según proceso
REQUEST_POST_INVOICE_DETAIL=[1,2,3,4]
REQUEST_PUT_INVOICE_DETAIL=[1,2,3,4]
# Usuarios
USER_FIELD_0={"key": "id", "required": True, "type": "numeric", "min": 1, "max": 11}
USER_FIELD_1={"key": "username", "required": True, "type": "string", "min": 6, "max": 30}
USER_FIELD_2={"key": "password", "required": True, "type": "string", "min": 6, "max": 25}
USER_FIELD_3={"key": "is_admin", "required": False, "type": "boolean", "min": 1, "max": 1}
# Usuarios - campos de validación según proceso
REQUEST_POST_USER=[1,2,3]
REQUEST_PUT_USER=[1,2,3]

# Log
LOG_FIELD_0={"key": "secuence_number", "required": True, "type": "string", "min": 1, "max": 12}
LOG_FIELD_1={"key": "trx_date", "required": True, "type": "string", "min": 8, "max": 8}
LOG_FIELD_2={"key": "trx_time", "required": True, "type": "string", "min": 7, "max": 7}
# Log - validación de campos para generar el log 
REQUEST_LOG=[0,1,2]

# Errores
ERROR_REQUETS="INFORMACIÓN DE ENTRADA NO VÁLIDA [VERIFIQUE POR FAVOR]"
ERROR_REQUETS_DATA="NO EXISTE PROPIEDAD 'DATA' [VERIFIQUE POR FAVOR]"
ERROR_REQUETS_INFO="NO EXISTE PROPIEDAD 'INFO' [VERIFIQUE POR FAVOR]"