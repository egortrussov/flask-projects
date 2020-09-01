from app import ma 

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

#init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)