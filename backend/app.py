import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD')
    )
    return conn

@app.route('/api/hello')
def hello():
    return 'Привет из бэкенда!'

@app.route('/api/users')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name VARCHAR(50));')
    cur.execute("INSERT INTO users (name) VALUES ('Тимур') RETURNING id;")
    conn.commit()
    cur.execute('SELECT * FROM users;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {'users': rows}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
