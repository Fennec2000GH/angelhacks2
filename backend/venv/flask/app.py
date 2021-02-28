import time #this is just testing
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/data')
def get_data():
    data = request.args.get('body')
    return data