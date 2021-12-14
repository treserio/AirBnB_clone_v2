#!/usr/bin/python3
'''Starts a Flask app'''
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def s():
        return 'Hello HBNB!'

    @app.route('/hbnb')
    def s_hbnb():
        return 'HBNB'

    @app.route('/c/<text>')
    def s_c_text(text):
        return 'C {}'.format(text.replace('_', ' '))

    @app.route('/python/')
    @app.route('/python/<text>')
    def s_python_text(text='is cool'):
        return 'Python {}'.format(text.replace('_', ' '))

    @app.route('/number/<int:n>')
    def s_number_n(n):
        return '{} is a number'.format(n)

    @app.route('/number_template/<int:n>')
    def s_numberTemplate_n(n):
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>')
    def s_numberOddOrEven_n(n):
        if n % 2:
            val = 'odd'
        else:
            val = 'even'
        return render_template('6-number_oddor_even.html', n=n, val=val)

    app.run(debug=True, host='0.0.0.0')
