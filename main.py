# imports
from app import create_app
from app.migrate import MigrateDatabase

app = create_app()

@app.route('/database', methods=["GET"])
def migrate_database():
    MigrateDatabase().migrate_database()

    return "Base de datos migrada exitosamente!!"

if __name__ == '__main__':
    app.app_context().push()
    app.run("0.0.0.0", debug=True)