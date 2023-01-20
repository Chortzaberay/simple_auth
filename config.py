from constants import DB_PASSWORD, DB_USER
class Config():
    TESTING = False

class DevConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/basic_login"
    SECRET_KEY = "secret_key"
    DEBUG = True

class ProductConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_db.sqlite"
    SECRET_KEY = "secret_key"