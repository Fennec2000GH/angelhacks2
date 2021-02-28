
import time #this is just testing
from flask import Flask, request, jsonify
import sys

import summary

app = Flask(__name__)
app.config['DEBUG'] = True

app.run(
    debug = True
)

data = []

@app.route('/')
def index():
    return "hello world"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    print(data)
    #Transform Data under here:
    summarified = summary.summarizeLexRank(data)
    print(summarified)
    return jsonify(summarified)
