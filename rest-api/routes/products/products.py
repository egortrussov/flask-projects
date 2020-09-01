from flask import Blueprint, request, jsonify
from app import db

from classes.Product import Product

from schemas.Product import product_schema, products_schema

import sys
# sys.path.insert(0, '../../')

# from app import Product

products = Blueprint('products', __name__)

@products.route('/create', methods=['POST'])
def create_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

@products.route('/all', methods=['GET'])
def get_all_products():
    all_products = Product.query.all()
    resp = products_schema.dump(all_products)
    return jsonify(resp)