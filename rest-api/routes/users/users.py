from flask import Blueprint, request, jsonify
from flask_jwt import JWT

import bcrypt

from app import db, app
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

    found_user = User.query.filter(User.username == username).scalar()
    print(found_user)
    if (found_user):
        return jsonify({
            'success': False,
            'msg': 'User already exists'
        })

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(13))

    new_user = User(username, hashed.decode('utf-8')) 

    db.session.add(new_user) 
    db.session.commit() 

    return user_schema.jsonify(new_user)    

@users.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    found_user = User.query.filter(User.username == username).scalar()

    if (not found_user):
        return jsonify({
            'success': False,
            'msg': 'User does not exist'
        })
    
    hashed = str(found_user.password)

    if (not bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))):
        return jsonify({
            success: False,
            msg: 'Wrong password'
        })
    else:
        resp = user_schema.dump(found_user)
        jwt = JWT(app, lambda: resp, lambda: resp.id)
        return jsonify({
            'user': resp
        })