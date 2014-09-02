import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, flash
from flask_bootstrap import Bootstrap
from db import get_db
from memo import memo_app

app = Flask(__name__)
app.register_blueprint(memo_app)

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select id, title, memo from test order by id desc')
    test = cur.fetchall()
    return render_template('index.html', entries=test)


if __name__ == '__main__':
    Bootstrap(app)
    app.debug = True
    app.secret_key = 'Test Key'
    app.run(host='0.0.0.0')
