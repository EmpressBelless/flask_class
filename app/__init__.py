from flask import Flask 
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__) 
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail= Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You shall not pass!'
login_manager.login_message_category = 'danger'

from app import routes, models

#commands - you will probably write them a lot
#flask db init - initiliazes the db
#flask db migrate = created a migrations folder, keeps track diff versions of your db
#flask db upgrade
