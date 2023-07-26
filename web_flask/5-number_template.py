#!/usr/bin/python3
"""
This module defines a Flask web application.
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Display "Hello HBNB!" on the root path.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Display "HBNB" on the path "/hbnb".
    """
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    """
    Display "C ", followed by the value of the text variable.
    Replace underscore (_) symbols with a space.
    """
    return 'C ' + text.replace("_", ' ')


@app.route('/python/')
@app.route('/python/<text>')
def ptext(text='is cool'):
    """
    Display "Python ", followed by the value of the text variable (default is 'is cool').
    Replace underscore (_) symbols with a space.
    """
    return 'Python {}'.format(text.replace("_", ' '))


@app.route('/number/<int:n>')
def ntext(n):
    """
    Display "{} is a number" only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Display an HTML page only if n is an integer.
    """
    return render_template('5-number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

