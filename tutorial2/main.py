from flask import Flask, render_template

# import sys
# sys.path.insert(0, './routes')

from routes.profile import profile
from routes.items.items import items

app = Flask(__name__)
app.register_blueprint(profile, url_prefix='/admin')
app.register_blueprint(items, url_prefix='/items')

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

if (__name__ == '__main__'):
    app.run(debug=True)