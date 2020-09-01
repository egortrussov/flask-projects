from flask import Blueprint, request
from classes.Product import Product

import sys
# sys.path.insert(0, '../../')

# from app import Product

products = Blueprint('products', __name__)

@products.route('/create', methods=['GET'])
def create_product():
    return 'HI'