from flask import Flask

app = Flask(__name__)

from app import routes


# It creates an application object app as an instance of class
# Flask (which is imported in the first line)
# The __name__ variable passed to the class is a predefined
# Python variable. It is set to the name of the module in which
# it is used.
#  Flask uses the location of the module passed here as a
# starting point when it needs to load resources such as
# template files – we will learn more about this later.
# The next line directs that the routes module be imported (this
# doesn’t exist at the moment - we are going to set that up now)
#
