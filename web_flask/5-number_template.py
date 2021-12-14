#!/usr/bin/python3
'''Starts a Flask app'''
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template

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

    @app.route('/python/', strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def s_python_text(text='is cool'):
        return 'Python {}'.format(text.replace('_', ' '))

    @app.route('/number/<int:n>', strict_slashes=False)
    def s_number_n(n):
        return '{} is a number'.format(n)

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def s_numberTemplate_n(n):
        return render_template('5-number.html', n=n)

    app.run(debug=True, host='0.0.0.0')
