from app import app
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Elitsa'}
    # return "Welcome to Lab Class WEEK TWO -Let the fun begin!"
    return render_template('index.html', title='Week 3 Index', content="Example of template inheritance.")


@app.route('/about')
def about():
    return render_template("about.html", title="About Week 3 App", content="Example template inheritance using a "
                                                                           "navigation bar.")


@app.route('/test')
def test():
    return render_template("test.html", title="Test Week 3 App")
