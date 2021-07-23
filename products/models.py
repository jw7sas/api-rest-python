""" Clase del modelo categorias. """
class CategoryModel():

    def __init__(self, category):
        if(category):
            self.name = category["name"]
            self.description = category["description"]


""" Clase del modelo producto. """
class ProductModel():

    def __init__(self, product):
        if(product):
            self.name = product["name"]
            self.stock = product["stock"]
            self.category_id = product["category_id"]