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
set FLASK_ENV=development
py main.py