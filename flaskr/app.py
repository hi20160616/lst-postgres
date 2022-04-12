from flask import Flask
from flask import make_response
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/tbl/<tbl_name>')
def show_table(tbl_name):
    # show the user profile for that user
    return f'Table: {escape(tbl_name)}'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

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
    from flask import current_app, render_template
    cur.execute(current_app.config['QUERY1'])
    records = cur.fetchall()
    cur.close()
    conn.close()
    db.close_db()

    return render_template('index.html', records=records)
