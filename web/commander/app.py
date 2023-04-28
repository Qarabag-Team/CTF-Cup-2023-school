from flask import Flask, render_template, request, redirect, session
from init_db import init, get_user
import subprocess
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '4_wh4t?'
init()

@app.get('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username, password)

        if user and user[1] == 'P@$$w0rD!':
            session['username'] = username
            return redirect('/sandbox')
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


import os
@app.route('/sandbox', methods=['GET', 'POST'])
def sandbox():
    if 'username' not in session:
        return render_template('unauth.html')
    if request.method == 'POST':
        command = request.form['command']
        if 'cat' in command:
            filename = command.split(' ')[1]
            if os.path.isfile(filename):
                with open(filename, 'r') as f:
                    output = f.read()
            else:
                output = f'{filename} not found'
        else:
            output = 'flag.txt'
        return render_template('sandbox.html', output=output)
    return render_template('sandbox.html')

if __name__ == '__main__':
    app.run()