from flask import Flask, request, jsonify
from flask.wrappers import Response
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Numbers:
    first: int
    second: int

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello World!"

@app.route('/calculator/add', methods=['POST'])
def add():
    numbers = Numbers(**request.json)
    result = numbers.first + numbers.second
    return jsonify({"result": result})

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    numbers = Numbers(**request.json)
    result = numbers.first - numbers.second
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
