from flask import Flask, request
import psycopg2
from datetime import datetime
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "logsdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/')
def index():
    ip = request.remote_addr
    timestamp = datetime.now()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO access_logs (ip, timestamp) VALUES (%s, %s)", (ip, timestamp))
    conn.commit()
    cur.close()
    conn.close()

    return f"Hello, your access has been logged at {timestamp} from IP {ip}!"

@app.route('/logs')
def get_logs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM access_logs ORDER BY id DESC LIMIT 10")
    logs = cur.fetchall()
    cur.close()
    conn.close()

    return {'logs': logs}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
