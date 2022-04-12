from flask import Flask
from flask import make_response
from flask import abort, redirect, url_for
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

#  @app.route("/<name>")
#  def hello(name):
#      return f"Hello, {escape(name)}!"

@app.route('/tbl/<tbl_name>')
def show_table(tbl_name):
    # show the user profile for that user
    return f'Table: {escape(tbl_name)}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
