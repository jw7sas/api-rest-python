# imports
from flask_jwt import jwt_required, current_identity
from flask import Flask

# imports app
from app import create_app, Database

app = create_app()


@app.route('/protected', methods=["POST"])
@jwt_required()
def protected():
    return '%s' % current_identity


if __name__ == '__main__':
    Database().createTables()
    app.run("0.0.0.0", debug=True)