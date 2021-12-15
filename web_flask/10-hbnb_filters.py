#!/usr/bin/python3
'''Flask app using filestorage'''


if __name__ == '__main__':
    from flask import Flask, render_template
    import models

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def teardown(context):
        models.storage.close()

    @app.route('/hbnb_filters')
    def s_hbnbFilters():
        return render_template(
            '10-hbnb_filters.html',
            db_st=models.storage.all(models.State),
            db_amnty=models.storage.all(models.Amenity)
        )

    app.run(host='0.0.0.0', port='5000')
