from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

app = Flask(__name__) 
app.secret_key = 'keyboardcat'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=10)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, email):
        self.name = name 
        self.email = email

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if (request.method == 'POST'):
        session.permanent = False
        usr = request.form['name']
        session['user'] = usr
        flash('Login successful')
        return redirect(url_for('user'))
    else:
        return render_template('login.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if (request.method == 'POST'):
            email = request.form['email']
            session['email'] = email
        elif 'email' in session:
            email = session['email']
        flash(f'Email set to {email}', 'info')
        return render_template('profile.html', email=email)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('email', None)
    flash('You have logged out', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)