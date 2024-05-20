#!/usr/bin/python3
""" A simple web application 
"""
from flask import Flask
app = Flask(__name__)

'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """
    Display HBNB
    """
    return 'HBNB'

app.route('/c/<text>')
def c_with_params(text):
    """
    is_fun
    """
    txt_no_underscore = text.replace('_', ' ')
    return 'C {}'.format(text_no_underscore)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
