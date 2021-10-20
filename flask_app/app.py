from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'New Test Response'
    else:
        return run_request()