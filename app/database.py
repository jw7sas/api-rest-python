# imports
import sqlite3

class Database():

    DATABASE_NAME = "database.db"

    def getConn(self):
        """ Método para obtener conexión con la DB"""
        try:
            conn = sqlite3.connect(self.DATABASE_NAME)
            conn.execute('pragma foreign_keys=ON')
            return conn
        except ValueError:
            print("Error de conexión con la DB")

    def createTables(self):
        """ Método de creación de tablas."""
        try:
            tables = [
                """ CREATE TABLE IF NOT EXISTS categories(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NULL
                )
                """,
                """ CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    stock INTEGER NOT NULL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories (id)
                )
                """,
                """ CREATE TABLE IF NOT EXISTS type_of_payments(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    other_details TEXT NULL
                )
                """,
                """ CREATE TABLE IF NOT EXISTS clients(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    address TEXT NOT NULL,
                    date_of_birth NUMERIC NOT NULL,
                    phones TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
                """,
                """ CREATE TABLE IF NOT EXISTS invoices(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE NOT NULL,
                    client_id INTEGER NOT NULL,
                    type_of_payment_id INTEGER NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES clients (id),
                    FOREIGN KEY (type_of_payment_id) REFERENCES type_of_payments (id)
                )
                """,
                """ CREATE TABLE IF NOT EXISTS invoice_details(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    invoice_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    units INTEGER NOT NULL,
                    price REAL NOT NULL,
                    FOREIGN KEY (invoice_id) REFERENCES invoices (id),
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
                """,
                """ CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    is_admin TEXT NOT NULL DEFAULT "N"
                )
                """,
            ]
            conn = self.getConn()
            cursor = conn.cursor()
            for table in tables:
                cursor.execute(table)
        except ValueError:
            print(str(ValueError))
