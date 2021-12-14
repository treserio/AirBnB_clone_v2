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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
