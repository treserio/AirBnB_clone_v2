#!/usr/bin/python3
'''Starts a Flask app'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def s():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def s_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def s_c_text(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def s_python_text(text):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
