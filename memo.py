from flask import Blueprint, request, flash, redirect, url_for
from db import get_db

memo_app = Blueprint('memo_app', __name__)

@memo_app.route('/write', methods=['POST'])
def write():
    db = get_db()
    db.execute('insert into test (title, memo) values (?, ?)', [request.form['title'], request.form['memo']])
    db.commit()
    flash('Write New Memo Success!!')
    return redirect(url_for('index'))

@memo_app.route('/delete', methods=['POST'])
def delete():
    db = get_db()
    db.execute('delete from test where id = ?', [request.form['id']])
    db.commit()
    flash('Delete Memo Success!!')
    return redirect(url_for('index'))

@memo_app.route('/memoApp')
def aboutMemoApp():
    return "<p>MEMO APP</p>"
