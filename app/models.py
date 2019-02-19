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
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@oauth_authorized.connect_via(blueprint)
def google_logged_in(blueprint, token):
    if not token:
        flask("Failed to log in with {name}".format(name=blueprint.name))
        return
    account_info = blueprint.session.get("/user")
    if account_info.ok:
        username = resp.json()["login"]
        query = User.query.filter_by(username=username)
        try:
            user = query.one()
        except NoResultFound:
            user =  User(username=username)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        flash("Successfully signed in with Google")
    else:
        msg = "Failed to fetch user info from {name}".format(name=blueprint.name)
        flash(msg, category="error")


@oauth_error.connect_via(blueprint)
def google_error(blueprint, error, error_description=None, error_uri=None):
    msg = ( 
        "OAuth error from {name}! "
        "error={error} description={description} uri={uri}"
    ).format(
        name=blueprint.name,
        error=error,
        description=error_description,
        uri=error_uri
    )   
    flash(msg, category="error")
'''
