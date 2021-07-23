# imports
import json
from app.base_service import BaseService
from app.models import ResponseModel
from products.models import CategoryModel
from app import tables as t, properties as p

class CategoryService(BaseService):
    def __init__(self):
        super().__init__()
        
    def create(self, category):
        query = f"INSERT INTO {t.TCATEGORY} ({t.TCATEGORY_NAME}, {t.TCATEGORY_DESCRIPTION}) values (?,?)"
        params = [category.name, category.description]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, category, category_id):
        query = f"UPDATE {t.TCATEGORY} SET {t.TCATEGORY_NAME} = ?, {t.TCATEGORY_DESCRIPTION} = ? WHERE {t.TCATEGORY_ID} = ?"
        params = [category.name, category.description, category_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def delete(self, category_id):
        query = f"DELETE FROM {t.TCATEGORY} WHERE {t.TCATEGORY_ID} = ?"
        params = [category_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def selectAll(self):
        query = f"SELECT * FROM {t.TCATEGORY}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, category_id):
        query = f"SELECT * FROM {t.TCATEGORY} WHERE {t.TCATEGORY_ID} = ?"
        response = self.executeQueryOne(query, [category_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()


class ProductService(BaseService):
    def __init__(self):
        super().__init__()

    def create(self, product):
        query = f"INSERT INTO {t.TPRODUCT} ({t.TPRODUCT_NAME}, {t.TPRODUCT_STOCK}, {t.TPRODUCT_CATEGORY_ID}) values (?,?,?)"
        params = [product.name, product.stock, product.category_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_CREATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def update(self, product, product_id):
        query = f"UPDATE {t.TPRODUCT} SET {t.TPRODUCT_NAME} = ?, {t.TPRODUCT_STOCK} = ?, {t.TPRODUCT_CATEGORY_ID} = ? WHERE {t.TPRODUCT_ID} = ?"
        params = [product.name, product.stock, product.category_id, product_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_UPDATE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()

    def delete(self, product_id):
        query = f"DELETE FROM {t.TPRODUCT} WHERE {t.TPRODUCT_ID} = ?"
        params = [product_id]
        response = self.executeUpdate(query, params)
        return ResponseModel(
            dict(
                response=(p.SUCCESSFUL_DELETE if response["error"] is False else response["data"]), 
                error=response["error"]
            )
        ).getResponseBasic()
        
    def selectAll(self):
        query = f"SELECT * FROM {t.TPRODUCT}"
        response = self.executeQuery(query, [])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseResults()

    def selectByPK(self, product_id):
        query = f"SELECT * FROM {t.TPRODUCT} WHERE {t.TPRODUCT_ID} = ?"
        response = self.executeQueryOne(query, [product_id])
        return ResponseModel(
            dict( response=response["data"], error=response["error"] )
        ).getResponseOneResult()

