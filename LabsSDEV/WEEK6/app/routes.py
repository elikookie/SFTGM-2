from app import app
from flask import render_template
from flask import session, redirect, request


@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    # Set the session variable lang to whatever code was used in the url
    session["language"] = lang_code
    # refresh the page from which the set language request was made
    return redirect(request.referrer)


@app.route('/')
@app.route('/index')
def index():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("index.html", lang_code=session["language"])


@app.route('/about')
def about():
    return render_template ("about.html", lang_code=session["language"])


@app.route('/products')
def products():
    return render_template ("products.html", lang_code=session["language"])


@app.route('/store')
def store():
    return render_template("store.html", lang_code=session["language"])
