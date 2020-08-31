from flask import Blueprint, render_template

profile = Blueprint('profile', __name__, static_folder='static', template_folder='templates')

@profile.route('/profile')
@profile.route('/')
def profile_page():
    return render_template('profile.html')