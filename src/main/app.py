from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route('/calculator/add', methods=['POST'])
def add_numbers():
    data = request.json
    first = data['first']
    second = data['second']
    result = first + second
    return jsonify(result=result)

@app.route('/calculator/subtract', methods=['POST'])
def subtract_numbers():
    data = request.json
    first = data['first']
    second = data['second']
    result = first - second
    return jsonify(result=result)

@app.route('/calculator/division', methods=['POST'])
def divide_numbers():
    data = request.json
    first = data['first']
    second = data['second']
    if second != 0:
        result = first / second
    return jsonify(result=result)

@app.route('/calculator/multiply', methods=['POST'])
def multiply_numbers():
    data = request.json
    first = data['first']
    second = data['second']
    result = first * second
    return jsonify(result=result)

if __name__ == '__main__':
    app.run()
