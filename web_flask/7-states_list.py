#!/usr/bin/python3
'''Flask app using filestorage'''


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(context):
    storage.close()


@app.route('/states_list')
def s_statesList():
    ls = storage.all(State)
    return render_template('7-states_list.html', States=ls)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
