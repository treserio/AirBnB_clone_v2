#!/usr/bin/python3
'''Flask app using filestorage'''


if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def teardown(context):
        storage.close()

    @app.route('/cities_by_states')
    def citiesByStates():
        ls = storage.all(State)
        return render_template('7-states_list.html', States=ls)

    app.run(host='0.0.0.0', port='5000')
