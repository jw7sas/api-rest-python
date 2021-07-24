# imports
import sqlite3
# Modulos de app
from app import properties as p
from app.models import ResponseModel
from app.database import db, Category, Product

""" Clase de servicio de categorias DB. """
class CategoryService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False
        
    def create(self, category):
        try:
            c = Category(
                name=category.name,
                description=category.description
            )

            db.session.add(c)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def update(self, category, category_id):
        try:
            c = self.selectByPK(category_id)
            c.name = category.name
            c.description = category.description

            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def delete(self, category_id):
        try:
            c = self.selectByPK(category_id)

            db.session.delete(c)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def selectAll(self):
        return Category.query.all()

    def selectByPK(self, category_id):
        return Category.query.get(category_id)


""" Clase de servicio de productos DB. """
class ProductService():
    def __init__(self):
        super().__init__()
        self.message = None
        self.error = False

    def create(self, product):
        try:
            pd = Product(
                name=product.name,
                stock=product.stock,
                category_id=product.category_id
            )

            db.session.add(pd)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_CREATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def update(self, product, product_id):
        try:
            pd = self.selectByPK(product_id)
            pd.name = product.name
            pd.stock = product.stock
            pd.category_id = product.category_id

            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_UPDATE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()

    def delete(self, product_id):
        try:
            pd = self.selectByPK(product_id)

            db.session.delete(pd)
            db.session.commit()

            self.message, self.error = p.SUCCESSFUL_DELETE, False
        except sqlite3.IntegrityError as err_aql:
            self.message, self.error = str(err_aql), True
        except Exception as err:
            self.message, self.error = str(err), True
        finally:
            db.session.close()
            return ResponseModel(dict(response=self.message, error=self.error)).getResponseBasic()
        
    def selectAll(self):
        return Product.query.all()

    def selectByPK(self, product_id):
        return Product.query.get(product_id)

