from app import app
from flask import send_file

@app.route('/')
@app.route('/index')
def index():
    try:
        return send_file('cloc_data.csv')
    except Exception as e:
        return str(e)