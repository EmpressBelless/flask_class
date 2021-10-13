from app import db
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime #if someone makes a post a time will auto attach and connect to database

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(150), nullable=False, unique=True)
  email = db.Column(db.String(150), nullable=False, unique=True)
  password = db.Column(db.String(256), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)
  #lazy allows a developer to specify. db relationship isn't going to be a field that shows up in a database. if you go into the db you won't see relationship. 

  def __init__(self, username, email, password):
    self.username=username
    self.email = email 
    self.password = generate_password_hash(password)
    #database stores a hash version of the password, really long random string

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200))
  content = db.Column(db.String(300))
  date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __init__(self, title, content, user_id):
    self.title=title
    self.content = content 
    self.user_id = user_id