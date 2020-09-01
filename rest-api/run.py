from app import app 
from routes.products.products import products

app.register_blueprint(products, url_prefix='/products')

if (__name__ == '__main__'):
    app.run(debug=True)