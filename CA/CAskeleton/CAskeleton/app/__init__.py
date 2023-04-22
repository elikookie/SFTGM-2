from flask import Flask
from flask_babel import Babel
#Create the flask app
app = Flask(__name__)
#If we are using session then we need to set a secret key
app.secret_key='a secret key'
def get_locale():
    return 'fr'

#Hook Babel into your app and pass the local returned by get_locale to it
babel = Babel(app, locale_selector=get_locale)

#Import your routes (you need to configure these in routes.py)
from app import routes
