import sqlite3
from flask import Flask, request

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print("Executing query with parameters:", query, (username, password))
    c.execute(query, (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == '__main__':
    create_database()
    app.run(debug=True)