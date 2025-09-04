from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.orm import backref
from socket import gethostname


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'akrtbj89777gfcg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'static.login'
login_manager.init_app(app)

from flask_login import UserMixin
class User(UserMixin, db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(30))
    name = db.Column(db.String(20), unique=True)
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(400))
    commenter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    commenter = db.relationship("User", backref=backref("user", uselist=False))
    comment_date = db.Column(sa.DATETIME)
    page = sa.Column(sa.String(70))
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

from staticp import static as st
from interactive import interactive as intact
from physicsPages import phyPs
from chemistryPages import chemPs
app.register_blueprint(st)
app.register_blueprint(intact)
app.register_blueprint(phyPs)
app.register_blueprint(chemPs)

if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run(debug=True)