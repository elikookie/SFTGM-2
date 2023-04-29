from app import app
from flask import render_template, session, redirect, request, url_for

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        session['option'] = request.form['option']  # set session variable based on user selection
        if session['option'] == 'japanese':
            return redirect(url_for('japanese_home'))
        elif session['option'] == 'finnish':
            return redirect(url_for('finnish_home'))
    return render_template('setoption.html')

@app.route('/japanese_home')
def japanese_home():
    session['japanese'] = 'japanese'
    return (render_template("japanese/japanese_home.html"))


@app.route('/finnish_home')
def finnish_home():
    session['finnish'] = 'finnish'
    return (render_template("finnish/finnish_home.html"))


@app.route('/about')
def about():
    return (render_template("about.html"))
