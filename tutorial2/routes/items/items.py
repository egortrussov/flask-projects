from flask import Blueprint

items = Blueprint('items', __name__, static_folder='static', template_folder='templates')

@items.route('/')
def items_page():
    return 'items';