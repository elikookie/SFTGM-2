from app import app
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user ={'username': request.form.get('username')}
    # return "Welcome to Lab Class WEEK TWO -Let the fun begin!"
    return render_template('index.html', title='Week 2', user=user)


@app.route('/data_input/', methods=('GET', 'POST'))
def data_input():
    user = {'username': request.form.get('username')}
    return render_template('index.html', title='Week 2', user=user)
