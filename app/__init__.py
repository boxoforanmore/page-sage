from flask import Flask, redirect
from config import Config
from flask_dance.contrib.google import make_google_blueprint, google
#from flask_pymongo import PyMongo

def create_app(object_name=Config):
    app = Flask(__name__)
    app.config.from_object(object_name)
    google_bp = make_google_blueprint(
        client_id="102163899252-gu4pmkr3jq4ttjumhd2v69gj986n489c.apps.googleusercontent.com",
        client_secret="FAGhh2s4tj_nQ-BtDRuGvFTf",
        scope=[
            "https://www.googleapis.com/auth/plus.me",
            "https://www.googleapis.com/auth/userinfo.email"
        ]
    )
    app.register_blueprint(google_bp, url_prefix="/login")
    #mongo = PyMongo(app)

    return app

app = create_app()

from app import routes, errors
