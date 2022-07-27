"""Flask Configuration"""
import datetime
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
    JWT_SECRET_KEY = "ik,ncbxh"
    SESSION_COOKIE_SECURE = True
    APP_ROOT_DIRECTORY = os.getcwd()
    DB_DIRECTORY_LOCATION = os.path.join(APP_ROOT_DIRECTORY, "database")
    DB_FILE_LOCATION = os.path.join(DB_DIRECTORY_LOCATION, "db.sqlite")
    LOG_DIRECTORY = os.path.join(APP_ROOT_DIRECTORY, "logs")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_FILE_LOCATION
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)
    API_TITLE = "My API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SESSION_COOKIE_SECURE = False
    DEBUG = True
