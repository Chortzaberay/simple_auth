class Config():
    TESTING = False

class DevConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:HomePass1@localhost/basic_login"
    SECRET_KEY = "secret_key"

class ProductConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_db.sqlite"
    SECRET_KEY = "secret_key"