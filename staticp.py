from flask import Blueprint, render_template
from flask_login import current_user, login_required


static = Blueprint("static", __name__)

@static.route('/')
def index():
    return render_template("index.html")


@static.route('/profile')
@login_required
def profile():
    return render_template('profile.htm', user=current_user)

