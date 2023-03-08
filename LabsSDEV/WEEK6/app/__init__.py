from flask import Flask
from flask_babel import Babel

#Create the flask app
app = Flask(__name__)
#If we are using session then we need to set a secret key
app.secret_key='a secret key'

#Hook Babel into your app
babel = Babel(app)

#Import your routes (you need to configure these in routes.py)
from app import routes

