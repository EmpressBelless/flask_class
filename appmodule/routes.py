#is where our routes will live
from appmodule import app
from flask import render_template
#create new folder in our appmodule named templates

@app.route('/')  
def index():
  name = 'Brian'
  title = 'Coding Temple Flask'
  return render_template('index.html', name_of_user=name, title=title)
  #puts name of brian into a dictionary, we can use those variables in our page

@app.route('/products')
def test():
  title = 'Coding Temple products'
  products = ['apple', 'orange', 'banana', 'peach']
  return render_template('products.html', title=title, products=products)