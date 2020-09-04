from app import db 


import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String) 

    def __init__(self, username, password):
        self.username = username 
        self.password = password 