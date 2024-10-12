from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "dictionary.db"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None

@app.route('/')
def render_homepage():
    return render_template('home.html')

@app.route('/contact')
def render_contact():
    return render_template('contact.html')

@app.route('/dictionary')
def render_dictionary():
    con = create_connection(DATABASE)
    query = "SELECT * FROM vocab_list"
    cur = con.cursor
    cur.execute(query)
    vocab_list = cur.fetchall
    print(vocab_list)
    return render_template('dictionary.html', vocab = vocab_list)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
