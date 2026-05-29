from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

SECRET_KEY = "admin123"

@app.route('/')
def home():
    return "Vulnerable Application"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login Successful"
    else:
        return "Invalid Credentials"

@app.route('/command')
def command():
    cmd = request.args.get('cmd')
    os.system(cmd)
    return "Command Executed"

if __name__ == '__main__':
    app.run(debug=True)