from flask_babel import Babel

from flask import Flask

app = Flask(__name__)

from app import routes

# a function which at the moment returns a 2 letter string code for a local
def get_locale():
    return 'fr'

# Hook Babel into your app and pass the local returned by get_locale to it
babel = Babel(app, locale_selector=get_locale)

