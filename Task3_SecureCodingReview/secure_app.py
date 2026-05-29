from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return "Secure Application"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']

    password = hashlib.sha256(
        request.form['password'].encode()
    ).hexdigest()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=? AND password=?"

    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run()