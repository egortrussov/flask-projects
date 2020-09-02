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

@products.route('/delete', methods=['POST'])
def delete_products():
    deleted_products = []
    products_ids = request.json['ids']
    for id in products_ids:
        curr_product = Product.query.filter_by(id=id)
        deleted_products.append(curr_product.one().__dict__)
        curr_product.delete()
        # print(curr_product.__dict__)
        db.session.commit()
    resp = products_schema.dump(deleted_products)
    return jsonify(resp)