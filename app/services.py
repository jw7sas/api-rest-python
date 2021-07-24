# imports
import sqlite3
# Modulos de app
from app.database import db, TransactionLog

""" Clase de servicio de LOG a la base de datos. """
class TransactionLogService():
    def __init__(self):
        super().__init__()
        
    def create(self, transaction_log):
        try:
            t_log = TransactionLog(
                secuence_number=transaction_log.secuence_number,
                trx_date=transaction_log.trx_date,
                trx_time=transaction_log.trx_time,
                view=transaction_log.view,
                method=transaction_log.method,
                user_id=transaction_log.user_id,
                ip_address=transaction_log.ip_address
            )

            db.session.add(t_log)
            db.session.commit()
        except sqlite3.IntegrityError as err_aql:
            t_log = None
        except Exception as err:
            t_log = None
        finally:
            return t_log

        
