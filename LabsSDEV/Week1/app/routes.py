from app import app
from flask import render_template
#The routes your app will respond to
@app.route('/')
@app.route('/index')

#This is a view which will be returned in response to a request
def index():
    user = {'username': 'Elitsa'}
    return render_template('index.html', title='Lab Class Week 1', user=user)
