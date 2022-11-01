from distutils.debug import DEBUG
from pickle import TRUE
from decouple import config
from pkg_resources import DEVELOP_DIST

DATABASE_URI = config("DATABASE_URI")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://","postgresql://",1)

class Config(object):
    DEBUG =  False
    TESTING = False
    CSRF_ENABLED = TRUE
    SECRET_KEY = config('SECRET_KEY',default='guess-me')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True