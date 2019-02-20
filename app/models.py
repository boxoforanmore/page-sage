from app import app, db, login_manager
#from app import google_bp as blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc  import NoResultFound
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # Formerly username
    email = db.Column(db.String(256), unique=True) 
    f_name = db.Column(db.String(30))

    def __repr__(self):
        return '<User {}>'.format(self.email)

class OAuth(db.Model, OAuthConsumerMixin):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
