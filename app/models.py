from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime #if someone makes a post a time will auto attach and connect to database
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(150), nullable=False, unique=True)
  email = db.Column(db.String(150), nullable=False, unique=True)
  password = db.Column(db.String(256), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __init__(self, username, email, password):
    self.username=username
    self.email = email 
    self.password = generate_password_hash(password)
    #database stores a hash version of the password, really long random string
  
  def check_password(self, password):
    return check_password_hash(self.password, password)
    
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