import psycopg2

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(current_app.config['DATABASE'])

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
