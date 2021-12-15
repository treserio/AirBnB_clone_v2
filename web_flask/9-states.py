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

    @app.route('/states')
    @app.route('/states/<id>')
    def s_states(id=None):
        st = storage.all(State)
        if id:
            st = st.get('State.{}'.format(id))

        return render_template('9-states.html',
                               States=st)

    app.run(host='0.0.0.0', port='5000')
