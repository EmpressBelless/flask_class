from flask import Flask 
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) 
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

#commands - you will probably write them a lot
#flask db init - initiliazes the db
#flask db migrate = created a migrations folder, keeps track diff versions of your db
#flask db upgrade
