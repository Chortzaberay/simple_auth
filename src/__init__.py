from flask import Flask

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import psycopg2
login_manager = LoginManager()
db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.sqlite"
    # app.config["SECRET_KEY"] = "secret_key"
    app.config.from_object(config)
    conn_string = "host='localhost' dbname='basic_login' user='postgres' password='HomePass1'"
    conn = psycopg2.connect(conn_string)
    with app.app_context():
        db.init_app(app)
        login_manager.init_app(app)
        from .routes import auth
        app.register_blueprint(auth)
    
    @app.route("/")
    @app.route("/index")
    def index():
        return {"message": "index"}, 200
    
        
    return app

