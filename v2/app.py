from flask import Flask
import platform, os, psutil

app = Flask(__name__)

@app.route('/')
def system_info():
    html = f"""
    <h1>System Info</h1>
    OS Name: {os.name}<br>
    System: {platform.system()}<br>
    Release: {platform.release()}<br>
    CPU Usage: {psutil.cpu_percent()}%<br>
    Memory Usage: {psutil.virtual_memory().percent}%<br>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)