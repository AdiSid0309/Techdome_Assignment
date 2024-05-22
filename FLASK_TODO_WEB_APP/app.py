from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

key = secrets.token_urlsafe(16)

app = Flask(__name__, static_folder='static')
app.secret_key = key

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

# Load user
@login_manager.user_loader
def load_user(user_id):
    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, password, role FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if user:
            return User(*user)
        return None

# Database setup
def init_db():
    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL CHECK (role IN ('admin', 'user'))
            )
        ''')
        conn.commit()

init_db()

@app.route('/')
@login_required
def index():
    return render_template('index.html', role=current_user.role)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('todo.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, username, password, role FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user and check_password_hash(user[2], password):
                user_obj = User(*user)
                login_user(user_obj)
                return redirect(url_for('index'))
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']
        with sqlite3.connect('todo.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
                conn.commit()
                flash('Registration successful! Please log in.')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username already exists.')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    if current_user.role != 'admin':
        return jsonify({'error': 'Permission denied'}), 403

    try:
        task_content = request.json['content']
        with sqlite3.connect('todo.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (content, completed) VALUES (?, ?)', (task_content, False))
            conn.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return get_tasks()


@app.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, content, completed FROM tasks')
        tasks = cursor.fetchall()
    tasks_list = [{'id': row[0], 'content': row[1], 'completed': bool(row[2])} for row in tasks]
    return jsonify(tasks_list)

@app.route('/complete_task', methods=['POST'])
@login_required
def complete_task():

    task_id = request.json['id']
    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (True, task_id))
        conn.commit()
    return get_tasks()

@app.route('/delete_task', methods=['POST'])
@login_required
def delete_task():
    if current_user.role != 'admin':
        return jsonify({'error': 'Permission denied'}), 403

    task_id = request.json['id']
    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
    return get_tasks()

if __name__ == '__main__':
    app.run(debug=True)