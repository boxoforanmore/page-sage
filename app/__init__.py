from flask import Flask, url_for
from config import Config
from flask_dance.contrib.google import make_google_blueprint, google
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(object_name=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    google_bp = make_google_blueprint(
        client_id=os.environ.get('GOOGLE_CLIENT_ID'),
        client_secret=os.environ.get('GOOGLE_SECRET'),
        scope=[
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/plus.me"
        ]
    )
    app.register_blueprint(google_bp, url_prefix="/google-login")
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    return app

app = create_app()

from app import routes, errors, models
