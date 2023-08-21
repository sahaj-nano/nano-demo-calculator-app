from flask import Flask, request, jsonify

app = Flask(_name_)

class Numbers:
    def _init_(self, first, second):
        self.first = first
        self.second = second

class Result:
    def _init_(self, value):
        self.result = value

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if data and 'first' in data and 'second' in data:
        numbers = Numbers(data['first'], data['second'])
        result = Result(numbers.first + numbers.second)
        return jsonify(result._dict_)
    else:
        return jsonify(error="Invalid input data"), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if data and 'first' in data and 'second' in data:
        numbers = Numbers(data['first'], data['second'])
        result = Result(numbers.first - numbers.second)
        return jsonify(result._dict_)
    else:
        return jsonify(error="Invalid input data"), 400

if _name_ == '_main_':
    app.run(port=8080, host='0.0.0.0')