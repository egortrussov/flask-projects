from app import app, db

from routes.products.products import products
from routes.users.users import users

from classes.User import User 
from classes.Product import Product

app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(users, url_prefix='/users')

db.create_all()
db.session.commit()

if (__name__ == '__main__'):
    app.run(debug=True)