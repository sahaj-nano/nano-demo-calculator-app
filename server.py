from dataclasses import dataclass

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    response = (numbers['first'] + numbers['second'])
    # print(response)
    return jsonify({'result':response})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    response = (numbers['first'] - numbers['second'])
    return jsonify({'result':response})
    
    app.run(port=8080,host='0.0.0.0')