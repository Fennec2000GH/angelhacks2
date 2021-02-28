
import time #this is just testing
from flask import Flask, request, jsonify
import sys

import summary

app = Flask(__name__)
app.config['DEBUG'] = True

app.run(
    debug = True
)

@app.route('/')
def index():
    return "hello world"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/data', methods=['POST'])
def get_data():
    raw_data = request.get_json()
    print(raw_data)
    data = list(raw_data)
    #Transform Data under here:
    summarified = "No algorithm chosen"
    if data[1] == "LexRank":
        summarified = summary.summarizeLexRank(data[0])
    elif data[1] == "Luhn":
        summarified = summary.summarizeLuhn(data[0])
    elif data[1] == "LSA":
        summarified = summary.summarizeLSA(data[0]) 
    elif data[1] == "KL":
        summarified = summary.summarizeKL(data[0]) 
    print(summarified)
    return jsonify(summarified)
