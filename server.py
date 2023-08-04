from flask import Flask, request, jsonify
from flask.wrappers import Response
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Numbers:
    first: int
    second: int

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello World!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = Numbers(**request.json)
    if numbers.first and numbers.second:
        result = numbers.first + numbers.second
        return jsonify({"result": result}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = Numbers(**request.json)
    result = numbers.first - numbers.second
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
    

