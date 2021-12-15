#!/usr/bin/python3
'''Flask app using filestorage'''


if __name__ == '__main__':
    import flask
    import models

    app = flask.Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def teardown(context):
        models.storage.close()

    @app.route('/states_list')
    def statesList():
        ls = models.storage.all(models.State)
        return flask.render_template('7-states_list.html', States=ls)

    app.run(host='0.0.0.0', port='5000')
