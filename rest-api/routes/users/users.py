from flask import Blueprint, request

from app import db
from classes.User import User 
from schemas.User import user_schema, users_schema

users = Blueprint('users', __name__)

@users.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    return user_id

@users.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    print(username, password)
    new_user = User(username, password) 

    db.session.add(new_user) 
    db.session.commit() 

    return user_schema.jsonify(new_user)    