from flask import Flask, render_template
import sqlite3 
from db import Test_data,ses
# DATABASE = ds.db
# def create_book_table():
#     con = sqlite3.connect(DATABASE)
#     con.execute("CREATE TABLE IF NOT books ()")

app = Flask(__name__)

@app.route('/list')
def list():
    students = ses.query(Test_data).order_by(Test_data.id).all()
    return render_template('list.html',students=students)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.debug = True
    app.run(host='localhost')

