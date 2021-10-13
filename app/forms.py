from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class UserInfoForm(FlaskForm):
  #will take in username and it will take a string field
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField()

class PostForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = StringField('Content', validators=[DataRequired()])
  submit = SubmitField()

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField()