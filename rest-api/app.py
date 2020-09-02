from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

# from classes.Product import Product
# from routes.products.products import products

import os 

app = Flask(__name__)
app.config.from_object('config')

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

db.create_all()
db.session.commit()

ma = Marshmallow(app) 

@app.route('/', methods=['GET'])
def get():
    return jsonify({
        'msg': 'Hello World'
    })