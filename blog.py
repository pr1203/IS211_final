from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import g
import sqlite3 as lite
import datetime

database = 'blog.db'
username = 'pr1203'
password = 'IS211pw'

app = Flask(__name__)
app.config['DATABASE'] = database
app.secret_key = 'dev'

def init_db():
    db = get_db()
    with app.open_resource('blog.sql') as f:
        db.executescript(f.read().decode('utf8'))


def connect_db():
    db = lite.connect(database)
    db.row_factory = lite.Row
    return db


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = lite.connect(database)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def index():
    return redirect('/homepage')


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        cur = g.db.execute(
            'SELECT title, author, published, content FROM Entries ORDER BY published desc'
            )

        res = cur.fetchall()
        entries = [dict(title=row[0], author=row[1], published=row[2], content=row[3]) for row in res]

    return render_template('homepage.html', entries=entries)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']

        if username == 'pr1203' and password == 'IS211pw':
                return redirect('/dashboard')

        else:
            print("Invalid username or password")
            return render_template('login.html')

    else:
        return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session['username'] == 'pr1203':
        cur = g.db.execute(
            'SELECT title, author, published, content FROM Entries ORDER BY published desc'
            )

        res = cur.fetchall()
        entries = [dict(title=row[0], author=row[1], published=row[2], content=row[3]) for row in res]
        return render_template('dashboard.html', entries=entries)

    else:
        return redirect('/login')

@app.route('/edit', methods=['GET', 'POST'])
def edit_post():
    current_date = datetime.datetime.today()
    if session['username'] == 'pr1203':
        if request.method == 'GET':
            return render_template('edit_post.html')
        elif request.method == 'POST':
            try:
                g.db.execute("INSERT INTO Entries (title, content, published) VALUES (?, ?, ?)", (request.form['title'], request.form['content'], current_date))
                g.db.commit()
                return redirect('/dashboard')
            except Exception as e:
                print(e)
                return render_template('edit_post.html')
    else:
        return redirect('/login')

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    author = username
    current_date = datetime.datetime.today()
    if session['username'] == 'pr1203':
            if request.method == 'GET':
                return render_template('add_post.html')
            elif request.method == 'POST':
                try:
                    g.db.execute("INSERT INTO entries (author, title, content, published) VALUES (?, ?, ?, ?)", (author, request.form['add_title'], request.form['add_content'], current_date))
                    g.db.commit()
                    return redirect('/dashboard')
                except Exception as e:
                    print(e)
                    return render_template('add_post.html')

    else:
        return redirect('/login')


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_post(id):
    if request.method == 'POST':
        g.db.execute('DELETE FROM Entries where id = ?', [id])
        g.db.commit()
    return redirect('/dashboard')


if __name__ == "__main__":
    app.run(debug=True)
    connect_db()
