import sqlite3
import hashlib

def init_db():
    conn = sqlite3.connect('retail_app.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS user_data (username TEXT PRIMARY KEY, data_csv BLOB)')
    conn.commit()
    conn.close()

def register_user(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('retail_app.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed))
        conn.commit()
        return True
    except: return False
    finally: conn.close()

def login_user(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('retail_app.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed))
    user = c.fetchone()
    conn.close()
    return user is not None

def save_data(username, csv_data):
    conn = sqlite3.connect('retail_app.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO user_data VALUES (?, ?)', (username, csv_data))
    conn.commit()
    conn.close()

def get_data(username):
    conn = sqlite3.connect('retail_app.db')
    c = conn.cursor()
    c.execute('SELECT data_csv FROM user_data WHERE username=?', (username,))
    res = c.fetchone()
    conn.close()
    return res[0] if res else None