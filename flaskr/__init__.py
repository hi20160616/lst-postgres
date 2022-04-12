import os

from flask import Flask, make_response, render_template, current_app

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = "dbname=mydb user=postgres password=mysecretpassword host=127.0.0.1",
        QUERY1 = "SELECT * FROM weather;"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    #  @app.route('/')
    #  def index():
    #      from . import db
    #      from flask import current_app, render_template
    #      conn = db.get_db()
    #      cur = conn.cursor()
    #      cur.execute(current_app.config['QUERY1'])
    #      records = cur.fetchall()
    #      cur.close()
    #      conn.close()

    @app.errorhandler(404)
    def not_found(error):
        resp = make_response(render_template('404.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp

    @app.route('/')
    def index():
        from . import db
        conn = db.get_db()
        cur = conn.cursor()
        cur.execute(current_app.config['QUERY1'])
        records = cur.fetchall()
        cur.close()
        conn.close()
        db.close_db()

        return render_template('index.html', records=records)

    return app
