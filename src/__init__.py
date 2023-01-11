from flask import Flask

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.sqlite"
    app.config["SECRET_KEY"] = "secret_key"

    return app

