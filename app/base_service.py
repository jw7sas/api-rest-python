# imports
import sqlite3
from app.database import Database
""" Clase Base para el manejo de servicios que apuntan a la base de datos. """ 
class BaseService():
    def __init__(self):
        self.db = Database().getConn()

    def dict_factory(self, cursor, row):
        """Método para retornar un diccionario al devolver resultados en sqlite3. """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def executeQuery(self, query, params):
        """ Método para ejecutar una consulta. """
        try:
            self.db.row_factory = self.dict_factory
            cursor = self.db.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()

            return {'error': False, 'data': results}
        except ValueError as err:
            return {'error': True, 'data': err}
        except sqlite3.IntegrityError as err:
            return {'error': True, 'data': err}
        finally:
            self.db.close()
    
    def executeQueryOne(self, query, params):
        """ Método para ejecutar una consulta y obtener un solo registro. """
        try:
            self.db.row_factory = self.dict_factory
            cursor = self.db.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()

            return {'error': False, 'data': result}
        except ValueError as err:
            return {'error': True, 'data': err}
        except sqlite3.IntegrityError as err:
            return {'error': True, 'data': err}
        finally:
            self.db.close()

    def executeUpdate(self, query, params):
        """ Método para ejecutar una consulta. """
        try:
            cursor = self.db.cursor()
            response = cursor.execute(query, params)
            self.db.commit()

            return {'error': False, 'data': None}
        except ValueError as err:
            return {'error': True, 'data': err}
        except sqlite3.IntegrityError as err:
            return {'error': True, 'data': err}
        finally:
            self.db.close()