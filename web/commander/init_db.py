import sqlite3

def init():
    connection = sqlite3.connect('db/database.db')

    with open('db/schema.sql') as f:
        connection.executescript(f.read())
        cur = connection.cursor()

        cur.execute('INSERT INTO users (username, password) VALUES (?, ?);', ('blaballablba', 'P@$$w0rD!'))

        connection.commit()
        connection.close()

def get_user(username, password):
    connection = sqlite3.connect('db/database.db')
    cur = connection.cursor()

    user = cur.execute("""SELECT username, password FROM users 
                       WHERE username=? AND password=?""", (username, password)).fetchone()
    
    return user