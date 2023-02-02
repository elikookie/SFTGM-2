# What goes into the routes file?
# The routes are the different URIs that the application
# implements.
# In Flask, handlers for the application routes are written as
# Python functions, called view functions.
# View functions are mapped to one or more route URLs so that
# Flask knows what logic to execute when a client requests a
# given URL

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
# Here we are setting up two routes, one which is when just the app
# is requested, and the other when an index page is requested.
def index():
    user = {'username': 'Eli'}
    return render_template('index.html', title='Lab Class Week 1', user=user)

#     return '''
# <html>
#     <head>
#         <title>Home Page - Lab Class Week 1</title>
#     </head>
#     <body>
#         <h1>Welcome to Software for the Global Market II, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''
