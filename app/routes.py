from app import app, db
#is where our routes will live
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import UserInfoForm, PostForm, LoginForm
from app.models import User, Post
#create new folder in our appmodule named templates

@app.route('/')  
def index():
  title = 'Coding Temple Flask'
  posts = Post.query.all()
  return render_template('index.html', title=title, posts=posts)

@app.route('/products')
def products():
  name = 'Tommy'
  title = 'Coding Temple products'
  products = ['apple', 'orange', 'banana', 'peach']
  return render_template('products.html', title=title, products=products)

@app.route('/register', methods=['GET', 'POST'])#uppercase matters
def register():
  register_form = UserInfoForm()
  if register_form.validate_on_submit():
    username = register_form.username.data
    email = register_form.email.data
    password = register_form.password.data
    print(username, email, password)

  # Check if username already exists
    existing_user = User.query.filter_by(username=username).all()
    #if there is a user with that username message them asking them to try again
    if existing_user:
        # Flash a warning message
        flash(f'The username {username} is already registered. Please try again.', 'danger')
        # Redirect back to the register page
        return redirect(url_for('register'))

    #if there isn't create a new user instant
    new_user = User(username, email, password)
    #add that user to the db
    db.session.add(new_user)
    db.session.commit()
    #flash a success message
    flash(f'Thank you {username}, you have successfully registered!', 'success')
    #adding a category as a string of success.  this wll help us choose a color theme for our message
    #redirect to homepage
    return redirect(url_for('index'))
  return render_template('register.html', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  #instance of our login form
  form = LoginForm()
  #Grab data from form
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
  #query our user table for a user with username
    user = User.query.filter_by(username=username).first()
  #check if the user is none or if password is incorrect

    if not user or not user.check_password(password):
      flash('Your username or password is incorrect', 'danger')
      return redirect(url_for('login'))

    login_user(user)

    flash(f'Welcome {user.username} You have successfully logged in.', 'success')

    return redirect(url_for('index'))

  return render_template('login.html', login_form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/createpost', methods=['GET', 'POST'])
@login_required 
#this ^ has to be below app.route
def createpost():
  form = PostForm()
  if form.validate_on_submit():
    title = form.title.data
    content = form.content.data
    new_post = Post(title, content, current_user.id)
    db.session.add(new_post)
    db.session.commit()

    flash(f'This post {title} has been created.', 'primary')
    return redirect(url_for('index')) 

  return render_template('createpost.html', form=form)
