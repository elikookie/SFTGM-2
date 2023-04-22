from app import app
from flask import render_template, session, redirect, request, url_for


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        session['option'] = request.form['option']  # set session variable based on user selection
#       return 'Option selected: {}'.format(session['option'])# you can comment this out if using this approach in your CA
        return(redirect(url_for("index")))
    return render_template('setoption.html')

@app.route('/index')
def index():
    return (render_template(session['option']+"/index.html"))


@app.route('/about')
def about():
    return (render_template ("about.html"))
