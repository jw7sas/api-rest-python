# Instalar Python - https://www.python.org/  - instalar pip -> se selecciona en la instalación de python.
    Python 3.8.3
    pip 21.1.3

# Opcional - Descargar SQL-LITE - https://www.sqlite.org/index.html

# Instalar el ambiente virtual
    pip install virtualenv==20.2.2
    virtualenv venv

# Activar el entorno virtual en Windows
    cd venv/Scripts
    activate

# Agregamos las dependencias al archivo de requerimientos y ejecutamos el comandos - archivo en la raíz del proyecto 
    cd ../../
    pip install -r requirements.txt

# Correr al app en desarrollo
    set FLASK_APP=main.py
    set FLASK_DEBUG=1
    set FLASK_ENV=development
    flask run

# Usuario Base:
    Archivo:
        app/migrate.py
    Credenciales:
        username=asperosGeek
        password=123Admin

# NOTA (OPCIONAL) Reinicar (Base de datos) y configuración (user Default) 
    Configuración usuario por defecto en:
        app/migrate.py
    
    ip:port/database