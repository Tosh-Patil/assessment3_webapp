import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Config to set SQLALCHEMY 
class Config(object):
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False