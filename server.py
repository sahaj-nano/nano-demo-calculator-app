from dataclasses import dataclass

#dataclasses is used to import the __init__,__repr__
from flask import Flask, jsonify, request

#Flask is used to create a new web application
#jsonify is used to convert the data to JSON format before sending it to the http
#request is the data in the JSON format we convert into required format using functions request.json,request.args,request.forms
#@dataclass
#class Result:
#    result: int


app = Flask(__name__)
@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    response = int(numbers['first'] + numbers['second'])
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    response = int(numbers['first'] - numbers['second'])
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
