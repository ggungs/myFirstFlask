import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, flash
from flask_bootstrap import Bootstrap
app = Flask(__name__)
DATABASE = 'test.db'

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
  return db

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

@app.route('/write', methods=['POST'])
def write():
    db = get_db()
    db.execute('insert into test (title, memo) values (?, ?)', [request.form['title'], request.form['memo']])
    db.commit()
    flash('Write New Memo Success!!')
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    db = get_db()
    db.execute('delete from test where id = ?', [request.form['id']])
    db.commit()
    flash('Delete Memo Success!!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    Bootstrap(app)
    app.debug = True
    app.secret_key = 'Test Key'
    app.run(host='0.0.0.0')
