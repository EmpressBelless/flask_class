import os

from flask_sqlalchemy import SQLAlchemy
#added this top line to config and ran pip install dotenv because the error told me to. and now my code works. 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

