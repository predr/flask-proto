#
# Flask application
# https://flask.palletsprojects.com/en/1.1.x/
#
import os
from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    database = os.getenv('DATABASE', '/repo/sqlite.db')
    conn = sqlite3.connect(database)
    ret = conn.execute('select sqlite_version();').fetchall()
    conn.close()
    return '''
        <html>
            <head>
                <title>Flask Proto</title>
            </head>
            <body>
                <h1>Hello World!</h1>
                <p>SQLite version: %s</p>
            </body>
        </html>
    ''' % ret[0][0]
