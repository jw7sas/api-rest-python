# imports
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from app.database import Product, Category

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Category
        fields = ('id', 'name', 'description',)
        load_instance = True

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Product
        fields = ('id', 'name', 'stock', 'category_id', 'category',)
        include_relationships = True
        load_instance = True
    
    category = fields.Nested(CategorySchema)

 