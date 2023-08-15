from flask import Flask
from flask import json, request, Response

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    res = {
        'result': "Hello world!",
        'Status': 200
    } 
    return res

@app.route("/calculator/add", methods=['POST'])
def add():
    first = request.json.get('first')
    second = request.json.get('second')
    res = {
        'result': first + second
    }
    return res

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first = request.json.get('first')
    second = request.json.get('second')
    if(first > second):
        x= first - second
    else:
        x= second - first
    res = {
        'result': x
    }
    return res

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')